import pytest

EXPECTED_TABLE_COUNTS = { 
        "customers" : 99441,
        "orders" : 99441,
        "order_items" : 112650,
        "order_payments" : 103886,
        "order_reviews" 99224,
        "products" : 32951,
        "sellers" : 3095,
        "geolocation" : 1000163,
        "product_category_translation": 71
        }
    }

@pytest.mark.parametrize("table_name", "record_count", EXPECTED_TABLE_COUNTS.items())
def test_record_count(cursor, table_name, record_count):
    cursor.execute('''
        SELECT COUNT(*) FROM ?
    ''', (table_name,))

    actual_count = cursor.fetchone()[0]

    assert actual_count == record_count, (
            f"Record count mismatch in {table_name}, expected {record_count}, recieved {actual_count}"
        )
