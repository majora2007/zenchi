"""Settings dump."""
from environs import Env

env = Env()
env.read_env()

ANIDB_SERVER = env.str("ANIDB_SERVER")
ANIDB_PORT = env.int("ANIDB_PORT")

ANIDB_USERNAME = env.str("ANIDB_USERNAME")
ANIDB_PASSWORD = env.str("ANIDB_PASSWORD")

ANIDB_ENCRYPT_API_KEY = env.str("ANIDB_ENCRYPT_API_KEY", "")

ZENCHI_CLIENTNAME = env.str("ZENCHI_CLIENTNAME")
ZENCHI_CLIENTVERSION = env.str("ZENCHI_CLIENTVERSION")

MONGODB_URI = env.str("MONGODB_URI", "mongodb://localhost:27017")
