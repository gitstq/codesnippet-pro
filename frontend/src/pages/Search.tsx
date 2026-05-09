import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { searchApi } from '../services/api';
import { SearchResult } from '../types';
import SnippetCard from '../components/SnippetCard';
import { Search as SearchIcon, Loader2, Sparkles } from 'lucide-react';

export default function Search() {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialQuery = searchParams.get('q') || '';
  
  const [query, setQuery] = useState(initialQuery);
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [searchTime, setSearchTime] = useState(0);
  const [isSemantic, setIsSemantic] = useState(false);

  useEffect(() => {
    if (initialQuery) {
      performSearch(initialQuery);
    }
  }, [initialQuery]);

  const performSearch = async (searchQuery: string, semantic = false) => {
    if (!searchQuery.trim()) return;
    
    try {
      setLoading(true);
      let response;
      
      if (semantic) {
        response = await searchApi.semanticSearch(searchQuery, 20);
      } else {
        response = await searchApi.search(searchQuery, {}, 20);
      }
      
      setResults(response.data.results);
      setSearchTime(response.data.search_time);
    } catch (err) {
      console.error('搜索失败:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSearchParams({ q: query });
    performSearch(query, isSemantic);
  };

  return (
    <div className="animate-fade-in">
      {/* Search Header */}
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-4">搜索代码片段</h1>
        
        <form onSubmit={handleSubmit} className="flex gap-4">
          <div className="flex-1 relative">
            <SearchIcon className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="输入关键词搜索..."
              className="w-full pl-12 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent text-lg"
            />
          </div>
          
          <button
            type="button"
            onClick={() => setIsSemantic(!isSemantic)}
            className={`flex items-center gap-2 px-4 py-3 rounded-lg border transition-colors ${
              isSemantic
                ? 'bg-purple-50 border-purple-300 text-purple-700'
                : 'border-gray-300 text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Sparkles className="w-5 h-5" />
            <span>AI语义</span>
          </button>
          
          <button
            type="submit"
            disabled={loading || !query.trim()}
            className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              '搜索'
            )}
          </button>
        </form>

        {/* Search Tips */}
        <div className="mt-4 text-sm text-gray-500">
          <p>搜索提示:</p>
          <ul className="list-disc list-inside mt-1 space-y-1">
            <li>支持关键词搜索标题、代码、描述和标签</li>
            <li>使用 AI语义搜索 可以找到语义相关的代码</li>
            <li>高级语法: language:python tag:web</li>
          </ul>
        </div>
      </div>

      {/* Results */}
      {results.length > 0 && (
        <div className="mb-4 text-sm text-gray-500">
          找到 {results.length} 个结果
          {searchTime > 0 && ` (耗时 ${(searchTime * 1000).toFixed(0)}ms)`}
        </div>
      )}

      {results.length === 0 && !loading && query && (
        <div className="text-center py-16 text-gray-400">
          <SearchIcon className="w-16 h-16 mx-auto mb-4" />
          <p className="text-lg">未找到相关结果</p>
          <p className="text-sm mt-2">尝试使用不同的关键词或开启AI语义搜索</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {results.map((result) => (
          <SnippetCard key={result.snippet.id} snippet={result.snippet} />
        ))}
      </div>
    </div>
  );
}