import axios from 'axios';
import { Snippet, SnippetCreate, Tag, Collection, SearchResponse, Stats } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Snippet API
export const snippetApi = {
  getAll: (params?: { language?: string; tag?: string; is_favorite?: boolean; limit?: number; offset?: number }) =>
    api.get<Snippet[]>('/snippets', { params }),
  
  getById: (id: string) =>
    api.get<Snippet>(`/snippets/${id}`),
  
  create: (data: SnippetCreate) =>
    api.post<Snippet>('/snippets', data),
  
  update: (id: string, data: Partial<SnippetCreate>) =>
    api.put<Snippet>(`/snippets/${id}`, data),
  
  delete: (id: string) =>
    api.delete(`/snippets/${id}`),
  
  toggleFavorite: (id: string) =>
    api.post<Snippet>(`/snippets/${id}/favorite`),
  
  incrementUsage: (id: string) =>
    api.post(`/snippets/${id}/usage`),
  
  import: (snippets: SnippetCreate[]) =>
    api.post('/snippets/import', snippets),
  
  export: (format: string, params?: { language?: string; tag?: string }) =>
    api.get(`/snippets/export/${format}`, { params }),
};

// Search API
export const searchApi = {
  search: (q: string, params?: { language?: string; tag?: string; is_favorite?: boolean; limit?: number }) =>
    api.get<SearchResponse>('/search', { params: { q, ...params } }),
  
  semanticSearch: (query: string, limit?: number) =>
    api.post<SearchResponse>('/search/semantic', { query, limit }),
  
  getSimilar: (snippetId: string, limit?: number) =>
    api.get<{ results: { snippet: Snippet; score: number }[] }>(`/search/similar/${snippetId}`, { params: { limit } }),
};

// Tag API
export const tagApi = {
  getAll: () =>
    api.get<Tag[]>('/tags'),
  
  getTree: () =>
    api.get<Tag[]>('/tags/tree'),
  
  create: (data: { name: string; color?: string; parent_id?: string }) =>
    api.post<Tag>('/tags', data),
  
  suggest: (code: string, description?: string) =>
    api.post<{ suggestions: string[] }>('/tags/suggest', { code, description }),
  
  autoTag: (snippetId: string) =>
    api.post<{ tags: string[] }>(`/tags/${snippetId}/auto-tag`),
};

// Collection API
export const collectionApi = {
  getAll: () =>
    api.get<Collection[]>('/collections'),
  
  getById: (id: string) =>
    api.get<Collection>(`/collections/${id}`),
  
  create: (data: { name: string; description?: string; snippet_ids?: string[] }) =>
    api.post<Collection>('/collections', data),
  
  update: (id: string, data: Partial<{ name: string; description: string; snippet_ids: string[] }>) =>
    api.put<Collection>(`/collections/${id}`, data),
  
  delete: (id: string) =>
    api.delete(`/collections/${id}`),
  
  addSnippet: (collectionId: string, snippetId: string) =>
    api.post(`/collections/${collectionId}/snippets/${snippetId}`),
  
  removeSnippet: (collectionId: string, snippetId: string) =>
    api.delete(`/collections/${collectionId}/snippets/${snippetId}`),
};

// Stats API
export const statsApi = {
  getOverview: () =>
    api.get<Stats>('/stats/overview'),
  
  getLanguages: () =>
    api.get<{ languages: Record<string, number>; total: number }>('/stats/languages'),
  
  getTags: () =>
    api.get<{ tags: Record<string, number>; total: number }>('/stats/tags'),
  
  getTrending: () =>
    api.get<{ snippets: Snippet[] }>('/stats/trending'),
  
  getRecent: () =>
    api.get<{ snippets: Snippet[] }>('/stats/recent'),
};

export default api;