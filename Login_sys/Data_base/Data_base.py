import pymysql.cursors
from abc import ABC, abstractmethod
import hashlib
import re


class DataBase(ABC):
    """
    Base class for DataBases
    """
    @abstractmethod
    def register_new_user(self, username, password, email): pass

    @abstractmethod
    def verify_if_user_is_registered(self, username): pass

    @abstractmethod
    def get_user_id(self, username): pass

    @abstractmethod
    def get_username(self, id_): pass

    @abstractmethod
    def get_email(self, id_): pass

    @abstractmethod
    def confirm_login(self, username, password, email): pass

    @abstractmethod
    def list_registered_users(self): pass

    @abstractmethod
    def delete_user_from_database(self, username, email): pass

    @abstractmethod
    def change_password(self, password, new_password): pass

    @abstractmethod
    def change_username(self, username, new_username): pass


class Usuarios(DataBase):
    """
    Usuarios Database class.
    """
    _state: dict = {
        # Establish a unique connection with the Database
        'conection': pymysql.connect(
            host='localhost',
            user='root',
            password='Password1331',
            db='usuarios',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self):
        self.conection = self._state['conection']
        self.cursor = self.conection.cursor()

    def register_new_user(self, username, email, password):
        """
        Insert a new user in the
        DB table.
        """
        enc_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()

        self.cursor.execute('INSERT INTO usuarios.login_usuarios (username,'
                            ' email, password_hash) VALUES'
                            '(%s, %s, %s)', [username, email, enc_pass])

        self.conection.commit()

    def verify_if_user_is_registered(self, username):
        """
        Verify if the user's username
        is already in the DB table.
        """
        self.cursor.execute('SELECT username FROM usuarios.login_usuarios'
                            f" WHERE username='{username}'")

        result = self.cursor.fetchall()

        return result

    def get_user_id(self, user_input):
        """
        Get the user id by his username
        or e-mail.
        """
        if re.search(r'@.*\.com', user_input):
            self.cursor.execute('SELECT id FROM usuarios.login_usuarios'
                                f" WHERE email='{user_input}'")

            return self.cursor.fetchall()[0]['id']

        self.cursor.execute('SELECT id FROM usuarios.login_usuarios'
                            f" WHERE username='{user_input}'")

        result = self.cursor.fetchall()

        return result[0]['id'] if result else None

    def get_username(self, user_input):
        """
        Get user's username by his id.
        """
        user_id = self.get_user_id(user_input)
        self.cursor.execute('SELECT username FROM usuarios.login_usuarios'
                            f" WHERE id='{user_id}'")

        return self.cursor.fetchall()[0]['username']

    def get_email(self, user_input):
        """
        Get user's e-mail by his id.
        """
        user_id = self.get_user_id(user_input)
        self.cursor.execute('SELECT email FROM usuarios.login_usuarios'
                            f" WHERE id='{user_id}'")

        return self.cursor.fetchall()[0]['email']

    def confirm_login(self, user_input, password):
        """
        Makes the user's login input
        validation for logging in the
        system.
        """
        user_id = self.get_user_id(user_input)

        if not user_id:
            return None

        enc_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
        self.cursor.execute('SELECT password_hash FROM usuarios.login_usuarios'
                            f" WHERE id='{user_id}'")

        confirmation = enc_pass == self.cursor.fetchall()[0]['password_hash']

        return 'Confirm' if confirmation else 'Invalid password'

    def list_registered_users(self):
        self.cursor.execute('Select * FROM usuarios.login_usuarios')
        return self.cursor.fetchall()

    def delete_user_from_database(self, user_input):
        """
        Delete a user in Database's Table
        using his id.
        """
        try:
            user_id = int(user_input)
        except Exception:
            user_id = self.get_user_id(user_input)

        if not user_id:
            return None

        self.cursor.execute('DELETE FROM usuarios.login_usuarios '
                            f"WHERE id='{user_id}'")

        self.conection.commit()

        return True

    def change_password(self, user_input, new_password):
        """
        Change user's password in Database's
        Table using his id.
        """
        user_id = self.get_user_id(user_input)

        if not user_id:
            return None

        new_enc_pass = hashlib.sha256(
            new_password.strip().encode('utf-8')).hexdigest()
        self.cursor.execute('UPDATE usuarios.login_usuarios SET '
                            f"password_hash='{new_enc_pass}' "
                            f"WHERE id='{user_id}'")
        self.conection.commit()

        return True

    def change_username(self, new_username, email):
        """
        Change user's username in Database's
        Table using his id.
        """
        user_id = self.get_user_id(email)

        if not user_id:
            return None

        self.cursor.execute('UPDATE usuarios.login_usuarios SET '
                            f"username='{new_username}' WHERE id='{user_id}'")
        self.conection.commit()
        return True
