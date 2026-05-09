export interface Snippet {
  id: string;
  title: string;
  code: string;
  language: string;
  description: string;
  tags: string[];
  source: string;
  created_at: string;
  updated_at: string;
  usage_count: number;
  is_favorite: boolean;
  is_public: boolean;
}

export interface SnippetCreate {
  title: string;
  code: string;
  language: string;
  description?: string;
  tags?: string[];
  source?: string;
  is_favorite?: boolean;
  is_public?: boolean;
}

export interface Tag {
  id: string;
  name: string;
  color: string;
  parent_id?: string;
  snippet_count: number;
  children?: Tag[];
}

export interface Collection {
  id: string;
  name: string;
  description: string;
  created_at: string;
  snippet_count: number;
  snippet_ids: string[];
}

export interface SearchResult {
  snippet: Snippet;
  score: number;
  highlights: string[];
}

export interface SearchResponse {
  results: SearchResult[];
  total: number;
  query: string;
  search_time: number;
}

export interface Stats {
  total_snippets: number;
  favorite_count: number;
  language_distribution: Record<string, number>;
  tag_distribution: Record<string, number>;
  trending_snippets: Snippet[];
  recent_snippets: Snippet[];
}