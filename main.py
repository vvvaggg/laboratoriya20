import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QComboBox, QDialog, QSizePolicy

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Логин:")
        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.central_widget.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("SELECT id, type FROM users WHERE login=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            user_id, user_type = user
            if user_type == 2:
                self.lab_window = LabWindow(user_id)
                self.lab_window.show()
                self.close()
            elif user_type == 1:
                self.admin_window = AdminWindow(user_id)
                self.admin_window.show()
                self.close()
            elif user_type == 3:
                self.client_window = ClientWindow(user_id)
                self.client_window.show()
                self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

class LabWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Окно лаборанта")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.l = QLabel("Добро пожаловать!\nЛаборатория №20 рада Вас видеть.")
        self.layout.addWidget(self.l)

        self.add_service_button = QPushButton("Добавить услугу")
        self.add_service_button.clicked.connect(self.open_add_service_window)
        self.layout.addWidget(self.add_service_button)

        self.view_services_button = QPushButton("Просмотреть все услуги")
        self.view_services_button.clicked.connect(self.view_services)
        self.layout.addWidget(self.view_services_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.central_widget.setLayout(self.layout)

    def open_add_service_window(self):
        self.add_service_window = AddServiceWindow(self.user_id)
        self.add_service_window.show()

    def view_services(self):
        self.view_services_window = ViewServicesWindow()
        self.view_services_window.show()

    def go_back(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class AdminWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Окно администратора")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.l = QLabel("Добро пожаловать!\nЛаборатория №20 рада Вас видеть.")
        self.layout.addWidget(self.l)

        self.view_services_button = QPushButton("Просмотреть все услуги")
        self.view_services_button.clicked.connect(self.view_services)
        self.layout.addWidget(self.view_services_button)

        self.add_service_button = QPushButton("Добавить услугу")
        self.add_service_button.clicked.connect(self.open_add_service_window)
        self.layout.addWidget(self.add_service_button)

        self.add_new_service_button = QPushButton("Добавить новый вид услуги")
        self.add_new_service_button.clicked.connect(self.open_add_new_service_window)
        self.layout.addWidget(self.add_new_service_button)

        self.view_all_services_button = QPushButton("Просмотреть все виды услуг")
        self.view_all_services_button.clicked.connect(self.view_all_services)
        self.layout.addWidget(self.view_all_services_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.central_widget.setLayout(self.layout)

    def view_services(self):
        self.view_services_window = ViewServicesWindow()
        self.view_services_window.show()

    def open_add_service_window(self):
        self.add_service_window = AddServiceWindow(self.user_id)
        self.add_service_window.show()

    def open_add_new_service_window(self):
        self.add_new_service_window = AddNewServiceWindow()
        self.add_new_service_window.show()

    def view_all_services(self):
        self.view_all_services_window = ViewAllServicesWindow()
        self.view_all_services_window.show()

    def go_back(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class ClientWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Окно клиента")
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.l = QLabel("Добро пожаловать!\nЛаборатория №20 рада Вас видеть.")
        self.layout.addWidget(self.l)

        self.view_services_button = QPushButton("Просмотреть мои анализы")
        self.view_services_button.clicked.connect(self.view_my_services)
        self.layout.addWidget(self.view_services_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.central_widget.setLayout(self.layout)

    def view_my_services(self):
        self.view_my_services_window = ViewMyServicesWindow(self.user_id)
        self.view_my_services_window.show()

    def go_back(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

class AddServiceWindow(QDialog):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Добавить услугу")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.service_label = QLabel("Услуга:")
        self.service_combo = QComboBox()
        self.layout.addWidget(self.service_label)
        self.layout.addWidget(self.service_combo)

        self.result_label = QLabel("Результат:")
        self.result_input = QLineEdit()
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_input)

        self.accepted_label = QLabel("Принято (1 или 0):")
        self.accepted_input = QLineEdit()
        self.layout.addWidget(self.accepted_label)
        self.layout.addWidget(self.accepted_input)

        self.status_label = QLabel("Статус:")
        self.status_combo = QComboBox()
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.status_combo)

        self.analyzer_label = QLabel("Анализатор:")
        self.analyzer_combo = QComboBox()
        self.layout.addWidget(self.analyzer_label)
        self.layout.addWidget(self.analyzer_combo)

        self.user_label = QLabel("Пользователь:")
        self.user_combo = QComboBox()
        self.layout.addWidget(self.user_label)
        self.layout.addWidget(self.user_combo)

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_service)
        self.layout.addWidget(self.add_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.load_combos()

    def load_combos(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()

        cursor.execute("SELECT id, name FROM service")
        services = cursor.fetchall()
        for service in services:
            self.service_combo.addItem(service[1], service[0])

        cursor.execute("SELECT id, name FROM status")
        statuses = cursor.fetchall()
        for status in statuses:
            self.status_combo.addItem(status[1], status[0])

        cursor.execute("SELECT id, name FROM analyzer")
        analyzers = cursor.fetchall()
        for analyzer in analyzers:
            self.analyzer_combo.addItem(analyzer[1], analyzer[0])

        cursor.execute("SELECT id, login FROM users")
        users = cursor.fetchall()
        for user in users:
            self.user_combo.addItem(user[1], user[0])

        connection.close()

    def add_service(self):
        service_id = self.service_combo.currentData()
        result = self.result_input.text()
        accepted = self.accepted_input.text()
        status_id = self.status_combo.currentData()
        analyzer_id = self.analyzer_combo.currentData()
        user_id = self.user_combo.currentData()

        if not service_id or not result or not accepted or not status_id or not analyzer_id or not user_id:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            accepted = int(accepted)
            if accepted not in [0, 1]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Поле 'Принято' должно быть 0 или 1")
            return

        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO blood_services (service, result, accepted, status, analyzer, user) VALUES (%s, %s, %s, %s, %s, %s)",
                       (service_id, result, accepted, status_id, analyzer_id, user_id))
        connection.commit()
        connection.close()

        QMessageBox.information(self, "Успех", "Услуга добавлена")
        self.close()

    def go_back(self):
        self.close()

class AddNewServiceWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить новый вид услуги")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Название услуги:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.price_label = QLabel("Цена услуги:")
        self.price_input = QLineEdit()
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_new_service)
        self.layout.addWidget(self.add_button)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def add_new_service(self):
        name = self.name_input.text()
        price = self.price_input.text()

        if not name or not price:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            price = float(price)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Цена должна быть числом")
            return

        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO service (name, price) VALUES (%s, %s)", (name, price))
        connection.commit()
        connection.close()

        QMessageBox.information(self, "Успех", "Новый вид услуги добавлен")
        self.close()

    def go_back(self):
        self.close()

class ViewServicesWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотр всех услуг")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.load_services()

    def load_services(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT bs.id, s.name, bs.result, bs.accepted, st.name, a.name, u.login
            FROM blood_services bs
            JOIN service s ON bs.service = s.id
            JOIN status st ON bs.status = st.id
            JOIN analyzer a ON bs.analyzer = a.id
            JOIN users u ON bs.user = u.id
            ORDER BY bs.id
        """)
        services = cursor.fetchall()

        self.table.setRowCount(len(services))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Услуга", "Результат", "Принято", "Статус", "Анализатор", "Пользователь"])

        for row, service in enumerate(services):
            for col, data in enumerate(service):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

        connection.close()

    def go_back(self):
        self.close()

class ViewAllServicesWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотр всех видов услуг")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.load_all_services()

    def load_all_services(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, price FROM service")
        services = cursor.fetchall()

        self.table.setRowCount(len(services))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Название", "Цена"])

        for row, service in enumerate(services):
            for col, data in enumerate(service):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

        connection.close()

    def go_back(self):
        self.close()

class ViewMyServicesWindow(QDialog):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Просмотр моих анализов")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.back_button = QPushButton("Назад")
        self.back_button.setFixedHeight(30)
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.load_my_services()

    def load_my_services(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='laboratoriya20')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT bs.id, s.name, bs.result, bs.accepted, st.name, a.name, u.login
            FROM blood_services bs
            JOIN service s ON bs.service = s.id
            JOIN status st ON bs.status = st.id
            JOIN analyzer a ON bs.analyzer = a.id
            JOIN users u ON bs.user = u.id
            WHERE bs.user = %s
            ORDER BY bs.id
        """, (self.user_id,))
        services = cursor.fetchall()

        self.table.setRowCount(len(services))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Услуга", "Результат", "Принято", "Статус", "Анализатор", "Пользователь"])

        for row, service in enumerate(services):
            for col, data in enumerate(service):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

        connection.close()

    def go_back(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())