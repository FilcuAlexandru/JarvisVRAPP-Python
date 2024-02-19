import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QMessageBox
import pytube
import os

class YTDownloadDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        layout = QVBoxLayout(self)

        self.url_field = QLineEdit()
        self.url_field.setPlaceholderText("Enter YouTube video URL")
        layout.addWidget(self.url_field)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4", "MP3"])
        layout.addWidget(self.format_combo)

        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["Highest", "Lowest"])
        layout.addWidget(self.quality_combo)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)

    def download_video(self):
        url = self.url_field.text().strip()
        if not url:
            QMessageBox.warning(self, "Empty URL", "Please enter a YouTube video URL.")
            return

        try:
            yt = pytube.YouTube(url)
            if self.format_combo.currentText() == "MP4":
                video = yt.streams.filter(file_extension='mp4').first()
            elif self.format_combo.currentText() == "MP3":
                video = yt.streams.filter(only_audio=True).first()

            if self.quality_combo.currentText() == "Highest":
                video_path = video.download()  # Download the video
            elif self.quality_combo.currentText() == "Lowest":
                video_lowest = yt.streams.get_lowest_resolution()
                video_path = video_lowest.download()  # Download the video with lowest resolution

            if self.format_combo.currentText() == "MP3":
                # Convert MP4 to MP3 if MP3 format is selected
                mp3_file = video_path.split(".")[0] + ".mp3"
                os.rename(video_path, mp3_file)
                video_path = mp3_file

            QMessageBox.information(self, "Download Complete", f"Video downloaded successfully at {video_path}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while downloading the video: {e}")

def main():
    app = QApplication(sys.argv)
    dialog = YTDownloadDialog()
    dialog.exec_()
    sys.exit()

if __name__ == "__main__":
    main()
