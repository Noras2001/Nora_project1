import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        if not self.is_username_unique(username):
            raise ValueError(f"Username '{username}' is already taken.")
        
        self.__username = username
        self.__email = email
        self.__password = self.hash_password(password)
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        """
        Хеширование пароля.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        return stored_password == User.hash_password(provided_password)

    @staticmethod
    def is_username_unique(username):
        """
        Проверка уникальности имени пользователя.
        """
        return not any(user.username == username for user in User.users)

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email

    def get_details(self):
        print(f"Username: {self.__username} \nEmail: {self.__email}")

    @classmethod
    def authenticate(cls, username, password):
        """
        Аутентификация пользователя.
        """
        for user in cls.users:
            if user.username == username and cls.check_password(user._User__password, password):
                return user
        return None

class Admin(User):
    def __init__(self, username: str, email: str, password: str, admin_level: int):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        super().get_details()
        print(f"Admin level: {self.admin_level}")
    
    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        for user in User.users:
            print(f"Username: {user.username}, Email: {user.email}")

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        user_to_delete = next((user for user in User.users if user.username == username), None)
        if user_to_delete:
            User.users.remove(user_to_delete)
            print(f"User '{username}' has been deleted.")
        else:
            print(f"User '{username}' not found.")

class Customer(User):
    def __init__(self, username, email, password, address=None):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        super().get_details()
        if self.address:
            print(f"Address: {self.address}")

class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None

    def register(self, user_class, username, email, password, *args):
        """
        Регистрация нового пользователя.
        """
        user = user_class(username, email, password, *args)
        print(f"Registered: {user.username}")

    def login(self, username, password):
        """
        Аутентификация пользователя.
        """
        authenticated_user = User.authenticate(username, password)
        if authenticated_user:
            self.current_user = authenticated_user
            print(f"Authenticated: {authenticated_user.username}")
        else:
            print("Authentication failed.")

    def logout(self):
        """
        Выход пользователя из системы.
        """
        if self.current_user:
            print(f"User '{self.current_user.username}' has logged out.")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        if self.current_user:
            print(f"Current user: {self.current_user.username}")
        else:
            print("No user is currently logged in.")

# Пример использования:
auth_service = AuthenticationService()

# Регистрация пользователя и администратора
auth_service.register(Admin, "nora", "me@nora.org", "12345", 1)
auth_service.register(Customer, "somebody", "somebody@que.com", "111", "404 Zero street")
auth_service.register(Customer, "anybody", "anybody@every.com", "xxx", "200 Word street")
auth_service.register(Customer, "user1", "user1@example.com", "111")
auth_service.register(Customer, "user2", "user2@example.com", "222" )        



# # Вход пользователя
print("Enter username:")
input_username = input()
print("Enter password:")
input_password = input()
auth_service.login(input_username, input_password)

# # Получение информации о текущем пользователе
auth_service.get_current_user()

# Просмотр всех пользователей (доступно только админу)
Admin.list_users()

# Удаление пользователя (доступно только админу)
Admin.delete_user("user2")
Admin.list_users()
# Выход пользователя
auth_service.logout()