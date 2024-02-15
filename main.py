import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from Features.jarvisvrapp_date_time import DateTimeDialog
from Features.jarvisvrapp_calendar import CalendarDialog
from Features.jarvisvrapp_weather import WeatherDialog
from Features.jarvisvrapp_recipes import RecipeDialog
from Features.jarvisvrapp_calculator import CalculatorDialog
from Features.jarvisvrapp_music import MusicPlayer
from Features.jarvisvrapp_email import EmailDialog
from Features.jarvisvrapp_whatsapp import WhatsAppDialog
from Features.jarvisvrapp_google import GoogleDialog
from Features.jarvisvrapp_processes import ProcessesDialog

class JarvisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis App")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Hi, I'm Jarvis, your virtual assistant!")
        layout.addWidget(self.label)

        self.time_button = QPushButton("Get Date & Time")
        self.time_button.clicked.connect(self.show_date_time_dialog)
        layout.addWidget(self.time_button)

        self.calendar_button = QPushButton("Show Calendar")
        self.calendar_button.clicked.connect(self.show_calendar_dialog)
        layout.addWidget(self.calendar_button)

        self.weather_button = QPushButton("Check Weather")
        self.weather_button.clicked.connect(self.show_weather_dialog)
        layout.addWidget(self.weather_button)

        self.recipe_button = QPushButton("Explore Recipes")
        self.recipe_button.clicked.connect(self.show_recipe_dialog)
        layout.addWidget(self.recipe_button)

        self.calculator_button = QPushButton("Open Calculator")
        self.calculator_button.clicked.connect(self.open_calculator)
        layout.addWidget(self.calculator_button)

        self.music_button = QPushButton("Play Music")
        self.music_button.clicked.connect(self.play_music)
        layout.addWidget(self.music_button)

        self.stop_music_button = QPushButton("Stop Music")
        self.stop_music_button.clicked.connect(self.stop_music)
        layout.addWidget(self.stop_music_button)

        self.email_button = QPushButton("Send Email")
        self.email_button.clicked.connect(self.send_email)
        layout.addWidget(self.email_button)

        self.whatsapp_button = QPushButton("Send WhatsApp Message")
        self.whatsapp_button.clicked.connect(self.send_whatsapp_message)
        layout.addWidget(self.whatsapp_button)

        self.google_search_button = QPushButton("Google Search")
        self.google_search_button.clicked.connect(self.google_search)
        layout.addWidget(self.google_search_button)

        self.process_button = QPushButton("Check Processes")
        self.process_button.clicked.connect(self.check_processes)
        layout.addWidget(self.process_button)

    def show_date_time_dialog(self):
        dialog = DateTimeDialog()
        dialog.exec_()

    def show_calendar_dialog(self):
        dialog = CalendarDialog()
        dialog.exec_()

    def show_weather_dialog(self):
        dialog = WeatherDialog()
        dialog.exec_()

    def show_recipe_dialog(self):
        dialog = RecipeDialog()
        dialog.exec_()

    def open_calculator(self):
        dialog = CalculatorDialog()
        dialog.exec_()

    def play_music(self):
        MusicPlayer().play_music_thread()

    def stop_music(self):
        MusicPlayer().stop_music()

    def send_email(self):
        sender_email = "YourE-Mail"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_password = "YourPassword"
        dialog = EmailDialog(sender_email, smtp_server, smtp_port, sender_password)
        dialog.exec_()

    def send_whatsapp_message(self):
        dialog = WhatsAppDialog()
        dialog.exec_()

    def google_search(self):
        dialog = GoogleDialog()
        dialog.exec_()

    def check_processes(self):
        dialog = ProcessesDialog()
        dialog.exec_()

def main():
    app = QApplication(sys.argv)
    window = JarvisApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
