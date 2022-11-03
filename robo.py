from insta import *
from PySide6 import QtCore, QtWidgets, QtGui
import webbrowser
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyInstaBot')
        self.resize(400, 200)
        self.github_icon = 'github.png'
        self.user_label = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.user_label.setPlaceholderText("Coloque seu usuário") 
        
        self.password_label = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.password_label.setPlaceholderText("Coloque sua senha")
        self.password_label.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.hashtag_label = QtWidgets.QLineEdit(alignment=QtCore.Qt.AlignCenter)
        self.hashtag_label.setPlaceholderText("Coloque a hashtag para curtir") 
        
        self.button_start = QtWidgets.QPushButton("começar a curtir") 
        self.button_start.setDefault(True)
        self.button_start.clicked.connect(self.open_browser)
        
        self.button_git = QtWidgets.QPushButton('Visite Meu Github', clicked=self.open_git_on_web)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.user_label)    
        self.layout.addWidget(self.password_label)   
        self.layout.addWidget(self.hashtag_label)
        self.layout.addWidget(self.button_start)   
       
        self.layout.addWidget(self.button_git)
        self.button_git.setIcon(QtGui.QIcon(self.github_icon))   
        
        
    def verify_user_and_password_not_empty(self, user, password, hashtag):
        if user and password and hashtag:
            return True 
        
        
        else:
            self.show_dialog("Coloque um usuário ou senha ou a hashtag primeiro!")
    
    def open_browser(self):
        if self.verify_user_and_password_not_empty(self.user_label.text(), self.password_label.text(), self.hashtag_label.text()) == True:
            self.close()
            self.instagram()
        
        
    def instagram(self):
        user = self.user_label.text()
        password = self.password_label.text()
        hashtag = self.hashtag_label.text()
        instagram = InstagramLogin(user, password, hashtag)
        instagram.go_to_hashtag()
        instagram.start_like()
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
           

    def open_git_on_web(self):
        webbrowser.open_new_tab(
        'https://github.com/vbsx'
        )  

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())

