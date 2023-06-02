import tkinter as tk
import openai
import numpy as np
import os
import sys
import pandas as pd
from openbb_terminal.sdk import openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Stocks(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        #self.stockEvents()
        
    def initUI(self):
        print('You clicked the Stocks button')
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Stocks')
        self.show()
        
        # add the button
        self.search = QPushButton("Stock Search", self)
        self.search.setToolTip('Search for stocks in a given country')
        self.search.clicked.connect(self.stockSearch)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addStretch(1)
        self.setLayout(self.hbox)
            
        
    def stockSearch(self):
        columns = ['name', 'country', 'sector', 'industry_group', 'industry', 'exchange']
        #stocks_df = pd.DataFrame(openbb.stocks.search(country="United States", exchange_country="Germany")) #this will open OpenBB dataframe
        #stocks_df = openbb.stocks.search(country="United States", exchange_country="Germany")
        stocks_df = openbb.stocks.search(country="United States", exchange_country="Canada")
        stocks_dict = stocks_df.to_dict()
        stocks_dict['title'] = "Satoshi Terminal"
        new_df = pd.DataFrame(stocks_dict)
        print(new_df[columns])

        