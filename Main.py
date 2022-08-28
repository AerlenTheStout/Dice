import tkinter as TK

global root
root = TK.Tk()

#TODO change to change dice rolling lable changer 
def changeWaterLabel(*args):
    ST.WaterLabel.config(text='') # clear label
    ST.WaterLabel.config(text= "Water = " + ST.numOfWaterEntry.get()) # set new label text

def rollDice():
    

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
    Title = TK.Label(root, text="Dice", font=("Helvetica", 20), bg="grey",padx=50)

    #init buttons
    MainMenu.StartButton = TK.Button(root, text="Start", command=lambda: ChangeScreen(window = "Start"))
    MainMenu.InstructionsButton = TK.Button(root, text="Instructions", command=lambda: ChangeScreen(window = "Instructions"))
    MainMenu.QuitButton = TK.Button(root, text="Quit", command=lambda: root.destroy())

    #grid buttons and lables
    Title.grid(row=1, column=5, columnspan=3)
    MainMenu.StartButton.grid(row=2, column=5)
    MainMenu.InstructionsButton.grid(row=3, column=5)
    MainMenu.QuitButton.grid(row=4, column=5)
    
    def Instruction(root):
    #TODO : import instructions file and display it
    
    f = open("README.md", "r")
    instructiontxt = f.read()
    
    InstructionBox = TK.Message(root, text = instructiontxt, width = 500, bg="white",pady=50,padx=50)
    BackButton = TK.Button(root,text="MainMenu", command=lambda:ChangeScreen(window = "MainMenu"))
    
    InstructionBox.grid(row = 2, column = 5)
    BackButton.grid(row = 3, column=5)

def Start(root):
    print("StartRoll")

    BackButton = TK.Button(root,text="MainMenu", command=lambda:ChangeScreen(window = "MainMenu"))
    BackButton.grid(row = 3, column=5)

    #create dice
    Dice1 = TK.Label(root, text="Dice1", bg="white", padx=50)
    Dice2 = TK.Label(root, text="Dice2", bg="white", padx=50)
    Dice3 = TK.Label(root, text="Dice3", bg="white", padx=50)
    Dice4 = TK.Label(root, text="Dice4", bg="white", padx=50)
    Dice5 = TK.Label(root, text="Dice5", bg="white", padx=50)


MainMenu(root)
root.mainloop()