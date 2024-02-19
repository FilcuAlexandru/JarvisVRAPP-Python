from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from datetime import datetime
import pytz

class DateTimeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date & Time")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        font = QFont("Roboto", 12, QFont.Normal)

        self.timezone_label = QLabel("Enter your timezone (e.g., UTC, GMT, America/New_York):")
        self.timezone_label.setFont(font)
        layout.addWidget(self.timezone_label)

        self.timezone_field = QLineEdit()
        self.timezone_field.setFont(font)
        self.timezone_field.setPlaceholderText("Enter your timezone here")
        self.timezone_field.setStyleSheet(
            "QLineEdit { border: 2px solid #2196F3; border-radius: 10px; padding: 10px; }"
            "QLineEdit:focus { border-color: #1976D2; }"
        )
        layout.addWidget(self.timezone_field)

        self.get_time_button = QPushButton("Get Date & Time")
        self.get_time_button.setFont(font)
        self.get_time_button.setStyleSheet(
            "QPushButton { background-color: #2196F3; color: white; border-radius: 10px; padding: 10px; }"
            "QPushButton:hover { background-color: #1976D2; }"
        )
        self.get_time_button.clicked.connect(self.get_date_time)
        layout.addWidget(self.get_time_button)

        self.time_label = QLabel("")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(font)
        layout.addWidget(self.time_label)

    def get_date_time(self):
        timezone_str = self.timezone_field.text().strip()
        if not timezone_str:
            QMessageBox.warning(self, "No Timezone Entered", "Please enter a timezone.")
            return

        try:
            user_timezone = pytz.timezone(timezone_str)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid timezone: {e}")
            return

        now = datetime.now(user_timezone)
        current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
        self.time_label.setText(f"Current date and time in {timezone_str}:\n{current_time}")
