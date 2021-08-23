#!/usr/bin/python3
from baro import baroKi
from events import get_events
import sys
from tkinter import Tk, Label, PhotoImage, LEFT, X, CENTER
from PyQt5 import QtGui, QtWidgets
import eel


image_for_baro = '/bar.png'
image_message_old = "/home/kaverianov/OneDrive/Cods/python/Warfreme/new_Warfreme/Lotus_icon_2.png"
image_message_new = "/home/kaverianov/OneDrive/Cods/python/Warfreme/new_Warfreme/1.png"
bgcolor_pickup_message = '#000000'
color_text = '#FFCC33'
time_to_close_pickup_message = 15


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        Baro = menu.addAction("Баро Ки'Тиир")
        show_alerts = menu.addAction("Посмотреть")
        exitAction = menu.addAction("Выход")
        self.setContextMenu(menu)
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        show_alerts.triggered.connect(self.show_alerts)
        Baro.triggered.connect(self.baro)

    def baro(self):
        root = self.message_box()
        logo = PhotoImage(file=image_for_baro)
        Label(root, justify=LEFT, bg=bgcolor_pickup_message, text=baroKi(2), font=('Helvetica', 10, 'bold italic'), fg=color_text).pack(fill=X)
        label = Label(root, image=logo, bg=bgcolor_pickup_message)
        label.pack(side="left")
        root.mainloop()

    def show_alerts(self):
        self.setIcon(QtGui.QIcon(image_message_old))
        messages = eel
        messages.init('web')
        messages.start('base.html', geometry={'size': (200, 100), 'position': (300, 50)})
        messages.sleep(1.0)
        messages.destroy()

    @eel.expose
    def bingR():
        return get_events()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image_message_new), windows)
    trayIcon.show()
    app.exec_()

# 
# class window(QMainWindow):
#     def __init__(self):
# 
#         super().__init__()
# 
#     def createUI(self):
# 
# 
#         self.setGeometry(500, 300, 700, 700)
# 
#         self.setWindowTitle("window")
# 
# 
#         quit = QAction("Quit", self)
#         quit.triggered.connect(self.closeEvent)
# 
#         menubar = self.menuBar()
#         fmenu = menubar.addMenu("File")
#         fmenu.addAction(quit)
# 
#     def closeEvent(self, event):
#         close = QMessageBox()
#         close.setText("You sure?")
#         close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
#         close = close.exec()
# 
#         if close == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
# 
# main = QApplication(sys.argv)
# window = window()
# window.createUI()
# window.show()
# sys.exit(main.exec_())
