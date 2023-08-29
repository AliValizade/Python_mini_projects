import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QLineEdit, QDialogButtonBox, QFormLayout, QDialog
import database

class AddEmployeeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Employee")
        self.camera_viewfinder = QLabel()
        self.camera_viewfinder.setAlignment(Qt.AlignCenter)
        self.camera_viewfinder.setFixedSize(320, 240) 
        self.capture_button = QPushButton("Capture Image")
        self.first_name_edit = QLineEdit()
        self.last_name_edit = QLineEdit()
        self.national_code_edit = QLineEdit()
        self.date_of_birth_edit = QLineEdit()
        self.face_image = QLabel()
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout = QFormLayout()
        layout.addRow("First Name:", self.first_name_edit)
        layout.addRow("Last Name:", self.last_name_edit)
        layout.addRow("National Code:", self.national_code_edit)
        layout.addRow("Date of Birth:", self.date_of_birth_edit)
        layout.addRow("Face Image:", self.camera_viewfinder)
        layout.addRow(self.capture_button)
        layout.addRow(self.button_box)
        self.setLayout(layout)
        self.capture_button.clicked.connect(self.capture_image)
        self.camera = cv2.VideoCapture(0)  # Open the default webcam (index 0)
        database.create_table()

    def capture_image(self):
        ret, frame = self.camera.read() 
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
            height, width, channels = frame.shape
            bytes_per_line = channels * width
            qt_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.camera_viewfinder.setPixmap(pixmap.scaled(self.camera_viewfinder.size()))
            first_name = self.first_name_edit.text()
            last_name = self.last_name_edit.text()
            national_code = self.national_code_edit.text()
            date_of_birth = self.date_of_birth_edit.text()
            face_image = cv2.imencode('.png', frame)[1].tobytes()  # Convert frame to bytes
            employee_data = (first_name, last_name, national_code, date_of_birth, face_image)
            database.save_employee(employee_data)
            
    def create_thumbnail(img, max_size):
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        aspect_ratio = pixmap.width() / pixmap.height()
        if aspect_ratio > 1:
            pixmap = pixmap.scaledToWidth(max_size)
        else:
            pixmap = pixmap.scaledToHeight(max_size)
        return pixmap

    def closeEvent(self, event):
        self.camera.release()
        self.connection.close()
        event.accept()