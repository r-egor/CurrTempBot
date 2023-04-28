import sqlite3

def add_user_to_db(user_id, username, first_name, last_name, language_code):
    # Connect to Database
    conn = sqlite3.connect("tg_users.db")
    # Object to interact with the database
    cursor = conn.cursor()

    # Check if user already exists in the database
    cursor.execute("SELECT id FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    if result is None:

        # Add user to BD
        cursor.execute("INSERT INTO users (id, username, first_name, last_name, language_code) VALUES (?, ?, ?, ?, ?)",
                       (user_id, username if username is not None else '',
                        first_name if first_name is not None else '',
                        last_name if last_name is not None else '',
                        language_code if language_code is not None else ''))

    # Save change
    conn.commit()
    # Close
    conn.close()