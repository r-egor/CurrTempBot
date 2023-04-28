import sqlite3

class DatabaseUsers:
    # Connect to Database
    def __init__(self):
        self.conn = sqlite3.connect("tg_users.db")
        self.cursor = self.conn.cursor()

    # Add users to tg_users.db
    def add_user(self, user_id, username, first_name, last_name, language_code):
        # Check if user already exists in the database
        self.cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()

        # If user does not exist, add them to the database
        if result is None:
            self.cursor.execute(
                "INSERT INTO users (user_id, username, first_name, last_name, language_code) VALUES (?, ?, ?, ?, ?)",
                (user_id, username if username is not None else '',
                 first_name if first_name is not None else '',
                 last_name if last_name is not None else '',
                 language_code if language_code is not None else ''))
            self.conn.commit()

    # Get users from users
    def get_user(self):
        self.cursor.execute("SELECT user_id, first_name FROM users")
        return self.cursor.fetchall()

    # Close the database connection
    def __del__(self):
        self.conn.close()