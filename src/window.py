import math

from PySide2.QtCore import QMetaObject, QRect, QUrl
from PySide2.QtWidgets import QWidget, QStatusBar, QMenuBar, QVBoxLayout, QTabWidget
from PySide2.QtWebEngineWidgets import QWebEngineView

from src.rocket_status import RocketStatusUI, RocketStatus
from src.server import ServerUI


class WindowUI(object):

    def __init__(self, main_window):
        # Set up the base UI elements
        if not main_window.objectName():
            main_window.setObjectName("MainWindow")
        main_window.resize(self.width, self.height)

        self.base_widget = QWidget(main_window)
        self.base_widget.setObjectName("base_widget")
        self.base_layout = QVBoxLayout()

        # Set up the main UI elements
        self.rocket_status = RocketStatusUI(self.base_layout)
        self.tab_widget = TabUI(
            left=0, top=self.height // 5,
            width=self.width, height=math.floor(self.height * 0.5),
            main_ui=self)
        self.base_layout.addWidget(self.tab_widget)
        self.set_up_bars(main_window)

        main_window.setWindowTitle("Red Kite Avionics Ground Station")
        main_window.setCentralWidget(self.base_widget)

        QMetaObject.connectSlotsByName(main_window)

        self.base_widget.setLayout(self.base_layout)

    def set_up_bars(self, main_window):
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName("statusbar")
        main_window.setStatusBar(self.status_bar)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName("menubar")
        self.menu_bar.setGeometry(QRect(0, 0, self.width, self.height // 10))
        main_window.setMenuBar(self.menu_bar)

    @property
    def width(self) -> int:
        return 1200

    @property
    def height(self) -> int:
        return 800


class TabUI(QWidget):

    def __init__(self, left, top, width, height, main_ui: WindowUI):
        super().__init__()
        self.main_ui = main_ui

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Initialise tabs
        self.map_tab = self.set_up_map_tab(left, top, width, height)
        self.data_tab = QWidget()
        self.server_tab = ServerUI(left, top, width, height)
        self.server_tab.attach_status_listener(self)
        self.tabs.resize(width, height)

        # Add tabs
        self.tabs.addTab(self.map_tab, "Rocket Tracker")
        self.tabs.addTab(self.data_tab, "Data")
        self.tabs.addTab(self.server_tab, "Server")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def set_up_map_tab(self, left, top, width, height) -> QWebEngineView:
        map_tab = QWebEngineView()
        map_tab.setObjectName("web_view")
        map_tab.setGeometry(QRect(left, top, width, height))
        map_tab.setUrl(QUrl("https://www.google.com/maps"))
        return map_tab

    def update_status(self, status: RocketStatus):
        self.main_ui.rocket_status.set_rocket_status(status)
