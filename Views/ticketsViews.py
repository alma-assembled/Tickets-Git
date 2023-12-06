# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketsMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TicketWindow(object):
    def setupUi(self, TicketWindow):
        TicketWindow.setObjectName("TicketWindow")
        TicketWindow.resize(950, 688)
        self.centralwidget = QtWidgets.QWidget(TicketWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color: rgb(0, 0, 0);\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"#leftMenu{\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"#heder{\n"
"background-color: rgb(6, 91, 103);\n"
"}\n"
"\n"
"#multiWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#h1{\n"
"color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20PX;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"#title,#title_2,#title_3,#title_4{\n"
"font-size: 18px;\n"
"color: rgb(139, 132, 132);\n"
"}\n"
"\n"
"QLabel {\n"
"font: 12px \"Arial\";\n"
"color:rgb(87, 85, 85)\n"
"}\n"
"\n"
"QFontComboBox {\n"
"    fill: rgb(217, 217, 217);\n"
"    background-color: rgba(217, 217, 217, 1);\n"
"color:rgb(154, 150, 150);\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(6, 91, 103);\n"
"color: rgb(237, 237, 237);\n"
"border-radius: 30px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setGeometry(QtCore.QRect(0, 50, 161, 671))
        self.leftMenu.setStyleSheet("\n"
"background-color: rgb(217, 217, 217);\n"
"color:  rgb(139, 132, 132);\n"
"\n"
"\n"
"QPushButton{\n"
"margin-left: -100px;\n"
"\n"
"\n"
"}")
        self.leftMenu.setObjectName("leftMenu")
        self.lb_name = QtWidgets.QLabel(self.leftMenu)
        self.lb_name.setGeometry(QtCore.QRect(10, 60, 151, 41))
        self.lb_name.setObjectName("lb_name")
        self.lb_menu = QtWidgets.QLabel(self.leftMenu)
        self.lb_menu.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.lb_menu.setObjectName("lb_menu")
        self.btn_dashboard = QtWidgets.QPushButton(self.leftMenu)
        self.btn_dashboard.setGeometry(QtCore.QRect(0, 170, 161, 21))
        self.btn_dashboard.setStyleSheet("image: url(:/left/hogar.png);\n"
"pading: 8px;\n"
"margin-left: -100px;")
        self.btn_dashboard.setText("")
        self.btn_dashboard.setObjectName("btn_dashboard")
        self.btn_addTicket = QtWidgets.QPushButton(self.leftMenu)
        self.btn_addTicket.setGeometry(QtCore.QRect(0, 212, 161, 16))
        self.btn_addTicket.setStyleSheet("image: url(:/left/mas.png);\n"
"margin-left: -100px;")
        self.btn_addTicket.setText("")
        self.btn_addTicket.setObjectName("btn_addTicket")
        self.btn_ticket = QtWidgets.QPushButton(self.leftMenu)
        self.btn_ticket.setGeometry(QtCore.QRect(0, 250, 161, 21))
        self.btn_ticket.setStyleSheet("image: url(:/left/lib.png);\n"
"margin-left: -100px;")
        self.btn_ticket.setText("")
        self.btn_ticket.setObjectName("btn_ticket")
        self.btn_myTickets = QtWidgets.QPushButton(self.leftMenu)
        self.btn_myTickets.setGeometry(QtCore.QRect(0, 290, 161, 21))
        self.btn_myTickets.setStyleSheet("image: url(:/left/nota.png);\n"
"margin-left: -100px;")
        self.btn_myTickets.setText("")
        self.btn_myTickets.setObjectName("btn_myTickets")
        self.lb_dashboard = QtWidgets.QLabel(self.leftMenu)
        self.lb_dashboard.setGeometry(QtCore.QRect(60, 170, 81, 21))
        self.lb_dashboard.setObjectName("lb_dashboard")
        self.lb_addTicket = QtWidgets.QLabel(self.leftMenu)
        self.lb_addTicket.setGeometry(QtCore.QRect(60, 210, 101, 21))
        self.lb_addTicket.setObjectName("lb_addTicket")
        self.lb_ticket = QtWidgets.QLabel(self.leftMenu)
        self.lb_ticket.setGeometry(QtCore.QRect(60, 250, 61, 21))
        self.lb_ticket.setObjectName("lb_ticket")
        self.lb_myTickets = QtWidgets.QLabel(self.leftMenu)
        self.lb_myTickets.setGeometry(QtCore.QRect(60, 290, 81, 16))
        self.lb_myTickets.setObjectName("lb_myTickets")
        self.lb_icon = QtWidgets.QLabel(self.leftMenu)
        self.lb_icon.setGeometry(QtCore.QRect(0, 10, 71, 51))
        self.lb_icon.setStyleSheet("image: url(:/left/usuario.png);")
        self.lb_icon.setText("")
        self.lb_icon.setObjectName("lb_icon")
        self.radioButton = QtWidgets.QRadioButton(self.leftMenu)
        self.radioButton.setGeometry(QtCore.QRect(10, 100, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.leftMenu)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 120, 131, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.heder = QtWidgets.QWidget(self.centralwidget)
        self.heder.setGeometry(QtCore.QRect(0, 0, 951, 51))
        self.heder.setObjectName("heder")
        self.h1 = QtWidgets.QLabel(self.heder)
        self.h1.setGeometry(QtCore.QRect(9, 9, 81, 24))
        self.h1.setObjectName("h1")
        self.lb_icon_2 = QtWidgets.QLabel(self.heder)
        self.lb_icon_2.setGeometry(QtCore.QRect(890, 10, 51, 31))
        self.lb_icon_2.setStyleSheet("image: url(:/logo/Logo_Verical_Blanco.png);")
        self.lb_icon_2.setText("")
        self.lb_icon_2.setObjectName("lb_icon_2")
        self.multiWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.multiWidget.setGeometry(QtCore.QRect(160, 50, 791, 681))
        self.multiWidget.setStyleSheet("#title{\n"
"color: rgb(139, 132, 132);\n"
"font-family: Inter;\n"
"font-size: 18px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}\n"
"")
        self.multiWidget.setObjectName("multiWidget")
        self.dashboard = QtWidgets.QWidget()
        self.dashboard.setObjectName("dashboard")
        self.resume = QtWidgets.QWidget(self.dashboard)
        self.resume.setGeometry(QtCore.QRect(0, 0, 791, 141))
        self.resume.setStyleSheet("#w_registered, #w_canceled , #w_assigned,#w_finalized, #w_inProgress{\n"
"padding:8px;\n"
"}")
        self.resume.setObjectName("resume")
        self.title = QtWidgets.QLabel(self.resume)
        self.title.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.title.setObjectName("title")
        self.btn_crearTicket = QtWidgets.QPushButton(self.resume)
        self.btn_crearTicket.setGeometry(QtCore.QRect(600, 10, 141, 21))
        self.btn_crearTicket.setStyleSheet("background-color: rgb(6, 91, 103);\n"
"color: rgb(237, 237, 237)")
        self.btn_crearTicket.setObjectName("btn_crearTicket")
        self.line = QtWidgets.QFrame(self.resume)
        self.line.setGeometry(QtCore.QRect(0, 130, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.resume)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 791, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.assigned = QtWidgets.QWidget(self.layoutWidget)
        self.assigned.setObjectName("assigned")
        self.w_assigned = QtWidgets.QWidget(self.assigned)
        self.w_assigned.setGeometry(QtCore.QRect(0, 20, 61, 51))
        self.w_assigned.setStyleSheet("background: #3B96D8;\n"
"image: url(:/resume/apreton-de-manos.png);")
        self.w_assigned.setObjectName("w_assigned")
        self.layoutWidget1 = QtWidgets.QWidget(self.assigned)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 0, 91, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_4 = QtWidgets.QWidget(self.layoutWidget1)
        self.text_4.setObjectName("text_4")
        self.label_5 = QtWidgets.QLabel(self.text_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.text_4)
        self.text_5 = QtWidgets.QWidget(self.layoutWidget1)
        self.text_5.setObjectName("text_5")
        self.count_assigned = QtWidgets.QLabel(self.text_5)
        self.count_assigned.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.count_assigned.setObjectName("count_assigned")
        self.verticalLayout_4.addWidget(self.text_5)
        self.gridLayout_2.addWidget(self.assigned, 0, 1, 1, 1)
        self.inProgress = QtWidgets.QWidget(self.layoutWidget)
        self.inProgress.setObjectName("inProgress")
        self.w_inProgress = QtWidgets.QWidget(self.inProgress)
        self.w_inProgress.setGeometry(QtCore.QRect(0, 20, 61, 51))
        self.w_inProgress.setStyleSheet("background: #063456;\n"
"image: url(:/resume/almuerzo-cohete.png);")
        self.w_inProgress.setObjectName("w_inProgress")
        self.layoutWidget_4 = QtWidgets.QWidget(self.inProgress)
        self.layoutWidget_4.setGeometry(QtCore.QRect(60, 0, 91, 91))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.text_10 = QtWidgets.QWidget(self.layoutWidget_4)
        self.text_10.setObjectName("text_10")
        self.label_17 = QtWidgets.QLabel(self.text_10)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.text_10)
        self.text_11 = QtWidgets.QWidget(self.layoutWidget_4)
        self.text_11.setObjectName("text_11")
        self.count_inProgress = QtWidgets.QLabel(self.text_11)
        self.count_inProgress.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.count_inProgress.setObjectName("count_inProgress")
        self.verticalLayout_7.addWidget(self.text_11)
        self.gridLayout_2.addWidget(self.inProgress, 0, 2, 1, 1)
        self.finalized = QtWidgets.QWidget(self.layoutWidget)
        self.finalized.setObjectName("finalized")
        self.w_finalized = QtWidgets.QWidget(self.finalized)
        self.w_finalized.setGeometry(QtCore.QRect(0, 20, 61, 51))
        self.w_finalized.setStyleSheet("background: #2B8544;\n"
"image: url(:/resume/cheque.png);")
        self.w_finalized.setObjectName("w_finalized")
        self.layoutWidget_3 = QtWidgets.QWidget(self.finalized)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 0, 91, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text_8 = QtWidgets.QWidget(self.layoutWidget_3)
        self.text_8.setObjectName("text_8")
        self.label_15 = QtWidgets.QLabel(self.text_8)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.text_8)
        self.text_9 = QtWidgets.QWidget(self.layoutWidget_3)
        self.text_9.setObjectName("text_9")
        self.count_finalized = QtWidgets.QLabel(self.text_9)
        self.count_finalized.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.count_finalized.setObjectName("count_finalized")
        self.verticalLayout_6.addWidget(self.text_9)
        self.gridLayout_2.addWidget(self.finalized, 0, 3, 1, 1)
        self.canceled = QtWidgets.QWidget(self.layoutWidget)
        self.canceled.setObjectName("canceled")
        self.w_canceled = QtWidgets.QWidget(self.canceled)
        self.w_canceled.setGeometry(QtCore.QRect(0, 20, 61, 51))
        self.w_canceled.setStyleSheet("background: #CE2323;\n"
"image: url(:/resume/eliminar.png);")
        self.w_canceled.setObjectName("w_canceled")
        self.layoutWidget_2 = QtWidgets.QWidget(self.canceled)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 0, 91, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.text_6 = QtWidgets.QWidget(self.layoutWidget_2)
        self.text_6.setObjectName("text_6")
        self.label_13 = QtWidgets.QLabel(self.text_6)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.text_6)
        self.text_7 = QtWidgets.QWidget(self.layoutWidget_2)
        self.text_7.setObjectName("text_7")
        self.count_canceled = QtWidgets.QLabel(self.text_7)
        self.count_canceled.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.count_canceled.setObjectName("count_canceled")
        self.verticalLayout_5.addWidget(self.text_7)
        self.gridLayout_2.addWidget(self.canceled, 0, 4, 1, 1)
        self.registered = QtWidgets.QWidget(self.layoutWidget)
        self.registered.setObjectName("registered")
        self.w_registered = QtWidgets.QWidget(self.registered)
        self.w_registered.setGeometry(QtCore.QRect(0, 20, 61, 51))
        self.w_registered.setStyleSheet("background: #D8863B;\n"
"image: url(:/resume/estrella.png);")
        self.w_registered.setObjectName("w_registered")
        self.layoutWidget2 = QtWidgets.QWidget(self.registered)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 0, 91, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QtWidgets.QWidget(self.layoutWidget2)
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(self.text)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.text)
        self.text_1 = QtWidgets.QWidget(self.layoutWidget2)
        self.text_1.setObjectName("text_1")
        self.count_registered = QtWidgets.QLabel(self.text_1)
        self.count_registered.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.count_registered.setObjectName("count_registered")
        self.verticalLayout_2.addWidget(self.text_1)
        self.gridLayout_2.addWidget(self.registered, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.dashboard)
        self.widget.setGeometry(QtCore.QRect(0, 260, 791, 451))
        self.widget.setObjectName("widget")
        self.table_tickets_dashboar = QtWidgets.QTableView(self.widget)
        self.table_tickets_dashboar.setGeometry(QtCore.QRect(20, 20, 751, 341))
        self.table_tickets_dashboar.setObjectName("table_tickets_dashboar")
        self.filters = QtWidgets.QWidget(self.dashboard)
        self.filters.setGeometry(QtCore.QRect(0, 150, 781, 111))
        self.filters.setObjectName("filters")
        self.cb_status = QtWidgets.QComboBox(self.filters)
        self.cb_status.setGeometry(QtCore.QRect(190, 10, 141, 31))
        self.cb_status.setObjectName("cb_status")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.date_edit = QtWidgets.QDateEdit(self.filters)
        self.date_edit.setGeometry(QtCore.QRect(500, 10, 121, 31))
        self.date_edit.setObjectName("date_edit")
        self.btn_allTickets = QtWidgets.QPushButton(self.filters)
        self.btn_allTickets.setGeometry(QtCore.QRect(580, 60, 181, 31))
        self.btn_allTickets.setObjectName("btn_allTickets")
        self.btn_seach = QtWidgets.QPushButton(self.filters)
        self.btn_seach.setGeometry(QtCore.QRect(220, 60, 141, 31))
        self.btn_seach.setObjectName("btn_seach")
        self.text_search = QtWidgets.QLineEdit(self.filters)
        self.text_search.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.text_search.setStyleSheet("width: 100%;\n"
"  padding: 6px;\n"
"  border: none;\n"
"  outline: none;\n"
"  background: transparent;\n"
"border-bottom: 2px solid rgb(118, 118, 118) ;\n"
"color:  rgb(139, 132, 132);")
        self.text_search.setObjectName("text_search")
        self.lb_icon_ = QtWidgets.QLabel(self.filters)
        self.lb_icon_.setGeometry(QtCore.QRect(146, 13, 21, 20))
        self.lb_icon_.setStyleSheet("image: url(:/general/busqueda.png);")
        self.lb_icon_.setText("")
        self.lb_icon_.setObjectName("lb_icon_")
        self.cb_employee = QtWidgets.QComboBox(self.filters)
        self.cb_employee.setGeometry(QtCore.QRect(350, 10, 141, 31))
        self.cb_employee.setObjectName("cb_employee")
        self.cb_category = QtWidgets.QComboBox(self.filters)
        self.cb_category.setGeometry(QtCore.QRect(630, 10, 141, 31))
        self.cb_category.setObjectName("cb_category")
        self.cb_ = QtWidgets.QComboBox(self.filters)
        self.cb_.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.cb_.setObjectName("cb_")
        self.multiWidget.addWidget(self.dashboard)
        self.myTickets = QtWidgets.QWidget()
        self.myTickets.setObjectName("myTickets")
        self.multiWidget.addWidget(self.myTickets)
        self.tickets = QtWidgets.QWidget()
        self.tickets.setObjectName("tickets")
        self.widget_8 = QtWidgets.QWidget(self.tickets)
        self.widget_8.setGeometry(QtCore.QRect(0, 190, 791, 451))
        self.widget_8.setObjectName("widget_8")
        self.tableView_3 = QtWidgets.QTableView(self.widget_8)
        self.tableView_3.setGeometry(QtCore.QRect(20, 20, 751, 411))
        self.tableView_3.setObjectName("tableView_3")
        self.resume_4 = QtWidgets.QWidget(self.tickets)
        self.resume_4.setGeometry(QtCore.QRect(0, 0, 791, 81))
        self.resume_4.setObjectName("resume_4")
        self.title_4 = QtWidgets.QLabel(self.resume_4)
        self.title_4.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.title_4.setObjectName("title_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.resume_4)
        self.pushButton_12.setGeometry(QtCore.QRect(600, 10, 141, 21))
        self.pushButton_12.setStyleSheet("background-color: rgb(6, 91, 103);\n"
"color: rgb(237, 237, 237)")
        self.pushButton_12.setObjectName("pushButton_12")
        self.line_4 = QtWidgets.QFrame(self.resume_4)
        self.line_4.setGeometry(QtCore.QRect(0, 60, 791, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.filters_3 = QtWidgets.QWidget(self.tickets)
        self.filters_3.setGeometry(QtCore.QRect(0, 80, 781, 111))
        self.filters_3.setObjectName("filters_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.filters_3)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 10, 141, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.fontComboBox_14 = QtWidgets.QFontComboBox(self.filters_3)
        self.fontComboBox_14.setGeometry(QtCore.QRect(340, 10, 141, 31))
        self.fontComboBox_14.setObjectName("fontComboBox_14")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.filters_3)
        self.dateEdit_3.setGeometry(QtCore.QRect(500, 10, 121, 31))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.fontComboBox_15 = QtWidgets.QFontComboBox(self.filters_3)
        self.fontComboBox_15.setGeometry(QtCore.QRect(630, 10, 141, 31))
        self.fontComboBox_15.setObjectName("fontComboBox_15")
        self.fontComboBox_16 = QtWidgets.QFontComboBox(self.filters_3)
        self.fontComboBox_16.setGeometry(QtCore.QRect(10, 60, 161, 31))
        self.fontComboBox_16.setObjectName("fontComboBox_16")
        self.pushButton_13 = QtWidgets.QPushButton(self.filters_3)
        self.pushButton_13.setGeometry(QtCore.QRect(190, 60, 191, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.filters_3)
        self.pushButton_14.setGeometry(QtCore.QRect(440, 60, 141, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.filters_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.multiWidget.addWidget(self.tickets)
        self.addTicket = QtWidgets.QWidget()
        self.addTicket.setStyleSheet("")
        self.addTicket.setObjectName("addTicket")
        self.resume_3 = QtWidgets.QWidget(self.addTicket)
        self.resume_3.setGeometry(QtCore.QRect(10, 10, 791, 61))
        self.resume_3.setObjectName("resume_3")
        self.title_3 = QtWidgets.QLabel(self.resume_3)
        self.title_3.setGeometry(QtCore.QRect(0, 0, 251, 31))
        self.title_3.setObjectName("title_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.resume_3)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 10, 141, 21))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_3 = QtWidgets.QFrame(self.resume_3)
        self.line_3.setGeometry(QtCore.QRect(0, 50, 791, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.add = QtWidgets.QWidget(self.addTicket)
        self.add.setGeometry(QtCore.QRect(10, 70, 781, 571))
        self.add.setStyleSheet("")
        self.add.setObjectName("add")
        self.fontComboBox_8 = QtWidgets.QFontComboBox(self.add)
        self.fontComboBox_8.setGeometry(QtCore.QRect(130, 20, 171, 31))
        self.fontComboBox_8.setObjectName("fontComboBox_8")
        self.fontComboBox_9 = QtWidgets.QFontComboBox(self.add)
        self.fontComboBox_9.setGeometry(QtCore.QRect(140, 360, 571, 31))
        self.fontComboBox_9.setObjectName("fontComboBox_9")
        self.fontComboBox_10 = QtWidgets.QFontComboBox(self.add)
        self.fontComboBox_10.setGeometry(QtCore.QRect(440, 20, 191, 31))
        self.fontComboBox_10.setObjectName("fontComboBox_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.add)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 520, 141, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.dte_fechoy = QtWidgets.QDateEdit(self.add)
        self.dte_fechoy.setEnabled(False)
        self.dte_fechoy.setGeometry(QtCore.QRect(660, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dte_fechoy.setFont(font)
        self.dte_fechoy.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dte_fechoy.setStyleSheet(" color: rgb(6, 91, 103);\n"
"   background: linear-gradient(360deg,#03e9f4);")
        self.dte_fechoy.setFrame(False)
        self.dte_fechoy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dte_fechoy.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dte_fechoy.setCalendarPopup(False)
        self.dte_fechoy.setDate(QtCore.QDate(2023, 10, 6))
        self.dte_fechoy.setObjectName("dte_fechoy")
        self.lbl_nombre = QtWidgets.QLabel(self.add)
        self.lbl_nombre.setGeometry(QtCore.QRect(10, 20, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre.setToolTip("")
        self.lbl_nombre.setToolTipDuration(1)
        self.lbl_nombre.setStyleSheet("")
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_nombre_2 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_2.setGeometry(QtCore.QRect(340, 20, 81, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_2.setFont(font)
        self.lbl_nombre_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_2.setToolTip("")
        self.lbl_nombre_2.setToolTipDuration(1)
        self.lbl_nombre_2.setStyleSheet("")
        self.lbl_nombre_2.setObjectName("lbl_nombre_2")
        self.lbl_nombre_3 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_3.setGeometry(QtCore.QRect(0, 140, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_3.setFont(font)
        self.lbl_nombre_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_3.setToolTip("")
        self.lbl_nombre_3.setToolTipDuration(1)
        self.lbl_nombre_3.setStyleSheet("")
        self.lbl_nombre_3.setObjectName("lbl_nombre_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.add)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 180, 751, 61))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lbl_nombre_7 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_7.setGeometry(QtCore.QRect(0, 250, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_7.setFont(font)
        self.lbl_nombre_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_7.setToolTip("")
        self.lbl_nombre_7.setToolTipDuration(1)
        self.lbl_nombre_7.setStyleSheet("")
        self.lbl_nombre_7.setObjectName("lbl_nombre_7")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.add)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(0, 280, 751, 61))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.lbl_nombre_8 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_8.setGeometry(QtCore.QRect(10, 370, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_8.setFont(font)
        self.lbl_nombre_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_8.setToolTip("")
        self.lbl_nombre_8.setToolTipDuration(1)
        self.lbl_nombre_8.setStyleSheet("")
        self.lbl_nombre_8.setObjectName("lbl_nombre_8")
        self.listView_5 = QtWidgets.QListView(self.add)
        self.listView_5.setGeometry(QtCore.QRect(0, 440, 741, 71))
        self.listView_5.setObjectName("listView_5")
        self.lbl_nombre_17 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_17.setGeometry(QtCore.QRect(10, 410, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_17.setFont(font)
        self.lbl_nombre_17.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_17.setToolTip("")
        self.lbl_nombre_17.setToolTipDuration(1)
        self.lbl_nombre_17.setStyleSheet("")
        self.lbl_nombre_17.setObjectName("lbl_nombre_17")
        self.fontComboBox_11 = QtWidgets.QFontComboBox(self.add)
        self.fontComboBox_11.setGeometry(QtCore.QRect(110, 80, 191, 31))
        self.fontComboBox_11.setObjectName("fontComboBox_11")
        self.lbl_nombre_4 = QtWidgets.QLabel(self.add)
        self.lbl_nombre_4.setGeometry(QtCore.QRect(10, 80, 81, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_4.setFont(font)
        self.lbl_nombre_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_4.setToolTip("")
        self.lbl_nombre_4.setToolTipDuration(1)
        self.lbl_nombre_4.setStyleSheet("")
        self.lbl_nombre_4.setObjectName("lbl_nombre_4")
        self.label_2 = QtWidgets.QLabel(self.add)
        self.label_2.setGeometry(QtCore.QRect(360, 90, 121, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.add)
        self.dateEdit.setGeometry(QtCore.QRect(510, 90, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.multiWidget.addWidget(self.addTicket)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.add_3 = QtWidgets.QWidget(self.page)
        self.add_3.setGeometry(QtCore.QRect(0, 60, 781, 571))
        self.add_3.setStyleSheet("")
        self.add_3.setObjectName("add_3")
        self.fontComboBox_26 = QtWidgets.QFontComboBox(self.add_3)
        self.fontComboBox_26.setGeometry(QtCore.QRect(150, 70, 171, 31))
        self.fontComboBox_26.setObjectName("fontComboBox_26")
        self.fontComboBox_27 = QtWidgets.QFontComboBox(self.add_3)
        self.fontComboBox_27.setGeometry(QtCore.QRect(100, 150, 301, 31))
        self.fontComboBox_27.setObjectName("fontComboBox_27")
        self.pushButton_25 = QtWidgets.QPushButton(self.add_3)
        self.pushButton_25.setGeometry(QtCore.QRect(290, 200, 141, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.add_3)
        self.pushButton_26.setGeometry(QtCore.QRect(620, 370, 141, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.dte_fechoy_3 = QtWidgets.QDateEdit(self.add_3)
        self.dte_fechoy_3.setEnabled(False)
        self.dte_fechoy_3.setGeometry(QtCore.QRect(670, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dte_fechoy_3.setFont(font)
        self.dte_fechoy_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dte_fechoy_3.setStyleSheet(" color: rgb(6, 91, 103);\n"
"   background: linear-gradient(360deg,#03e9f4);")
        self.dte_fechoy_3.setFrame(False)
        self.dte_fechoy_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dte_fechoy_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dte_fechoy_3.setCalendarPopup(False)
        self.dte_fechoy_3.setDate(QtCore.QDate(2023, 10, 6))
        self.dte_fechoy_3.setObjectName("dte_fechoy_3")
        self.lbl_nombre_11 = QtWidgets.QLabel(self.add_3)
        self.lbl_nombre_11.setGeometry(QtCore.QRect(30, 80, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_11.setFont(font)
        self.lbl_nombre_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_11.setToolTip("")
        self.lbl_nombre_11.setToolTipDuration(1)
        self.lbl_nombre_11.setStyleSheet("")
        self.lbl_nombre_11.setObjectName("lbl_nombre_11")
        self.lbl_nombre_15 = QtWidgets.QLabel(self.add_3)
        self.lbl_nombre_15.setGeometry(QtCore.QRect(30, 160, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_15.setFont(font)
        self.lbl_nombre_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_15.setToolTip("")
        self.lbl_nombre_15.setToolTipDuration(1)
        self.lbl_nombre_15.setStyleSheet("")
        self.lbl_nombre_15.setObjectName("lbl_nombre_15")
        self.listView_3 = QtWidgets.QListView(self.add_3)
        self.listView_3.setGeometry(QtCore.QRect(30, 290, 731, 71))
        self.listView_3.setObjectName("listView_3")
        self.title_10 = QtWidgets.QLabel(self.add_3)
        self.title_10.setGeometry(QtCore.QRect(30, 20, 61, 31))
        self.title_10.setObjectName("title_10")
        self.listView_4 = QtWidgets.QListView(self.add_3)
        self.listView_4.setGeometry(QtCore.QRect(90, 20, 561, 31))
        self.listView_4.setObjectName("listView_4")
        self.lbl_nombre_16 = QtWidgets.QLabel(self.add_3)
        self.lbl_nombre_16.setGeometry(QtCore.QRect(40, 260, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_nombre_16.setFont(font)
        self.lbl_nombre_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_nombre_16.setToolTip("")
        self.lbl_nombre_16.setToolTipDuration(1)
        self.lbl_nombre_16.setStyleSheet("")
        self.lbl_nombre_16.setObjectName("lbl_nombre_16")
        self.resume_9 = QtWidgets.QWidget(self.page)
        self.resume_9.setGeometry(QtCore.QRect(0, 0, 791, 61))
        self.resume_9.setObjectName("resume_9")
        self.title_9 = QtWidgets.QLabel(self.resume_9)
        self.title_9.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.title_9.setObjectName("title_9")
        self.pushButton_27 = QtWidgets.QPushButton(self.resume_9)
        self.pushButton_27.setGeometry(QtCore.QRect(600, 10, 141, 21))
        self.pushButton_27.setStyleSheet("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.line_9 = QtWidgets.QFrame(self.resume_9)
        self.line_9.setGeometry(QtCore.QRect(0, 50, 791, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.multiWidget.addWidget(self.page)
        TicketWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TicketWindow)
        self.multiWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TicketWindow)

    def retranslateUi(self, TicketWindow):
        _translate = QtCore.QCoreApplication.translate
        TicketWindow.setWindowTitle(_translate("TicketWindow", "MainWindow"))
        self.lb_name.setText(_translate("TicketWindow", "Nombre nombre"))
        self.lb_menu.setText(_translate("TicketWindow", "MENU"))
        self.lb_dashboard.setText(_translate("TicketWindow", "DASHBOARD"))
        self.lb_addTicket.setText(_translate("TicketWindow", "CREAR TICKETS"))
        self.lb_ticket.setText(_translate("TicketWindow", "TICKETS"))
        self.lb_myTickets.setText(_translate("TicketWindow", "MIS TICKETS"))
        self.radioButton.setText(_translate("TicketWindow", "Solicitante"))
        self.radioButton_2.setText(_translate("TicketWindow", "Responsable"))
        self.h1.setText(_translate("TicketWindow", "TICKETS"))
        self.title.setText(_translate("TicketWindow", "DASHBOARD"))
        self.btn_crearTicket.setText(_translate("TicketWindow", "Crear Ticcket"))
        self.label_5.setText(_translate("TicketWindow", "Asignados"))
        self.count_assigned.setText(_translate("TicketWindow", "0"))
        self.label_17.setText(_translate("TicketWindow", "En Proceso"))
        self.count_inProgress.setText(_translate("TicketWindow", "0"))
        self.label_15.setText(_translate("TicketWindow", "Finalizados"))
        self.count_finalized.setText(_translate("TicketWindow", "0"))
        self.label_13.setText(_translate("TicketWindow", "Cancelados"))
        self.count_canceled.setText(_translate("TicketWindow", "0"))
        self.label.setText(_translate("TicketWindow", "Registrados"))
        self.count_registered.setText(_translate("TicketWindow", "0"))
        self.cb_status.setItemText(0, _translate("TicketWindow", "-------------"))
        self.cb_status.setItemText(1, _translate("TicketWindow", "ASIGANDO"))
        self.cb_status.setItemText(2, _translate("TicketWindow", "EN PROCESO"))
        self.cb_status.setItemText(3, _translate("TicketWindow", "FINALIZADO"))
        self.cb_status.setItemText(4, _translate("TicketWindow", "CANCELADO"))
        self.btn_allTickets.setText(_translate("TicketWindow", "TODOS LOS TICKETS"))
        self.btn_seach.setText(_translate("TicketWindow", "Buscar"))
        self.text_search.setText(_translate("TicketWindow", "ASUNTO"))
        self.title_4.setText(_translate("TicketWindow", "TICKETS"))
        self.pushButton_12.setText(_translate("TicketWindow", "Crear Ticcket"))
        self.pushButton_13.setText(_translate("TicketWindow", "TODOS LOS TICKETS"))
        self.pushButton_14.setText(_translate("TicketWindow", "PushButton"))
        self.title_3.setText(_translate("TicketWindow", "AGREGAR TICKET"))
        self.pushButton_7.setText(_translate("TicketWindow", "Crear Ticcket"))
        self.pushButton_8.setText(_translate("TicketWindow", "GUARDAR"))
        self.lbl_nombre.setText(_translate("TicketWindow", "DEPARTAMENTO"))
        self.lbl_nombre_2.setText(_translate("TicketWindow", "CATEGORIA"))
        self.lbl_nombre_3.setText(_translate("TicketWindow", "ASUNTO*"))
        self.lbl_nombre_7.setText(_translate("TicketWindow", "DESCRIPCION*"))
        self.lbl_nombre_8.setText(_translate("TicketWindow", "ASIGNAR*"))
        self.lbl_nombre_17.setText(_translate("TicketWindow", "COMENTARIO"))
        self.lbl_nombre_4.setText(_translate("TicketWindow", "PRIORIDAD"))
        self.label_2.setText(_translate("TicketWindow", "FECHA SOLUCION"))
        self.pushButton_25.setText(_translate("TicketWindow", "GUARDAR"))
        self.pushButton_26.setText(_translate("TicketWindow", "Enviar"))
        self.lbl_nombre_11.setText(_translate("TicketWindow", "DEPARTAMENTO*"))
        self.lbl_nombre_15.setText(_translate("TicketWindow", "ASIGNAR*"))
        self.title_10.setText(_translate("TicketWindow", "ASUNTO"))
        self.lbl_nombre_16.setText(_translate("TicketWindow", "COMENTARIO"))
        self.title_9.setText(_translate("TicketWindow", "ASIGNAR TICKET"))
        self.pushButton_27.setText(_translate("TicketWindow", "Editar Ticcket"))
import  Resources.iconos.iconos
