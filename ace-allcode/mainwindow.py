"""
mainwindow.py

Holds the MainWindow class, top level widget of the application.
MainWindow has instances of each page in a stacked widget, and 
is responsible for switching between them.
"""
from PyQt4 import QtCore, QtGui
from mainmenu import MainMenu
from trainer import Trainer
from stats import Statistics
from editor import Editor
from enum import ModeEnum

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()        
        
        self.setWindowTitle("Algae Count Estimator")
        self.setMinimumSize(800,600)
        
        self.initPages()
        self.initMenuBar()       
        
        self.show()
    
    #creates QStackedWidget to contain the different modes (pages)
    #populates the stacked widget with instances of the modes
    def initPages(self):
        self.mode_stack = QtGui.QStackedWidget()
        
        main_menu = MainMenu(self)
        self.mode_stack.addWidget(main_menu)
           
        trainer = Trainer(self)
        self.mode_stack.addWidget(trainer)
        
        stats = Statistics(self)
        self.mode_stack.addWidget(stats)
        
        self.editor = Editor(self)
        self.editor.toolbar.toggleViewAction().trigger()
        self.mode_stack.addWidget(self.editor)
     
        
        self.setCentralWidget(self.mode_stack)
                
    def initMenuBar(self):
        menu_bar = self.menuBar()
        
        file_menu = menu_bar.addMenu('&File')
        to_menu_action = QtGui.QAction('Main Menu', self)
        to_menu_action.triggered.connect(lambda: self.changeMode(ModeEnum.MENU))
        
        exit_action = QtGui.QAction('Exit', self)
        exit_action.triggered.connect(QtGui.qApp.quit )
        
        file_menu.addAction(to_menu_action)
        file_menu.addAction(exit_action)
        
        edit_menu = menu_bar.addMenu('&Help')
        
    def changeMode(self, page_num):
        #Editor Mode uses a toolbar that must be owned by MainWindow
        #If switching away from editor, hide the toolbar
        if self.mode_stack.currentIndex() == ModeEnum.EDITOR:
            self.editor.toolbar.toggleViewAction().trigger()
        #If switching to Editor, show the toolbar
        if page_num == ModeEnum.EDITOR:
            self.editor.toolbar.toggleViewAction().trigger()

        
        self.mode_stack.setCurrentIndex(page_num)
        