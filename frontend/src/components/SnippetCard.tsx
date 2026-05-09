import { Link } from 'react-router-dom';
import { Heart, Copy, ExternalLink } from 'lucide-react';
import { Snippet } from '../types';
import { getLanguageColor, getLanguageName } from '../utils/languages';

interface SnippetCardProps {
  snippet: Snippet;
}

export default function SnippetCard({ snippet }: SnippetCardProps) {
  const languageColor = getLanguageColor(snippet.language);
  const languageName = getLanguageName(snippet.language);

  const handleCopy = async (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    try {
      await navigator.clipboard.writeText(snippet.code);
      // 可以添加toast提示
    } catch (err) {
      console.error('复制失败:', err);
    }
  };

  return (
    <Link
      to={`/snippet/${snippet.id}`}
      className="block bg-white rounded-xl border border-gray-200 hover:border-primary-300 hover:shadow-lg transition-all duration-200 group"
    >
      {/* Header */}
      <div className="p-4 border-b border-gray-100">
        <div className="flex items-start justify-between gap-2">
          <h3 className="font-semibold text-gray-900 line-clamp-1 group-hover:text-primary-600 transition-colors">
            {snippet.title}
          </h3>
          {snippet.is_favorite && (
            <Heart className="w-4 h-4 text-red-500 fill-red-500 flex-shrink-0" />
          )}
        </div>
        
        {/* Language & Meta */}
        <div className="flex items-center gap-3 mt-2">
          <span
            className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium"
            style={{
              backgroundColor: `${languageColor}20`,
              color: languageColor,
            }}
          >
            {languageName}
          </span>
          <span className="text-xs text-gray-400">
            使用 {snippet.usage_count} 次
          </span>
        </div>
      </div>

      {/* Code Preview */}
      <div className="p-4 bg-gray-50">
        <pre className="text-xs text-gray-600 line-clamp-3 overflow-hidden font-mono">
          <code>{snippet.code}</code>
        </pre>
      </div>

      {/* Footer */}
      <div className="p-4 border-t border-gray-100">
        <div className="flex items-center justify-between">
          {/* Tags */}
          <div className="flex items-center gap-1 flex-wrap">
            {snippet.tags.slice(0, 3).map((tag) => (
              <span
                key={tag}
                className="px-2 py-0.5 bg-gray-100 text-gray-600 text-xs rounded-full"
              >
                {tag}
              </span>
            ))}
            {snippet.tags.length > 3 && (
              <span className="text-xs text-gray-400">
                +{snippet.tags.length - 3}
              </span>
            )}
          </div>

          {/* Actions */}
          <div className="flex items-center gap-1">
            <button
              onClick={handleCopy}
              className="p-1.5 text-gray-400 hover:text-primary-600 hover:bg-primary-50 rounded transition-colors"
              title="复制代码"
            >
              <Copy className="w-4 h-4" />
            </button>
            <span className="p-1.5 text-gray-400 group-hover:text-primary-600 transition-colors">
              <ExternalLink className="w-4 h-4" />
            </span>
          </div>
        </div>
      </div>
    </Link>
  );
}