from sources.trends import get_trending_searches
from sources.reddit import get_reddit_posts
from utils.filter import filter_topics

def main():
    print("🔍 Buscando tendencias...\n")

    trends = get_trending_searches()
    reddit = get_reddit_posts()

    all_topics = trends + reddit

    filtered = filter_topics(all_topics)

    print("🔥 TOP IDEAS PARA VIDEO:\n")

    for i, topic in enumerate(filtered[:10], 1):
        print(f"{i}. {topic}")

if __name__ == "__main__":
    main()