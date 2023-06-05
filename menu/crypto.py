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
from modules.CryptoNamesComboBox import CryptoNamesComboBox

class Crypto(QWidget):
    def __init__(self):
        super().__init__()
        global crypto_currency_combobox
        crypto_currency_combobox = CryptoNamesComboBox()
        self.initUI()
        
        
    def initUI(self):
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Crypto Currencies')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        # add crypto currencly list
        crypto_currency_combobox.currentIndexChanged.connect(self.on_index_changed)
        
        # add the button
        self.search = QPushButton("Find Crypto", self)
        self.search.setToolTip('Search for stablecoins')
        self.search.clicked.connect(self.cryptoFind)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(crypto_currency_combobox)
        self.hbox.addStretch(1)
               
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
       
        self.setLayout(self.vbox)  
        
    def on_index_changed(self):
        global selected_crypto
        selected_crypto = crypto_currency_combobox.currentText()   
        
    def cryptoFind(self):
        print("Selected ticker: %s" % selected_crypto)
        #crypto_df = pd.DataFrame(openbb.crypto.find("eth", "CoinGecko", "name", 25))
        crypto_df = pd.DataFrame(openbb.crypto.find(selected_crypto))
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

        self.setLayout(self.vbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()