import numpy as np
from typing import List, Optional
import re


class EmbeddingGenerator:
    """嵌入向量生成器（简化版，使用TF-IDF替代深度学习模型）"""
    
    def __init__(self, vector_size: int = 128):
        self.vector_size = vector_size
        self.vocab = {}
        self.idf = {}
    
    def _tokenize(self, text: str) -> List[str]:
        """分词"""
        # 提取代码中的标识符、关键字等
        tokens = []
        
        # 提取单词
        words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', text)
        tokens.extend(words)
        
        # 提取字符串
        strings = re.findall(r'["\']([^"\']+)["\']', text)
        tokens.extend(strings)
        
        # 提取注释
        comments = re.findall(r'[#//]+\s*(.+)', text)
        tokens.extend(comments)
        
        return [t.lower() for t in tokens if len(t) > 1]
    
    def _build_vocab(self, texts: List[str]):
        """构建词汇表"""
        from collections import Counter
        
        all_tokens = []
        doc_tokens = []
        
        for text in texts:
            tokens = self._tokenize(text)
            doc_tokens.append(tokens)
            all_tokens.extend(tokens)
        
        # 选择最常见的词
        counter = Counter(all_tokens)
        most_common = counter.most_common(self.vector_size)
        
        self.vocab = {word: idx for idx, (word, _) in enumerate(most_common)}
        
        # 计算IDF
        n_docs = len(texts)
        for word in self.vocab:
            doc_count = sum(1 for tokens in doc_tokens if word in tokens)
            self.idf[word] = np.log(n_docs / (doc_count + 1)) + 1
    
    def generate_embedding(self, text: str) -> List[float]:
        """生成文本的嵌入向量"""
        tokens = self._tokenize(text)
        
        if not self.vocab:
            # 如果没有词汇表，使用简单的哈希方法
            vector = np.zeros(self.vector_size)
            for i, token in enumerate(tokens[:self.vector_size]):
                idx = hash(token) % self.vector_size
                vector[idx] += 1
            # 归一化
            norm = np.linalg.norm(vector)
            if norm > 0:
                vector = vector / norm
            return vector.tolist()
        
        # 使用TF-IDF
        from collections import Counter
        token_counts = Counter(tokens)
        
        vector = np.zeros(len(self.vocab))
        for token, count in token_counts.items():
            if token in self.vocab:
                idx = self.vocab[token]
                tf = count / len(tokens) if tokens else 0
                idf = self.idf.get(token, 1)
                vector[idx] = tf * idf
        
        # 归一化
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector.tolist()
    
    @staticmethod
    def cosine_similarity(a: List[float], b: List[float]) -> float:
        """计算余弦相似度"""
        a, b = np.array(a), np.array(b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        return float(np.dot(a, b) / (norm_a * norm_b))


# 全局实例
_embedding_generator = None

def get_embedding_generator() -> EmbeddingGenerator:
    """获取嵌入生成器实例"""
    global _embedding_generator
    if _embedding_generator is None:
        _embedding_generator = EmbeddingGenerator()
    return _embedding_generator