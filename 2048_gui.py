from tkinter import *
from time import sleep
import tkinter
import tkinter.messagebox
import logic_2048
import random

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        self.myboard = logic_2048.Board()
        self.buttons = [[],[],[],[]] # list of all buttons for easy access via "buttons[row][col]"

        self.button00 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button01 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button02 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button03 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"), command=self.leftPressed)

        self.button10 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button11 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button12 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button13 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))

        self.button20 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button21 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button22 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button23 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))

        self.button30 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button31 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button32 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))
        self.button33 = Button(self, text="",bg="#FFDDCC", fg="#5E5E5E", width=6, height=2, font=("Bahnschrift 45"))

        self.buttonStartRandomAI = Button(self, text="Start Random AI", font=("Arial 20"), command=self.startRandomAI)
        self.buttonStartAI = Button(self, text="Start AI", font=("Arial 20"), command=self.startAI)

        self.appendButtons()
        self.placeButtons()

        self.spawnTile()
        self.spawnTile()

    def appendButtons(self):
        self.buttons[0].append(self.button00)
        self.buttons[0].append(self.button01)
        self.buttons[0].append(self.button02)
        self.buttons[0].append(self.button03)

        self.buttons[1].append(self.button10)
        self.buttons[1].append(self.button11)
        self.buttons[1].append(self.button12)
        self.buttons[1].append(self.button13)

        self.buttons[2].append(self.button20)
        self.buttons[2].append(self.button21)
        self.buttons[2].append(self.button22)
        self.buttons[2].append(self.button23)

        self.buttons[3].append(self.button30)
        self.buttons[3].append(self.button31)
        self.buttons[3].append(self.button32)
        self.buttons[3].append(self.button33)

    def placeButtons(self):
        self.button00.grid(row=0, column=0, padx=10, pady=10)
        self.button01.grid(row=0, column=1, padx=10, pady=10)
        self.button02.grid(row=0, column=2, padx=10, pady=10)
        self.button03.grid(row=0, column=3, padx=10, pady=10)

        self.button10.grid(row=1, column=0, padx=10, pady=10)
        self.button11.grid(row=1, column=1, padx=10, pady=10)
        self.button12.grid(row=1, column=2, padx=10, pady=10)
        self.button13.grid(row=1, column=3, padx=10, pady=10)

        self.button20.grid(row=2, column=0, padx=10, pady=10)
        self.button21.grid(row=2, column=1, padx=10, pady=10)
        self.button22.grid(row=2, column=2, padx=10, pady=10)
        self.button23.grid(row=2, column=3, padx=10, pady=10)

        self.button30.grid(row=3, column=0, padx=10, pady=10)
        self.button31.grid(row=3, column=1, padx=10, pady=10)
        self.button32.grid(row=3, column=2, padx=10, pady=10)
        self.button33.grid(row=3, column=3, padx=10, pady=10)

        self.buttonStartRandomAI.grid(row=4, column=0, padx=10, pady=10)
        self.buttonStartAI.grid(row=4, column=1, padx=10, pady=10)

    def updateButtons(self):
        for row in range(0,4):
            for col in range(0,4):
                if self.myboard.getTile(row, col) == 0:
                    self.buttons[row][col]["text"] = ""
                    self.buttons[row][col]["bg"] = self.getColor(0)

                elif not self.buttons[row][col]["text"] == str(self.myboard.getTile(row, col)):
                    self.buttons[row][col]["text"] = str(self.myboard.getTile(row, col))
                    self.buttons[row][col]["bg"] = self.getColor(self.myboard.getTile(row, col))
        self.update()

    def getColor(self, number):
        switcher = {
            0 : "#FFDDCC",
            2 : "#EEE4DA",
            4 : "#ECE0C8",
            8 : "#F2B179",
            16 : "#f59563",
            32 : "#f67c5f",
            64 : "#f65e3b",
            128 : "#edcf72",
            256 : "#edcc61",
            512 : "#edc850",
            1024 : "#edc53f",
            2048 : "#edc22e"
        }
        return switcher.get(number, "#FF0000")

    def flashBackground(self):
        self.configure(bg="#7aafbf")
        self.update()
        sleep(0.15)
        self.configure(bg="#69abc0")

    def upPressed(self, event=None): 
        if self.myboard.moveUp():
            self.updateButtons()
            sleep(0.2)
            self.spawnTile()
            self.updateButtons()
            if self.myboard.isLossState():
                self.playerLost()
        else:   # move was not possible
            self.flashBackground()

    def downPressed(self, event=None):
        if self.myboard.moveDown():
            self.updateButtons()
            sleep(0.2)
            self.spawnTile()
            self.updateButtons()
            if self.myboard.isLossState():
                self.playerLost()
        else:   # move was not possible
            self.flashBackground()

    def leftPressed(self, event=None):
        if self.myboard.moveLeft():
            self.updateButtons()
            sleep(0.2)
            self.spawnTile()
            self.updateButtons()
            if self.myboard.isLossState():
                self.playerLost()
        else:   # move was not possible
            self.flashBackground()

    def rightPressed(self, event=None):
        if self.myboard.moveRight():
            self.updateButtons()
            sleep(0.2)
            self.spawnTile()
            self.updateButtons()
            if self.myboard.isLossState():
                self.playerLost()
        else:   # move was not possible
            self.flashBackground()


    def spawnTile(self):
        placed  = self.myboard.spawnTile()
        self.updateButtons()
        return placed
    
    def playerLost(self):
        tkinter.messagebox.showinfo("YOU LOST")
        self.myboard.resetBoard()
        self.updateButtons()
    
    def startRandomAI(self):
        lost = False
        while not lost:
            self.myboard.makeRandomMove()
            self.updateButtons()
            sleep(0.01)
            self.spawnTile()
            if self.myboard.isLossState():
                self.playerLost()
                lost = True 
            self.update()
            sleep(0.2)
    
    def startAI(self):
        lost = False
        self.myboard.moveDown()
        self.myboard.moveRight()
        self.updateButtons()
        while not lost:
            self.myboard.makeGoodMove()
            self.updateButtons()
            #sleep(0.05)
            self.spawnTile()
            if self.myboard.isLossState():
                self.playerLost()
                lost = True 
            self.update()
            #sleep(0.05)



    

# Init Tkinter
root = Tk()
app = Window(root)

root.wm_title("2048")
root.geometry("1000x1000")
root.bind("<Up>", app.upPressed)
root.bind("<Down>", app.downPressed)
root.bind("<Left>", app.leftPressed)
root.bind("<Right>", app.rightPressed)

app.configure(bg="#69abc0")
# show window
root.mainloop()