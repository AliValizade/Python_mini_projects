from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

class employeeAttendanceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('ui/employList.ui', None)
        self.ui.show()



app = QApplication()
window = employeeAttendanceApp()
app.exec_()
