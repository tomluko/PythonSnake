# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import ttk
import FileIO
import Game

class GUI(Tk):

    MouseClick = "<Button-1>"
    ComboBoxValueSelected = "<<ComboboxSelected>>"

    def __init__(self):
        super(GUI, self).__init__()
        self.levelFile = ""
        self.btnPlay = None
        self.btnQuit = None
        self.lblScoreVar = StringVar() #to change score lable text dynamically
        self.cBoxLevel = None
        self.buildGUI()

    def buildGUI(self):
        self.title("PythonSnake by Tomas Lukošius")
        #select level
        frSelect = ttk.LabelFrame(self, text="Select level")
        frSelect.pack(side=TOP, fill=X)
        self.cBoxLevel = ttk.Combobox(frSelect, values=FileIO.getLevels())
        self.cBoxLevel.bind(self.ComboBoxValueSelected, self.cBoxLevelSelected)
        self.cBoxLevel.current(1)
        self.cBoxLevelSelected()
        self.cBoxLevel.pack()

        #last score
        frScore = ttk.LabelFrame(self, text="Last score")
        frScore.pack(side=TOP, fill=X)
        self.lblScoreVar.set("Not played yet")
        lblScore = ttk.Label(frScore, textvariable = self.lblScoreVar)
        lblScore.pack()

        #buttons play and quit
        frBtns = ttk.LabelFrame(self, text="What yout want to do next?")
        frBtns.pack(side=TOP, fill=X)
        self.btnPlay = ttk.Button(frBtns, text="Play")
        self.btnPlay.bind(GUI.MouseClick, self.btnPlayClic)
        self.btnPlay.pack(side=LEFT)
        self.btnQuit = ttk.Button(frBtns, text="Quit")
        self.btnQuit.bind(GUI.MouseClick, self.btnQuitClick)
        self.btnQuit.pack(side=RIGHT)

        #center window
        self.centerGUI()

    def centerGUI(self):
        self.update_idletasks()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        sizeString = self.geometry().split("+")[0].split("x")
        size = tuple(int(number) for number in sizeString)
        newX = (width - size[0])/2
        newY = (height - size[1])/2
        self.geometry("%dx%d+%d+%d" % (size + (newX, newY)))

    #interaction functions
    def btnPlayClic(self, event = None):
        game = Game.Game(self.levelFile)
        game.run()
        self.lblScoreVar.set(str(game.getLevel().getSnake().getBodyLength()) + " points in " + self.levelFile + " map")
    def btnQuitClick(self, event = None):
        quit()
    def cBoxLevelSelected(self, event = None):
        self.levelFile = self.cBoxLevel.get()

gui = GUI()
gui.mainloop()