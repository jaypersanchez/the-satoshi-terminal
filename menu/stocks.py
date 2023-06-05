import tkinter as tk
import openai
import numpy as np
import os
import sys
import pandas as pd
from openbb_terminal.sdk import openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QProgressBar, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from modules.CountriesComboBox import CountriesComboBox

class Stocks(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
               
    def initUI(self):
        
        # Set size and position of the window
        self.resize(1300, 800)
        self.move(0, 200)
        self.setWindowTitle('Stocks')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        #create country combo instances
        country_combo1 = CountriesComboBox()
        exchange_country_combo2 = CountriesComboBox()
        
        # add the search for stocks in a given country button
        self.search = QPushButton("Stock Search", self)
        self.search.setToolTip('Search for stocks in a given country')
        self.search.clicked.connect(self.stockSearch)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(country_combo1)
        self.hbox.addWidget(exchange_country_combo2)
        self.hbox.addStretch(1)
        #self.setLayout(self.hbox)
             
        
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        
        self.setLayout(self.vbox)
        
    def stockSearch(self):
        columns = ['name', 'country', 'sector', 'industry_group', 'industry', 'exchange']
        #stocks_df = pd.DataFrame(openbb.stocks.search(country="United States", exchange_country="Germany")) #this will open OpenBB dataframe
        #stocks_df = openbb.stocks.search(country="United States", exchange_country="Germany")
        stocks_df = openbb.stocks.search(country="United States", exchange_country="Canada")
        stocks_dict = stocks_df.to_dict()
        stocks_dict['title'] = "Satoshi Terminal"
        new_df = pd.DataFrame(stocks_dict)
        print(new_df[columns])

        #create status bar
        
        #self.progress = QProgressBar(self)
        #self.progress.setGeometry(200, 80, 250, 20)
        #self.progress.setMinimum(0)
        #self.progress.setMaximum(100)
        #self.progress.setValue(0)
        #self.progress.setVisible(True)
        
        #run stockSearch function and start status bar
        #for i in range (1,100):
        #    self.progress.setValue(i)
        #    QtTest.QTest.qWait(100)
        #    i +=1

        #self.progress.setVisible(False)
        