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
from modules.CryptoSymbolsComboBox import CryptoSymbolsComboBox
from modules.CurrencySymbolsComboBox import CurrencySymbolsComboBox

class Crypto(QWidget):
    def __init__(self):
        super().__init__()
        global crypto_currency_combobox
        crypto_currency_combobox = CryptoNamesComboBox()
        global crypto_symbols
        crypto_symbols = CryptoSymbolsComboBox()
        global symbolsComboBox
        symbolsComboBox = CurrencySymbolsComboBox()
        self.initUI()
        
        
    def initUI(self):
        # Create a new window
        #stockWindow = QWidget()

        # Set size and position of the window
        #self.resize(500, 500)
        #self.move(800, 200)
        self.resize(1300, 800)
        self.move(0, 200)
        self.setWindowTitle('Crypto Currencies')
        self.setWindowIcon(QIcon('assets/icon.jpeg'))
        self.show()
        
        #main layout of the screen
        self.vbox = QVBoxLayout()
        
        # add crypto currencly list
        crypto_currency_combobox.currentIndexChanged.connect(self.on_index_changed)
        crypto_symbols.currentIndexChanged.connect(self.on_change_cryptoSymbol)
        symbolsComboBox.currentIndexChanged.connect(self.on_currency_symbol_changed)
        
        # add area to display crypto market data
        self.dashboard_vbox = QVBoxLayout()
         
        # add data to display ~1500 top performing ERC20 tokens
        self.displayERC20()
        self.displayNFTCollections()
        self.displayRecentTokenSwaps()
        #self.dashboard_vbox.addWidget(erc_df)
        
        # add button to chart crypto and currency pairs
        self.chart_crypto_currency_pair_btn = QPushButton("Chart Crypto/Fiat Pair", self)
        self.chart_crypto_currency_pair_btn.setToolTip("To chart the selected crypto currency and the selected fiat symbol")
        self.chart_crypto_currency_pair_btn.clicked.connect(self.chart_crypto_currency_pair)
        
        # add the button
        self.search = QPushButton("Find Crypto", self)
        self.search.setToolTip('Search for stablecoins')
        self.search.clicked.connect(self.cryptoFind)
        self.graph = QPushButton("Graph Selected Crypto Currency", self)
        self.graph.setToolTip("Select a crypto currency from the list and graph on a candlestick")
        self.graph.clicked.connect(self.graphCrypto)
        # set the layout
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.search)
        self.hbox.addWidget(crypto_currency_combobox)
        self.hbox.addWidget(self.graph)
        self.hbox.addWidget(crypto_symbols)
        self.hbox.addWidget(self.chart_crypto_currency_pair_btn)
        self.hbox.addWidget(symbolsComboBox)
        self.hbox.addStretch(1)
               
        #now add all other layouts on the main layouts
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.dashboard_vbox)
        self.vbox.addLayout(self.hbox)
       
        self.setLayout(self.vbox)  
    
    def displayRecentTokenSwaps(self):
        global swap_df
        swap_df = pd.DataFrame(openbb.crypto.defi.swaps()) #default list last 100 swaps
        swap_df.head()
        print(swap_df)
        self.show()
        self.label = QLabel("Last 100 Token Swap", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(swap_df))
        for i in range(len(swap_df)):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(
                    swap_df.iloc[i][j])))

        self.setLayout(self.vbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
        
    def displayERC20(self):
        global erc_df
        erc_df = pd.DataFrame(openbb.crypto.onchain.erc20_tokens())
        erc_df.head()
        print(erc_df)
        self.show()
        self.label = QLabel("Top Performing ERC20 Tokens", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(erc_df))
        for i in range(len(erc_df)):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(
                    erc_df.iloc[i][j])))

        self.setLayout(self.vbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
        
    def displayNFTCollections(self):
        global nft_df
        nft_df = pd.DataFrame(openbb.crypto.nft.collections())
        nft_df.head()
        print(nft_df)
        self.show()
        self.label = QLabel("NFT Collections from OpenSea", self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(nft_df))
        for i in range(len(nft_df)):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(
                    nft_df.iloc[i][j])))

        self.setLayout(self.vbox)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.table)
        self.show()
    
    def on_currency_symbol_changed(self):
        print("on currency symbol change")
        global selected_currency_symbol
        selected_currency_symbol = symbolsComboBox.currentText()
        print("To pair: %s" % selected_currency_symbol)
        
    def on_index_changed(self):
        global selected_crypto
        selected_crypto = crypto_currency_combobox.currentText()  
        
    def chart_crypto_currency_pair(self):
        chart_df = pd.DataFrame(openbb.crypto.load(selected_symbol,selected_currency_symbol))
        openbb.crypto.chart(chart_df, selected_symbol, selected_currency_symbol)
        
        
    def graphCrypto(self):
        print("Selected crypto: %s" % selected_symbol)
        chart_df = openbb.crypto.candle(selected_symbol) 
        chart_dict = chart_df.to_dict()
        new_df = pd.DataFrame(chart_df)
    
    def on_change_cryptoSymbol(self):
        global selected_symbol
        selected_symbol = crypto_symbols.currentText()
        
    def cryptoFind(self):
        print("Selected symbol: %s" % selected_crypto)
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