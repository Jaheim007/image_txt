import sys 
from PyQt5.QtWidgets import QApplication
from Widget.text_commands import command

def main():
    app = QApplication(sys.argv)
    home = command()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
