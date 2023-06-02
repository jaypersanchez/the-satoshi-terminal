import tkinter as tk
import openai
import numpy as np
import os
import sys
import pandas as pd
from pandasgui import show
from openbb_terminal.sdk import openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTableView, QHeaderView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
#menu actions
from menu.stocks import Stocks
from menu.crypto import Crypto
from menu.funds import Funds
from menu.forex import Forex
 
# Create main window
class MainWindow(QMainWindow):
       
    def __init__(self):
        super().__init__()
 
        self.title = 'The Satoshi Terminal'
        self.left = 100
        self.top = 100
        self.width = 1000 #640
        self.height = 100 #480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.showMaximized()
 
        #Create QWidget
        hbox = QHBoxLayout()
        widget = QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)
        
        # Create buttons in the window
        btnStocks = QPushButton('Stocks', self)
        btnStocks.setToolTip('Click to open Stocks page')
        btnStocks.adjustSize()
        btnStocks.clicked.connect(self.on_click_stocks)

        btnCrypto = QPushButton('Crypto', self)
        btnCrypto.setToolTip('Click to open Cryptocurrency page')
        btnCrypto.adjustSize()
        btnCrypto.clicked.connect(self.on_click_crypto)

        btnFunds = QPushButton('Funds', self)
        btnFunds.setToolTip('Click to open Funds page')
        btnFunds.adjustSize()
        btnFunds.clicked.connect(self.on_click_funds)
        
        btnForex = QPushButton('Forex', self)
        btnForex.setToolTip('Click to open Forex page')
        btnForex.adjustSize()
        btnForex.clicked.connect(self.on_click_forex)
        
        btnEconomicEvents = QPushButton('Economic Events', self)
        btnEconomicEvents.setToolTip('Click to view current economic events')
        btnEconomicEvents.adjustSize()
        btnEconomicEvents.clicked.connect(self.on_click_economic_events)
 
        # Create horizontal layout for the buttons
        main_hbox = QHBoxLayout()
        main_hbox.addWidget(btnStocks)
        main_hbox.addWidget(btnCrypto)
        main_hbox.addWidget(btnFunds)
        main_hbox.addWidget(btnForex)
        main_hbox.addWidget(btnEconomicEvents)
        
        # Add vertical contaier to horizontal container
        hbox.addLayout(main_hbox)
        self.show()
 
    def on_click_stocks(self):
        #print('You clicked the Stocks button')
        window = QWidget()
        try:
            self.stocks = Stocks()
            
        except Exception as e:
            print(e)
        
    def on_click_crypto(self):
        #print('You clicked the Crypto button')
        window = QWidget()
        try:
            self.crypto = Crypto()
            
        except Exception as e:
            print(e)
    
    def on_click_funds(self):
        #print('You clicked the Funds button')
        window = QWidget()
        try:
            self.funds = Funds()
            
        except Exception as e:
            print(e)
            
    def on_click_forex(self):
        window = QWidget()
        try:
            self.forex = Forex()
            
        except Exception as e:
            print(e)
        
    def on_click_economic_events(self):
        events_df = pd.DataFrame(openbb.economy.events(countries="United States"))
        events_df.head()
        show(events_df)
        print(events_df) 
         
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.setWindowIcon(QIcon('icon.png'))
    app.exec_()