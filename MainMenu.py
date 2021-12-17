import tkinter as TK
import Instructions as IN
import Start as ST

root = TK.Tk()

def ChangeScreen(window):
    StartButton.grid_remove()
    InstructionsButton.grid_remove()
    QuitButton.grid_remove()
    if window == "Instructions":
        IN.Instructions(root)
    if window == "Start":
        ST.StartRoll(root)
    if window == "MainMenu":
        StartMainMenu

def StartMainMenu(root):
    root.title("Dice")
    root.configure(background="grey")
    
    # make title label
    Title = TK.Label(root, text="Dice", font=("Helvetica", 20), bg="grey")

    #init buttons
    global StartButton
    StartButton = TK.Button(root, text="Start", command=lambda: ChangeScreen(window = "Start"))
    global InstructionsButton
    InstructionsButton = TK.Button(root, text="Instructions", command=lambda: ChangeScreen(window = "Instructions"))
    global QuitButton
    QuitButton = TK.Button(root, text="Quit", command=root.destroy)
    
    #grid buttons and lables
    Title.grid(row=1, column=5, columnspan=3)
    StartButton.grid(row=2, column=5)
    InstructionsButton.grid(row=3, column=5)
    QuitButton.grid(row=4, column=5)
    
StartMainMenu(root)
root.mainloop()
StartMainMenu(root)