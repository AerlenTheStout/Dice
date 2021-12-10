# Dice
## This project is meant to replicate a dice game I played at a friends house
this project will be using tkinter to create visuals and a python script to simulate the dice game
### The game is a dice game for any ages, any people, any groups and as many people as wanted

#### Points
- 1's are worth 100 points. 5's are worth 50
- all the other numbers dont have any base value
- runs can only be in the same roll, if you get '6 6' in one roll and a '6' in the next that is not a run
- if you get a run of 3 ones '1 1 1' that is 1000 points
- if you get a run of 3 '4 4 4' that would be 400 points. 
- if you get a run of 4 it is the run of 3 multiplied by 2 '4 4 4 4' would be 400 x 2 = 800 points
- if you get a run of 5 '4 4 4 4 4' it is 1000 points no matter what.

#### Gameplay
- there are five dice that you roll,
- to get on the board you need at least 1000 points before you have 1000 points on the board you cannot keep anything below that 1000 points 
  - ex: I have no points on the board and i get 500 points my first roll i cant just keep that i have to roll until I have 1000 points, after I have 1000 points in the pot I dont have to roll again and I can keep that 1000, now that i have 1000 points on the board I can keep anything under 1000

- if on your roll you do not get any points you pass the dice to the next person rinse and repeat
- if you gain points you can roll again with the dice left
  - ex: i roll a '1 4 3 3 2' I can roll again becasue i got 100 points from the 1
  -  now i re roll the '4 3 3 2' and get '4 6 6 2', i lose the 100 points because i cannot keep anything below 1000 and give the dice to the next person
  -  now after i have 1000 points on the board I dont have to keep rolling until I get 1000
  - ex: if i get 600 points from '6 6 6' i can keep that and i pass the dice to the next person
  -  if you roll all the dice and they all give you points (ex' 1 5 3 3 3 ') those points get stored in a pot (so 100 + 50 + 300 = 450)
  -  now you reroll all the dice and keep adding tom that pot 
  -  next roll i get is '1 4 4 4 2' i lose everything in the pot and pass the dice because i got a 2 which does not have a point value
 
 
> special rule for later about roll off the last person's roll (ASK JACK)
