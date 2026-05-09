"""编程语言工具"""

# 支持的语言列表
SUPPORTED_LANGUAGES = {
    "python": {
        "name": "Python",
        "extensions": [".py", ".pyw", ".pyi"],
        "aliases": ["py", "python3"],
        "color": "#3776AB"
    },
    "javascript": {
        "name": "JavaScript",
        "extensions": [".js", ".mjs", ".cjs"],
        "aliases": ["js", "node"],
        "color": "#F7DF1E"
    },
    "typescript": {
        "name": "TypeScript",
        "extensions": [".ts", ".tsx"],
        "aliases": ["ts"],
        "color": "#3178C6"
    },
    "java": {
        "name": "Java",
        "extensions": [".java"],
        "aliases": [],
        "color": "#007396"
    },
    "go": {
        "name": "Go",
        "extensions": [".go"],
        "aliases": ["golang"],
        "color": "#00ADD8"
    },
    "rust": {
        "name": "Rust",
        "extensions": [".rs"],
        "aliases": [],
        "color": "#DEA584"
    },
    "cpp": {
        "name": "C++",
        "extensions": [".cpp", ".cc", ".cxx", ".hpp"],
        "aliases": ["c++"],
        "color": "#00599C"
    },
    "c": {
        "name": "C",
        "extensions": [".c", ".h"],
        "aliases": [],
        "color": "#A8B9CC"
    },
    "csharp": {
        "name": "C#",
        "extensions": [".cs"],
        "aliases": ["cs", "dotnet"],
        "color": "#239120"
    },
    "php": {
        "name": "PHP",
        "extensions": [".php"],
        "aliases": [],
        "color": "#777BB4"
    },
    "ruby": {
        "name": "Ruby",
        "extensions": [".rb"],
        "aliases": [],
        "color": "#CC342D"
    },
    "swift": {
        "name": "Swift",
        "extensions": [".swift"],
        "aliases": [],
        "color": "#FA7343"
    },
    "kotlin": {
        "name": "Kotlin",
        "extensions": [".kt", ".kts"],
        "aliases": [],
        "color": "#7F52FF"
    },
    "sql": {
        "name": "SQL",
        "extensions": [".sql"],
        "aliases": [],
        "color": "#336791"
    },
    "html": {
        "name": "HTML",
        "extensions": [".html", ".htm"],
        "aliases": [],
        "color": "#E34F26"
    },
    "css": {
        "name": "CSS",
        "extensions": [".css"],
        "aliases": [],
        "color": "#1572B6"
    },
    "shell": {
        "name": "Shell",
        "extensions": [".sh", ".bash", ".zsh"],
        "aliases": ["bash", "zsh", "powershell"],
        "color": "#89E051"
    },
    "yaml": {
        "name": "YAML",
        "extensions": [".yml", ".yaml"],
        "aliases": [],
        "color": "#CB171E"
    },
    "json": {
        "name": "JSON",
        "extensions": [".json"],
        "aliases": [],
        "color": "#000000"
    },
    "markdown": {
        "name": "Markdown",
        "extensions": [".md", ".markdown"],
        "aliases": ["md"],
        "color": "#083FA1"
    },
    "dockerfile": {
        "name": "Dockerfile",
        "extensions": ["Dockerfile"],
        "aliases": ["docker"],
        "color": "#2496ED"
    },
    "regex": {
        "name": "Regex",
        "extensions": [],
        "aliases": ["regexp"],
        "color": "#CC6633"
    },
    "other": {
        "name": "Other",
        "extensions": [],
        "aliases": [],
        "color": "#808080"
    }
}


def get_language_list() -> list:
    """获取语言列表"""
    return [
        {
            "id": lang_id,
            "name": info["name"],
            "color": info["color"]
        }
        for lang_id, info in SUPPORTED_LANGUAGES.items()
    ]


def detect_language(code: str, filename: str = "") -> str:
    """检测代码语言"""
    # 根据文件名检测
    if filename:
        for lang_id, info in SUPPORTED_LANGUAGES.items():
            for ext in info["extensions"]:
                if filename.endswith(ext):
                    return lang_id
    
    # 根据代码特征检测
    patterns = {
        "python": [r'^\s*def\s+\w+\s*\(', r'^\s*import\s+\w+', r'^\s*from\s+\w+\s+import', r'print\s*\(', r':\s*$'],
        "javascript": [r'function\s+\w+\s*\(', r'const\s+\w+\s*=', r'let\s+\w+\s*=', r'var\s+\w+\s*=', r'=>\s*\{', r'console\.log'],
        "typescript": [r':\s*(string|number|boolean|any)\s*[;=]', r'interface\s+\w+', r'type\s+\w+\s*='],
        "java": [r'public\s+class', r'private\s+\w+\s+\w+;', r'System\.out\.println'],
        "go": [r'func\s+\w+\s*\(', r'package\s+\w+', r'fmt\.Print'],
        "rust": [r'fn\s+\w+\s*\(', r'let\s+mut\s+', r'impl\s+'),
        "cpp": [r'#include\s*<', r'std::', r'int\s+main\s*\('],
        "c": [r'#include\s*<', r'int\s+main\s*\(', r'printf\s*\('],
        "csharp": [r'using\s+System', r'namespace\s+\w+', r'Console\.WriteLine'],
        "php": [r'<\?php', r'\$\w+\s*=', r'echo\s+'],
        "ruby": [r'def\s+\w+', r'require\s+', r'puts\s+'],
        "swift": [r'func\s+\w+\s*\([^)]*\)\s*->', r'import\s+\w+', r'let\s+\w+\s*:\s*\w+'],
        "kotlin": [r'fun\s+\w+\s*\(', r'val\s+\w+', r'var\s+\w+'],
        "sql": [r'SELECT\s+', r'INSERT\s+INTO', r'CREATE\s+TABLE', r'UPDATE\s+\w+\s+SET'],
        "html": [r'<html', r'<div', r'<script', r'<!DOCTYPE'],
        "css": [r'\{\s*\w+\s*:', r'@media', r'@import'],
        "shell": [r'^#!/bin/bash', r'^#!/bin/sh', r'echo\s+', r'\$\w+'],
        "yaml": [r'^\w+:\s*\w+', r'^-\s+\w+:', r'^---\s*$'],
        "json": [r'^\{', r'^\[', r'"\w+":\s*'],
        "dockerfile": [r'^FROM\s+', r'^RUN\s+', r'^COPY\s+', r'^CMD\s+'],
    }
    
    import re
    scores = {}
    
    for lang_id, pattern_list in patterns.items():
        score = 0
        for pattern in pattern_list:
            if re.search(pattern, code, re.MULTILINE | re.IGNORECASE):
                score += 1
        if score > 0:
            scores[lang_id] = score
    
    if scores:
        return max(scores, key=scores.get)
    
    return "other"


def get_language_name(language_id: str) -> str:
    """获取语言名称"""
    info = SUPPORTED_LANGUAGES.get(language_id)
    return info["name"] if info else "Other"


def get_language_color(language_id: str) -> str:
    """获取语言颜色"""
    info = SUPPORTED_LANGUAGES.get(language_id)
    return info["color"] if info else "#808080"