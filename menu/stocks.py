import tkinter as tk
import openai
import numpy as np
import os
import sys
import openbb_terminal.sdk as openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Stocks(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print('You clicked the Stocks button')
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Stocks')
        self.show()

        