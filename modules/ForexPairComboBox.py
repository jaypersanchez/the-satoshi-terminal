import PyQt5  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class ForexPairComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        tickers = ['EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'AUDUSD', 'USDCAD', 'NZDUSD', 
                   'EURGBP', 'EURJPY', 'GBPJPY', 'CHFJPY', 'EURCHF', 'GBPCHF', 'AUDJPY', 
                   'AUDNZD', 'AUDCAD', 'CADJPY', 'NZDJPY', 'GBPAUD', 'GBPCAD', 'GBPNZD', 
                   'EURAUD', 'EURCAD', 'EURNZD', 'USDHKD', 'USDSGD', 'USDTRY', 'USDZAR', 
                   'USDMXN', 'USDNOK', 'USDSEK', 'USDDKK', 'USDCNH', 'EURTRY', 'EURNOK', 
                   'EURSEK', 'EURDKK', 'EURHUF', 'EURPLN', 'AUDCHF', 'AUDHKD', 'AUDSGD', 
                   'AUDNZD', 'CADCHF', 'CADHKD', 'NZDCHF', 'NZDHKD', 'SGDJPY', 'SGDHKD', 
                   'HKDJPY', 'TRYJPY', 'ZARJPY', 'MXNJPY', 'NOKJPY', 'SEKJPY', 'DKKJPY', 
                   'CNHJPY', 'HUFJPY', 'PLNJPY'] 
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
        self.comboBox = ForexPairComboBox(self)
        self.comboBox.move(50, 50) 
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())