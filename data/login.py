import bcrypt
from database.mysql import create_db_connection

# Function to perform login check
def check_login(username: str, password: str):
    db_connection = create_db_connection()
    db_cursor = db_connection.cursor()
    try:
        # Get the hashed password from the database for the given username
        query = "SELECT * FROM users WHERE username = %s"
        db_cursor.execute(query, (username,))
        result = db_cursor.fetchone()
        user_data = dict(zip([col[0] for col in db_cursor.description], result))
        print("Result from the database:", user_data)
        # If the username is found in the database
        if user_data and user_data['status'] == 'active':
            hashed_password = user_data['password'].encode('utf-8')
            print(hashed_password)

            # Check if the provided password matches the hashed password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return user_data

        return False
    except Exception as e:
        # Handle any exceptions, such as database connection or query errors
        print(f"Error: {e}")
        return False

    finally:
        # Close the database connection to free resources
        if db_cursor is not None:
            db_cursor.close()
        if db_connection is not None:
            db_connection.close()

def update_user_token(user_data):
    db_connection = create_db_connection()
    db_cursor = db_connection.cursor()

    try:
        # Update the user in the database with the new token
        query = "UPDATE users SET access_token = %s WHERE username = %s"
        db_cursor.execute(query, (user_data['access_token'], user_data['username']))
        db_connection.commit()
    except Exception as e:
        db_connection.rollback()
        print(f"Error: {e}")

    finally:
        db_cursor.close()
        db_connection.close()