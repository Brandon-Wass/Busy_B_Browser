#! python
import sys
import os
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Busy B Private Browser")
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "busyb.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.back_button = QAction("Back", self)
        self.back_button.setIcon(QIcon.fromTheme("go-previous"))
        self.back_button.triggered.connect(self.browser.back)
        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.addAction(self.back_button)
        self.forward_button = QAction("Forward", self)
        self.forward_button.setIcon(QIcon.fromTheme("go-next"))
        self.forward_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(self.forward_button)
        self.reload_button = QAction("Reload", self)
        self.reload_button.setIcon(QIcon.fromTheme("view-refresh"))
        self.reload_button.triggered.connect(self.browser.reload)
        self.toolbar.addAction(self.reload_button)
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        self.toolbar.addWidget(self.address_bar)
        self.browser.urlChanged.connect(self.update_address_bar)
        self.download_progress = QProgressBar()
        self.download_progress.setMaximum(100)
        self.access_button = QPushButton("Access Downloaded File")
        self.access_button.setEnabled(False)
        self.download_layout = QHBoxLayout()
        self.download_layout.setContentsMargins(0, 0, 0, 0)
        spacer_item = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.download_layout.addItem(spacer_item)
        self.download_layout.addWidget(self.download_progress)
        self.download_layout.addWidget(self.access_button)
        self.bottom_bar = QFrame()
        self.bottom_bar.setLayout(self.download_layout)
        self.statusBar().addPermanentWidget(self.bottom_bar)
        self.bottom_bar.setMinimumHeight(20)
        self.bottom_bar.setMaximumHeight(20)
        self.extensions = ['.com', '.org', '.net', '.edu', '.gov', '.mil', '.int', '.info',
                           '.io', '.biz', '.name', '.pro', '.coop', '.aero', '.museum']
        profile.downloadRequested.connect(self.download_requested)
        self.current_download = None
        profile.downloadRequested.connect(self.track_download_progress)
        self.access_button.clicked.connect(self.open_downloaded_file)
    def load_url(self):
        input_text = self.address_bar.text()
        if any(ext in input_text for ext in self.extensions):
            url = QUrl.fromUserInput(input_text)
        else:
            url = QUrl.fromUserInput(f'https://duckduckgo.com/?q={input_text}')
        self.browser.load(url)
    def update_address_bar(self):
        self.address_bar.setText(self.browser.url().toString())
    def download_requested(self, download):
        reply = QMessageBox.question(self, "Download File", "Do you want to download this file?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.current_download = download
            download.accept()
    def track_download_progress(self, download):
        if download == self.current_download:
            download.finished.connect(self.download_finished)
            download.downloadProgress.connect(self.update_download_progress)
    def update_download_progress(self, bytes_received, total_bytes):
        if total_bytes > 0:
            progress = int((bytes_received / total_bytes) * 100)
            self.download_progress.setValue(progress)
    def download_finished(self):
        self.download_progress.setValue(0)
        self.access_button.setEnabled(True)
    def open_downloaded_file(self):
        if self.current_download:
            download_path = self.current_download.path()
            if download_path:
                directory_path = os.path.dirname(download_path)
                QDesktopServices.openUrl(QUrl.fromLocalFile(directory_path))
    def closeEvent(self, event):
        event.accept()
def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()