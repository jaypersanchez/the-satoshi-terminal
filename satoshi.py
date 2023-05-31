import tkinter as tk
import openai
import numpy as np
import os
import openbb_terminal.sdk as openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
 
# Create main window
class MainWindow(QMainWindow):
       
    def __init__(self):
        super().__init__()
 
        self.title = 'The Satoshi Terminal'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.showMaximized()
 
        # Create a button in the window
        button = QPushButton('Click here', self)
        button.setToolTip('Click to open your desktop app!')
        button.move(200,175) 
        button.clicked.connect(self.on_click)
 
        self.show()
 
    def on_click(self):
        print('You clicked the button')
 
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.setWindowIcon(QIcon('icon.png'))
    app.exec_()