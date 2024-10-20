# This function creates a desktop GUI
#  This script scraped an currency rate website
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests


def get_currency(from_currency, to_currency):
  url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate = float(rate[:-4])
  
  return rate

def show_currency():
    input_text = float(text.text())
    from_cur = from_combo.currentText()
    to_cur = to_combo.currentText()
    rate = get_currency(from_cur, to_cur)
    result = round(input_text * rate, 2)
    message = f"{input_text} {from_cur} is {result} {to_cur}"
    output_label.setText(str(message))  # Corrected input.text


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

# Use QVBoxLayout for the layout manager
layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

# Output label
output_label = QLabel('')
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

# Added list of currencies
from_combo = QComboBox()
currencies = ['USD', 'EUR', 'AED', 'INR', 'CAD', 'GBP',
              'CHF', 'ZAR', 'CNY']
from_combo.addItems(currencies)
layout2.addWidget(from_combo)

to_combo = QComboBox()
to_combo.addItems(currencies)
layout2.addWidget(to_combo)

# Input field
text = QLineEdit()
layout3.addWidget(text)

# Button
btn = QPushButton('Convert')
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)



# Set the layout and show the window
window.setLayout(layout)
window.show()
app.exec()
