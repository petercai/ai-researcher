from .base import BaseConfig

DEFAULT_CONFIG: BaseConfig = {
    "RETRIEVER": "tavily",
    "SIMILARITY_THRESHOLD": 0.42,

    # "EMBEDDING": "google:text-embedding-gecko",  # Google's latest embedding model
    # "EMBEDDING": "google:models/embedding-001",  # Google's latest embedding model
    "EMBEDDING": "google_genai:text-embedding-004",  # Google's latest embedding model
    "FAST_LLM": "google_genai:gemini-2.0-flash",        # Faster, more concise responses
    "SMART_LLM": "google_genai:gemini-2.0-flash",       # More capable, longer responses
    "STRATEGIC_LLM": "google_genai:gemini-2.0-flash",   # Using 2.5 for complex reasoning
    
    # "FAST_LLM": "xai:grok-3-beta",
    # "SMART_LLM": "xai:grok-3-beta",
    # "STRATEGIC_LLM": "xai:grok-3-beta",
    
    # "EMBEDDING": "openai:text-embedding-3-small",
    # "FAST_LLM": "openai:gpt-4o-mini",
    # "SMART_LLM": "openai:gpt-4.1",
    # "STRATEGIC_LLM": "openai:o4-mini",
    "FAST_TOKEN_LIMIT": 2000,
    "SMART_TOKEN_LIMIT": 4000,
    "STRATEGIC_TOKEN_LIMIT": 4000,
    "BROWSE_CHUNK_MAX_LENGTH": 8192,
    "CURATE_SOURCES": False,
    "SUMMARY_TOKEN_LIMIT": 700,
    "TEMPERATURE": 0.4,
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "MAX_SEARCH_RESULTS_PER_QUERY": 5,
    "MEMORY_BACKEND": "local",
    "TOTAL_WORDS": 1200,
    "REPORT_FORMAT": "APA",
    "MAX_ITERATIONS": 3,
    "AGENT_ROLE": None,
    "SCRAPER": "bs",
    "MAX_SCRAPER_WORKERS": 15,
    "MAX_SUBTOPICS": 3,
    "LANGUAGE": "english",
    "REPORT_SOURCE": "web",
    "DOC_PATH": "./my-docs",
    # Deep research specific settings
    "DEEP_RESEARCH_BREADTH": 3,
    "DEEP_RESEARCH_DEPTH": 2,
    "DEEP_RESEARCH_CONCURRENCY": 4,
}
