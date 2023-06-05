import PyQt5  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class TickerSymbolsComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        tickers = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADP', 'ADSK', 'AMAT', 'AMGN', 'AMZN', 'APA',
                    'APC', 'AT&T', 'AXP', 'BA', 'BAC', 'BDX', 'BMY', 'BRKB', 'BRK.A', 'BRK.B',
                    'C', 'CAT', 'CELG', 'CHM', 'CL', 'COF', 'COST', 'CRM', 'CSCO', 'CVS',
                    'DHR', 'DIS', 'DOV', 'DOW', 'DTE', 'EIX', 'EMR', 'EXC', 'EXPD', 'F',
                    'FB', 'FDX', 'FIS', 'FITB', 'FLS', 'GE', 'GOOG', 'GOOGL', 'GS', 'HAL',
                    'HON', 'HPQ', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'MA',
                    'MMM', 'MO', 'MSFT', 'MTD', 'RTN', 'SBUX', 'SO', 'SPG', 'T', 'TGT',
                    'UNH', 'UNP', 'UPS', 'V', 'VZ', 'WMT', 'XOM'] 
        tickers.sort() 
        self.addItems(tickers)

class App(QMainWindow): 
    
    def __init__(self): 
        super().__init__() 
        
        self.title = 'PyQt5 dropdown box example'
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
        self.comboBox = TickerSymbolsComboBox(self)
        self.comboBox.move(50, 50) 
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())