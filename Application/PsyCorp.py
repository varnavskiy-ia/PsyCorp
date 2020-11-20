import sys, sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap


def stringMaker(x):
    a = list()
    for i in x:
        a.append(str(i))
    return ' '.join(a)

def listMaker(x):
    a = set()
    for i in x:
        a.add(i[0])
    a = list(a)
    return a


def changer(x, y):
    x.show()
    y.hide()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Designes Of Application
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Ui_AboutUsPage(object):
    def setupUi(self, AboutUsPage):
        AboutUsPage.setObjectName("AboutUsPage")
        AboutUsPage.setEnabled(True)
        AboutUsPage.resize(1000, 490)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        AboutUsPage.setFont(font)
        AboutUsPage.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(AboutUsPage)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#tests_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(380, 70, 310, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(48)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(217, 201, 186);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.varn_name = QtWidgets.QLabel(self.centralwidget)
        self.varn_name.setGeometry(QtCore.QRect(280, 130, 390, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(36)
        self.varn_name.setFont(font)
        self.varn_name.setStyleSheet("color: rgb(217, 201, 186);")
        self.varn_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.varn_name.setObjectName("varn_name")
        self.varn_biography = QtWidgets.QLabel(self.centralwidget)
        self.varn_biography.setGeometry(QtCore.QRect(290, 170, 390, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        self.varn_biography.setFont(font)
        self.varn_biography.setStyleSheet("color: rgb(217, 201, 186);")
        self.varn_biography.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.varn_biography.setObjectName("varn_biography")
        self.ogorod_biography = QtWidgets.QLabel(self.centralwidget)
        self.ogorod_biography.setGeometry(QtCore.QRect(290, 330, 390, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        self.ogorod_biography.setFont(font)
        self.ogorod_biography.setStyleSheet("color: rgb(217, 201, 186);")
        self.ogorod_biography.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ogorod_biography.setObjectName("ogorod_biography")
        self.ogorod_name = QtWidgets.QLabel(self.centralwidget)
        self.ogorod_name.setGeometry(QtCore.QRect(280, 290, 390, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(36)
        self.ogorod_name.setFont(font)
        self.ogorod_name.setStyleSheet("color: rgb(217, 201, 186);")
        self.ogorod_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ogorod_name.setObjectName("ogorod_name")
        AboutUsPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutUsPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        AboutUsPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutUsPage)
        self.statusbar.setObjectName("statusbar")
        AboutUsPage.setStatusBar(self.statusbar)

        self.retranslateUi(AboutUsPage)
        QtCore.QMetaObject.connectSlotsByName(AboutUsPage)

    def retranslateUi(self, AboutUsPage):
        _translate = QtCore.QCoreApplication.translate
        AboutUsPage.setWindowTitle(_translate("AboutUsPage", "MainWindow"))
        self.name.setText(_translate("AboutUsPage", "PsyCorp"))
        self.tests_menu_button.setText(_translate("AboutUsPage", "TESTS"))
        self.about_us_menu_button.setText(_translate("AboutUsPage", "ABOUT US"))
        self.section_name.setText(_translate("AboutUsPage", "ABOUT US"))
        self.varn_name.setText(_translate("AboutUsPage", "Варнавский Илья"))
        self.varn_biography.setText(_translate("AboutUsPage", " ▹Ведущий программист и руководитель проекта\n"
" ▹Входит в топ выпускников первого года Яндекс.Лицея,\n"
"   а также закончил курсы по педагогике и психологии\n"
" ▹Всегда на позитиве и полный энтузиазма"))
        self.ogorod_biography.setText(_translate("AboutUsPage", " ▹Ведущий разработчик UI-дизайна приложения\n"
" ▹Входит в топ выпускников первого года Яндекс.Лицея,\n"
"   а также закончила художественную школу\n"
" ▹Полностью состоит из оптимизма и креатива"))
        self.ogorod_name.setText(_translate("AboutUsPage", "Огородник Лиза"))


class Ui_AyzenkTest(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 490)
        MainWindow.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.section_name.setObjectName("section_name")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(430, 290, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.yes_button.setFont(font)
        self.yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.yes_button.setObjectName("yes_button")
        self.sometimes_button = QtWidgets.QPushButton(self.centralwidget)
        self.sometimes_button.setGeometry(QtCore.QRect(430, 330, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.sometimes_button.setFont(font)
        self.sometimes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.sometimes_button.setObjectName("sometimes_button")
        self.no_button = QtWidgets.QPushButton(self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(430, 370, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.no_button.setFont(font)
        self.no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.no_button.setObjectName("no_button")
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(70, 210, 911, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question_text.setObjectName("question_text")
        self.question_number = QtWidgets.QLabel(self.centralwidget)
        self.question_number.setGeometry(QtCore.QRect(480, 170, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(34)
        self.question_number.setFont(font)
        self.question_number.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_number.setObjectName("question_number")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "PsyCorp"))
        self.tests_menu_button.setText(_translate("MainWindow", "TESTS"))
        self.about_us_menu_button.setText(_translate("MainWindow", "ABOUT US"))
        self.section_name.setText(_translate("MainWindow", "Тест самооценки психических состояний Айзенка"))
        self.yes_button.setText(_translate("MainWindow", "Да, это состояние мне присуще часто"))
        self.sometimes_button.setText(_translate("MainWindow", "Такое состояние у меня иногда бывает"))
        self.no_button.setText(_translate("MainWindow", "Нет, это мне совсем не подходит"))
        self.question_text.setText(_translate("MainWindow", "Не чувствую в себе уверенности"))
        self.question_number.setText(_translate("MainWindow", "1/40"))


class Ui_AyzenkTestResult(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 490)
        MainWindow.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 130, 761, 84))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frustration_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.frustration_result.setFont(font)
        self.frustration_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.frustration_result.setText("")
        self.frustration_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.frustration_result.setObjectName("frustration_result")
        self.gridLayout.addWidget(self.frustration_result, 1, 1, 1, 1)
        self.anxiety_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.anxiety_result.setFont(font)
        self.anxiety_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.anxiety_result.setText("")
        self.anxiety_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.anxiety_result.setObjectName("anxiety_result")
        self.gridLayout.addWidget(self.anxiety_result, 0, 1, 1, 1)
        self.aggressiveness_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.aggressiveness_scale.setFont(font)
        self.aggressiveness_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.aggressiveness_scale.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.aggressiveness_scale.setObjectName("aggressiveness_scale")
        self.gridLayout.addWidget(self.aggressiveness_scale, 0, 3, 1, 1)
        self.aggressiveness_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.aggressiveness_result.setFont(font)
        self.aggressiveness_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.aggressiveness_result.setText("")
        self.aggressiveness_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.aggressiveness_result.setObjectName("aggressiveness_result")
        self.gridLayout.addWidget(self.aggressiveness_result, 0, 4, 1, 1)
        self.anxiety_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.anxiety_scale.setFont(font)
        self.anxiety_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.anxiety_scale.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.anxiety_scale.setObjectName("anxiety_scale")
        self.gridLayout.addWidget(self.anxiety_scale, 0, 0, 1, 1)
        self.frustration_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.frustration_scale.setFont(font)
        self.frustration_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.frustration_scale.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frustration_scale.setObjectName("frustration_scale")
        self.gridLayout.addWidget(self.frustration_scale, 1, 0, 1, 1)
        self.stiffness_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.stiffness_result.setFont(font)
        self.stiffness_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.stiffness_result.setText("")
        self.stiffness_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stiffness_result.setObjectName("stiffness_result")
        self.gridLayout.addWidget(self.stiffness_result, 1, 4, 1, 1)
        self.stiffness_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.stiffness_scale.setFont(font)
        self.stiffness_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.stiffness_scale.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stiffness_scale.setObjectName("stiffness_scale")
        self.gridLayout.addWidget(self.stiffness_scale, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.unsave_button = QtWidgets.QPushButton(self.centralwidget)
        self.unsave_button.setGeometry(QtCore.QRect(730, 373, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.unsave_button.setFont(font)
        self.unsave_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.unsave_button.setObjectName("unsave_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "PsyCorp"))
        self.tests_menu_button.setText(_translate("MainWindow", "TESTS"))
        self.about_us_menu_button.setText(_translate("MainWindow", "ABOUT US"))
        self.section_name.setText(_translate("MainWindow", "Результат"))
        self.aggressiveness_scale.setText(_translate("MainWindow", "Шкала агрессивности       "))
        self.anxiety_scale.setText(_translate("MainWindow", "Шкала тревожности       "))
        self.frustration_scale.setText(_translate("MainWindow", "Шкала фрустрации"))
        self.stiffness_scale.setText(_translate("MainWindow", "Шкала ригидности"))
        self.unsave_button.setText(_translate("MainWindow", "Завершить тест"))


class Ui_EqTest(object):
    def setupUi(self, EqTest):
        EqTest.setObjectName("EqTest")
        EqTest.setEnabled(True)
        EqTest.resize(1000, 490)
        EqTest.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(EqTest)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.notatall_no_button = QtWidgets.QPushButton(self.centralwidget)
        self.notatall_no_button.setGeometry(QtCore.QRect(610, 290, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.notatall_no_button.setFont(font)
        self.notatall_no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.notatall_no_button.setObjectName("notatall_no_button")
        self.onthewhole_no_button = QtWidgets.QPushButton(self.centralwidget)
        self.onthewhole_no_button.setGeometry(QtCore.QRect(610, 330, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.onthewhole_no_button.setFont(font)
        self.onthewhole_no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.onthewhole_no_button.setObjectName("onthewhole_no_button")
        self.fully_no_button = QtWidgets.QPushButton(self.centralwidget)
        self.fully_no_button.setGeometry(QtCore.QRect(610, 370, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.fully_no_button.setFont(font)
        self.fully_no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.fully_no_button.setObjectName("fully_no_button")
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(60, 190, 911, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question_text.setObjectName("question_text")
        self.question_number = QtWidgets.QLabel(self.centralwidget)
        self.question_number.setGeometry(QtCore.QRect(470, 150, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(34)
        self.question_number.setFont(font)
        self.question_number.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_number.setObjectName("question_number")
        self.notatall_yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.notatall_yes_button.setGeometry(QtCore.QRect(250, 370, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.notatall_yes_button.setFont(font)
        self.notatall_yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.notatall_yes_button.setObjectName("notatall_yes_button")
        self.fully_yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.fully_yes_button.setGeometry(QtCore.QRect(250, 290, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.fully_yes_button.setFont(font)
        self.fully_yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.fully_yes_button.setObjectName("fully_yes_button")
        self.onthewhole_yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.onthewhole_yes_button.setGeometry(QtCore.QRect(250, 330, 330, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.onthewhole_yes_button.setFont(font)
        self.onthewhole_yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.onthewhole_yes_button.setObjectName("onthewhole_yes_button")
        EqTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EqTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        EqTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EqTest)
        self.statusbar.setObjectName("statusbar")
        EqTest.setStatusBar(self.statusbar)

        self.retranslateUi(EqTest)
        QtCore.QMetaObject.connectSlotsByName(EqTest)

    def retranslateUi(self, EqTest):
        _translate = QtCore.QCoreApplication.translate
        EqTest.setWindowTitle(_translate("EqTest", "MainWindow"))
        self.name.setText(_translate("EqTest", "PsyCorp"))
        self.tests_menu_button.setText(_translate("EqTest", "TESTS"))
        self.about_us_menu_button.setText(_translate("EqTest", "ABOUT US"))
        self.section_name.setText(_translate("EqTest", "Тест эмоционального интеллекта(EQ)"))
        self.notatall_no_button.setText(_translate("EqTest", "Отчасти не согласен"))
        self.onthewhole_no_button.setText(_translate("EqTest", "В основном не согласен"))
        self.fully_no_button.setText(_translate("EqTest", "Полностью не согласен"))
        self.question_text.setText(_translate("EqTest", "Для меня как отрицательные, так и положительные эмоции\n"
"служат источником знания о том, как поступать в жизни"))
        self.question_number.setText(_translate("EqTest", "1/30"))
        self.notatall_yes_button.setText(_translate("EqTest", "Отчасти согласен"))
        self.fully_yes_button.setText(_translate("EqTest", "Полностью согласен"))
        self.onthewhole_yes_button.setText(_translate("EqTest", "В основном согласен"))


class Ui_EqTestResult(object):
    def setupUi(self, EqTestResult):
        EqTestResult.setObjectName("EqTestResult")
        EqTestResult.setEnabled(True)
        EqTestResult.resize(1000, 490)
        EqTestResult.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(EqTestResult)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.unsave_button = QtWidgets.QPushButton(self.centralwidget)
        self.unsave_button.setGeometry(QtCore.QRect(810, 420, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.unsave_button.setFont(font)
        self.unsave_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.unsave_button.setObjectName("unsave_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 130, 731, 256))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.eq_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Mincho")
        font.setPointSize(28)
        self.eq_result.setFont(font)
        self.eq_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.eq_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.eq_result.setObjectName("eq_result")
        self.gridLayout.addWidget(self.eq_result, 0, 2, 1, 1)
        self.control_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.control_scale.setFont(font)
        self.control_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.control_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.control_scale.setObjectName("control_scale")
        self.gridLayout.addWidget(self.control_scale, 6, 0, 1, 1)
        self.self_control_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.self_control_result.setFont(font)
        self.self_control_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.self_control_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.self_control_result.setObjectName("self_control_result")
        self.gridLayout.addWidget(self.self_control_result, 2, 2, 1, 1)
        self.empathy_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.empathy_result.setFont(font)
        self.empathy_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.empathy_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.empathy_result.setObjectName("empathy_result")
        self.gridLayout.addWidget(self.empathy_result, 5, 2, 1, 1)
        self.control_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.control_result.setFont(font)
        self.control_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.control_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.control_result.setObjectName("control_result")
        self.gridLayout.addWidget(self.control_result, 6, 2, 1, 1)
        self.self_motivation_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.self_motivation_scale.setFont(font)
        self.self_motivation_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.self_motivation_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.self_motivation_scale.setObjectName("self_motivation_scale")
        self.gridLayout.addWidget(self.self_motivation_scale, 4, 0, 1, 1)
        self.self_motivation_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.self_motivation_result.setFont(font)
        self.self_motivation_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.self_motivation_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.self_motivation_result.setObjectName("self_motivation_result")
        self.gridLayout.addWidget(self.self_motivation_result, 4, 2, 1, 1)
        self.awareness_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.awareness_scale.setFont(font)
        self.awareness_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.awareness_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.awareness_scale.setObjectName("awareness_scale")
        self.gridLayout.addWidget(self.awareness_scale, 1, 0, 1, 1)
        self.awareness_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.awareness_result.setFont(font)
        self.awareness_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.awareness_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.awareness_result.setObjectName("awareness_result")
        self.gridLayout.addWidget(self.awareness_result, 1, 2, 1, 1)
        self.empathy_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.empathy_scale.setFont(font)
        self.empathy_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.empathy_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.empathy_scale.setObjectName("empathy_scale")
        self.gridLayout.addWidget(self.empathy_scale, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.eq_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.eq_scale.setFont(font)
        self.eq_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.eq_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.eq_scale.setObjectName("eq_scale")
        self.gridLayout.addWidget(self.eq_scale, 0, 0, 1, 1)
        self.self_control_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.self_control_scale.setFont(font)
        self.self_control_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.self_control_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.self_control_scale.setObjectName("self_control_scale")
        self.gridLayout.addWidget(self.self_control_scale, 2, 0, 1, 1)
        EqTestResult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EqTestResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        EqTestResult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EqTestResult)
        self.statusbar.setObjectName("statusbar")
        EqTestResult.setStatusBar(self.statusbar)

        self.retranslateUi(EqTestResult)
        QtCore.QMetaObject.connectSlotsByName(EqTestResult)

    def retranslateUi(self, EqTestResult):
        _translate = QtCore.QCoreApplication.translate
        EqTestResult.setWindowTitle(_translate("EqTestResult", "MainWindow"))
        self.name.setText(_translate("EqTestResult", "PsyCorp"))
        self.tests_menu_button.setText(_translate("EqTestResult", "TESTS"))
        self.about_us_menu_button.setText(_translate("EqTestResult", "ABOUT US"))
        self.section_name.setText(_translate("EqTestResult", "Результат"))
        self.unsave_button.setText(_translate("EqTestResult", "Завершить тест"))
        self.eq_result.setText(_translate("EqTestResult", "0/90"))
        self.control_scale.setText(_translate("EqTestResult", "Управление эмоциями других людей"))
        self.self_control_result.setText(_translate("EqTestResult", "0/18"))
        self.empathy_result.setText(_translate("EqTestResult", "0/18"))
        self.control_result.setText(_translate("EqTestResult", "0/18"))
        self.self_motivation_scale.setText(_translate("EqTestResult", "Самомотивация"))
        self.self_motivation_result.setText(_translate("EqTestResult", "0/18"))
        self.awareness_scale.setText(_translate("EqTestResult", "Эмоциональная осведомленность"))
        self.awareness_result.setText(_translate("EqTestResult", "0/18"))
        self.empathy_scale.setText(_translate("EqTestResult", "Эмпатия"))
        self.eq_scale.setText(_translate("EqTestResult", "Уровень эмоционального интеллекта"))
        self.self_control_scale.setText(_translate("EqTestResult", "Управление своими эмоциями"))


class Ui_HaninTest(object):
    def setupUi(self, HaninTest):
        HaninTest.setObjectName("HaninTest")
        HaninTest.setEnabled(True)
        HaninTest.resize(1000, 490)
        HaninTest.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(HaninTest)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.always_button = QtWidgets.QPushButton(self.centralwidget)
        self.always_button.setGeometry(QtCore.QRect(320, 260, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        self.always_button.setFont(font)
        self.always_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.always_button.setObjectName("always_button")
        self.often_button = QtWidgets.QPushButton(self.centralwidget)
        self.often_button.setGeometry(QtCore.QRect(320, 300, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        self.often_button.setFont(font)
        self.often_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.often_button.setObjectName("often_button")
        self.rarely_button = QtWidgets.QPushButton(self.centralwidget)
        self.rarely_button.setGeometry(QtCore.QRect(320, 340, 381, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        self.rarely_button.setFont(font)
        self.rarely_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.rarely_button.setObjectName("rarely_button")
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(70, 190, 911, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question_text.setObjectName("question_text")
        self.question_number = QtWidgets.QLabel(self.centralwidget)
        self.question_number.setGeometry(QtCore.QRect(480, 150, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(34)
        self.question_number.setFont(font)
        self.question_number.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_number.setObjectName("question_number")
        self.never_button = QtWidgets.QPushButton(self.centralwidget)
        self.never_button.setGeometry(QtCore.QRect(320, 380, 481, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        self.never_button.setFont(font)
        self.never_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.never_button.setObjectName("never_button")
        HaninTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HaninTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        HaninTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HaninTest)
        self.statusbar.setObjectName("statusbar")
        HaninTest.setStatusBar(self.statusbar)

        self.retranslateUi(HaninTest)
        QtCore.QMetaObject.connectSlotsByName(HaninTest)

    def retranslateUi(self, HaninTest):
        _translate = QtCore.QCoreApplication.translate
        HaninTest.setWindowTitle(_translate("HaninTest", "MainWindow"))
        self.name.setText(_translate("HaninTest", "PsyCorp"))
        self.tests_menu_button.setText(_translate("HaninTest", "TESTS"))
        self.about_us_menu_button.setText(_translate("HaninTest", "ABOUT US"))
        self.section_name.setText(_translate("HaninTest", "Шкала тревоги Спилбергера-Ханина"))
        self.always_button.setText(_translate("HaninTest", "Почти всегда"))
        self.often_button.setText(_translate("HaninTest", "Часто"))
        self.rarely_button.setText(_translate("HaninTest", "Почти никогда"))
        self.question_text.setText(_translate("HaninTest", "Я спокоен"))
        self.question_number.setText(_translate("HaninTest", "1/40"))
        self.never_button.setText(_translate("HaninTest", "Никогда"))


class Ui_HaninTestResult(object):
    def setupUi(self, HaninTestResult):
        HaninTestResult.setObjectName("HaninTestResult")
        HaninTestResult.setEnabled(True)
        HaninTestResult.resize(1000, 490)
        HaninTestResult.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(HaninTestResult)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.unsave_button = QtWidgets.QPushButton(self.centralwidget)
        self.unsave_button.setGeometry(QtCore.QRect(729, 410, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.unsave_button.setFont(font)
        self.unsave_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.unsave_button.setObjectName("unsave_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 240, 471, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.situational_anxiety_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(28)
        self.situational_anxiety_scale.setFont(font)
        self.situational_anxiety_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.situational_anxiety_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.situational_anxiety_scale.setObjectName("situational_anxiety_scale")
        self.gridLayout.addWidget(self.situational_anxiety_scale, 1, 0, 1, 1)
        self.situational_anxiety_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.situational_anxiety_result.setFont(font)
        self.situational_anxiety_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.situational_anxiety_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.situational_anxiety_result.setObjectName("situational_anxiety_result")
        self.gridLayout.addWidget(self.situational_anxiety_result, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.personal_anxiety_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.personal_anxiety_scale.setFont(font)
        self.personal_anxiety_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.personal_anxiety_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.personal_anxiety_scale.setObjectName("personal_anxiety_scale")
        self.gridLayout.addWidget(self.personal_anxiety_scale, 2, 0, 1, 1)
        self.personal_anxiety_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.personal_anxiety_result.setFont(font)
        self.personal_anxiety_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.personal_anxiety_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.personal_anxiety_result.setObjectName("personal_anxiety_result")
        self.gridLayout.addWidget(self.personal_anxiety_result, 2, 2, 1, 1)
        self.result_interpretation = QtWidgets.QLabel(self.centralwidget)
        self.result_interpretation.setGeometry(QtCore.QRect(570, 210, 411, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(20)
        self.result_interpretation.setFont(font)
        self.result_interpretation.setStyleSheet("color: rgb(217, 201, 186);")
        self.result_interpretation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.result_interpretation.setObjectName("result_interpretation")
        HaninTestResult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HaninTestResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        HaninTestResult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HaninTestResult)
        self.statusbar.setObjectName("statusbar")
        HaninTestResult.setStatusBar(self.statusbar)

        self.retranslateUi(HaninTestResult)
        QtCore.QMetaObject.connectSlotsByName(HaninTestResult)

    def retranslateUi(self, HaninTestResult):
        _translate = QtCore.QCoreApplication.translate
        HaninTestResult.setWindowTitle(_translate("HaninTestResult", "MainWindow"))
        self.name.setText(_translate("HaninTestResult", "PsyCorp"))
        self.tests_menu_button.setText(_translate("HaninTestResult", "TESTS"))
        self.about_us_menu_button.setText(_translate("HaninTestResult", "ABOUT US"))
        self.section_name.setText(_translate("HaninTestResult", "Результат"))
        self.unsave_button.setText(_translate("HaninTestResult", "Завершить тест"))
        self.situational_anxiety_scale.setText(_translate("HaninTestResult", "Ситуативная тревожность"))
        self.situational_anxiety_result.setText(_translate("HaninTestResult", "0/80"))
        self.personal_anxiety_scale.setText(_translate("HaninTestResult", "Личностная тревожность"))
        self.personal_anxiety_result.setText(_translate("HaninTestResult", "0/80"))
        self.result_interpretation.setText(_translate("HaninTestResult", "Менее 30 баллов – низкая тревожность\n"
"31 — 44 балла — умеренная тревожность\n"
"45 и более — высокая тревожность"))


class Ui_HomePage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 490)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#tests_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(380, 100, 310, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(48)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(217, 201, 186);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.lsi_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.lsi_test_button.setGeometry(QtCore.QRect(50, 210, 900, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.lsi_test_button.setFont(font)
        self.lsi_test_button.setStyleSheet("color: rgb(217, 200, 184);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;\n"
"")
        self.lsi_test_button.setObjectName("lsi_test_button")
        self.eq_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.eq_test_button.setGeometry(QtCore.QRect(50, 250, 900, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.eq_test_button.setFont(font)
        self.eq_test_button.setStyleSheet("color: rgb(217, 200, 184);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.eq_test_button.setObjectName("eq_test_button")
        self.rathus_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.rathus_test_button.setGeometry(QtCore.QRect(50, 290, 900, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.rathus_test_button.setFont(font)
        self.rathus_test_button.setStyleSheet("color: rgb(217, 200, 184);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.rathus_test_button.setObjectName("rathus_test_button")
        self.ayzenk_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.ayzenk_test_button.setGeometry(QtCore.QRect(50, 170, 900, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.ayzenk_test_button.setFont(font)
        self.ayzenk_test_button.setStyleSheet("color: rgb(217, 200, 184);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.ayzenk_test_button.setObjectName("ayzenk_test_button")
        self.hanin_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.hanin_test_button.setGeometry(QtCore.QRect(50, 330, 900, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(28)
        self.hanin_test_button.setFont(font)
        self.hanin_test_button.setStyleSheet("color: rgb(217, 200, 184);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.hanin_test_button.setObjectName("hanin_test_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "PsyCorp"))
        self.tests_menu_button.setText(_translate("MainWindow", "TESTS"))
        self.about_us_menu_button.setText(_translate("MainWindow", "ABOUT US"))
        self.section_name.setText(_translate("MainWindow", "TESTS"))
        self.lsi_test_button.setText(_translate("MainWindow", "2.Тест индекса жизненной удовлетворенности"))
        self.eq_test_button.setText(_translate("MainWindow", "3.Тест эмоционального интеллекта(EQ)"))
        self.rathus_test_button.setText(_translate("MainWindow", "4.Тест уверенности в себе Рейзаса"))
        self.ayzenk_test_button.setText(_translate("MainWindow", "1.Тест самооценки психических состояний Айзенка"))
        self.hanin_test_button.setText(_translate("MainWindow", "5.Шкала тревоги Спилбергера-Ханина"))


class Ui_LsiTest(object):
    def setupUi(self, LsiTest):
        LsiTest.setObjectName("LsiTest")
        LsiTest.setEnabled(True)
        LsiTest.resize(1000, 490)
        LsiTest.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(LsiTest)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(500, 290, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.yes_button.setFont(font)
        self.yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.yes_button.setObjectName("yes_button")
        self.no_button = QtWidgets.QPushButton(self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(500, 330, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.no_button.setFont(font)
        self.no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.no_button.setObjectName("no_button")
        self.idontknow_button = QtWidgets.QPushButton(self.centralwidget)
        self.idontknow_button.setGeometry(QtCore.QRect(500, 370, 280, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(22)
        self.idontknow_button.setFont(font)
        self.idontknow_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.idontknow_button.setObjectName("idontknow_button")
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(70, 210, 911, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question_text.setObjectName("question_text")
        self.question_number = QtWidgets.QLabel(self.centralwidget)
        self.question_number.setGeometry(QtCore.QRect(480, 170, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(34)
        self.question_number.setFont(font)
        self.question_number.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_number.setObjectName("question_number")
        LsiTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LsiTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        LsiTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LsiTest)
        self.statusbar.setObjectName("statusbar")
        LsiTest.setStatusBar(self.statusbar)

        self.retranslateUi(LsiTest)
        QtCore.QMetaObject.connectSlotsByName(LsiTest)

    def retranslateUi(self, LsiTest):
        _translate = QtCore.QCoreApplication.translate
        LsiTest.setWindowTitle(_translate("LsiTest", "MainWindow"))
        self.name.setText(_translate("LsiTest", "PsyCorp"))
        self.tests_menu_button.setText(_translate("LsiTest", "TESTS"))
        self.about_us_menu_button.setText(_translate("LsiTest", "ABOUT US"))
        self.section_name.setText(_translate("LsiTest", "Индекс жизненной удовлетворенности"))
        self.yes_button.setText(_translate("LsiTest", "Согласен"))
        self.no_button.setText(_translate("LsiTest", "Не согласен"))
        self.idontknow_button.setText(_translate("LsiTest", "Не знаю"))
        self.question_text.setText(_translate("LsiTest", "С возрастом многое мне кажется лучше, чем я ожидал раньше"))
        self.question_number.setText(_translate("LsiTest", "1/20"))


class Ui_LsiTestResult(object):
    def setupUi(self, LsiTestResult):
        LsiTestResult.setObjectName("LsiTestResult")
        LsiTestResult.setEnabled(True)
        LsiTestResult.resize(1000, 490)
        LsiTestResult.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(LsiTestResult)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.unsave_button = QtWidgets.QPushButton(self.centralwidget)
        self.unsave_button.setGeometry(QtCore.QRect(760, 410, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.unsave_button.setFont(font)
        self.unsave_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.unsave_button.setObjectName("unsave_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 150, 671, 256))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lsi_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Mincho")
        font.setPointSize(28)
        self.lsi_result.setFont(font)
        self.lsi_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.lsi_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lsi_result.setObjectName("lsi_result")
        self.gridLayout.addWidget(self.lsi_result, 0, 2, 1, 1)
        self.background_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.background_scale.setFont(font)
        self.background_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.background_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.background_scale.setObjectName("background_scale")
        self.gridLayout.addWidget(self.background_scale, 6, 0, 1, 1)
        self.sequence_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.sequence_result.setFont(font)
        self.sequence_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.sequence_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_result.setObjectName("sequence_result")
        self.gridLayout.addWidget(self.sequence_result, 2, 2, 1, 1)
        self.appraisal_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.appraisal_result.setFont(font)
        self.appraisal_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.appraisal_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.appraisal_result.setObjectName("appraisal_result")
        self.gridLayout.addWidget(self.appraisal_result, 5, 2, 1, 1)
        self.background_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.background_result.setFont(font)
        self.background_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.background_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.background_result.setObjectName("background_result")
        self.gridLayout.addWidget(self.background_result, 6, 2, 1, 1)
        self.consistency_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.consistency_scale.setFont(font)
        self.consistency_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.consistency_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.consistency_scale.setObjectName("consistency_scale")
        self.gridLayout.addWidget(self.consistency_scale, 4, 0, 1, 1)
        self.consistency_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.consistency_result.setFont(font)
        self.consistency_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.consistency_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.consistency_result.setObjectName("consistency_result")
        self.gridLayout.addWidget(self.consistency_result, 4, 2, 1, 1)
        self.interest_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.interest_scale.setFont(font)
        self.interest_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.interest_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.interest_scale.setObjectName("interest_scale")
        self.gridLayout.addWidget(self.interest_scale, 1, 0, 1, 1)
        self.interest_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.interest_result.setFont(font)
        self.interest_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.interest_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.interest_result.setObjectName("interest_result")
        self.gridLayout.addWidget(self.interest_result, 1, 2, 1, 1)
        self.appraisal_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.appraisal_scale.setFont(font)
        self.appraisal_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.appraisal_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.appraisal_scale.setObjectName("appraisal_scale")
        self.gridLayout.addWidget(self.appraisal_scale, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.lsi_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.lsi_scale.setFont(font)
        self.lsi_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.lsi_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lsi_scale.setObjectName("lsi_scale")
        self.gridLayout.addWidget(self.lsi_scale, 0, 0, 1, 1)
        self.sequence_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.sequence_scale.setFont(font)
        self.sequence_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.sequence_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequence_scale.setObjectName("sequence_scale")
        self.gridLayout.addWidget(self.sequence_scale, 2, 0, 1, 1)
        LsiTestResult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LsiTestResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        LsiTestResult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LsiTestResult)
        self.statusbar.setObjectName("statusbar")
        LsiTestResult.setStatusBar(self.statusbar)

        self.retranslateUi(LsiTestResult)
        QtCore.QMetaObject.connectSlotsByName(LsiTestResult)

    def retranslateUi(self, LsiTestResult):
        _translate = QtCore.QCoreApplication.translate
        LsiTestResult.setWindowTitle(_translate("LsiTestResult", "MainWindow"))
        self.name.setText(_translate("LsiTestResult", "PsyCorp"))
        self.tests_menu_button.setText(_translate("LsiTestResult", "TESTS"))
        self.about_us_menu_button.setText(_translate("LsiTestResult", "ABOUT US"))
        self.section_name.setText(_translate("LsiTestResult", "Результат"))
        self.unsave_button.setText(_translate("LsiTestResult", "Завершить тест"))
        self.lsi_result.setText(_translate("LsiTestResult", "0/40"))
        self.background_scale.setText(_translate("LsiTestResult", "Общий фон настроения"))
        self.sequence_result.setText(_translate("LsiTestResult", "0/8  "))
        self.appraisal_result.setText(_translate("LsiTestResult", "0/8  "))
        self.background_result.setText(_translate("LsiTestResult", "0/8  "))
        self.consistency_scale.setText(_translate("LsiTestResult", "Согласованность между поставленными и достигнутыми целями"))
        self.consistency_result.setText(_translate("LsiTestResult", "0/8  "))
        self.interest_scale.setText(_translate("LsiTestResult", "Интерес к жизни"))
        self.interest_result.setText(_translate("LsiTestResult", "0/8  "))
        self.appraisal_scale.setText(_translate("LsiTestResult", "Положительная оценка себя и собственных поступков"))
        self.lsi_scale.setText(_translate("LsiTestResult", "Индекс  жизненной  удовлетворенности"))
        self.sequence_scale.setText(_translate("LsiTestResult", "Последовательность  в  достижении  целей"))


class Ui_RathusTest(object):
    def setupUi(self, RathusTest):
        RathusTest.setObjectName("RathusTest")
        RathusTest.setEnabled(True)
        RathusTest.resize(1000, 490)
        RathusTest.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(RathusTest)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.very_yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.very_yes_button.setGeometry(QtCore.QRect(320, 260, 321, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.very_yes_button.setFont(font)
        self.very_yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.very_yes_button.setObjectName("very_yes_button")
        self.yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.yes_button.setGeometry(QtCore.QRect(320, 300, 451, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.yes_button.setFont(font)
        self.yes_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.yes_button.setObjectName("yes_button")
        self.so_so_button = QtWidgets.QPushButton(self.centralwidget)
        self.so_so_button.setGeometry(QtCore.QRect(320, 340, 381, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.so_so_button.setFont(font)
        self.so_so_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.so_so_button.setObjectName("so_so_button")
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(70, 190, 911, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.question_text.setObjectName("question_text")
        self.question_number = QtWidgets.QLabel(self.centralwidget)
        self.question_number.setGeometry(QtCore.QRect(480, 150, 91, 35))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(34)
        self.question_number.setFont(font)
        self.question_number.setStyleSheet("color: rgb(217, 201, 186);")
        self.question_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_number.setObjectName("question_number")
        self.very_no_button = QtWidgets.QPushButton(self.centralwidget)
        self.very_no_button.setGeometry(QtCore.QRect(320, 420, 441, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.very_no_button.setFont(font)
        self.very_no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.very_no_button.setObjectName("very_no_button")
        self.no_button = QtWidgets.QPushButton(self.centralwidget)
        self.no_button.setGeometry(QtCore.QRect(320, 380, 481, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.no_button.setFont(font)
        self.no_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.no_button.setObjectName("no_button")
        RathusTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RathusTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        RathusTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RathusTest)
        self.statusbar.setObjectName("statusbar")
        RathusTest.setStatusBar(self.statusbar)

        self.retranslateUi(RathusTest)
        QtCore.QMetaObject.connectSlotsByName(RathusTest)

    def retranslateUi(self, RathusTest):
        _translate = QtCore.QCoreApplication.translate
        RathusTest.setWindowTitle(_translate("RathusTest", "MainWindow"))
        self.name.setText(_translate("RathusTest", "PsyCorp"))
        self.tests_menu_button.setText(_translate("RathusTest", "TESTS"))
        self.about_us_menu_button.setText(_translate("RathusTest", "ABOUT US"))
        self.section_name.setText(_translate("RathusTest", "Тест уверенности в себе Рейзаса"))
        self.very_yes_button.setText(_translate("RathusTest", "Очень характерно для меня, описание очень верное"))
        self.yes_button.setText(_translate("RathusTest", "Довольно характерно для меня — скорее да, чем нет"))
        self.so_so_button.setText(_translate("RathusTest", "Отчасти характерно, отчасти не характерно"))
        self.question_text.setText(_translate("RathusTest", "Большинство людей, по-видимому, агрессивнее и увереннее в себе, чем я"))
        self.question_number.setText(_translate("RathusTest", "1/30"))
        self.very_no_button.setText(_translate("RathusTest", "Совсем не характерно для меня, описание не верно"))
        self.no_button.setText(_translate("RathusTest", "Довольно не характерно для меня — скорее нет, чем да"))


class Ui_RathusTestResult(object):
    def setupUi(self, RathusTestResult):
        RathusTestResult.setObjectName("RathusTestResult")
        RathusTestResult.setEnabled(True)
        RathusTestResult.resize(1000, 490)
        RathusTestResult.setStyleSheet("background-color: rgb(76, 68, 57);")
        self.centralwidget = QtWidgets.QWidget(RathusTestResult)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(70, 0, 930, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(223, 206, 190);\n"
"color: rgb(48, 43, 38);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.tests_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.tests_menu_button.setGeometry(QtCore.QRect(70, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(26)
        self.tests_menu_button.setFont(font)
        self.tests_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;")
        self.tests_menu_button.setObjectName("tests_menu_button")
        self.about_us_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_us_menu_button.setGeometry(QtCore.QRect(535, 40, 465, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(26)
        self.about_us_menu_button.setFont(font)
        self.about_us_menu_button.setStyleSheet("background-color: rgb(129, 123, 109);\n"
"color: rgb(76, 68, 57);\n"
"border: 0;\n"
"padding: 0;\n"
"QPushButton#about_us_menu_button:hover {\n"
"    background-color: rgb(224, 255, 0);\n"
"}\n"
"")
        self.about_us_menu_button.setObjectName("about_us_menu_button")
        self.section_name = QtWidgets.QLabel(self.centralwidget)
        self.section_name.setGeometry(QtCore.QRect(9, 80, 991, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(40)
        self.section_name.setFont(font)
        self.section_name.setStyleSheet("color: rgb(223, 206, 190);")
        self.section_name.setAlignment(QtCore.Qt.AlignCenter)
        self.section_name.setObjectName("section_name")
        self.unsave_button = QtWidgets.QPushButton(self.centralwidget)
        self.unsave_button.setGeometry(QtCore.QRect(739, 410, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.unsave_button.setFont(font)
        self.unsave_button.setStyleSheet("color: rgb(243, 225, 208);\n"
"border: 0;\n"
"padding: 0;\n"
"text-align: left;")
        self.unsave_button.setObjectName("unsave_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 240, 351, 63))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.confidence_result = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Mincho")
        font.setPointSize(28)
        self.confidence_result.setFont(font)
        self.confidence_result.setStyleSheet("color: rgb(217, 201, 186);")
        self.confidence_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confidence_result.setObjectName("confidence_result")
        self.gridLayout.addWidget(self.confidence_result, 1, 2, 1, 1)
        self.confidence_scale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.confidence_scale.setFont(font)
        self.confidence_scale.setStyleSheet("color: rgb(217, 201, 186);")
        self.confidence_scale.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confidence_scale.setObjectName("confidence_scale")
        self.gridLayout.addWidget(self.confidence_scale, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.result_interpretation = QtWidgets.QLabel(self.centralwidget)
        self.result_interpretation.setGeometry(QtCore.QRect(590, 210, 381, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(20)
        self.result_interpretation.setFont(font)
        self.result_interpretation.setStyleSheet("color: rgb(217, 201, 186);")
        self.result_interpretation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.result_interpretation.setObjectName("result_interpretation")
        RathusTestResult.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RathusTestResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        RathusTestResult.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RathusTestResult)
        self.statusbar.setObjectName("statusbar")
        RathusTestResult.setStatusBar(self.statusbar)

        self.retranslateUi(RathusTestResult)
        QtCore.QMetaObject.connectSlotsByName(RathusTestResult)

    def retranslateUi(self, RathusTestResult):
        _translate = QtCore.QCoreApplication.translate
        RathusTestResult.setWindowTitle(_translate("RathusTestResult", "MainWindow"))
        self.name.setText(_translate("RathusTestResult", "PsyCorp"))
        self.tests_menu_button.setText(_translate("RathusTestResult", "TESTS"))
        self.about_us_menu_button.setText(_translate("RathusTestResult", "ABOUT US"))
        self.section_name.setText(_translate("RathusTestResult", "Результат"))
        self.unsave_button.setText(_translate("RathusTestResult", "Завершить тест"))
        self.confidence_result.setText(_translate("RathusTestResult", "0/120"))
        self.confidence_scale.setText(_translate("RathusTestResult", "Уверенность в себе"))
        self.result_interpretation.setText(_translate("RathusTestResult", "0 - 24: Очень неуверен в себе\n"
"25 - 48: Скорее не уверен, чем уверен\n"
"49 - 72: Среднее значение уверенности\n"
"73 - 96: Уверен в себе\n"
"97 - 120: Слишком самоуверен"))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Logic Of Application
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class HomePage(QMainWindow, Ui_HomePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.ayzenk_test_button.setStyleSheet("""
                                         #ayzenk_test_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #ayzenk_test_button:hover {color: rgb(179, 166, 154);}
                                         """)
        self.lsi_test_button.setStyleSheet("""
                                         #lsi_test_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #lsi_test_button:hover {color: rgb(179, 166, 154);}
                                         """)
        self.eq_test_button.setStyleSheet("""
                                         #eq_test_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #eq_test_button:hover {color: rgb(179, 166, 154);}
                                         """)
        self.rathus_test_button.setStyleSheet("""
                                         #rathus_test_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #rathus_test_button:hover {color: rgb(179, 166, 154);}
                                         """)
        self.hanin_test_button.setStyleSheet("""
                                         #hanin_test_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #hanin_test_button:hover {color: rgb(179, 166, 154);}
                                         """)

        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.ayzenk_test_button.clicked.connect(self.ayzenkTestRun)
        self.lsi_test_button.clicked.connect(self.lsiTestRun)
        self.eq_test_button.clicked.connect(self.eqTestRun)
        self.rathus_test_button.clicked.connect(self.rathusTestRun)
        self.hanin_test_button.clicked.connect(self.haninTestRun)


    def aboutUsRun(self):
        changer(a_u_p, h_p)

    def ayzenkTestRun(self):
        changer(a_t, h_p)

    def lsiTestRun(self):
        changer(l_t, h_p)

    def eqTestRun(self):
        changer(e_t, h_p)

    def rathusTestRun(self):
        changer(r_t, h_p)

    def haninTestRun(self):
        changer(h_t, h_p)


class AboutUsPage(QMainWindow, Ui_AboutUsPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")

        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)


        self.pixmap_ogorod_photo = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\ogorodnik_photo.png')
        
        self.ogorod_photo = QLabel(self)
        self.ogorod_photo.move(700, 290)
        self.ogorod_photo.resize(130, 130)
        self.ogorod_photo.setPixmap(self.pixmap_ogorod_photo)


        self.pixmap_varn_photo = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\varn_photo.png')
        
        self.varn_photo = QLabel(self)
        self.varn_photo.move(140, 130)
        self.varn_photo.resize(130, 130)
        self.varn_photo.setPixmap(self.pixmap_varn_photo)


        self.tests_menu_button.clicked.connect(self.testsRun)

    def testsRun(self):
        changer(h_p, a_u_p)


class AyzenkTest(QMainWindow, Ui_AyzenkTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.TESTS_DB = sqlite3.connect("C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Data Bases\\tests.sqlite")
        self.cursor = self.TESTS_DB.cursor()

        self.take_question_sql = "SELECT * FROM AYZENK_TEST WHERE QUESTION_NUMBERS=?"
        
        self.counter = 1
        self.points = [0, 0, 0, 0]
        #1. Тревожность, 2. Фрустрация, 3. Агрессивность, 4. Ригидность

        self.setWindowTitle('PsyCorp')

        self.sometimes_button.setStyleSheet("""
                                         #sometimes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #sometimes_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.yes_button.setStyleSheet("""
                                         #yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #yes_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.no_button.setStyleSheet("""
                                         #no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #no_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.yes_button.clicked.connect(self.yesAnswerRun)
        self.sometimes_button.clicked.connect(self.sometimesAnswerRun)
        self.no_button.clicked.connect(self.noAnswerRun)

    def questionChanger(self):
        self.counter += 1
        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[1])

    def testsRun(self):
        self.points = [0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(h_p, a_t)

    def aboutUsRun(self):
        self.points = [0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(a_u_p, h_p)

    def yesAnswerRun(self):
        if self.counter <= 10:
            self.points[0] += 2
        elif self.counter <= 20:
            self.points[1] += 2
        elif self.counter <= 30:
            self.points[2] += 2
        else:
            self.points[3] += 2

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def sometimesAnswerRun(self):
        if self.counter <= 10:
            self.points[0] += 1
        elif self.counter <= 20:
            self.points[1] += 1
        elif self.counter <= 30:
            self.points[2] += 1
        else:
            self.points[3] += 1

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def noAnswerRun(self):
        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def resulter(self):
        a_t_r.anxiety_result.setText(str(self.points[0]) + '/20')
        a_t_r.frustration_result.setText(str(self.points[1]) + '/20')
        a_t_r.aggressiveness_result.setText(str(self.points[2]) + '/20')
        a_t_r.stiffness_result.setText(str(self.points[3]) + '/20')
        a_t_r.x = stringMaker(self.points)

        self.points = [0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(a_t_r, a_t)


class AyzenkTestResult(QMainWindow, Ui_AyzenkTestResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')

        self.unsave_button.setStyleSheet("""
                                         #unsave_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: right;}
                                         #unsave_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       

        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.user_name = ''
        self.x = '0 0 0 0'

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.unsave_button.clicked.connect(self.unsaveRun)

    def testsRun(self):
        changer(h_p, a_t_r)

    def aboutUsRun(self):
        changer(a_u_p, a_t_r)

    def unsaveRun(self):
        self.testsRun()


class LsiTest(QMainWindow, Ui_LsiTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.TESTS_DB = sqlite3.connect("C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Data Bases\\tests.sqlite")
        self.cursor = self.TESTS_DB.cursor()

        self.take_question_sql = "SELECT * FROM LSI_TEST WHERE QUESTION_NUMBERS=?"
        
        self.counter = 1
        self.points = [0, 0, 0, 0, 0]
        self.question_category = ((1, 6, 9, 11), (8, 13, 16, 17), (2, 4, 5, 19),
                                  (12, 14, 15, 20), (3, 7, 10, 18))
        # 1. Интерес к жизни, 2. Последовательность  в  достижении  целей, 
        # 3. Согласованность между поставленными и достигнутыми целями,
        # 4. Положительная оценка себя и собственных поступков,
        # 5. Общий фон настроения

        self.setWindowTitle('PsyCorp')

        self.idontknow_button.setStyleSheet("""
                                         #idontknow_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #idontknow_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.yes_button.setStyleSheet("""
                                         #yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #yes_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.no_button.setStyleSheet("""#no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #no_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.yes_button.clicked.connect(self.yesAnswerRun)
        self.idontknow_button.clicked.connect(self.idontknowAnswerRun)
        self.no_button.clicked.connect(self.noAnswerRun)

    def questionChanger(self):
        self.counter += 1
        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/20')
        self.question_text.setText(self.cursor.fetchone()[1])

    def testsRun(self):
        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/20')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(h_p, l_t)

    def aboutUsRun(self):
        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/20')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(a_u_p, l_t)

    def yesAnswerRun(self):
        self.cursor.execute(self.take_question_sql, [(self.counter)])

        if self.counter in self.question_category[0]:
            self.points[0] += self.cursor.fetchone()[2]
        elif self.counter in self.question_category[1]:
            self.points[1] += self.cursor.fetchone()[2]
        elif self.counter in self.question_category[2]:
            self.points[2] += self.cursor.fetchone()[2]
        elif self.counter in self.question_category[3]:
            self.points[3] += self.cursor.fetchone()[2]
        else:
            self.points[4] += self.cursor.fetchone()[2]

        if self.counter < 20:
            self.questionChanger()
        else:
            self.resulter()

    def idontknowAnswerRun(self):
        self.cursor.execute(self.take_question_sql, [(self.counter)])

        if self.counter in self.question_category[0]:
            self.points[0] += self.cursor.fetchone()[4]
        elif self.counter in self.question_category[1]:
            self.points[1] += self.cursor.fetchone()[4]
        elif self.counter in self.question_category[2]:
            self.points[2] += self.cursor.fetchone()[4]
        elif self.counter in self.question_category[3]:
            self.points[3] += self.cursor.fetchone()[4]
        else:
            self.points[4] += self.cursor.fetchone()[4]

        if self.counter < 20:
            self.questionChanger()
        else:
            self.resulter()

    def noAnswerRun(self):
        self.cursor.execute(self.take_question_sql, [(self.counter)])

        if self.counter in self.question_category[0]:
            self.points[0] += self.cursor.fetchone()[3]
        elif self.counter in self.question_category[1]:
            self.points[1] += self.cursor.fetchone()[3]
        elif self.counter in self.question_category[2]:
            self.points[2] += self.cursor.fetchone()[3]
        elif self.counter in self.question_category[3]:
            self.points[3] += self.cursor.fetchone()[3]
        else:
            self.points[4] += self.cursor.fetchone()[3]

        if self.counter < 20:
            self.questionChanger()
        else:
            self.resulter()

    def resulter(self):
        self.points.append(sum(self.points))
        l_t_r.lsi_result.setText(str(self.points[5]) + '/40')
        l_t_r.interest_result.setText(str(self.points[0]) + '/8')
        l_t_r.sequence_result.setText(str(self.points[1]) + '/8')
        l_t_r.consistency_result.setText(str(self.points[2]) + '/8')
        l_t_r.appraisal_result.setText(str(self.points[3]) + '/8')
        l_t_r.background_result.setText(str(self.points[4]) + '/8')
        l_t_r.x = stringMaker(self.points)


        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/20')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(l_t_r, l_t)


class LsiTestResult(QMainWindow, Ui_LsiTestResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')

        self.unsave_button.setStyleSheet("""
                                         #unsave_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #unsave_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.user_name = ''
        self.x = '0 0 0 0 0'

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.unsave_button.clicked.connect(self.unsaveRun)

    def testsRun(self):
        changer(h_p, l_t_r)

    def aboutUsRun(self):
        changer(a_u_p, l_t_r)

    def unsaveRun(self):
        self.testsRun()


class EqTest(QMainWindow, Ui_EqTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.TESTS_DB = sqlite3.connect("C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Data Bases\\tests.sqlite")
        self.cursor = self.TESTS_DB.cursor()

        self.take_question_sql = "SELECT * FROM EQ_TEST WHERE QUESTION_NUMBERS=?"
        
        self.counter = 1
        self.points = [0, 0, 0, 0, 0]

        self.question_category = ((1, 2, 4, 17, 19, 25), (3, 7, 8, 10, 18, 30), 
                                  (5, 6, 13, 14, 16, 22), (9, 11, 20, 21, 23, 28),
                                  (12, 15, 24, 26, 27, 29))
        # 1.Эмоциональная осведомленность, 2.Управление своими эмоциями,
        # 3.Самомотивация, 4.Эмпатия, 5.Управление эмоциями других людей

        self.setWindowTitle('PsyCorp')

        self.fully_yes_button.setStyleSheet("""
                                         #fully_yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #fully_yes_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.onthewhole_yes_button.setStyleSheet("""
                                         #onthewhole_yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #onthewhole_yes_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.fully_no_button.setStyleSheet("""
                                         #fully_no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #fully_no_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.onthewhole_no_button.setStyleSheet("""
                                         #onthewhole_no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #onthewhole_no_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.notatall_yes_button.setStyleSheet("""
                                         #notatall_yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #notatall_yes_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.notatall_no_button.setStyleSheet("""
                                         #notatall_no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #notatall_no_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.fully_yes_button.clicked.connect(self.fullyYesAnswerRun)
        self.fully_no_button.clicked.connect(self.fullyNoAnswerRun)
        self.notatall_yes_button.clicked.connect(self.notatallYesAnswerRun)
        self.onthewhole_yes_button.clicked.connect(self.onthewholeYesAnswerRun)
        self.onthewhole_no_button.clicked.connect(self.onthewholeNoAnswerRun)
        self.notatall_no_button.clicked.connect(self.notatallNoAnswerRun)

    def questionChanger(self):
        self.counter += 1
        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[1])

    def testsRun(self):
        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(h_p, e_t)

    def aboutUsRun(self):
        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(a_u_p, e_t)

    def fullyYesAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 3
        elif self.counter in self.question_category[1]:
            self.points[1] += 3
        elif self.counter in self.question_category[2]:
            self.points[2] += 3
        elif self.counter in self.question_category[3]:
            self.points[3] += 3
        else:
            self.points[4] += 3

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def fullyNoAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] -= 3
        elif self.counter in self.question_category[1]:
            self.points[1] -= 3
        elif self.counter in self.question_category[2]:
            self.points[2] -= 3
        elif self.counter in self.question_category[3]:
            self.points[3] -= 3
        else:
            self.points[4] -= 3

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def onthewholeYesAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 2
        elif self.counter in self.question_category[1]:
            self.points[1] += 2
        elif self.counter in self.question_category[2]:
            self.points[2] += 2
        elif self.counter in self.question_category[3]:
            self.points[3] += 2
        else:
            self.points[4] += 2

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def onthewholeNoAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] -= 2
        elif self.counter in self.question_category[1]:
            self.points[1] -= 2
        elif self.counter in self.question_category[2]:
            self.points[2] -= 2
        elif self.counter in self.question_category[3]:
            self.points[3] -= 2
        else:
            self.points[4] -= 2

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def notatallYesAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 1
        elif self.counter in self.question_category[1]:
            self.points[1] += 1
        elif self.counter in self.question_category[2]:
            self.points[2] += 1
        elif self.counter in self.question_category[3]:
            self.points[3] += 1
        else:
            self.points[4] += 1

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def notatallNoAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] -= 1
        elif self.counter in self.question_category[1]:
            self.points[1] -= 1
        elif self.counter in self.question_category[2]:
            self.points[2] -= 1
        elif self.counter in self.question_category[3]:
            self.points[3] -= 1
        else:
            self.points[4] -= 1

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def resulter(self):
        self.points.append(sum(self.points))
        e_t_r.awareness_result.setText(str(self.points[0]) + '/18')
        e_t_r.self_control_result.setText(str(self.points[1]) + '/18')
        e_t_r.self_motivation_result.setText(str(self.points[2]) + '/18')
        e_t_r.empathy_result.setText(str(self.points[3]) + '/18')
        e_t_r.control_result.setText(str(self.points[4]) + '/18')
        e_t_r.eq_result.setText(str(self.points[5]) + '/90')
        e_t_r.x = stringMaker(self.points)

        self.points = [0, 0, 0, 0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, [(self.counter)])
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[1])

        changer(e_t_r, e_t)


class EqTestResult(QMainWindow, Ui_EqTestResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')

        self.unsave_button.setStyleSheet("""
                                         #unsave_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #unsave_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.user_name = ''
        self.x = '0 0 0 0 0 0'

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.unsave_button.clicked.connect(self.unsaveRun)

    def testsRun(self):
        changer(h_p, e_t_r)

    def aboutUsRun(self):
        changer(a_u_p, e_t_r)

    def unsaveRun(self):
        self.testsRun()


class RathusTest(QMainWindow, Ui_RathusTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.TESTS_DB = sqlite3.connect("C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Data Bases\\tests.sqlite")
        self.cursor = self.TESTS_DB.cursor()

        self.take_question_sql = "SELECT QUESTIONS FROM RATHUS_TEST WHERE QUESTION_NUMBERS=?"
        
        self.counter = 1
        self.points = [0, 0]

        self.question_category = ((3, 6, 7, 8, 10, 18, 20, 21, 22, 25, 27, 28, 29),
                                  (1, 2, 4, 5, 9, 11, 12, 13, 14, 15, 16,
                                   17, 19, 23, 24, 26, 30))

        self.setWindowTitle('PsyCorp')

        self.very_yes_button.setStyleSheet("""
                                         #very_yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #very_yes_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.yes_button.setStyleSheet("""
                                         #yes_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #yes_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.very_no_button.setStyleSheet("""
                                         #very_no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #very_no_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.no_button.setStyleSheet("""
                                         #no_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #no_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.so_so_button.setStyleSheet("""
                                         #so_so_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #so_so_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")

        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.no_button.clicked.connect(self.noAnswerRun)
        self.very_no_button.clicked.connect(self.veryNoAnswerRun)
        self.yes_button.clicked.connect(self.yesAnswerRun)
        self.very_yes_button.clicked.connect(self.veryYesAnswerRun)
        self.so_so_button.clicked.connect(self.soSoAnswerRun)

    def questionChanger(self):
        self.counter += 1
        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[0])

    def testsRun(self):
        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(h_p, r_t)

    def aboutUsRun(self):
        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(a_u_p, r_t)

    def noAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 2
        else:
            self.points[1] += 2

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def veryNoAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 1
        else:
            self.points[1] += 1

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def yesAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 4
        else:
            self.points[1] += 4

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def veryYesAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 5
        else:
            self.points[1] += 5

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def soSoAnswerRun(self):
        if self.counter in self.question_category[0]:
            self.points[0] += 3
        else:
            self.points[1] += 3

        if self.counter < 30:
            self.questionChanger()
        else:
            self.resulter()

    def resulter(self):
        self.points.append(sum(self.points))
        r_t_r.confidence_result.setText(str(self.points[0] + 72 - self.points[1]) + '/120')
        r_t_r.x = str(self.points[0] + 72 - self.points[1])

        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/30')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(r_t_r, r_t)


class RathusTestResult(QMainWindow, Ui_RathusTestResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')

        self.unsave_button.setStyleSheet("""
                                         #unsave_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #unsave_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.user_name = ''
        self.x = '0'

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.unsave_button.clicked.connect(self.unsaveRun)

    def testsRun(self):
        changer(h_p, r_t_r)

    def aboutUsRun(self):
        changer(a_u_p, r_t_r)

    def unsaveRun(self):
        self.testsRun()


class HaninTest(QMainWindow, Ui_HaninTest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.TESTS_DB = sqlite3.connect("C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Data Bases\\tests.sqlite")
        self.cursor = self.TESTS_DB.cursor()

        self.take_question_sql = "SELECT QUESTIONS FROM HANIN_TEST WHERE QUESTION_NUMBERS=?"
        
        self.counter = 1
        self.points = [0, 0]

        self.answer_weight = ((3, 4, 6, 7, 9, 12, 13, 14, 17, 18, 22, 23, 24,
                               25, 28, 29, 31, 32, 33, 34, 35, 37, 38, 40),
                              (1, 2, 5, 8, 10, 11, 15, 16, 19, 20,
                               21, 26, 27, 30, 36, 39))

        self.setWindowTitle('PsyCorp')

        self.always_button.setStyleSheet("""
                                         #always_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #always_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.often_button.setStyleSheet("""
                                         #often_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #often_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.rarely_button.setStyleSheet("""
                                         #rarely_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #rarely_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.never_button.setStyleSheet("""
                                         #never_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #never_button:hover {color: rgb(179, 166, 154);}
                                      """)

        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")

        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.always_button.clicked.connect(self.alwaysAnswerRun)
        self.often_button.clicked.connect(self.oftenAnswerRun)
        self.rarely_button.clicked.connect(self.rarelyAnswerRun)
        self.never_button.clicked.connect(self.neverAnswerRun)

    def questionChanger(self):
        self.counter += 1
        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[0])

    def testsRun(self):
        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(h_p, r_t)

    def aboutUsRun(self):
        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(a_u_p, r_t)

    def alwaysAnswerRun(self):
        if self.counter <= 20:
            if self.counter in self.answer_weight[0]:
                self.points[0] += 4
            else:
                self.points[0] += 1
        else:
            if self.counter in self.answer_weight[0]:
                self.points[1] += 4
            else:
                self.points[1] += 1

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def oftenAnswerRun(self):
        if self.counter <= 20:
            if self.counter in self.answer_weight[0]:
                self.points[0] += 3
            else:
                self.points[0] += 2
        else:
            if self.counter in self.answer_weight[0]:
                self.points[1] += 3
            else:
                self.points[1] += 2

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def rarelyAnswerRun(self):
        if self.counter <= 20:
            if self.counter in self.answer_weight[0]:
                self.points[0] += 2
            else:
                self.points[0] += 3
        else:
            if self.counter in self.answer_weight[0]:
                self.points[1] += 2
            else:
                self.points[1] += 3

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def neverAnswerRun(self):
        if self.counter <= 20:
            if self.counter in self.answer_weight[0]:
                self.points[0] += 1
            else:
                self.points[0] += 4
        else:
            if self.counter in self.answer_weight[0]:
                self.points[1] += 1
            else:
                self.points[1] += 4

        if self.counter < 40:
            self.questionChanger()
        else:
            self.resulter()

    def resulter(self):
        h_t_r.situational_anxiety_result.setText(str(self.points[0]) + '/80')
        h_t_r.personal_anxiety_result.setText(str(self.points[1]) + '/80')
        h_t_r.x = stringMaker(self.points)

        self.points = [0, 0]
        self.counter = 1

        self.cursor.execute(self.take_question_sql, (self.counter,))
        self.question_number.setText(str(self.counter) + '/40')
        self.question_text.setText(self.cursor.fetchone()[0])

        changer(h_t_r, h_t)


class HaninTestResult(QMainWindow, Ui_HaninTestResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PsyCorp')

        self.unsave_button.setStyleSheet("""
                                         #unsave_button {color: rgb(243, 225, 208);
                                         border: 0;
                                         padding: 0;
                                         text-align: left;}
                                         #unsave_button:hover {color: rgb(179, 166, 154);}
                                      """)
        self.tests_menu_button.setStyleSheet("""#tests_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #tests_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
        self.about_us_menu_button.setStyleSheet("""#about_us_menu_button{
                                         background-color: rgb(129, 123, 109);
                                         color: rgb(76, 68, 57);
                                         border: 0;
                                         padding: 0;
                                         }
                                         
                                         #about_us_menu_button:hover {
                                         background-color: rgb(147, 140, 125);     
                                         }""")
       


        self.pixmap_icon = QPixmap('C:\\Users\\varna\\Desktop\\Code\\PsyCorp\\Images\\icon_small.png')
        
        self.icon = QLabel(self)
        self.icon.move(0, 0)
        self.icon.resize(70, 70)
        self.icon.setPixmap(self.pixmap_icon)

        self.user_name = ''
        self.x = '0 0'

        self.tests_menu_button.clicked.connect(self.testsRun)
        self.about_us_menu_button.clicked.connect(self.aboutUsRun)
        self.unsave_button.clicked.connect(self.unsaveRun)

    def testsRun(self):
        changer(h_p, h_t_r)

    def aboutUsRun(self):
        changer(a_u_p, h_t_r)

    def unsaveRun(self):
        self.testsRun()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    h_p = HomePage()
    a_u_p = AboutUsPage()
    a_t = AyzenkTest()
    a_t_r = AyzenkTestResult()
    l_t = LsiTest()
    l_t_r = LsiTestResult()
    e_t = EqTest()
    e_t_r = EqTestResult()
    r_t = RathusTest()
    r_t_r = RathusTestResult()
    h_t = HaninTest()
    h_t_r = HaninTestResult()

    h_p.show()
    sys.exit(app.exec())
