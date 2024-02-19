from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QMessageBox
import psutil

class ProcessesDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Running Processes")
        layout = QVBoxLayout(self)

        self.process_text = QTextEdit()
        layout.addWidget(self.process_text)

        self.setStyleSheet(
            """
            QTextEdit {
                padding: 10px;
                border: 2px solid #D3D3D3;
                border-radius: 5px;
                font-size: 14px;
            }
            """
        )

        self.display_processes()

    def display_processes(self):
        try:
            processes = psutil.process_iter(['pid', 'name', 'username'])
            process_info = "Running Processes:\n"
            for process in processes:
                process_info += f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}\n"
            self.process_text.setPlainText(process_info)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while checking processes: {e}")
