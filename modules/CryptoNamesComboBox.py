import PyQt5  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class CryptoNamesComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        tickers = ['Aave', 'ABBC Coin', 'Aergo', 'AION', 'AirSwap', 'Altcoin', 'Amplify', 'AnChain X', 'Ankr', 'Augur',
                    'AVA', 'AVAX', 'Aventus', 'Axie Infinity', 'BAND Protocol', 'Basic Attention Token', 'Basic Energy Token', 'Binance Coin', 'BitCoke Token', 'Bitcoin',
                    'Bitcoin Cash', 'Bitcoin Diamond', 'Bitcoin Gold', 'Bitcoin SV', 'BitTorrent', 'BitShares', 'Blockstack', 'Blox', 'BRD', 'Bytom',
                    'Celo', 'Chainlink', 'Chronos', 'Citadel', 'CityCoins', 'CoinEx Token', 'CoinGecko Token', 'CoinMarketCap Coin', 'Compound', 'ContentBox',
                    'Cosmos', 'CougarCoin', 'COTI', 'Crown', 'Crypto.com Coin', 'CryptoKitties', 'Crypto.com Coin (OLD)', 'CyberMiles', 'DASH', 'Decentraland',
                    'Decred', 'DeepBrain Chain', 'DigiByte', 'Dogecoin', 'DOT', 'Dragonchain', 'Enjin Coin', 'EOS', 'EquiTrader Token', 'Ether',
                    'Ethereum Classic', 'Everipedia', 'Exo', 'Fantom', 'Filecoin', 'FIO Protocol', 'Flexacoin', 'Flow', 'Force', 'Fosstoken',
                    'Fusion', 'Gnosis', 'Golem', 'GRT', 'Haven Protocol', 'Hedera Hashgraph', 'Huobi Token', 'IOST', 'IOTA', 'JUST',
                    'Kyber Network', 'Litecoin', 'Loopring', 'Maker', 'MANA', 'Mastercard', 'Matic Network', 'Monero', 'NEO', 'Nervos Network',
                    'Nexo', 'OmiseGO', 'OMG Network', 'Ontology', 'Orchid Protocol', 'PAX Gold', 'Paytomat', 'Polkadot', 'Polygon', 'Power Ledger',
                    'Quant', 'Rarible', 'Ravencoin', 'Ripple', 'SafePal', 'SALT', 'Sandbox', 'Shiba Inu', 'Solana', 'Stacks',
                    'Status Network', 'Stellar', 'StormX', 'Swipe', 'Synthetix Network Token', 'Tether', 'THORChain', 'THETA Fuel', 'Theta Network', 'TRON',
                    'TrueUSD', 'UMA', 'Uniswap', 'USD Coin', 'VeChain', 'Wrapped Bitcoin', 'Wrapped Ether', 'XLM', 'XRP', 'Yearn Finance'] 
        tickers.sort() 
        self.addItems(tickers)

class App(QMainWindow): 
    
    def __init__(self): 
        super().__init__() 
        
        self.title = 'Ticker Symbols'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.initUI() 
  
    
    def initUI(self): 
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
  
        self.createComboBox() 
  
        self.show() 
        
    def createComboBox(self):
        self.comboBox = CryptoNamesComboBox(self)
        self.comboBox.move(50, 50) 
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())