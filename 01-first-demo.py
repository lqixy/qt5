"""
第一个例子
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = QWidget()
    widget.resize(250, 150)
    widget.move(300,300)
    widget.setWindowTitle('first PyQt5')
    widget.show()

    sys.exit(app.exec_())
