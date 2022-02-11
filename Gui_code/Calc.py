from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton, QMessageBox, QTextEdit
from PyQt6 import QtWidgets
import sys
import requests


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500, 300)
    w.move(300, 200)
    w.setWindowTitle('Simple')
    a=QLabel(w)
    a.setText('Enter your number')
    a.move(20,20)
    b=QLineEdit(w)
    b.move(150,20)
    c=QPushButton('Find Square',w)
    c.move(350,20)
    ne=QTextEdit(w)
    # ne.setText("This is the place where messages are printed")
    ne.insertHtml("<b>This is the place where Answer is Printed</b>")
    ne.setReadOnly(True)
    ne.move(80,60)
    def Onclick():
        val_a=b.text()
        try:
            url="http://localhost:5000/{}".format(val_a)
            res=requests.get(url)
            res=res.json()
            res=res["square"]
            ne.append("The square of {} is {}".format(val_a,res))
            # QMessageBox.question(w,"Results","The square of {} is {}".format(val_a,res))
        except:
            print("INVALID INPUT")    
        b.setText("")
    c.clicked.connect(Onclick)
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()