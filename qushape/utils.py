from PyQt4 import QtGui


def check_bsddb3():
    global is_legacy_files_available_
    is_legacy_files_available = True
    try:
        import bsddb3
        import shelve
    except ImportError:
        is_legacy_files_available = False


def no_bsddb3_dialog():
    dialog = QtGui.QMessageBox()
    dialog.setText("Legacy format .qushape is not available because shelve+bsddb3 are not correctly installed, please use .qushapey format")
    dialog.exec_()
