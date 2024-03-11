from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QMessageBox
from random import randint  #This is to generate random numbers

app = QApplication([])
main_win = QWidget()
main_win.show()  #what is this line for...the "show" specifically

#widgets object
#To make a button that one can push
button = QPushButton("Generate")
#To label something on the screen, name them in order of appearance
firstLabel = QLabel("Click the button to generate the winner")
secondLabel = QLabel("?")

#layout
v_line = QVBoxLayout() #check what this funtion is used for again

#placement of widget objects
v_line.addWidget(firstLabel,alignment = QAlignCenter)
v_line.addWidget(secondLabel,alignment = Qt.AlignCenter)
v_line.addWidget(button,alignment = Qt.AlignCenter)

#application of layout to screen
main_win.setLayout(v_line) #wait...what exactly does v_line stand for? Must check

victory_win = QMessageBox()

#functions
def writeWinner():
    number + randint(1,100)
    firstLabel.setText("winner")

app>exec_()