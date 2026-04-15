import os


def load_env_file(path=".env"):
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


load_env_file()


def get_env_bool(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default

    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_env_list(name, default):
    value = os.getenv(name)
    if not value:
        return default

    return [item.strip() for item in value.split(",") if item.strip()]


def get_env_int(name, default):
    value = os.getenv(name)
    if value is None or value == "":
        return default

    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"La variable de entorno {name} debe ser un entero.") from error


REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "gossip-topic-finder")
ENABLE_REDDIT = get_env_bool("ENABLE_REDDIT", False)
REDDIT_SUBREDDITS = get_env_list(
    "REDDIT_SUBREDDITS",
    ["technology", "programming", "gadgets", "artificial"],
)
REDDIT_POST_LIMIT = get_env_int("REDDIT_POST_LIMIT", 10)

TRENDS_LANGUAGE = os.getenv("TRENDS_LANGUAGE", "es-MX")
TRENDS_TIMEZONE = get_env_int("TRENDS_TIMEZONE", 360)
TRENDS_REGION = os.getenv("TRENDS_REGION", "mexico")
TRENDS_REGIONS = get_env_list(
    "TRENDS_REGIONS",
    ["mexico", "colombia", "spain", "argentina"],
)