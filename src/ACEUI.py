# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACE.ui'
#
# Created: Thu Jun  5 13:49:51 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1021, 721))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.MainPage = QtGui.QWidget()
        self.MainPage.setObjectName(_fromUtf8("MainPage"))
        self.verticalLayoutWidget = QtGui.QWidget(self.MainPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 110, 301, 391))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_mm = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_mm.setMargin(0)
        self.verticalLayout_mm.setObjectName(_fromUtf8("verticalLayout_mm"))
        self.pushButton_mm_trainer = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_mm_trainer.setObjectName(_fromUtf8("pushButton_mm_trainer"))
        self.verticalLayout_mm.addWidget(self.pushButton_mm_trainer)
        self.pushButton_mm_editor = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_mm_editor.setObjectName(_fromUtf8("pushButton_mm_editor"))
        self.verticalLayout_mm.addWidget(self.pushButton_mm_editor)
        self.pushButton_mm_statistics = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_mm_statistics.setObjectName(_fromUtf8("pushButton_mm_statistics"))
        self.verticalLayout_mm.addWidget(self.pushButton_mm_statistics)
        self.pushButton_mm_exit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_mm_exit.setObjectName(_fromUtf8("pushButton_mm_exit"))
        self.verticalLayout_mm.addWidget(self.pushButton_mm_exit)
        self.stackedWidget.addWidget(self.MainPage)
        self.Statistics = QtGui.QWidget()
        self.Statistics.setObjectName(_fromUtf8("Statistics"))
        self.layoutWidget_17 = QtGui.QWidget(self.Statistics)
        self.layoutWidget_17.setGeometry(QtCore.QRect(20, 20, 991, 691))
        self.layoutWidget_17.setObjectName(_fromUtf8("layoutWidget_17"))
        self.horizontalLayout_s = QtGui.QHBoxLayout(self.layoutWidget_17)
        self.horizontalLayout_s.setMargin(0)
        self.horizontalLayout_s.setObjectName(_fromUtf8("horizontalLayout_s"))
        self.statFrame = QtGui.QFrame(self.layoutWidget_17)
        self.statFrame.setMinimumSize(QtCore.QSize(600, 0))
        self.statFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.statFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.statFrame.setObjectName(_fromUtf8("statFrame"))
        self.label = QtGui.QLabel(self.statFrame)
        self.label.setGeometry(QtCore.QRect(220, 260, 191, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget_s = QtGui.QTableWidget(self.statFrame)
        self.tableWidget_s.setGeometry(QtCore.QRect(0, 0, 601, 691))
        self.tableWidget_s.setObjectName(_fromUtf8("tableWidget_s"))
        self.tableWidget_s.setColumnCount(0)
        self.tableWidget_s.setRowCount(0)
        self.horizontalLayout_s.addWidget(self.statFrame)
        self.scrollArea_s = QtGui.QScrollArea(self.layoutWidget_17)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_s.sizePolicy().hasHeightForWidth())
        self.scrollArea_s.setSizePolicy(sizePolicy)
        self.scrollArea_s.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_s.setWidgetResizable(True)
        self.scrollArea_s.setObjectName(_fromUtf8("scrollArea_s"))
        self.scrollAreaWidgetContents_22 = QtGui.QWidget()
        self.scrollAreaWidgetContents_22.setGeometry(QtCore.QRect(0, 0, 381, 687))
        self.scrollAreaWidgetContents_22.setObjectName(_fromUtf8("scrollAreaWidgetContents_22"))
        self.pushButton_s_mm = QtGui.QPushButton(self.scrollAreaWidgetContents_22)
        self.pushButton_s_mm.setGeometry(QtCore.QRect(270, 650, 98, 27))
        self.pushButton_s_mm.setObjectName(_fromUtf8("pushButton_s_mm"))
        self.label_51 = QtGui.QLabel(self.scrollAreaWidgetContents_22)
        self.label_51.setGeometry(QtCore.QRect(70, 260, 261, 17))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.scrollArea_s.setWidget(self.scrollAreaWidgetContents_22)
        self.horizontalLayout_s.addWidget(self.scrollArea_s)
        self.stackedWidget.addWidget(self.Statistics)
        self.Editor = QtGui.QWidget()
        self.Editor.setObjectName(_fromUtf8("Editor"))
        self.layoutWidget = QtGui.QWidget(self.Editor)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 991, 691))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_e = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_e.setMargin(0)
        self.horizontalLayout_e.setObjectName(_fromUtf8("horizontalLayout_e"))
        self.scrollArea_e_tool_settings = QtGui.QScrollArea(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_e_tool_settings.sizePolicy().hasHeightForWidth())
        self.scrollArea_e_tool_settings.setSizePolicy(sizePolicy)
        self.scrollArea_e_tool_settings.setMinimumSize(QtCore.QSize(100, 0))
        self.scrollArea_e_tool_settings.setWidgetResizable(True)
        self.scrollArea_e_tool_settings.setObjectName(_fromUtf8("scrollArea_e_tool_settings"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 687))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 61, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.scrollArea_e_tool_settings.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_e.addWidget(self.scrollArea_e_tool_settings)
        self.algaeFrame_e = QtGui.QFrame(self.layoutWidget)
        self.algaeFrame_e.setMinimumSize(QtCore.QSize(700, 0))
        self.algaeFrame_e.setFrameShape(QtGui.QFrame.StyledPanel)
        self.algaeFrame_e.setFrameShadow(QtGui.QFrame.Raised)
        self.algaeFrame_e.setObjectName(_fromUtf8("algaeFrame_e"))
        self.label_e_algaetext = QtGui.QLabel(self.algaeFrame_e)
        self.label_e_algaetext.setGeometry(QtCore.QRect(200, 220, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_e_algaetext.setFont(font)
        self.label_e_algaetext.setObjectName(_fromUtf8("label_e_algaetext"))
        self.horizontalLayout_e.addWidget(self.algaeFrame_e)
        self.scrollArea_e_tools = QtGui.QScrollArea(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_e_tools.sizePolicy().hasHeightForWidth())
        self.scrollArea_e_tools.setSizePolicy(sizePolicy)
        self.scrollArea_e_tools.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_e_tools.setWidgetResizable(True)
        self.scrollArea_e_tools.setObjectName(_fromUtf8("scrollArea_e_tools"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 175, 687))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_e_mm = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_e_mm.setGeometry(QtCore.QRect(70, 650, 98, 27))
        self.pushButton_e_mm.setObjectName(_fromUtf8("pushButton_e_mm"))
        self.scrollArea_e_tools.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_e.addWidget(self.scrollArea_e_tools)
        self.stackedWidget.addWidget(self.Editor)
        self.Trainer = QtGui.QWidget()
        self.Trainer.setObjectName(_fromUtf8("Trainer"))
        self.layoutWidget_2 = QtGui.QWidget(self.Trainer)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 991, 691))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_t = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_t.setMargin(0)
        self.horizontalLayout_t.setObjectName(_fromUtf8("horizontalLayout_t"))
        self.algaeFrame_t = QtGui.QFrame(self.layoutWidget_2)
        self.algaeFrame_t.setMinimumSize(QtCore.QSize(700, 0))
        self.algaeFrame_t.setFrameShape(QtGui.QFrame.StyledPanel)
        self.algaeFrame_t.setFrameShadow(QtGui.QFrame.Raised)
        self.algaeFrame_t.setObjectName(_fromUtf8("algaeFrame_t"))
        self.label_10 = QtGui.QLabel(self.algaeFrame_t)
        self.label_10.setGeometry(QtCore.QRect(220, 220, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_t_zoom_minus = QtGui.QPushButton(self.algaeFrame_t)
        self.pushButton_t_zoom_minus.setGeometry(QtCore.QRect(640, 560, 16, 16))
        self.pushButton_t_zoom_minus.setObjectName(_fromUtf8("pushButton_t_zoom_minus"))
        self.pushButton_t_zoom_plus = QtGui.QPushButton(self.algaeFrame_t)
        self.pushButton_t_zoom_plus.setGeometry(QtCore.QRect(660, 560, 16, 16))
        self.pushButton_t_zoom_plus.setObjectName(_fromUtf8("pushButton_t_zoom_plus"))
        self.label_t_zoom = QtGui.QLabel(self.algaeFrame_t)
        self.label_t_zoom.setGeometry(QtCore.QRect(595, 553, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_t_zoom.setFont(font)
        self.label_t_zoom.setObjectName(_fromUtf8("label_t_zoom"))
        self.label_t_focus = QtGui.QLabel(self.algaeFrame_t)
        self.label_t_focus.setGeometry(QtCore.QRect(495, 553, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_t_focus.setFont(font)
        self.label_t_focus.setObjectName(_fromUtf8("label_t_focus"))
        self.pushButton_t_focus_minus = QtGui.QPushButton(self.algaeFrame_t)
        self.pushButton_t_focus_minus.setGeometry(QtCore.QRect(540, 560, 16, 16))
        self.pushButton_t_focus_minus.setObjectName(_fromUtf8("pushButton_t_focus_minus"))
        self.pushButton_t_focus_plus = QtGui.QPushButton(self.algaeFrame_t)
        self.pushButton_t_focus_plus.setGeometry(QtCore.QRect(560, 560, 16, 16))
        self.pushButton_t_focus_plus.setObjectName(_fromUtf8("pushButton_t_focus_plus"))
        self.label_t_status = QtGui.QLabel(self.algaeFrame_t)
        self.label_t_status.setGeometry(QtCore.QRect(0, 560, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_t_status.setFont(font)
        self.label_t_status.setObjectName(_fromUtf8("label_t_status"))
        self.line_t_1 = QtGui.QFrame(self.algaeFrame_t)
        self.line_t_1.setGeometry(QtCore.QRect(230, 530, 3, 61))
        self.line_t_1.setFrameShape(QtGui.QFrame.VLine)
        self.line_t_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_t_1.setObjectName(_fromUtf8("line_t_1"))
        self.line_t_2 = QtGui.QFrame(self.algaeFrame_t)
        self.line_t_2.setGeometry(QtCore.QRect(580, 530, 3, 61))
        self.line_t_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_t_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_t_2.setObjectName(_fromUtf8("line_t_2"))
        self.horizontalLayout_t.addWidget(self.algaeFrame_t)
        self.scrollArea_t = QtGui.QScrollArea(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_t.sizePolicy().hasHeightForWidth())
        self.scrollArea_t.setSizePolicy(sizePolicy)
        self.scrollArea_t.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_t.setWidgetResizable(True)
        self.scrollArea_t.setObjectName(_fromUtf8("scrollArea_t"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 281, 687))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.textEdit_t_guess = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_t_guess.setGeometry(QtCore.QRect(10, 60, 171, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_t_guess.sizePolicy().hasHeightForWidth())
        self.textEdit_t_guess.setSizePolicy(sizePolicy)
        self.textEdit_t_guess.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_t_guess.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_t_guess.setObjectName(_fromUtf8("textEdit_t_guess"))
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_t_submit = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_t_submit.setGeometry(QtCore.QRect(190, 60, 71, 21))
        self.pushButton_t_submit.setObjectName(_fromUtf8("pushButton_t_submit"))
        self.textEdit_t_output = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_t_output.setGeometry(QtCore.QRect(10, 90, 261, 551))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_t_output.sizePolicy().hasHeightForWidth())
        self.textEdit_t_output.setSizePolicy(sizePolicy)
        self.textEdit_t_output.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_t_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_t_output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_t_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_t_output.setObjectName(_fromUtf8("textEdit_t_output"))
        self.pushButton_t_mm = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_t_mm.setGeometry(QtCore.QRect(170, 650, 98, 27))
        self.pushButton_t_mm.setObjectName(_fromUtf8("pushButton_t_mm"))
        self.scrollArea_t.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_t.addWidget(self.scrollArea_t)
        self.stackedWidget.addWidget(self.Trainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionMain_Menu = QtGui.QAction(MainWindow)
        self.actionMain_Menu.setObjectName(_fromUtf8("actionMain_Menu"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionZoom_in = QtGui.QAction(MainWindow)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionLighting = QtGui.QAction(MainWindow)
        self.actionLighting.setObjectName(_fromUtf8("actionLighting"))
        self.actionFocus = QtGui.QAction(MainWindow)
        self.actionFocus.setObjectName(_fromUtf8("actionFocus"))
        self.actionFocus_2 = QtGui.QAction(MainWindow)
        self.actionFocus_2.setObjectName(_fromUtf8("actionFocus_2"))
        self.actionDraw_Shape = QtGui.QAction(MainWindow)
        self.actionDraw_Shape.setObjectName(_fromUtf8("actionDraw_Shape"))
        self.actionAdjust_Density = QtGui.QAction(MainWindow)
        self.actionAdjust_Density.setObjectName(_fromUtf8("actionAdjust_Density"))
        self.actionChange_Algae_Type = QtGui.QAction(MainWindow)
        self.actionChange_Algae_Type.setObjectName(_fromUtf8("actionChange_Algae_Type"))
        self.actionInstructions = QtGui.QAction(MainWindow)
        self.actionInstructions.setObjectName(_fromUtf8("actionInstructions"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMain_Menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionLighting)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFocus)
        self.menuView.addAction(self.actionFocus_2)
        self.menuTools.addAction(self.actionDraw_Shape)
        self.menuTools.addAction(self.actionAdjust_Density)
        self.menuTools.addAction(self.actionChange_Algae_Type)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ACE (Algae Count Estimator)", None))
        self.pushButton_mm_trainer.setText(_translate("MainWindow", "Trainer", None))
        self.pushButton_mm_editor.setText(_translate("MainWindow", "Editor", None))
        self.pushButton_mm_statistics.setText(_translate("MainWindow", "Statistics", None))
        self.pushButton_mm_exit.setText(_translate("MainWindow", "Exit", None))
        self.label.setText(_translate("MainWindow", "[Table with result data]", None))
        self.pushButton_s_mm.setText(_translate("MainWindow", "Main Menu", None))
        self.label_51.setText(_translate("MainWindow", "[Overall results, averages, charts]", None))
        self.label_7.setText(_translate("MainWindow", "Tool List", None))
        self.label_9.setText(_translate("MainWindow", "Buttons!", None))
        self.label_e_algaetext.setText(_translate("MainWindow", "[Super Realistic Algae Here]", None))
        self.label_2.setText(_translate("MainWindow", "Tool adjustments", None))
        self.label_3.setText(_translate("MainWindow", "Sliders and stuff!", None))
        self.pushButton_e_mm.setText(_translate("MainWindow", "Main Menu", None))
        self.label_10.setText(_translate("MainWindow", "[Super Realistic Algae Here]", None))
        self.pushButton_t_zoom_minus.setText(_translate("MainWindow", "-", None))
        self.pushButton_t_zoom_plus.setText(_translate("MainWindow", "+", None))
        self.label_t_zoom.setText(_translate("MainWindow", "Zoom", None))
        self.label_t_focus.setText(_translate("MainWindow", "Focus", None))
        self.pushButton_t_focus_minus.setText(_translate("MainWindow", "-", None))
        self.pushButton_t_focus_plus.setText(_translate("MainWindow", "+", None))
        self.label_t_status.setText(_translate("MainWindow", "Zoom level | Focus level | Algae Type", None))
        self.label_15.setText(_translate("MainWindow", "Algae Count Guess:", None))
        self.label_16.setText(_translate("MainWindow", "Slide 9 / 10", None))
        self.pushButton_t_submit.setText(_translate("MainWindow", "Submit", None))
        self.textEdit_t_output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 8 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 174 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 235</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> -61 <span style=\" font-style:italic;\">(25.96% off) </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 7 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 <span style=\" font-style:italic;\">(1.68% off) </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 5 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) <br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 4 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 3 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 2 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>) </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Slide 1 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Guessed: 643 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actual: 654 </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-11 (<span style=\" font-style:italic;\">1.68% off</span>)</p></body></html>", None))
        self.pushButton_t_mm.setText(_translate("MainWindow", "Main Menu", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionMain_Menu.setText(_translate("MainWindow", "Main Menu", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom In", None))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out", None))
        self.actionLighting.setText(_translate("MainWindow", "Lighting", None))
        self.actionFocus.setText(_translate("MainWindow", "Focus+", None))
        self.actionFocus_2.setText(_translate("MainWindow", "Focus-", None))
        self.actionDraw_Shape.setText(_translate("MainWindow", "Draw Shape", None))
        self.actionAdjust_Density.setText(_translate("MainWindow", "Adjust Density", None))
        self.actionChange_Algae_Type.setText(_translate("MainWindow", "Change Algae Type", None))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

