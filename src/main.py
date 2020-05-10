import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from src.rocket_status import RocketStatus
from src.window import WindowUI


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = WindowUI(self)

    def set_rocket_status(self, status: RocketStatus):
        self.ui.rocket_status.set_rocket_status(status)


def window():
    app = QApplication(sys.argv)
    base_widget = Window()
    base_widget.show()
    base_widget.set_rocket_status(RocketStatus.NO_SERVER_CONNECTION)
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
