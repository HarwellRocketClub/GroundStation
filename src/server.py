import requests

from PySide2.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout
from PySide2.QtCore import Qt, QRect
from apscheduler.schedulers.background import BackgroundScheduler

from src.rocket_status import RocketStatus


class Server:

    def __init__(self):
        self.host = "http://127.0.0.1:5000"

    def get_connection_status(self) -> RocketStatus:
        try:
            response = requests.get(self.host)
            if 300 > response.status_code >= 200:
                return RocketStatus.from_string(response.json()["status"])
            else:
                return RocketStatus.NO_SERVER_CONNECTION
        except requests.ConnectionError:
            return RocketStatus.NO_SERVER_CONNECTION


class ServerUI(QWidget):

    def __init__(self, left, top, width, height):
        super().__init__()
        # Set layout
        self.server = Server()
        self.setObjectName("server_container")
        self.setGeometry(QRect(left, top, width, height))
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        server_input = QLineEdit()
        server_input.setText(self.server.host)
        server_input.setMaximumWidth(width // 3)
        server_set_button = QPushButton()
        server_set_button.setText("Set Server")
        server_set_button.setMaximumWidth(width // 7)
        layout.addWidget(server_input)
        layout.addWidget(server_set_button)
        # Check the connection to the server every two seconds
        self.status_checker = BackgroundScheduler()
        self.status_checker.add_job(self.update_status, 'interval', seconds=2, id='connection check')
        self.status_checker.start()
        self.status_listeners = []

    def update_status(self):
        for listener in self.status_listeners:
            listener.update_status(self.server.get_connection_status())

    def attach_status_listener(self, listener):
        self.status_listeners.append(listener)
