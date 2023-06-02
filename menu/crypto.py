import tkinter as tk
import openai
import numpy as np
import os
import sys
import pandas as pd
from openbb_terminal.sdk import openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Crypto(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        print('You clicked the Crypto button')
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Crypto Currencies')
        self.show()
        
        # add the button
        self.search = QPushButton("Find", self)
        self.search.setToolTip('Search for stablecoins')
        self.search.clicked.connect(self.cryptoFind)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addStretch(1)
        self.setLayout(self.hbox)
            
        
    def cryptoFind(self):
        crypto_df = pd.DataFrame(openbb.crypto.find("polka", "CoinGecko", "name", 25))
        crypto_df.head()
        print(crypto_df)
        self.show()
        
        self.label = QLabel("Crypto Currencies", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(crypto_df))
        for i in range(len(crypto_df)):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(
                    crypto_df.iloc[i][j])))

        self.setLayout(self.hbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()