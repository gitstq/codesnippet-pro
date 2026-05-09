export const SUPPORTED_LANGUAGES = [
  { id: 'python', name: 'Python', color: '#3776AB' },
  { id: 'javascript', name: 'JavaScript', color: '#F7DF1E' },
  { id: 'typescript', name: 'TypeScript', color: '#3178C6' },
  { id: 'java', name: 'Java', color: '#007396' },
  { id: 'go', name: 'Go', color: '#00ADD8' },
  { id: 'rust', name: 'Rust', color: '#DEA584' },
  { id: 'cpp', name: 'C++', color: '#00599C' },
  { id: 'c', name: 'C', color: '#A8B9CC' },
  { id: 'csharp', name: 'C#', color: '#239120' },
  { id: 'php', name: 'PHP', color: '#777BB4' },
  { id: 'ruby', name: 'Ruby', color: '#CC342D' },
  { id: 'swift', name: 'Swift', color: '#FA7343' },
  { id: 'kotlin', name: 'Kotlin', color: '#7F52FF' },
  { id: 'sql', name: 'SQL', color: '#336791' },
  { id: 'html', name: 'HTML', color: '#E34F26' },
  { id: 'css', name: 'CSS', color: '#1572B6' },
  { id: 'shell', name: 'Shell', color: '#89E051' },
  { id: 'yaml', name: 'YAML', color: '#CB171E' },
  { id: 'json', name: 'JSON', color: '#000000' },
  { id: 'markdown', name: 'Markdown', color: '#083FA1' },
  { id: 'dockerfile', name: 'Dockerfile', color: '#2496ED' },
  { id: 'regex', name: 'Regex', color: '#CC6633' },
  { id: 'other', name: 'Other', color: '#808080' },
];

export function getLanguageColor(languageId: string): string {
  const lang = SUPPORTED_LANGUAGES.find(l => l.id === languageId);
  return lang?.color || '#808080';
}

export function getLanguageName(languageId: string): string {
  const lang = SUPPORTED_LANGUAGES.find(l => l.id === languageId);
  return lang?.name || 'Other';
}