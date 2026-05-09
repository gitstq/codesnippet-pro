import { useEffect, useState } from 'react';
import { collectionApi } from '../services/api';
import { Collection } from '../types';
import { Folder, Plus, Loader2 } from 'lucide-react';

export default function Collections() {
  const [collections, setCollections] = useState<Collection[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadCollections();
  }, []);

  const loadCollections = async () => {
    try {
      setLoading(true);
      const response = await collectionApi.getAll();
      setCollections(response.data);
    } catch (err) {
      console.error('加载集合失败:', err);
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
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">集合</h1>
          <p className="text-gray-500 mt-1">共 {collections.length} 个集合</p>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700">
          <Plus className="w-5 h-5" />
          新建集合
        </button>
      </div>

      {collections.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <Folder className="w-16 h-16 mx-auto mb-4" />
          <p className="text-lg">还没有集合</p>
          <p className="text-sm mt-2">创建集合来组织相关代码片段</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {collections.map((collection) => (
            <div
              key={collection.id}
              className="bg-white rounded-xl border border-gray-200 p-6 hover:border-primary-300 hover:shadow-lg transition-all cursor-pointer"
            >
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                  <Folder className="w-6 h-6 text-primary-600" />
                </div>
                <div className="flex-1 min-w-0">
                  <h3 className="font-semibold text-gray-900 truncate">
                    {collection.name}
                  </h3>
                  {collection.description && (
                    <p className="text-sm text-gray-500 mt-1 line-clamp-2">
                      {collection.description}
                    </p>
                  )}
                  <p className="text-sm text-gray-400 mt-2">
                    {collection.snippet_count} 个片段
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}