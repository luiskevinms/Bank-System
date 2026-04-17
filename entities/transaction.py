from datetime import datetime
import pymysql
from enums.transaction_type import TransactionType
from persistence.db import get_connection

class Transaction:

    def __init__(self, id: int, description: str, date: datetime, amount: float, type: TransactionType):
        self.id = id
        self.description = description
        self.date = date
        self.amount = amount
        self.type = type

    @staticmethod
    def get_transactions_by_account(id_account: int):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            query = """
                SELECT id, date, amount, type, description
                FROM `transaction`
                WHERE id_account = %s
                ORDER BY date DESC
            """

            cursor.execute(query, (id_account,))
            rs = cursor.fetchall()

            cursor.close()
            connection.close()

            return rs

        except Exception as ex:
            print("Algo salio mal al conseguir las transactions", ex)
            return []