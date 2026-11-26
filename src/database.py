import sqlite3
from pathlib import Path

def getConnection(dbPath: Path) -> sqlite3.Connection:
    # connect/create to database
    conn = sqlite3.connect(dbPath)
    
    # enable foriegn keys
    conn.execute("PRAGMA foriegn_keys = ON")

    return conn
