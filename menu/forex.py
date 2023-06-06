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
from modules.ForexPairComboBox import ForexPairComboBox
from modules.CurrencySymbolsComboBox import CurrencySymbolsComboBox

class Forex(QWidget):
    def __init__(self):
        super().__init__()
        global forexComboBox
        global symbolsComboBox_to
        global symbolsComboBox_from
        forexComboBox = ForexPairComboBox()
        symbolsComboBox_to = CurrencySymbolsComboBox()
        symbolsComboBox_from = CurrencySymbolsComboBox()
        
        self.initUI()
        
    def initUI(self):
        # Set size and position of the window
        #self.resize(500, 500)
        #self.move(800, 200)
        self.resize(1300, 800)
        self.move(0, 200)
        self.setWindowTitle('Forex Commodities')
        self.setWindowIcon(QIcon('assets/icon.jpeg'))
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        self.loadCurrencyList()
        forexComboBox.currentIndexChanged.connect(self.on_index_changed)
        symbolsComboBox_to.currentIndexChanged.connect(self.to_symbol_changed)
        symbolsComboBox_from.currentIndexChanged.connect(self.from_symbol_changed)
        
        # add graph button
        # add search for specific stock symbol for candle stick graphing
        self.graph_btn = QPushButton("Graph Selected Commodity",self)
        self.graph_btn.setToolTip("Load currency pairs to displayed on a candle stick chart")
        self.graph_btn.clicked.connect(self.graphCurrencyPair)
        
        # add the button
        self.search = QPushButton("Forex Pair Quote", self)
        self.search.setToolTip('Forex Pair Quote')
        self.search.clicked.connect(self.forexQuote)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(forexComboBox)
        self.hbox.addWidget(self.graph_btn)
        self.hbox.addWidget(symbolsComboBox_to)
        self.hbox.addWidget(symbolsComboBox_from)
        self.hbox.addStretch(1)
        
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        self.setLayout(self.vbox)
    
    def graphCurrencyPair(self):
        print("graphing")
        graph_df = pd.DataFrame(openbb.forex.load(selected_to, selected_from))
        openbb.forex.candle(graph_df)
        graph_dict = graph_df.to_dict()
        new_df = pd.DataFrame(graph_df)
        
    def to_symbol_changed(self):
        global selected_to
        selected_to = symbolsComboBox_to.currentText()
        print("To pair: %s" % selected_to)
        
    def from_symbol_changed(self):
        global selected_from
        selected_from = symbolsComboBox_from.currentText()    
        print("From pair: %s" % selected_from)
        
    def on_index_changed(self):
        global selected_pair
        selected_pair = forexComboBox.currentText()
        print("Selected pair: %s" % selected_pair) 
        
    def loadCurrencyList(self):
        global currency_list
        currency_list = openbb.forex.get_currency_list()
        print(currency_list)
        
    def forexQuote(self):
        forex_df = pd.DataFrame(openbb.forex.quote(selected_pair))
        forex_df.head()
        print(forex_df)
        self.show()
        
        self.label = QLabel("Forex Pair Quote", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(forex_df))
        for i in range(len(forex_df)):
            for j in range(4):
                if j < forex_df.shape[1]:
                     self.table.setItem(i, j, QTableWidgetItem(str(
                    forex_df.iloc[i][j])))

        self.setLayout(self.hbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()

        