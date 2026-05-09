import { useEffect, useState } from 'react';
import { statsApi } from '../services/api';
import { Stats as StatsType, Snippet } from '../types';
import { getLanguageColor, getLanguageName } from '../utils/languages';
import { 
  Code2, 
  Heart, 
  Tag, 
  TrendingUp, 
  Clock,
  Loader2
} from 'lucide-react';

export default function Stats() {
  const [stats, setStats] = useState<StatsType | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      setLoading(true);
      const response = await statsApi.getOverview();
      setStats(response.data);
    } catch (err) {
      console.error('加载统计失败:', err);
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

  if (!stats) {
    return (
      <div className="text-center py-16 text-gray-500">
        加载统计信息失败
      </div>
    );
  }

  const languageEntries = Object.entries(stats.language_distribution)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8);

  const tagEntries = Object.entries(stats.tag_distribution)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

  return (
    <div className="animate-fade-in">
      <h1 className="text-2xl font-bold text-gray-900 mb-8">统计概览</h1>

      {/* Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatCard
          icon={Code2}
          label="总片段数"
          value={stats.total_snippets}
          color="blue"
        />
        <StatCard
          icon={Heart}
          label="收藏数"
          value={stats.favorite_count}
          color="red"
        />
        <StatCard
          icon={Tag}
          label="标签数"
          value={Object.keys(stats.tag_distribution).length}
          color="green"
        />
        <StatCard
          icon={TrendingUp}
          label="使用次数"
          value={stats.trending_snippets.reduce((sum, s) => sum + s.usage_count, 0)}
          color="purple"
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Language Distribution */}
        <div className="bg-white rounded-xl border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">语言分布</h2>
          {languageEntries.length === 0 ? (
            <p className="text-gray-400 text-center py-8">暂无数据</p>
          ) : (
            <div className="space-y-3">
              {languageEntries.map(([lang, count]) => {
                const percentage = (count / stats.total_snippets) * 100;
                const color = getLanguageColor(lang);
                return (
                  <div key={lang}>
                    <div className="flex items-center justify-between text-sm mb-1">
                      <span className="font-medium">{getLanguageName(lang)}</span>
                      <span className="text-gray-500">{count} ({percentage.toFixed(1)}%)</span>
                    </div>
                    <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className="h-full rounded-full transition-all"
                        style={{ 
                          width: `${percentage}%`,
                          backgroundColor: color,
                        }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        {/* Tag Distribution */}
        <div className="bg-white rounded-xl border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">热门标签</h2>
          {tagEntries.length === 0 ? (
            <p className="text-gray-400 text-center py-8">暂无数据</p>
          ) : (
            <div className="flex flex-wrap gap-2">
              {tagEntries.map(([tag, count]) => (
                <span
                  key={tag}
                  className="px-3 py-1.5 bg-gray-100 text-gray-700 rounded-full text-sm"
                >
                  {tag} ({count})
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Trending Snippets */}
        <div className="bg-white rounded-xl border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <TrendingUp className="w-5 h-5" />
            热门片段
          </h2>
          {stats.trending_snippets.length === 0 ? (
            <p className="text-gray-400 text-center py-8">暂无数据</p>
          ) : (
            <div className="space-y-3">
              {stats.trending_snippets.slice(0, 5).map((snippet) => (
                <SnippetListItem key={snippet.id} snippet={snippet} />
              ))}
            </div>
          )}
        </div>

        {/* Recent Snippets */}
        <div className="bg-white rounded-xl border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <Clock className="w-5 h-5" />
            最近添加
          </h2>
          {stats.recent_snippets.length === 0 ? (
            <p className="text-gray-400 text-center py-8">暂无数据</p>
          ) : (
            <div className="space-y-3">
              {stats.recent_snippets.slice(0, 5).map((snippet) => (
                <SnippetListItem key={snippet.id} snippet={snippet} />
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

interface StatCardProps {
  icon: React.ElementType;
  label: string;
  value: number;
  color: 'blue' | 'red' | 'green' | 'purple';
}

function StatCard({ icon: Icon, label, value, color }: StatCardProps) {
  const colorClasses = {
    blue: 'bg-blue-50 text-blue-600',
    red: 'bg-red-50 text-red-600',
    green: 'bg-green-50 text-green-600',
    purple: 'bg-purple-50 text-purple-600',
  };

  return (
    <div className="bg-white rounded-xl border border-gray-200 p-6">
      <div className="flex items-center gap-4">
        <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${colorClasses[color]}`}>
          <Icon className="w-6 h-6" />
        </div>
        <div>
          <p className="text-sm text-gray-500">{label}</p>
          <p className="text-2xl font-bold text-gray-900">{value}</p>
        </div>
      </div>
    </div>
  );
}

function SnippetListItem({ snippet }: { snippet: Snippet }) {
  return (
    <div className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
      <div
        className="w-3 h-3 rounded-full flex-shrink-0"
        style={{ backgroundColor: getLanguageColor(snippet.language) }}
      />
      <div className="flex-1 min-w-0">
        <p className="font-medium text-gray-900 truncate">{snippet.title}</p>
        <p className="text-sm text-gray-500">
          {getLanguageName(snippet.language)} · 使用 {snippet.usage_count} 次
        </p>
      </div>
    </div>
  );
}