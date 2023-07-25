import MySQLdb 
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL database configuration
mysql_config = {
    'host': os.getenv('DATABASE_HOST'),
    'port': 3306,
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASS'),
    'database': os.getenv('DATABASE_NAME'),
}

# MySQL connection setup function
def create_db_connection():
    return MySQLdb.connect(**mysql_config)