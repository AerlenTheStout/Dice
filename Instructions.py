import tkinter as TK
import MainMenu as MM

def Instructions(root):
    
    InstructionBox = TK.Message(root, text = "Instructions: \n\n")
    
    BackButton = TK.Button(root,text="MainMenu", command=lambda:MM.ChangeScreen(window = "MainMenu"))
    
    InstructionBox.grid(row = 2, column = 5)
    BackButton.grid(row = 3, column=5)