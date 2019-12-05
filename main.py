from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            with open('input.txt', 'r') as numbers:
                a = list(map(lambda x: int(x), ''.join(list(map(lambda x: x, numbers.readlines()))).split()))
                print(a)
                self.label.setText(f'Max: {max(a)} Min: {min(a)} Average: {sum(a) / len(a)}')
                output = open('output.txt', 'w')
                output.write(f'Max: {max(a)} Min: {min(a)} Average: {sum(a) / len(a)}')
                output.close()
        except:
            self.label.setText('Файл input.txt не найден или содержит данные не числового типа')


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())