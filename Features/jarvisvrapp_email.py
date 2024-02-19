from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class EmailDialog(QDialog):
    def __init__(self, sender_email, smtp_server, smtp_port, sender_password):
        super().__init__()
        self.sender_email = "YourE-Mail"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_password = "Your-Password"

        self.setWindowTitle("Send Email")
        layout = QVBoxLayout(self)

        self.receiver_field = QLineEdit()
        self.receiver_field.setPlaceholderText("Recipient's Email Address")
        layout.addWidget(self.receiver_field)

        self.subject_field = QLineEdit()
        self.subject_field.setPlaceholderText("Subject")
        layout.addWidget(self.subject_field)

        self.body_field = QLineEdit()
        self.body_field.setPlaceholderText("Your Message")
        layout.addWidget(self.body_field)

        self.send_button = QPushButton("Send Email")
        self.send_button.clicked.connect(self.send_email)
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
                border: 2px solid #32CD32;
                border-radius: 5px;
                font-size: 16px;
                background-color: #32CD32;
                color: white;
            }

            QPushButton:hover {
                background-color: #228B22;
                border-color: #228B22;
            }
            """
        )

    def send_email(self):
        receiver_email = self.receiver_field.text().strip()
        email_subject = self.subject_field.text().strip()
        email_body = self.body_field.text().strip()

        if not (receiver_email and email_subject and email_body):
            QMessageBox.warning(self, "Incomplete Information", "Please provide all required information for sending the email.")
            return

        try:
            # Your email sending code here
            QMessageBox.information(self, "Email Sent", f"Email sent successfully to {receiver_email}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while sending the email: {e}")
