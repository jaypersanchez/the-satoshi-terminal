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
        #create country combo instances
        global country_combo1
        country_combo1 = CountriesComboBox()
        global exchange_country_combo2
        exchange_country_combo2 = CountriesComboBox()
        #global selected_country
        #global selected_exchange
        self.initUI()
               
    def initUI(self):
        
        # Set size and position of the window
        self.resize(1300, 800)
        self.move(0, 200)
        self.setWindowTitle('Stocks')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        # Connect the signal to the slot
        country_combo1.currentIndexChanged.connect(self.on_index_changed)
        exchange_country_combo2.currentIndexChanged.connect(self.on_index_changed)
        
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
    
    def on_index_changed(self):
        #country_combo1Index = country_combo1.currentIndex()
        global selected_country
        global selected_exchange
        selected_country = country_combo1.currentText()
        selected_exchange = exchange_country_combo2.currentText()
        #exchange_country_combo2.setCurrentIndex(country_combo1Index)
        #print("Selected country: %s" % selected_country)
        #print("Selected country: %s" % selected_exchange_country)
    
    def stockSearch(self):
        print("Selected country: %s" % selected_country)
        print("Selected country: %s" % selected_exchange)
        
        columns = ['name', 'country', 'sector', 'industry_group', 'industry', 'exchange']
        stocks_df = openbb.stocks.search(country=selected_country, exchange_country=selected_exchange)
        stocks_dict = stocks_df.to_dict()
        stocks_dict['title'] = "Satoshi Terminal"
        new_df = pd.DataFrame(stocks_dict, index=stocks_dict.keys())
        print(new_df)

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
        