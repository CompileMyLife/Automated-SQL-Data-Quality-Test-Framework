import pytest
import sqlite3

def test_db_connection(dbConnection):
    assert dbConnection is not None

def test_query_execution(cursor):
    cursor.execute("SELECT 1")

    result = cursor.fetchone()[0]

    assert result == 1

def test_db_integrity(cursor):
    cursor.execute("PRAGMA integrity_check")

    result = cursor.fetchall()

    assert result == [("ok",)], (f"Database integrity violations: {result}")
