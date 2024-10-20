# This function creates a desktop GUI
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit


def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize())  # Corrected input.text


app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')

# Use QVBoxLayout for the layout manager
layout = QVBoxLayout()

# Input field
text = QLineEdit()
layout.addWidget(text)

# Button
btn = QPushButton('Make')
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

# Output label
output_label = QLabel('')
layout.addWidget(output_label)

# Set the layout and show the window
window.setLayout(layout)
window.show()
app.exec()
