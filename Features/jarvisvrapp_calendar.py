from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QCalendarWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QStyleOption
from PyQt5.QtWidgets import QStyle


import calendar as cal

class CalendarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        font = QFont("Helvetica", 12, QFont.Normal)

        # Set a light color scheme
        self.set_light_palette()

        self.calendar = QCalendarWidget()
        self.calendar.setFont(font)
        layout.addWidget(self.calendar)

        self.show_button = QPushButton("Show Calendar")
        self.show_button.setFont(font)
        self.show_button.setStyleSheet(
            "QPushButton { background-color: #007AFF; color: white; border-radius: 10px; padding: 10px; }"
            "QPushButton:hover { background-color: #0056B3; }"
        )
        self.show_button.clicked.connect(self.show_calendar)
        layout.addWidget(self.show_button)

        self.calendar_text = QTextEdit()
        self.calendar_text.setFont(font)
        layout.addWidget(self.calendar_text)

    def set_light_palette(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Base, Qt.white)
        palette.setColor(QPalette.AlternateBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.black)
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Button, QColor(230, 230, 230))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(0, 122, 255))
        palette.setColor(QPalette.Highlight, QColor(0, 122, 255))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        self.setPalette(palette)

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

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

    def sizeHint(self):
        return QSize(300, 400)
