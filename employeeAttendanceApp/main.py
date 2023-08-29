from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QWindow, QIcon
from PySide6.QtCore import QSize
from employee import Employee
from addEmployee import AddEmployeeDialog
import database

class loginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('ui/login.ui', None)
        self.ui.show()
        self.username = 'admin'
        self.password = '123'
        self.ui.login_lbl.setStyleSheet("background-image: url(img/key4.PNG)")
        self.ui.login_btn.clicked.connect(self.login)
    def login(self):
        if self.username == self.ui.username_tb.text() and self.password == self.ui.password_tb.text():
            self.ui = employeeAttendanceApp()
        else:
            self.msgBox('Wrong! Try again.')

    def msgBox(self, message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()

class employeeAttendanceApp(QWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('ui/employList.ui', None)
        self.ui.show()
        self.page_size = 5
        self.current_page = 1
        self.readFromDatabase()
        self.ui.add_btn.clicked.connect(self.show_add_employee_dialog)
        self.ui.prev_btn.setIcon(QIcon('img/6646435_arrow_button_circle_essentials_previous_icon.png'))
        self.ui.prev_btn.setIconSize(QSize(30, 30))
        self.ui.prev_btn.setStyleSheet('border:0px')
        self.ui.prev_btn.clicked.connect(self.previous_page)
        self.ui.next_btn.setIcon(QIcon('img/6646422_arrow_button_circle_essentials_next_icon.png'))
        self.ui.next_btn.setIconSize(QSize(30, 30))
        self.ui.next_btn.setStyleSheet('border:0px')
        self.ui.next_btn.clicked.connect(self.next_page)

    def readFromDatabase(self):
        offset = (self.current_page - 1) * self.page_size
        results = database.page_rowsLimit(self.page_size, offset)
        self.clear_grid()
        for i in range(len(results)):
            pixmap = AddEmployeeDialog.create_thumbnail(results[i][5], 50)
            new_pic = QLabel()
            new_pic.setPixmap(pixmap)
            new_Fname = QLabel()
            new_Fname.setText(results[i][1])
            new_Lname = QLabel()
            new_Lname.setText(results[i][2])
            new_edit_btn = QPushButton()
            new_edit_btn.setIcon(QIcon('img/103775_edit_user_half_icon.png'))
            new_edit_btn.setIconSize(QSize(25, 25))
            new_edit_btn.setStyleSheet('border:0px')
            new_edit_btn.setObjectName(f'edit_btn_{results[i][0]}')
            new_del_btn = QPushButton()
            new_del_btn.setIcon(QIcon('img/3844459_can_delete_remove_trash_icon.png'))
            new_del_btn.setIconSize(QSize(25, 25))
            new_del_btn.setStyleSheet('border:0px')
            new_del_btn.setObjectName(f'edit_btn_{results[i][0]}')
            self.ui.page_lbl.setText(f'Page {self.current_page}')
            self.ui.gridLayout.addWidget(new_pic, i, 0)
            self.ui.gridLayout.addWidget(new_Fname, i, 1)
            self.ui.gridLayout.addWidget(new_Lname, i, 2)
            self.ui.gridLayout.addWidget(new_edit_btn, i, 3)
            self.ui.gridLayout.addWidget(new_del_btn, i, 4)
            new_del_btn.clicked.connect(self.deleteEmployee)
            new_edit_btn.clicked.connect(self.editEmployee)
        
    def show_add_employee_dialog(self):
        dialog = AddEmployeeDialog()
        if dialog.exec_():
            first_name = dialog.first_name_edit.text()
            last_name = dialog.last_name_edit.text()
            national_code = dialog.national_code_edit.text()
            date_of_birth = dialog.date_of_birth_edit.text()
            face_image = None 
            new_employee = Employee(first_name, last_name, national_code, date_of_birth, face_image)
            self.update_employee_list_widget()

    def clear_grid(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            item = self.ui.gridLayout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()

    def deleteEmployee(self):
        del_id = self.sender().objectName().split('_')[-1]
        database.deleteEmployee(del_id)
        self.update_employee_list_widget()

    def editEmployee(self):
        edit_id = int(self.sender().objectName().split('_')[-1])
        employee_list = database.getAll()
        employee_to_edit = None
        for employee in employee_list:
            if employee[0] == edit_id:
                employee_to_edit = list(employee)
                break
        if employee_to_edit:
            dialog = AddEmployeeDialog()
            dialog.setWindowTitle("Edit Employee")
            dialog.first_name_edit.setText(employee_to_edit[1])
            dialog.last_name_edit.setText(employee_to_edit[2])
            dialog.national_code_edit.setText(employee_to_edit[3])
            dialog.date_of_birth_edit.setText(employee_to_edit[4])

        if dialog.exec_():
            employee_to_edit[1] = dialog.first_name_edit.text()
            employee_to_edit[2] = dialog.last_name_edit.text()
            employee_to_edit[3] = dialog.national_code_edit.text()
            employee_to_edit[4] = dialog.date_of_birth_edit.text()
            database.editEmployee(employee_to_edit, edit_id)
            self.update_employee_list_widget()

    def update_employee_list_widget(self):
        self.clear_grid()
        self.readFromDatabase()

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.readFromDatabase()

    def next_page(self):
        total_employees = database.countEmployees()
        max_page = (total_employees + self.page_size - 1) // self.page_size
        if self.current_page < max_page:
            self.current_page += 1
            self.readFromDatabase()

app = QApplication()
window = loginPage()
app.exec_()