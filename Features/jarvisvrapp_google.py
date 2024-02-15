from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import webbrowser

class GoogleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Search")
        layout = QVBoxLayout(self)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText("Enter your search query")
        layout.addWidget(self.search_field)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.google_search)
        layout.addWidget(self.search_button)

    def google_search(self):
        search_query = self.search_field.text().strip()

        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
        else:
            QMessageBox.warning(self, "No Query Entered", "Please enter a search query.")
