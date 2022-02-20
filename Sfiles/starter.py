import sys
from main import main_menu


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    main_menu()
    sys.excepthook = except_hook
