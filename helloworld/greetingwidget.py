from PyQt4.QtGui import QWidget, QLabel, QPushButton, QVBoxLayout
from helloworld.greetings import GREETINGS, get_random_greeting

class GreetingWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent=parent)
        
        self.label = QLabel(text=GREETINGS[0])
        button = QPushButton("Change Greeting", parent=self, clicked=self.change_greeting)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)

    def change_greeting(self):
        self.label.setText( get_random_greeting() )
