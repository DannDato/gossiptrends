TECH_KEYWORDS = [
    "ai", "inteligencia artificial", "programming", "software",
    "hardware", "apple", "google", "microsoft", "openai",
    "nvidia", "tesla", "startup", "tech", "robot", "gpu"
]

def is_tech_related(text):
    text = text.lower()
    return any(keyword in text for keyword in TECH_KEYWORDS)


def filter_topics(topics):
    return list(set([t for t in topics if is_tech_related(t)]))