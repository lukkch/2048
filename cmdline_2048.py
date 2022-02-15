import msvcrt
import logic_2048

myBoard = logic_2048.Board()
myBoard.spawnTile()
myBoard.spawnTile()

def tryAI(rounds):
    AvgScore = 0
    for i in range(0,rounds):
        lost = False
        while not lost:
            myBoard.makeGoodMove()
            myBoard.spawnTile()
            if myBoard.isLossState():
                lost=True
                print("MAX WAS " + str(myBoard.getMaxTile()))
        max, secondMax = myBoard.getMaxTile() 
        AvgScore += max + 0.5*secondMax
        myBoard.resetBoard()
    AvgScore *= 1 / rounds
    print("AVG SCORE: " + str(AvgScore))

print("Welcome to 2048. Use WASD to move the tiles around, press k to try out the 'AI' (it's pretty dumb, still is moderatly successful)")
print("Press c to exit the game")
while True:
    myBoard.spawnTile()
    myBoard.printBoard()
    action = msvcrt.getch().decode("utf-8")
    print(action)
    if action == "c":
        print("Exiting...")
        break
    if action == "w":
        myBoard.moveUp()
    elif action == "a":
        myBoard.moveLeft()
    elif action == "s":
        myBoard.moveDown()
    elif action == "d":
        myBoard.moveRight()
    elif action == "k":
        exit = False
        while(not exit):
            print("How many rounds should the AI play? Please enter a number between 0 and 100.")
            amount = input()
            if amount == "c" or amount == "C":
                exit=True
            try:
                amount = int(amount)
                if not amount > 0 and amount <=100:
                    print("For your own good, please try a number between 0 and 100. It is slow.")
                else:
                    print("Starting the AI, this might take a while...")
                    tryAI(amount)
                    exit = True
            except:
                print("Please enter a number. To exit, enter <C>")
    else:
        print("invalid input")
