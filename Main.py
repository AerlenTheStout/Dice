import tkinter as TK

global root
root = TK.Tk()

def ChangeScreen(window):
    for widgets in root.winfo_children():
      widgets.destroy()
    
    if window == "Instructions":
        Instruction(root)
    if window == "Start":
        Start(root)
    if window == "MainMenu":
        MainMenu(root)

def MainMenu(root):
    root.title("Dice")
    root.configure(background="grey")
    
    # make title label
    Title = TK.Label(root, text="Dice", font=("Helvetica", 20), bg="grey")

    #init buttons
    MainMenu.StartButton = TK.Button(root, text="Start", command=lambda: ChangeScreen(window = "Start"))
    MainMenu.InstructionsButton = TK.Button(root, text="Instructions", command=lambda: ChangeScreen(window = "Instructions"))
    MainMenu.QuitButton = TK.Button(root, text="Quit", command=lambda: root.destroy())

    #grid buttons and lables
    Title.grid(row=1, column=5, columnspan=3)
    MainMenu.StartButton.grid(row=2, column=5)
    MainMenu.InstructionsButton.grid(row=3, column=5)
    MainMenu.QuitButton.grid(row=4, column=5)
    

def Start(root):
    print("StartRoll")


def Instruction(root):
    
    InstructionBox = TK.Message(root, text = "Instructions: \n\n")
    BackButton = TK.Button(root,text="MainMenu", command=lambda:ChangeScreen(window = "MainMenu"))
    
    InstructionBox.grid(row = 2, column = 5)
    BackButton.grid(row = 3, column=5)



MainMenu(root)
root.mainloop()