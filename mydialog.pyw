from PyQt5 import QtCore,QtWidgets
import mywindow
import sys,time

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.myWidget = mywindow.MyWindow()
        self.myWidget.vbox.setContentsMargins(0,0,0,0)
        self.button = QtWidgets.QPushButton("&Change sign")
        self.button2 = QtWidgets.QPushButton('Sleep')
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        mainBox.addWidget(self.button2)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)
        self.button2.clicked.connect(self.on_clicked_sleep)

    def on_clicked(self):
        if self.myWidget.label.text() == 'Hello World!':
           self.myWidget.label.setText('New Sign')
        elif self.myWidget.label.text() == 'New Sign':
           self.myWidget.label.setText('Hello World!')

    def on_clicked_sleep(self):
        self.button2.setDisabled(True)
        for i in range(1,21):
            QtWidgets.qApp.processEvents()
            time.sleep(1)
            print('step -', i)
        self.button2.setDisabled(False)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('OOP')
    window.resize(300,100)
    window.show()
    sys.exit(app.exec_())


