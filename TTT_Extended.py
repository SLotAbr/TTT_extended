from time import sleep
from tkinter import *
import random


tk = Tk()
tk.title("Tic-tac-toe.extend")
tk.resizable(0, 0)  # The window size becomes fixed
tk.wm_attributes("-topmost", 1)  # The canvas window is placed on top of all other windows ("–topmost")
canvas = Canvas(tk, width=520, height=550, bd=0,highlightthickness=0)
canvas.pack()  # After this command, the canvas resizes according to the specified parameters


class Cell:
	def __init__(self,canvas,x,y):
		self.canvas=canvas
		self.ZeroImage=PhotoImage(file="Resources/Zero.png")
		self.CrossImage=PhotoImage(file="Resources/Cross.png")
	# 25 here - padding size between buttons (20 - button's size)
	# Due to the presence of 4 fictitious buttons on each side need 
	# to add an offset (Now is not +10, but +10 - 25*4 = -90)
		self.B=Button(tk, width=3, height=1, command=self.SetButton)
		self.x_pos=x
		self.y_pos=y
		self.B.place(x=x*25-90,y=y*25-90, width=20, height=20)

	# Replacing a button with an image
	def SetButton(self):
		global Button_type
		global globalType
		global last_action
		global TypeCells
		
		if Win==0:
			self.B.place(x=-100,y=-100, width=90, height=90)
			if globalType==1:
				self.B=canvas.create_image(self.x_pos*25-90, self.y_pos*25-90, \
					image=self.ZeroImage, anchor='nw')
				# Creates a mark in the list storing cell types 
				# about user action
				TypeCells[self.y_pos*28 + self.x_pos]=1
				# Saves the coordinate of the last move
				last_action = [self.x_pos, self.y_pos]

				# Changes the number of the current player and paints 
				# the Button_type in the appropriate color
				globalType=2
				Button_type.config(bg='red')
			elif globalType==2:
				self.B=canvas.create_image(self.x_pos*25-90, self.y_pos*25-90, \
					image=self.CrossImage, anchor='nw')
				TypeCells[self.y_pos*28 + self.x_pos]=2
				last_action = [self.x_pos, self.y_pos]

				globalType=1
				Button_type.config(bg='green')


def center_check():
	global globalType
	global last_action
	global TypeCells
	global Win
	# since globalType instantly changes for the next player's move, 
	# you must remember that the previous move was made by another player
	if globalType==1:
		last_color=2
	elif globalType==2:
		last_color=1

	x = last_action[0]
	y = last_action[1]

	# loop of checks
	for b in range(5):
		# vertical check
		if (TypeCells[(y-b)*28 + x]==last_color) &\
		 (TypeCells[(y+1-b)*28 + x]==last_color) &\
		 (TypeCells[(y+2-b)*28 + x]==last_color) &\
		 (TypeCells[(y+3-b)*28 + x]==last_color) &\
		 (TypeCells[(y+4-b)*28 + x]==last_color):
			Win=last_color
			break
		# horizontal check
		if (TypeCells[y*28 + (x-b)]==last_color) &\
		 (TypeCells[y*28 + (x+1-b)]==last_color) &\
		 (TypeCells[y*28 + (x+2-b)]==last_color) &\
		 (TypeCells[y*28 + (x+3-b)]==last_color) &\
		 (TypeCells[y*28 + (x+4-b)]==last_color):
			Win=last_color
			break
		# main diagonal check
		if (TypeCells[(y-b)*28 + (x-b)]==last_color) &\
		 (TypeCells[(y+1-b)*28 + (x+1-b)]==last_color) &\
		 (TypeCells[(y+2-b)*28 + (x+2-b)]==last_color) &\
		 (TypeCells[(y+3-b)*28 + (x+3-b)]==last_color) &\
		 (TypeCells[(y+4-b)*28 + (x+4-b)]==last_color):
			Win=last_color
			break
		# secondary diagonal check
		if (TypeCells[(y-b)*28 + (x+b)]==last_color) &\
		 (TypeCells[(y+1-b)*28 + (x-1+b)]==last_color) &\
		 (TypeCells[(y+2-b)*28 + (x-2+b)]==last_color) &\
		 (TypeCells[(y+3-b)*28 + (x-3+b)]==last_color) &\
		 (TypeCells[(y+4-b)*28 + (x-4+b)]==last_color):
			Win=last_color
			break


def check():
	global last_action

	if (last_action[0]>=4 & last_action[0]<24) & \
		(last_action[1]>=4 & last_action[1]<24):
		center_check()


Win=0
BaseCells=[x*0 for x in range(28*28)] 	# Cell field formation
for y in range(4,24):
	for x in range(4,24):
		BaseCells[y*28 + x]=Cell(canvas,x,y)

TypeCells=[x*0 for x in range(28*28)]

# Displays the color of the acting side
Button_type=Button(tk, width=3, height=1,bg='green')
Button_type.place(x=488,y=510, width=15, height=15)

last_action=[0,0]
globalType=1

while 1:
	check()
	if Win==1:
		canvas.create_text(165, 525, text='Green Victory',font=('Courier',15))
	elif Win==2:
		canvas.create_text(165, 525, text='Red Victory',font=('Courier',15))
	elif (Win==0) and (TypeCells.count(0)==384):
		canvas.create_text(165, 525, text='Draw',font=('Courier',15))
		
	tk.update_idletasks()
	tk.update()
	sleep(0.01)
