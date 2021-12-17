def ChangeScreen(window):
    StartButton.grid_remove()
    InstructionsButton.grid_remove()
    QuitButton.grid_remove()
    if window == "Instructions":
        Instructions(root)
    if window == "Start":
        StartRoll(root)
    if window == "MainMenu":
        StartMainMenu