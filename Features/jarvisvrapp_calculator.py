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
            ("C", self.clear, "#FF6F61"), ("/", lambda: self.add_to_expression("/"), "#6B5B95"),
            ("7", lambda: self.add_to_expression(7), "#88B04B"), ("8", lambda: self.add_to_expression(8), "#F7CAC9"),
            ("9", lambda: self.add_to_expression(9), "#92A8D1"), ("*", lambda: self.add_to_expression("*"), "#955251"),
            ("4", lambda: self.add_to_expression(4), "#B565A7"), ("5", lambda: self.add_to_expression(5), "#009B77"),
            ("6", lambda: self.add_to_expression(6), "#F89A9D"), ("-", lambda: self.add_to_expression("-"), "#3B3B98"),
            ("1", lambda: self.add_to_expression(1), "#C70039"), ("2", lambda: self.add_to_expression(2), "#FF5733"),
            ("3", lambda: self.add_to_expression(3), "#FFC300"), ("+", lambda: self.add_to_expression("+"), "#DAF7A6"),
            ("0", lambda: self.add_to_expression(0), "#7FB3D5"), (".", lambda: self.add_to_expression("."), "#FF5733"),
            ("=", self.calculate, "#9A9A9A"),
            ("√", self.sqrt, "#D6A2E8"), ("^2", self.square, "#83C5BE"), ("%", self.modulo, "#E6B0AA")
        ]

        positions = [(i, j) for i in range(6) for j in range(4)]

        for position, (text, func, color) in zip(positions, buttons):
            button = QPushButton(text)
            button.setStyleSheet(f"QPushButton {{ background-color: {color}; border-radius: 25px; font-size: 24px; }}")
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
