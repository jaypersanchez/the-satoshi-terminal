import PyQt5  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class CryptoSymbolsComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        tickers = ['AAVE', 'ADA', 'ALGO', 'AMP', 'APE', 'ATOM', 'AVAX', 'AXS', 'BCH', 'BNB',
                    'BTC', 'CRO', 'DOGE', 'DOT', 'EOS', 'ETH', 'FTM', 'GRT', 'LUNA', 'MATIC',
                    'NEO', 'NEXO', 'ONE', 'OMG', 'SOL', 'UNI', 'USDC', 'USDT', 'VET', 'XLM',
                    'XRP', 'XTZ', 'YFI'] 
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
        self.comboBox = CryptoSymbolsComboBox(self)
        self.comboBox.move(50, 50) 
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())