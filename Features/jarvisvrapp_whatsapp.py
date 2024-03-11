from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import pywhatkit as kit

class WhatsAppDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Send WhatsApp Message")
        layout = QVBoxLayout(self)

        self.phone_number_field = QLineEdit()
        self.phone_number_field.setPlaceholderText("Recipient's phone number (with country code)")
        layout.addWidget(self.phone_number_field)

        self.message_field = QLineEdit()
        self.message_field.setPlaceholderText("WhatsApp message")
        layout.addWidget(self.message_field)

        self.send_button = QPushButton("Send WhatsApp Message")
        self.send_button.clicked.connect(self.send_whatsapp_message)
        layout.addWidget(self.send_button)

        # Set Styles
        self.setStyleSheet(
            """
            QLineEdit {
                padding: 10px;
                border: 2px solid #D3D3D3;
                border-radius: 5px;
                font-size: 16px;
            }

            QPushButton {
                padding: 10px 20px;
                border: 2px solid #32CD32; /* Changed to green color */
                border-radius: 5px;
                font-size: 16px;
                background-color: #32CD32; /* Changed to green color */
                color: white;
            }

            QPushButton:hover {
                background-color: #228B22; /* Darker green on hover */
                border-color: #228B22; /* Darker green on hover */
            }
            """
        )

    def send_whatsapp_message(self):
        phone_number = self.phone_number_field.text().strip()
        message = self.message_field.text().strip()

        if not (phone_number and message):
            QMessageBox.warning(self, "Incomplete Information", "Please provide all required information for sending the WhatsApp message.")
            return

        try:
            kit.sendwhatmsg_instantly(phone_number, message)
            QMessageBox.information(self, "WhatsApp Message Sent", f"WhatsApp message sent successfully to {phone_number}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while sending the WhatsApp message: {e}")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dialog = WhatsAppDialog()
    dialog.show()
    sys.exit(app.exec_())