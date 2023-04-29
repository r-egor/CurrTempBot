import sqlite3

class DatabaseUsers:
    # Connect to Database
    def __init__(self):
        self.conn = sqlite3.connect("tg_users.db")
        self.cursor = self.conn.cursor()

    # Add users to Database users
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

    # Get users from Database users
    def get_user(self):
        self.cursor.execute("SELECT user_id, first_name FROM users")
        return self.cursor.fetchall()

    # Update users in Database users
    def update_user(self, user_id, username, first_name, last_name, language_code):
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()

        # If user exists, update the data
        if result is not None:
            if username is not None and result[1] != username:
                self.cursor.execute("UPDATE users SET username=? WHERE user_id=?", (username, user_id))
            if first_name is not None and result[2] != first_name:
                self.cursor.execute("UPDATE users SET first_name=? WHERE user_id=?", (first_name, user_id))
            if last_name is not None and result[3] != last_name:
                self.cursor.execute("UPDATE users SET last_name=? WHERE user_id=?", (last_name, user_id))
            if language_code is not None and result[4] != language_code:
                self.cursor.execute("UPDATE users SET language_code=? WHERE user_id=?", (language_code, user_id))
            self.conn.commit()

    # Close the database connection
    def __del__(self):
        self.conn.close()