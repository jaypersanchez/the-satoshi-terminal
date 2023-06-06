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

class Forex(QWidget):
    def __init__(self):
        super().__init__()
        global forexComboBox
        forexComboBox = ForexPairComboBox()
        
        self.initUI()
        
    def initUI(self):
        # Set size and position of the window
        self.resize(500, 500)
        self.move(800, 200)
        self.setWindowTitle('Forex Commodities')
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        forexComboBox.currentIndexChanged.connect(self.on_index_changed)
        
        # add the button
        self.search = QPushButton("Forex Pair Quote", self)
        self.search.setToolTip('Forex Pair Quote')
        self.search.clicked.connect(self.forexQuote)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(forexComboBox)
        self.hbox.addStretch(1)
        
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        
        self.setLayout(self.vbox)
    
    def on_index_changed(self):
        global selected_pair
        selected_pair = forexComboBox.currentText()
        print("Selected pair: %s" % selected_pair) 
        
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

        