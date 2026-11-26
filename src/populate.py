import kagglehub
import pandas as pd
import sqlite3

from pathlib import Path
from database import getConnection

DATASETS = {
    "olist_customers_dataset.csv"           : 'customers', 
    "olist_geolocation_dataset.csv"         : 'geolocation', 
    "olist_order_items_dataset.csv"         : 'order_items', 
    "olist_order_payments_dataset.csv"      : 'order_payments', 
    "olist_order_reviews_dataset.csv"       : 'order_reviews', 
    "olist_orders_dataset.csv"              : 'orders', 
    "olist_products_dataset.csv"            : 'products', 
    "olist_sellers_dataset.csv"             : 'sellers', 
    "product_category_name_translation.csv" : 'product_category_name_translation' 
    }


def populateDB(dbPath: Path, conn: sqlite3.Connection):
    try:
        for csvFile, tableName in DATASETS.items():

            filePath = dbPath / csvFile
            
            print(f"INFO: Loading {filePath}...")
            
            # Load into DataFrame and preserve zip codes of leading 0s as string type
            df = pd.read_csv(
                    filePath,
                    dtype={
                        "customer_zip_code_prefix" : str,
                        "seller_zip_code_prefix" : str,
                        "geolocation_zip_code_prefix" : str
                        }
                    )

            # Import the DataFrame
            df.to_sql(
                    tableName, 
                    con=conn, 
                    if_exists="replace", 
                    index=False,
                    chunksize=1000
                    )

            print(f"INFO: Imported {df.shape[0]} records into {tableName}")

    finally:
        conn.close()
    

def loadData():
    
    db_path = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))

    conn = getConnection("olist.db")

    populateDB(db_path, conn)
