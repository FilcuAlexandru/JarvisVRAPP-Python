from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailDialog(QDialog):
    def __init__(self, sender_email, smtp_server, smtp_port, sender_password):
        super().__init__()
        self.sender_email = "YourE-Mail"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_password = "YourPassword"

        self.setWindowTitle("Send Email")
        layout = QVBoxLayout(self)

        self.receiver_field = QLineEdit()
        self.receiver_field.setPlaceholderText("Enter the recipient's email address")
        layout.addWidget(self.receiver_field)

        self.subject_field = QLineEdit()
        self.subject_field.setPlaceholderText("Enter the email subject")
        layout.addWidget(self.subject_field)

        self.body_field = QLineEdit()
        self.body_field.setPlaceholderText("Enter the email body")
        layout.addWidget(self.body_field)

        self.send_button = QPushButton("Send Email")
        self.send_button.clicked.connect(self.send_email)
        layout.addWidget(self.send_button)

    def send_email(self):
        receiver_email = self.receiver_field.text().strip()
        email_subject = self.subject_field.text().strip()
        email_body = self.body_field.text().strip()

        if not (receiver_email and email_subject and email_body):
            QMessageBox.warning(self, "Incomplete Information", "Please provide all required information for sending the email.")
            return

        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = receiver_email
            message['Subject'] = email_subject
            message.attach(MIMEText(email_body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, receiver_email, message.as_string())

            QMessageBox.information(self, "Email Sent", f"Email sent successfully to {receiver_email}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while sending the email: {e}")
