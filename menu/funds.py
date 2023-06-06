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
        #self.resize(500, 500)
        #self.move(800, 200)
        self.resize(1300, 800)
        self.move(0, 200)
        self.setWindowTitle('Mutual Funds')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        fund_term.currentIndexChanged.connect(self.on_index_changed)
        
        # add load and view holdings button.  This will require user to select or enter a fund then click this load button
        self.load_fund_view_holdings = QPushButton("View Current Fund Holdings", self)
        self.load_fund_view_holdings.setToolTip("View holdings of your current selected fund.")
        self.load_fund_view_holdings.clicked.connect(self.loadSelectedFund)
        
        # add manual search button
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
        self.hbox.addWidget(self.load_fund_view_holdings)
        self.hbox.addStretch(1)
        
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        self.setLayout(self.vbox) 
        
    def loadSelectedFund(self):
        #Must confirm that a fund has been selected from manual input or fund list
        
        print("Loaded Fund Name: %s" % loadFundName)
        f = openbb.funds.load(loadFundName)
        holding_df = pd.DataFrame(openbb.funds.holdings(f))
        holding_df.head()
        print(holding_df)
        self.show()
        
        self.label = QLabel("Fund Holdings", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(holding_df))
        for i in range(len(holding_df)):
            for j in range(4):
                if j < holding_df.shape[1]:
                     self.table.setItem(i, j, QTableWidgetItem(str(
                    holding_df.iloc[i][j])))

        self.setLayout(self.hbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
        
    def searchInputFund(self):
        global inputFundName
        global loadFundName
        inputFundName = self.manual_search_input_field.text()
        loadFundName = inputFundName
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
        global loadFundName
        selected_term = fund_term.currentText()
        loadFundName = selected_term
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
        

        