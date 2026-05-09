import { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { snippetApi } from '../services/api';
import { Snippet } from '../types';
import { getLanguageColor, getLanguageName } from '../utils/languages';
import { 
  Heart, 
  Edit2, 
  Trash2, 
  Copy, 
  ArrowLeft,
  Tag,
  Clock,
  Eye
} from 'lucide-react';

export default function SnippetDetail() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [snippet, setSnippet] = useState<Snippet | null>(null);
  const [loading, setLoading] = useState(true);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    if (id) {
      loadSnippet(id);
    }
  }, [id]);

  const loadSnippet = async (snippetId: string) => {
    try {
      setLoading(true);
      const response = await snippetApi.getById(snippetId);
      setSnippet(response.data);
      // 增加使用次数
      snippetApi.incrementUsage(snippetId);
    } catch (err) {
      console.error('加载片段失败:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = async () => {
    if (!snippet) return;
    try {
      await navigator.clipboard.writeText(snippet.code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('复制失败:', err);
    }
  };

  const handleToggleFavorite = async () => {
    if (!snippet) return;
    try {
      const response = await snippetApi.toggleFavorite(snippet.id);
      setSnippet(response.data);
    } catch (err) {
      console.error('切换收藏失败:', err);
    }
  };

  const handleDelete = async () => {
    if (!snippet) return;
    if (!confirm('确定要删除这个片段吗？')) return;
    
    try {
      await snippetApi.delete(snippet.id);
      navigate('/');
    } catch (err) {
      console.error('删除失败:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (!snippet) {
    return (
      <div className="text-center py-16">
        <p className="text-gray-500">片段不存在</p>
        <Link to="/" className="text-primary-600 hover:underline mt-2 inline-block">
          返回首页
        </Link>
      </div>
    );
  }

  const languageColor = getLanguageColor(snippet.language);
  const languageName = getLanguageName(snippet.language);

  return (
    <div className="animate-fade-in max-w-4xl mx-auto">
      {/* Back Button */}
      <Link
        to="/"
        className="inline-flex items-center gap-2 text-gray-500 hover:text-gray-700 mb-6"
      >
        <ArrowLeft className="w-4 h-4" />
        返回
      </Link>

      {/* Header */}
      <div className="bg-white rounded-xl border border-gray-200 p-6 mb-6">
        <div className="flex items-start justify-between gap-4">
          <div className="flex-1">
            <h1 className="text-2xl font-bold text-gray-900">{snippet.title}</h1>
            
            {/* Meta Info */}
            <div className="flex items-center gap-4 mt-3 text-sm text-gray-500">
              <span
                className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium"
                style={{
                  backgroundColor: `${languageColor}20`,
                  color: languageColor,
                }}
              >
                {languageName}
              </span>
              <span className="flex items-center gap-1">
                <Eye className="w-4 h-4" />
                使用 {snippet.usage_count} 次
              </span>
              <span className="flex items-center gap-1">
                <Clock className="w-4 h-4" />
                {new Date(snippet.created_at).toLocaleDateString('zh-CN')}
              </span>
            </div>
          </div>

          {/* Actions */}
          <div className="flex items-center gap-2">
            <button
              onClick={handleToggleFavorite}
              className={`p-2 rounded-lg transition-colors ${
                snippet.is_favorite
                  ? 'text-red-500 bg-red-50'
                  : 'text-gray-400 hover:text-red-500 hover:bg-red-50'
              }`}
              title={snippet.is_favorite ? '取消收藏' : '收藏'}
            >
              <Heart className={`w-5 h-5 ${snippet.is_favorite ? 'fill-current' : ''}`} />
            </button>
            <Link
              to={`/snippet/${snippet.id}/edit`}
              className="p-2 text-gray-400 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors"
              title="编辑"
            >
              <Edit2 className="w-5 h-5" />
            </Link>
            <button
              onClick={handleDelete}
              className="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
              title="删除"
            >
              <Trash2 className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Description */}
        {snippet.description && (
          <p className="mt-4 text-gray-600">{snippet.description}</p>
        )}

        {/* Tags */}
        {snippet.tags.length > 0 && (
          <div className="flex items-center gap-2 mt-4">
            <Tag className="w-4 h-4 text-gray-400" />
            {snippet.tags.map((tag) => (
              <span
                key={tag}
                className="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full"
              >
                {tag}
              </span>
            ))}
          </div>
        )}
      </div>

      {/* Code Block */}
      <div className="bg-white rounded-xl border border-gray-200 overflow-hidden">
        {/* Code Header */}
        <div className="flex items-center justify-between px-4 py-3 bg-gray-50 border-b border-gray-200">
          <span className="text-sm text-gray-500">代码</span>
          <button
            onClick={handleCopy}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm transition-colors ${
              copied
                ? 'bg-green-100 text-green-700'
                : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
            }`}
          >
            <Copy className="w-4 h-4" />
            {copied ? '已复制' : '复制'}
          </button>
        </div>

        {/* Code Content */}
        <div className="p-4 overflow-x-auto">
          <pre className="text-sm">
            <code className={`language-${snippet.language}`}>
              {snippet.code}
            </code>
          </pre>
        </div>
      </div>
    </div>
  );
}