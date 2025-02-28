from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys

class MyTable(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QTableWidget
        self.table = QTableWidget()

        # Set table dimensions
        self.table.setRowCount(3)  # Set 3 rows
        self.table.setColumnCount(2)  # Set 2 columns

        # Adding data to the table
        self.table.setItem(0, 0, QTableWidgetItem("Apple"))
        self.table.setItem(0, 1, QTableWidgetItem("100"))
        self.table.setItem(1, 0, QTableWidgetItem("Banana"))
        self.table.setItem(1, 1, QTableWidgetItem("50"))
        self.table.setItem(2, 0, QTableWidgetItem("Cherry"))
        self.table.setItem(2, 1, QTableWidgetItem("75"))

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MyTable()
window.show()
sys.exit(app.exec_())
