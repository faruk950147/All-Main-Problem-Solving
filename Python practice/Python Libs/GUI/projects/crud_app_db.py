import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)

class CRUDManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Manager with SQLite")
        self.setGeometry(100, 100, 450, 350)

        # SQLite setup
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # UI Elements
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.list_widget = QListWidget()

        self.create_ui()
        self.refresh_list()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)
        self.conn.commit()

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
            self.cursor.execute("INSERT INTO records (name, phone) VALUES (?, ?)", (name, phone))
            self.conn.commit()
            self.refresh_list()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Input Error", "Both fields are required.")

    def load_selected_data(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            record_id = int(current_item.text().split(".")[0])
            self.cursor.execute("SELECT name, phone FROM records WHERE id=?", (record_id,))
            result = self.cursor.fetchone()
            if result:
                self.name_input.setText(result[0])
                self.phone_input.setText(result[1])

    def update_data(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            record_id = int(current_item.text().split(".")[0])
            name = self.name_input.text().strip()
            phone = self.phone_input.text().strip()
            if name and phone:
                self.cursor.execute("UPDATE records SET name=?, phone=? WHERE id=?", (name, phone, record_id))
                self.conn.commit()
                self.refresh_list()
                self.clear_inputs()
            else:
                QMessageBox.warning(self, "Input Error", "Both fields are required.")
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a data to update.")

    def delete_data(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            record_id = int(current_item.text().split(".")[0])
            self.cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
            self.conn.commit()
            self.refresh_list()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a data to delete.")

    def refresh_list(self):
        self.list_widget.clear()
        self.cursor.execute("SELECT id, name, phone FROM records")
        for row in self.cursor.fetchall():
            self.list_widget.addItem(f"{row[0]}. {row[1]} - {row[2]}")

    def clear_inputs(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.list_widget.clearSelection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CRUDManager()
    window.show()
    sys.exit(app.exec_())
