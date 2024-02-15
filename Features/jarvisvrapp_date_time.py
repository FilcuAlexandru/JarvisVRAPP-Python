from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from datetime import datetime
import pytz

class DateTimeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date & Time")
        layout = QVBoxLayout(self)

        self.timezone_field = QLineEdit()
        self.timezone_field.setPlaceholderText("Enter your timezone (e.g., UTC, GMT, America/New_York)")
        layout.addWidget(self.timezone_field)

        self.get_time_button = QPushButton("Get Date & Time")
        self.get_time_button.clicked.connect(self.get_date_time)
        layout.addWidget(self.get_time_button)

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
        QMessageBox.information(self, "Date & Time", f"Current date and time in {timezone_str}:\n{current_time}")
