import bcrypt
from database.mysql import create_db_connection

# Function to perform login check
def check_login(username: str, password: str):
    db_cursor = None
    try:
        db_connection = create_db_connection()
        db_cursor = db_connection.cursor()

        # Get the hashed password from the database for the given username
        query = "SELECT password FROM users WHERE username = %s"
        db_cursor.execute(query, (username,))
        result = db_cursor.fetchone()

        # If the username is found in the database
        if result:
            hashed_password = result[0].encode('utf-8')

            # Check if the provided password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True

        return False
    except Exception as e:
        # Handle any exceptions, such as database connection or query errors
        print(f"Error: {e}")
        return False

    finally:
        # Close the database connection to free resources
        if db_cursor is not None:
            db_cursor.close()
        db_connection.close()
