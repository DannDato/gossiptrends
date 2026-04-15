from config import (
    ENABLE_REDDIT,
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_POST_LIMIT,
    REDDIT_SUBREDDITS,
    REDDIT_USER_AGENT,
)

def get_reddit_posts():
    if not ENABLE_REDDIT:
        return []

    if not REDDIT_CLIENT_ID or not REDDIT_CLIENT_SECRET:
        print("Aviso: Reddit no esta configurado en .env. Se omite esta fuente.")
        return []

    try:
        import praw
    except ImportError:
        print("Aviso: praw no esta instalado. Se omite la fuente de Reddit.")
        return []

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )

    posts = []

    for sub in REDDIT_SUBREDDITS:
        for post in reddit.subreddit(sub).hot(limit=REDDIT_POST_LIMIT):
            posts.append(post.title)

    return posts