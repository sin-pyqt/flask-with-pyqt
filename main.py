import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import QWebEngineView
import os
import sys


PORT = 5000
ROOT_URL = "http://localhost:{}".format(PORT)


class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # components

        self.left_btn = QPushButton("Show")
        self.right_btn = QPushButton("Hide")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(ROOT_URL))

        ## functionality

        # show hide
        self.left_btn.clicked.connect(self.show_b)
        self.right_btn.clicked.connect(self.hide_b)

        # layout

        layout = QHBoxLayout()

        layout.addWidget(self.left_btn)
        layout.addWidget(self.right_btn)
        layout.addWidget(self.browser)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_b(self):
        self.browser.show()

    def hide_b(self):
        self.browser.hide()


app = QApplication(sys.argv)

window = MainWindow()

# Running Flask Server as Thread

from web.server import server

webapp = FlaskThread(server)
webapp.start()

app.aboutToQuit.connect(webapp.terminate)   # End Flask Server Thread Before Quiting

window.show()

app.exec()
