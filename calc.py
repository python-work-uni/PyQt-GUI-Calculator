import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QVBoxLayout, QWidget,
)

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class PyCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
        
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                self.buttonMap[key].clicked.connect(self._buttonClicked)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        
        self.generalLayout.addLayout(buttonsLayout)
    
    def _buttonClicked(self):
        button = self.sender()
        key = button.text()
        
        if key == 'C':
            self.display.setText('')
        elif key == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText('ERROR')
        else:
            self.display.setText(self.display.text() + key)

def main():
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()