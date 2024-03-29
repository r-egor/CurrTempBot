import sqlite3

class DatabaseUsers:
    # Connect to Database
    def __init__(self):
        self.conn = sqlite3.connect("/app/tg_database.db")
        self.cursor = self.conn.cursor()

    # Add users to Database users
    def add_user(self, user_id, username, first_name, last_name, language_code):
        self.cursor.execute(
            "INSERT OR REPLACE INTO users (user_id, username, first_name, last_name, "
            "language_code, push) VALUES (?, ?, ?, ?, ?, 1)",
            (user_id, username if username else '',
                first_name if first_name else '',
                last_name if last_name else '',
                language_code if language_code else ''))
        self.conn.commit()

    # Get users from Database users
    def get_user(self):
        self.cursor.execute("SELECT user_id, first_name FROM users WHERE push=1")
        return self.cursor.fetchall()

    # Delete user
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        self.conn.commit()

    # Add currency rate to Database currency
    def insert_currency_data(self, cur_addr, cur_rate):
        self.cursor.execute("INSERT INTO currency (cur_addr, cur_rate) VALUES (?, ?);", (cur_addr, cur_rate))
        self.conn.commit()

    # Get previous rate
    def get_previous_rate(self, currency):
        self.cursor.execute("SELECT cur_rate, cur_addr FROM currency WHERE cur_addr=? ORDER BY cur_time DESC LIMIT 3",
                            (currency,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    # Set notification ON - OFF
    def notification_on_off(self, user_id, push_value):
        self.cursor.execute("UPDATE users SET push=? WHERE user_id=?", (push_value, user_id))
        self.conn.commit()

    # Close the database connection
    def __del__(self):
        self.conn.close()