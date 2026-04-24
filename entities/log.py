from datetime import datetime
from entities.user import User
from enums.log_type import LogType
from persistence.db import get_connection

class Log:
    
    def __init__(self,id: int, date: datetime, user: User, description: str, type: LogType):
        self.id = id
        self.date = date
        self.user = user
        self.description = description
        self.type = type

    def save_log(user: User, description: str, type: LogType) -> bool:
        """
            Guarda un registro de log en la base de datos.

            Parameters:
                user (User): Usuario asociado al log.
                description (str): Descripción del evento registrado.
                type (LogType): Tipo de evento registrado.

            Returns:
                bool: True si el log se guardó correctamente; de lo contrario, False.
        """
        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = "INSERT INTO log (date, id_user, description, type) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (datetime.now(), user.id, description, type.value))
            connection.commit()

            cursor.close()
            connection.close()
            return True
        except Exception as ex:
            print(f"Error saving log:{ex}")
            return False