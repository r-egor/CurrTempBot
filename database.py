import sqlite3

class DatabaseUsers:
    # Connect to Database
    def __init__(self):
        self.conn = sqlite3.connect("tg_database.db")
        self.cursor = self.conn.cursor()

    # Add users to Database users
    def add_user(self, user_id, username, first_name, last_name, language_code):
            self.cursor.execute(
                "INSERT OR REPLACE INTO users (user_id, username, first_name, last_name, "
                "language_code) VALUES (?, ?, ?, ?, ?)",
                (user_id, username if username else '',
                 first_name if first_name else '',
                 last_name if last_name else '',
                 language_code if language_code else ''))
            self.conn.commit()

    # Get users from Database users
    def get_user(self):
        self.cursor.execute("SELECT user_id, first_name FROM users")
        return self.cursor.fetchall()

    # Delete user
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        self.conn.commit()

    # Close the database connection
    def __del__(self):
        self.conn.close()