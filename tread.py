from PyQt5 import QtCore, QtWidgets

class MyTread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self,parent)
    def run(self):
        for i in range(1,21):
            self.sleep(3)
            self.mysignal.emit("i = %s" % i)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.label = QtWidgets.QLabel("Click button to start the thread")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Start the Thread")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyTread()
        self.button.clicked.connect(self.on_clicked)
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
    def on_clicked(self):
        self.button.setDisabled(True)
        self.mythread.start()
    def on_started(self):
        self.label.setText('On_started method was called')
    def on_finished(self):
        self.label.setText('On_finished method was called')
        self.button.setDisabled(False)
    def on_change(self, s):
        self.label.setText(s)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Ussing class "QThread"')
    window.resize(300,100)
    window.show()
    sys.exit(app.exec_())
