import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)


class CRUDManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Manager")
        self.setGeometry(100, 100, 400, 300)

        # Store data as list of dictionaries
        self.data = []

        # UI Elements
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.list_widget = QListWidget()

        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout()

        # Input Fields
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.phone_input)

        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Add")
        update_btn = QPushButton("Update")
        delete_btn = QPushButton("Delete")
        clear_btn = QPushButton("Clear")

        add_btn.clicked.connect(self.add_data)
        update_btn.clicked.connect(self.update_data)
        delete_btn.clicked.connect(self.delete_data)
        clear_btn.clicked.connect(self.clear_inputs)

        button_layout.addWidget(add_btn)
        button_layout.addWidget(update_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(clear_btn)

        layout.addLayout(button_layout)

        # Data List
        self.list_widget.itemClicked.connect(self.load_selected_data)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_data(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            self.data.append({'name': name, 'phone': phone})
            self.refresh_list()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Input Error", "Both fields are required.")

    def load_selected_data(self):
        selected = self.list_widget.currentRow()
        if selected >= 0:
            data = self.data[selected]
            self.name_input.setText(data['name'])
            self.phone_input.setText(data['phone'])

    def update_data(self):
        selected = self.list_widget.currentRow()
        if selected >= 0:
            name = self.name_input.text().strip()
            phone = self.phone_input.text().strip()
            if name and phone:
                self.data[selected] = {'name': name, 'phone': phone}
                self.refresh_list()
                self.clear_inputs()
            else:
                QMessageBox.warning(self, "Input Error", "Both fields are required.")
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a data to update.")

    def delete_data(self):
        selected = self.list_widget.currentRow()
        if selected >= 0:
            del self.data[selected]
            self.refresh_list()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a data to delete.")

    def refresh_list(self):
        self.list_widget.clear()
        for data in self.data:
            self.list_widget.addItem(f"{data['name']} - {data['phone']}")

    def clear_inputs(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.list_widget.clearSelection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CRUDManager()
    window.show()
    sys.exit(app.exec_())
