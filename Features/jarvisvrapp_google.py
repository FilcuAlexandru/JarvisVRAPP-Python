from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class GoogleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Search")
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background
        layout = QVBoxLayout(self)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Enter your search query")
        self.search_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4CAF50; /* Green border */
                border-radius: 8px;
                font-size: 16px;
                padding: 8px;
            }
        """)
        layout.addWidget(self.search_field)

        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 12px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green */
            }
            QPushButton:pressed {
                background-color: #0e7a0d; /* Even darker green */
            }
        """)
        self.search_button.clicked.connect(self.google_search)
        layout.addWidget(self.search_button)

    def google_search(self):
        search_query = self.search_field.text().strip()

        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
        else:
            QMessageBox.warning(self, "No Query Entered", "Please enter a search query.")

