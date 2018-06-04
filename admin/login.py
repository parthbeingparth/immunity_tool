from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from Table_PYQT import NewWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self._new_window = None
        self.win = QWidget() 
        self.setWindowTitle("Team jarvis") 
        self.textName = QLineEdit(self.win)
        self.textPass = QLineEdit(self.win)
        self.buttonLogin = QPushButton('Login', self.win)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QVBoxLayout(self.win)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.setCentralWidget(self.win)

    def create_new_window(self):
        self._new_window = NewWindow()
        self._new_window.show()
    
    def handleLogin(self):
        if (self.textName.text() == 'ADMIN' and
            self.textPass.text() == '12345'):
            self.create_new_window()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')

if __name__ == '__main__':
    app = QApplication([])
    gui = Window()
    gui.show()
    app.exec_()