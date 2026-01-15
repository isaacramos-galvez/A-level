import PyQt6.QtWidgets as qtw
# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg
layout = qtw.QGridLayout()

# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")
        widget = qtw.QWidget()
        #self.combo = QcomboBox()
        #self.combo.addItems("One", "Two", "Three")
        #self.combo.setCurrentIndex(2)
        #layout.addwidget(self.combo)
        #widget.setLayout(layout)

        #self.label = qtw.QLabel("Template")
        #layout.addWidget(self.label)

        self.ok_btn = qtw.QPushButton("Done")
        self.ok_btn.clicked.connect(self.button_click)

        self.edit_box = qtw.QLineEdit("Enter your number here in Kelvin")
        
        self.label = qtw.QLabel("Kelvin")
        self.label1 = qtw.QLabel("Celcius")
        self.label2 = qtw.QLabel("0")
        

        layout.addWidget(self.label, 1, 1)
        layout.addWidget(self.label1, 2, 1)
        layout.addWidget(self.edit_box, 1, 2)
        layout.addWidget(self.ok_btn, 3, 1, 1, 3)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    #def on_text_change(self, new_text):
    #    print(new_text)

    def button_click(self):
        if self.edit_box.text().isnumeric() == False:
            self.label2 = qtw.QLabel("Please enter a number")
            layout.addWidget(self.label2)
        else:
            self.label2 = qtw.QLabel("")
            layout.addWidget(self.label2, 2, 2) 
            converted_value = int(self.edit_box.text()) - 273
            converted_value = f"{str(converted_value)} Celcius"
            self.label2 = qtw.QLabel(converted_value)
            layout.addWidget(self.label2, 2, 2)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

app = qtw.QApplication([])
window = MainWindow()
window.show()

# Start the event loop.
app.exec()