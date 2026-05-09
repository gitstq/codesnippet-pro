import { useEffect, useState } from 'react';
import { snippetApi } from '../services/api';
import { Snippet } from '../types';
import SnippetCard from '../components/SnippetCard';
import { Loader2, Code2 } from 'lucide-react';

export default function Home() {
  const [snippets, setSnippets] = useState<Snippet[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadSnippets();
  }, []);

  const loadSnippets = async () => {
    try {
      setLoading(true);
      const response = await snippetApi.getAll({ limit: 50 });
      setSnippets(response.data);
    } catch (err) {
      setError('加载片段失败');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <Loader2 className="w-8 h-8 animate-spin text-primary-600" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-64 text-gray-500">
        <p>{error}</p>
        <button
          onClick={loadSnippets}
          className="mt-4 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
        >
          重试
        </button>
      </div>
    );
  }

  return (
    <div className="animate-fade-in">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">我的代码片段</h1>
        <p className="text-gray-500 mt-1">
          共 {snippets.length} 个片段
        </p>
      </div>

      {/* Snippets Grid */}
      {snippets.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-16 text-gray-400">
          <Code2 className="w-16 h-16 mb-4" />
          <p className="text-lg">还没有代码片段</p>
          <p className="text-sm mt-2">点击左侧"新建片段"开始添加</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {snippets.map((snippet) => (
            <SnippetCard key={snippet.id} snippet={snippet} />
          ))}
        </div>
      )}
    </div>
  );
}