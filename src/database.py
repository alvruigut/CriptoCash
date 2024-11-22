import sqlite3

class Database:
    def __init__(self, db_name="cryptocash.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Crea las tablas necesarias para almacenar monedas y transacciones."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS coins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            signature BLOB NOT NULL,
            is_used BOOLEAN NOT NULL DEFAULT 0
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_user_id TEXT NOT NULL,
            receiver_user_id TEXT NOT NULL,
            coin_id INTEGER,
            FOREIGN KEY(coin_id) REFERENCES coins(id)
        )
        """)
        self.connection.commit()

    def add_coin(self, user_id, signature):
        """Agrega una nueva moneda a la base de datos."""
        self.cursor.execute("INSERT INTO coins (user_id, signature) VALUES (?, ?)", (user_id, signature))
        self.connection.commit()

    def get_unused_coin(self):
        """Obtiene una moneda que no haya sido utilizada."""
        self.cursor.execute("SELECT * FROM coins WHERE is_used = 0 LIMIT 1")
        return self.cursor.fetchone()

    def mark_coin_as_used(self, coin_id):
        """Marca una moneda como utilizada."""
        self.cursor.execute("UPDATE coins SET is_used = 1 WHERE id = ?", (coin_id,))
        self.connection.commit()

    def record_transaction(self, sender_user_id, receiver_user_id, coin_id):
        """Registra una transacción entre un usuario y otro."""
        self.cursor.execute("INSERT INTO transactions (sender_user_id, receiver_user_id, coin_id) VALUES (?, ?, ?)",
                            (sender_user_id, receiver_user_id, coin_id))
        self.connection.commit()

    def get_all_transactions(self):
        """Obtiene todas las transacciones registradas."""
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.connection.close()