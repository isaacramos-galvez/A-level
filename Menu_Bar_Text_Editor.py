import PyQt6.QtWidgets as qtw
from PyQt6.QtWidgets import QMessageBox, QApplication
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
layout = qtw.QGridLayout()

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

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        save_action = qtg.QAction('Save', self)
        save_action.setIcon(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogSaveButton))
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        open_action = qtg.QAction('Open', self)
        open_action.setIcon(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogOpenButton))
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = qtg.QAction('Exit', self)
        exit_action.setIcon(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogCancelButton))
        exit_action.triggered.connect(self.quit_button_click)
        file_menu.addAction(exit_action)

        layout.addWidget(self.edit_box, 1, 1, 3, 3)
        layout.addWidget(self.save_btn, 4, 1)
        layout.addWidget(self.restore_btn, 4, 2)
        layout.addWidget(self.quit_btn, 4, 3)
                
        self.setCentralWidget(widget)
        widget.setLayout(layout)


    def open_file(self):
        filename, _= qtw.QFileDialog.getOpenFileName(self, "Open File", ".", "TextFiles (*.txt *.html)")
        print(filename)

    def save_button_click(self):
        self.saved_value = self.edit_box.toPlainText()
        print(self.saved_value)
    
    def save_file():
        #filename = qtw.QFileDialog.getSaveFilename 
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html)")
        print(filename)
        

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