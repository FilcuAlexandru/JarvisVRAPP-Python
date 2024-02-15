from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QGridLayout
from math import sqrt

class CalculatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        layout = QVBoxLayout(self)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        grid_layout = QGridLayout()
        buttons = [
            ("C", self.clear), ("/", lambda: self.add_to_expression("/")),
            ("7", lambda: self.add_to_expression(7)), ("8", lambda: self.add_to_expression(8)), ("9", lambda: self.add_to_expression(9)), ("*", lambda: self.add_to_expression("*")),
            ("4", lambda: self.add_to_expression(4)), ("5", lambda: self.add_to_expression(5)), ("6", lambda: self.add_to_expression(6)), ("-", lambda: self.add_to_expression("-")),
            ("1", lambda: self.add_to_expression(1)), ("2", lambda: self.add_to_expression(2)), ("3", lambda: self.add_to_expression(3)), ("+", lambda: self.add_to_expression("+")),
            ("0", lambda: self.add_to_expression(0)), (".", lambda: self.add_to_expression(".")), ("=", self.calculate),
            ("√", self.sqrt), ("^2", self.square), ("%", self.modulo)
        ]

        positions = [(i, j) for i in range(6) for j in range(4)]

        for position, (text, func) in zip(positions, buttons):
            button = QPushButton(text)
            button.clicked.connect(func)
            grid_layout.addWidget(button, *position)

        layout.addLayout(grid_layout)
        self.expression = ""

    def clear(self):
        self.input_field.clear()
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)
        self.input_field.setText(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_field.setText(str(result))
            self.expression = str(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid expression: {e}")
            self.clear()

    def sqrt(self):
        try:
            result = sqrt(eval(self.expression))
            self.input_field.setText(str(result))
            self.expression = str(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid expression: {e}")
            self.clear()

    def square(self):
        try:
            result = eval(self.expression) ** 2
            self.input_field.setText(str(result))
            self.expression = str(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid expression: {e}")
            self.clear()

    def modulo(self):
        try:
            result = eval(self.expression) % 2
            self.input_field.setText(str(result))
            self.expression = str(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid expression: {e}")
            self.clear()
