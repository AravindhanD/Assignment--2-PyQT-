import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QSlider
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class WaveformGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Waveform Generator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Dropdown menu for waveform selection
        self.waveform_label = QLabel("Select Waveform:")
        self.waveform_combobox = QComboBox()
        self.waveform_combobox.addItems(["Sine", "Cosine", "Triangular"])

        # Frequency and amplitude sliders
        self.frequency_label = QLabel("Frequency:")
        self.frequency_slider = QSlider(Qt.Horizontal)
        self.frequency_slider.setRange(1, 100)
        self.amplitude_label = QLabel("Amplitude:")
        self.amplitude_slider = QSlider(Qt.Horizontal)
        self.amplitude_slider.setRange(1, 100)

        # Matplotlib plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # Add widgets to layout
        self.layout.addWidget(self.waveform_label)
        self.layout.addWidget(self.waveform_combobox)
        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.frequency_slider)
        self.layout.addWidget(self.amplitude_label)
        self.layout.addWidget(self.amplitude_slider)
        self.layout.addWidget(self.canvas)

        # Connect signals to slots
        self.waveform_combobox.currentIndexChanged.connect(self.update_plot)
        self.frequency_slider.valueChanged.connect(self.update_plot)
        self.amplitude_slider.valueChanged.connect(self.update_plot)

        # Initialize the plot
        self.update_plot()

    def update_plot(self):
        frequency = self.frequency_slider.value()
        amplitude = self.amplitude_slider.value()

        # Time range
        x_values = np.linspace(0, 3000, 1000)

        # Plot all three waveforms
        self.ax.clear()
        self.ax.plot(x_values, amplitude * np.sin(2 * np.pi * frequency * x_values / 3000), label='Sine')
        self.ax.plot(x_values, amplitude * np.cos(2 * np.pi * frequency * x_values / 3000), label='Cosine')
        self.ax.plot(x_values, amplitude * (2 * np.abs((x_values / 3000 - 0.5) % 1) - 1), label='Triangular')

        self.ax.set_title("Combined Waveforms")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amplitude")
        self.ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaveformGeneratorApp()
    window.show()
    sys.exit(app.exec_())
