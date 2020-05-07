import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from src.rocket_status import RocketStatus


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        print(self.children())

    def set_rocket_status(self, status: RocketStatus):
        rocket_status_text = self.findChild(QWidget, name="rocket_status_text")
        rocket_status_text.setStyleSheet(
            "color: #222222;"
            "background-color: {};"
            "font: 18pt;".format(status.value["colour"])
        )
        rocket_status_text.setText(status.value["text"])


def window():
    app = QApplication(sys.argv)
    base_widget = Window()
    base_widget.show()
    base_widget.set_rocket_status(RocketStatus.READY_FOR_FLIGHT)
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
