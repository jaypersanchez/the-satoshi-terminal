import tkinter as tk
import openai
import numpy as np
import os
import sys
import pandas as pd
from openbb_terminal.sdk import openbb
# Import necessary libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from modules.FundNamesComboBox import FundNamesComboBox

class Funds(QWidget):
    def __init__(self):
        super().__init__()
        global fund_term
        fund_term = FundNamesComboBox()
        self.initUI()
                
    def initUI(self):
        
        
        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Mutual Funds')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        fund_term.currentIndexChanged.connect(self.on_index_changed)
        
        # add manual search
        self.manual_search_btn = QPushButton("Search This Fund Manually", self)
        self.manual_search_btn.setToolTip("Provide a mutual fund name that's not on the list")
        self.manual_search_btn.clicked.connect(self.searchInputFund)
        self.manual_search_input_field = QLineEdit(self)
        
        
        # add the button
        self.search = QPushButton("Search Funds", self)
        self.search.setToolTip('Search for mutual funds')
        self.search.clicked.connect(self.fundSearch)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(fund_term)
        self.hbox.addWidget(self.manual_search_btn)
        self.hbox.addWidget(self.manual_search_input_field)
        self.hbox.addStretch(1)
        
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        self.setLayout(self.vbox) 
        
    def searchInputFund(self):
        global inputFundName
        inputFundName = self.manual_search_input_field.text()
        print("Fund Name: %s" % inputFundName)
        funds_df = pd.DataFrame(openbb.funds.search(inputFundName,"",10))
        funds_df.head()
        print(funds_df)
        self.show()
        
        self.label = QLabel("Mutual Funds", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(funds_df))
        for i in range(len(funds_df)):
            for j in range(4):
                if j < funds_df.shape[1]:
                     self.table.setItem(i, j, QTableWidgetItem(str(
                    funds_df.iloc[i][j])))

        self.setLayout(self.hbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
        
    def on_index_changed(self):
        global selected_term
        selected_term = fund_term.currentText()
        print("Selected term: %s" % selected_term)   
        
    def fundSearch(self):
        #funds_df = pd.DataFrame(openbb.funds.search("Vanguard", "United States"))
        #funds_df = pd.DataFrame(openbb.funds.search("","",1000))
        #funds_df = pd.DataFrame(openbb.funds.search("AMP","",200))
        funds_df = pd.DataFrame(openbb.funds.search(selected_term,"",200))
        funds_df.head()
        print(funds_df)
        self.show()
        
        self.label = QLabel("Mutual Funds", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(funds_df))
        for i in range(len(funds_df)):
            for j in range(4):
                if j < funds_df.shape[1]:
                     self.table.setItem(i, j, QTableWidgetItem(str(
                    funds_df.iloc[i][j])))

        self.setLayout(self.hbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
        

        