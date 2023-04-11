from envparse import Env

env = Env()


DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql://rseitov:postgres@localhost:5432/oil_pumps"
)
