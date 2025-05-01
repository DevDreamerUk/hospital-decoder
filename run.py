import logging


from app import create_app
from yoyo import read_migrations, get_backend
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_migrations():
    db_url = os.getenv("DATABASE_URL")
    backend = get_backend(db_url)
    migrations = read_migrations("app/migrations")

    migrations_to_apply = backend.to_apply(migrations)
    logger.info("Starting migrations...")
    if migrations_to_apply:
        logger.info(f"Applying {len(migrations_to_apply)} new migrations.")
        backend.apply_migrations(migrations_to_apply)
    else:
        logger.info("No new migrations to apply.")


if __name__ == "__main__":
    run_migrations()
    app.run(host="0.0.0.0", port=80, debug=True)
