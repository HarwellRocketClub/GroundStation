import requests
import asyncio

from PySide2.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout
from PySide2.QtCore import Qt, QRect
from apscheduler.schedulers.background import BackgroundScheduler


class Server:

    def __init__(self):
        self.host = "http://127.0.0.1:5000"

    def is_connected(self) -> bool:
        try:
            response = requests.get(self.host)
            return 300 > response.status_code >= 200
        except requests.ConnectionError:
            return False


class ServerUI(QWidget):

    def __init__(self, left, top, width, height):
        super().__init__()
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
        connection_checker = BackgroundScheduler()
        connection_checker.add_job(self.update_server_connection_status, 'interval', seconds=2, id='connection check')
        connection_checker.start()
        self.connection_listeners = []

    def update_server_connection_status(self):
        for listener in self.connection_listeners:
            listener.update_connection(self.server.is_connected())

    def attach_connection_listener(self, listener):
        self.connection_listeners.append(listener)
