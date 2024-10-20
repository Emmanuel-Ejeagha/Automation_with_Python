# This function creates a desktop GUI
#  This script scraped an currency rate website
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests


def get_currency(from_curr='EUR', to_curr='USD'):
  url = f'https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate = float(rate[:-4])
  
  return rate

def show_currency():
    input_text = float(text.text())
    rate = get_currency()
    result = round(input_text * rate, 2)
    output_label.setText(str(result))  # Corrected input.text


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

# Use QVBoxLayout for the layout manager
layout = QVBoxLayout()

# Input field
text = QLineEdit()
layout.addWidget(text)

# Button
btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

# Output label
output_label = QLabel('')
layout.addWidget(output_label)

# Set the layout and show the window
window.setLayout(layout)
window.show()
app.exec()
