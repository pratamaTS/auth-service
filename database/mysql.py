import MySQLdb 
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL database configuration
mysql_config = {
    'host': os.getenv('DATABAES_HOST'),
    'user': os.getenv('DATABAES_USER'),
    'password': os.getenv('DATABAES_PASS'),
    'database': os.getenv('DATABASE_NAME'),
}

# MySQL connection setup function
def create_db_connection():
    return MySQLdb.connect(**mysql_config)