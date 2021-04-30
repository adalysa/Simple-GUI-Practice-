#Adalysa Rosales
#4/29/2021
#Lab 6

from tkinter import *


class Info(Frame):

    def __init__(self):
        self.window = Tk()

        self.new_frame = Frame(self.window, width=450, height=50, padx=50, pady=30)

        self.new_frame.grid(row=5, sticky="nsew")

        self.name = '\tSteven Marcus\n\t274 Bally Drive\n\tWaynesville, NC 27999'

        self.l1 = Label(self.new_frame, text='\n\n')

        self.l1.grid(row=0, column=1)

        self.show_info_button = Button(self.new_frame, text="Show Info", command=self.show_info)

        self.show_info_button.grid(row=8, column=1, padx=20, pady=30)

        self.quit = Button(self.new_frame, text='Quit', command=self.quit_window)

        self.quit.grid(row=8, column=4, padx=20, pady=30)

        self.window.mainloop();


    def show_info(self):

        self.l1['text'] = self.name


    def quit_window(self):

        self.window.destroy()


ob = Info()