import { useEffect, useState } from 'react';
import { tagApi } from '../services/api';
import { Tag } from '../types';
import { Tag as TagIcon, Hash, Loader2 } from 'lucide-react';

export default function Tags() {
  const [tags, setTags] = useState<Tag[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadTags();
  }, []);

  const loadTags = async () => {
    try {
      setLoading(true);
      const response = await tagApi.getAll();
      setTags(response.data);
    } catch (err) {
      console.error('加载标签失败:', err);
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

  return (
    <div className="animate-fade-in">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">标签管理</h1>
        <p className="text-gray-500 mt-1">共 {tags.length} 个标签</p>
      </div>

      {tags.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <TagIcon className="w-16 h-16 mx-auto mb-4" />
          <p className="text-lg">还没有标签</p>
          <p className="text-sm mt-2">创建代码片段时会自动提取标签</p>
        </div>
      ) : (
        <div className="flex flex-wrap gap-3">
          {tags.map((tag) => (
            <div
              key={tag.id}
              className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-200 rounded-lg hover:border-primary-300 hover:shadow-sm transition-all cursor-pointer"
            >
              <Hash className="w-4 h-4" style={{ color: tag.color }} />
              <span className="font-medium text-gray-700">{tag.name}</span>
              <span className="text-sm text-gray-400">({tag.snippet_count})</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}