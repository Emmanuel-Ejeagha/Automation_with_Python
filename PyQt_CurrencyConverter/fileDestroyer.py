from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    """Opens a diaglue box when it is clicked"""
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files') # Opens computer file path, can select multiple files
    message.setText('\n'.join(filenames))

def destroy_files():
    """Destroys files when it is clicked"""
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction Successful!')
    

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer') 
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will <font color="red">permanently</font> deleted')
layout.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open File')
open_btn.setFixedWidth(120) # sets the size of the button
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter) # Align Button to the centre
open_btn.clicked.connect(open_files) # Connect btn to a function

destroy_btn = QPushButton('Destroy Files')
destroy_btn.setFixedWidth(120)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter) # Align Button to the centre
destroy_btn.clicked.connect(destroy_files) # Connect btn to a function

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()
app.exec()