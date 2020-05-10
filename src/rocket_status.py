from enum import Enum, unique
from PySide2.QtWidgets import QWidget, QLabel
from PySide2.QtCore import Qt


@unique
class RocketStatus(Enum):
    IN_FLIGHT = {"colour": "rgb(51, 255, 51)", "text": "In Flight"}
    READY_FOR_FLIGHT = {"colour": "rgb(51, 153, 255)", "text": "Ready For Flight"}
    READYING = {"colour": "rgb(255, 255, 51)", "text": "Readying"}
    OFFLINE = {"colour": "rgb(255, 165, 0)", "text": "Rocket offline"}
    NO_SERVER_CONNECTION = {"colour": "rgb(255, 51, 51)", "text": "No connection to server"}

    @classmethod
    def from_string(cls, string: str):
        for status in RocketStatus:
            if status.value["text"] == string:
                return status
        raise ValueError("{} is not a valid status".format(string))


class RocketStatusUI(QWidget):

    def __init__(self, parent_layout):
        super().__init__()
        self.rocket_status_text = QLabel()
        self.rocket_status_text.setObjectName("rocket_status_text")
        self.rocket_status_text.setLayoutDirection(Qt.LeftToRight)
        self.rocket_status_text.setAlignment(Qt.AlignCenter)
        self.rocket_status_text_base_stylesheet = "padding: 15px; font: 18pt;"
        parent_layout.addWidget(self.rocket_status_text)

    def set_rocket_status(self, status: RocketStatus):
        self.rocket_status_text.setStyleSheet(
            self.rocket_status_text_base_stylesheet +
            "color: #222222;"
            "background-color: {};".format(status.value["colour"])
        )
        self.rocket_status_text.setText(status.value["text"])
