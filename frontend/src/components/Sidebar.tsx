import { NavLink } from 'react-router-dom';
import { 
  Home, 
  Search, 
  Tag, 
  Folder, 
  BarChart3, 
  Plus,
  Heart,
  Settings
} from 'lucide-react';

const navItems = [
  { path: '/', icon: Home, label: '首页' },
  { path: '/search', icon: Search, label: '搜索' },
  { path: '/tags', icon: Tag, label: '标签' },
  { path: '/collections', icon: Folder, label: '集合' },
  { path: '/stats', icon: BarChart3, label: '统计' },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white border-r border-gray-200 flex flex-col">
      {/* Logo */}
      <div className="p-6 border-b border-gray-200">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-primary-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-lg">CS</span>
          </div>
          <div>
            <h1 className="font-bold text-gray-900">CodeSnippet</h1>
            <p className="text-xs text-gray-500">Pro</p>
          </div>
        </div>
      </div>

      {/* New Button */}
      <div className="p-4">
        <NavLink
          to="/snippet/new"
          className="flex items-center justify-center gap-2 w-full bg-primary-600 hover:bg-primary-700 text-white py-2.5 px-4 rounded-lg transition-colors"
        >
          <Plus className="w-5 h-5" />
          <span>新建片段</span>
        </NavLink>
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-3 py-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2.5 rounded-lg transition-colors mb-1 ${
                isActive
                  ? 'bg-primary-50 text-primary-700 font-medium'
                  : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              }`
            }
          >
            <item.icon className="w-5 h-5" />
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>

      {/* Bottom Section */}
      <div className="p-4 border-t border-gray-200">
        <NavLink
          to="/?favorite=true"
          className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-gray-600 hover:bg-gray-50 hover:text-gray-900 transition-colors"
        >
          <Heart className="w-5 h-5" />
          <span>收藏夹</span>
        </NavLink>
      </div>
    </aside>
  );
}