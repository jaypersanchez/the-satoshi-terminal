import PyQt5  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class CountriesComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 
                     'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 
                     'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 
                     'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
                     'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
                     'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 
                     'Congo', 'Republic of the', 'Costa Rica', 'Côte d''Ivoire (Ivory Coast)', 'Croatia', 'Cuba', 
                     'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                     'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
                     'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany',
                     'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 
                     'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
                     'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
                     'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                     'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
                     'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
                     'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
                     'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
                     'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau',
                     'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
                     'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
                     'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'São Tomé and Príncipe',
                     'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
                     'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain',
                     'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan',
                     'Tanzania', 'Thailand', 'Timor-Leste (East Timor)', 'Togo', 'Tonga', 'Trinidad and Tobago', 
                     'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                     'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
                     'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'] 
        countries.sort() 
        self.addItems(countries)

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
        self.comboBox = CountriesComboBox(self)
        self.comboBox.move(50, 50) 
  
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_())