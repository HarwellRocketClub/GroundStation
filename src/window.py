import math

from PySide2.QtCore import QMetaObject, QRect, QUrl, Qt
from PySide2.QtWidgets import QWidget, QStatusBar, QGridLayout, QLabel, QMenuBar, QVBoxLayout, QTabWidget

from PySide2.QtWebEngineWidgets import QWebEngineView


class WindowUI(object):

    def __init__(self, main_window):
        # Set up the base UI elements
        if not main_window.objectName():
            main_window.setObjectName("MainWindow")
        main_window.resize(self.width, self.height)
        self.base_widget = QWidget(main_window)
        self.base_widget.setObjectName("base_widget")

        self.base_layout = QVBoxLayout()

        self.set_up_status(parent_layout=self.base_layout)
        self.set_up_tabs(
            parent_layout=self.base_layout,
            left=0, top=self.height // 5,
            width=self.width, height=math.floor(self.height * 0.5)
        )
        self.set_up_bars(main_window)

        main_window.setWindowTitle("Red Kite Avionics Ground Station")
        main_window.setCentralWidget(self.base_widget)

        QMetaObject.connectSlotsByName(main_window)

        self.base_widget.setLayout(self.base_layout)

    def set_up_status(self, parent_layout):
        self.rocket_status_text = QLabel()
        self.rocket_status_text.setObjectName("rocket_status_text")
        self.rocket_status_text.setLayoutDirection(Qt.LeftToRight)
        self.rocket_status_text.setAlignment(Qt.AlignCenter)
        self.rocket_status_text.setText("Loading...")
        self.rocket_status_text_base_stylesheet = "padding: 15px; font: 18pt;"
        self.rocket_status_text.setStyleSheet(self.rocket_status_text_base_stylesheet)
        parent_layout.addWidget(self.rocket_status_text)

    def set_up_tabs(self, parent_layout, left, top, width, height):
        self.tab_widget = TabUI(left, top, width, height)
        parent_layout.addWidget(self.tab_widget)

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

    def __init__(self, left, top, width, height):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Initialise tabs
        self.map_tab = self.set_up_map_tab(left, top, width, height)
        self.data_tab = QWidget()
        self.tabs.resize(width, height)

        # Add tabs
        self.tabs.addTab(self.map_tab, "Rocket Tracker")
        self.tabs.addTab(self.data_tab, "Data")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def set_up_map_tab(self, left, top, width, height) -> QWebEngineView:
        map_tab = QWebEngineView()
        map_tab.setObjectName("web_view")
        map_tab.setGeometry(QRect(left, top, width, height))
        map_tab.setUrl(QUrl("https://www.google.com/maps"))
        return map_tab







