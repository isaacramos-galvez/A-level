


import PyQt6.QtWidgets as qtw
from PyQt6.QtWidgets import QMessageBox, QApplication
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg
layout = qtw.QGridLayout()

# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow): 

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")
        widget = qtw.QWidget()

        self.save_btn = qtw.QPushButton("Save")
        self.save_btn.clicked.connect(self.save_button_click)

        self.restore_btn = qtw.QPushButton("Restore to Last Save")
        self.restore_btn.clicked.connect(self.restore_button_click)
        
        self.quit_btn = qtw.QPushButton("Quit")
        self.quit_btn.clicked.connect(self.quit_button_click)

        self.edit_box = qtw.QTextEdit()

        
        layout.addWidget(self.edit_box, 1, 1, 3, 3)
        layout.addWidget(self.save_btn, 4, 1)
        layout.addWidget(self.restore_btn, 4, 2)
        layout.addWidget(self.quit_btn, 4, 3)
        
        
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    #def on_text_change(self, new_text):
    #    print(new_text)

    def save_button_click(self):
        self.saved_value = self.edit_box.toPlainText()
        print(self.saved_value)
    

    def restore_button_click(self):
        try:
            self.edit_box.setText(self.saved_value)
            layout.addWidget(self.edit_box, 1, 1, 3, 3)
        except AttributeError:
            self.label = qtw.QLabel("You haven't saved any values")
            layout.addWidget(self.label, 5, 1)

    def quit_button_click(self):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if dlg == QMessageBox.StandardButton.Ok:
            QApplication.instance().quit()
        elif dlg == QMessageBox.StandardButton.Cancel:
            pass

app = qtw.QApplication([])
window = MainWindow()
window.show()

app.exec()
