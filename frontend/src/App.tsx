import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import SnippetDetail from './pages/SnippetDetail';
import SnippetEdit from './pages/SnippetEdit';
import Search from './pages/Search';
import Tags from './pages/Tags';
import Collections from './pages/Collections';
import Stats from './pages/Stats';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/snippet/:id" element={<SnippetDetail />} />
          <Route path="/snippet/new" element={<SnippetEdit />} />
          <Route path="/snippet/:id/edit" element={<SnippetEdit />} />
          <Route path="/search" element={<Search />} />
          <Route path="/tags" element={<Tags />} />
          <Route path="/collections" element={<Collections />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;