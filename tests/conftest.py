import pytest
import sqlite3

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = ROOT / "database" / "olist.db"


@pytest.fixture(scope="session")
def dbConnection():
    # setup read only connection
    if not DATABASE_PATH.is_file():
        pytest.fail(f"Database not found: {DATABASE_PATH}")

    conn = sqlite3.connect(DATABASE_PATH.as_uri() + "?mode=ro", uri=True)

    conn.execute("PRAGMA foreign_keys = ON")

    # clean up
    yield conn

    conn.close()


@pytest.fixture
def cursor(dbConnection):
    # setup cursor
    cursor = dbConnection.cursor()

    # clean up
    yield cursor

    cursor.close()
