import PyQt6.QtWidgets as qtw
from PyQt6 import QtCore
layout = qtw.QGridLayout()

# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")
        widget = qtw.QWidget()
        self.combo = qtw.QComboBox()
        options = ["0", "1", "2"]
        self.combo.addItems(options)
        self.combo.setCurrentIndex(2)
        self.label = qtw.QLabel("Widget Demo")
        self.lineedit = qtw.QLineEdit("Type Here")
        self.check = qtw.QCheckBox("Choose this")
        self.check2 = qtw.QCheckBox("And This?")
        self.rad_btn = qtw.QRadioButton("This One?")
        self.rad_btn2 = qtw.QRadioButton("Or This One?")    
        self.slider = qtw.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.ok_btn = qtw.QPushButton("Ok")
        widget.setLayout(layout)

        #self.label = qtw.QLabel("Template")
        #layout.addWidget(self.label)

        #self.ok_btn.clicked.connect(self.button_click)

        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.check)
        layout.addWidget(self.check2)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.rad_btn)
        layout.addWidget(self.rad_btn2)
        layout.addWidget(self.slider)
        layout.addWidget(self.ok_btn)


        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    #def on_text_change(self, new_text):
    #    print(new_text)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

app = qtw.QApplication([])
window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
