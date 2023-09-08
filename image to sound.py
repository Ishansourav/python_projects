import sys
import numpy as np
import imageio
import soundfile as sf
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog

class ImageToSoundConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image to Sound Converter")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Select an image to convert to sound:")
        self.layout.addWidget(self.label)

        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)
        self.layout.addWidget(self.select_button)

        self.convert_button = QPushButton("Convert to Sound")
        self.convert_button.clicked.connect(self.convert_image_to_sound)
        self.layout.addWidget(self.convert_button)

        self.central_widget.setLayout(self.layout)

        self.image_data = None

    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.image_data = imageio.imread(file_name, as_gray=True)
            self.label.setText(f"Selected Image: {file_name}")

    def convert_image_to_sound(self):
        if self.image_data is not None:
            # Normalize pixel values to the range [0, 1]
            image_data_normalized = self.image_data / 255.0

            # Define audio parameters
            sample_rate = 44100  # Samples per second
            duration = 5.0  # seconds

            # Generate a simple audio signal based on image data
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            frequency = 440.0  # Hz (adjust as needed)
            audio_data = np.sin(2 * np.pi * frequency * t)

            # Map the image data to audio amplitude
            amplitude_data = np.interp(t, np.linspace(0, duration, len(image_data_normalized), endpoint=False), image_data_normalized)

            # Combine the audio signal and image-based amplitude
            final_audio = audio_data * amplitude_data

            # Normalize the audio to prevent clipping
            final_audio = np.int16(final_audio / np.max(np.abs(final_audio)) * 32767)

            # Save the audio to a WAV file
            save_file_name, _ = QFileDialog.getSaveFileName(self, "Save Audio", "", "Audio Files (*.wav)")
            if save_file_name:
                sf.write(save_file_name, final_audio, sample_rate)

                self.label.setText(f"Audio saved as: {save_file_name}")

def main():
    app = QApplication(sys.argv)
    window = ImageToSoundConverter()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

