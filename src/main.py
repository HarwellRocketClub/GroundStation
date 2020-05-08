import sys
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from src.rocket_status import RocketStatus
from src.window import WindowUI


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = WindowUI(self)

    def set_rocket_status(self, status: RocketStatus):
        self.ui.rocket_status_text.setStyleSheet(
            self.ui.rocket_status_text_base_stylesheet +
            "color: #222222;"
            "background-color: {};".format(status.value["colour"])
        )
        self.ui.rocket_status_text.setText(status.value["text"])


def window():
    app = QApplication(sys.argv)
    base_widget = Window()
    base_widget.show()
    base_widget.set_rocket_status(RocketStatus.READY_FOR_FLIGHT)
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
