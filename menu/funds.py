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

class Funds(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        #self.stockEvents()
        
    def initUI(self):
        print('You clicked the Funds button')
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Mutual Funds')
        self.show()
        
        # add the button
        self.search = QPushButton("Search Funds", self)
        self.search.setToolTip('Search for mutual funds')
        self.search.clicked.connect(self.fundSearch)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addStretch(1)
        self.setLayout(self.hbox)    
        
    def fundSearch(self):
        funds_df = pd.DataFrame(openbb.funds.search("Vanguard", "US"))
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
        

        