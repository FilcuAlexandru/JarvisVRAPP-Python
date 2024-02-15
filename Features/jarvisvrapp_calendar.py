from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QCalendarWidget, QPushButton, QMessageBox
import calendar as cal

class CalendarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        layout = QVBoxLayout(self)

        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        self.show_button = QPushButton("Show Calendar")
        self.show_button.clicked.connect(self.show_calendar)
        layout.addWidget(self.show_button)

        self.calendar_text = QTextEdit()
        layout.addWidget(self.calendar_text)

    def show_calendar(self):
        selected_date = self.calendar.selectedDate()
        year = selected_date.year()
        month = selected_date.month()
        calendar_text = ""
        try:
            for i in range(1, 13):
                calendar_text += f"{cal.month_name[i]:^20}\n"
                calendar_text += cal.TextCalendar(6).formatmonth(year, i, w=0, l=0)
                calendar_text += "\n" + "-" * 20 + "\n"
            self.calendar_text.setPlainText(f"Calendar for {year}:\n{calendar_text}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error occurred: {e}")
