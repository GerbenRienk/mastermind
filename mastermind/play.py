import random




#Generate a random sequence of colors of length game length
def init(gl):
    _answer = []
    for i in range(gl):
        a = random.randint(0, 5)
        _color = colors[a]
        _answer.append(_color)
        i += 1
    return(_answer)
    

def check(guess, gl, answer):
    hg = 0
    bg = 0
    available = []
    for i in range(gl):
        available.append(True)
        if guess[i] == answer[i]:
            hg += 1
            available[i] = False
            
    for j in range(gl):
        if available[j] == True:
            for i in range(gl):
                if available[i] == True:
                    if guess[j] == answer[i]:
                        bg += 1
                        break 
    
    returnanswer = ''.join(guess)
    returnanswer += ' , '
    returnanswer += str(hg)
    returnanswer += ' , '
    returnanswer += str(bg)
    
    return(returnanswer)

def playgame():
    
    #initialize variables
    global colors
    colors = ["r", "g", "b", "y", "w", "o"]
    global game_length
    game_length = 0
    global answer
    guess = 0
    global continue_game
    continue_game = True
    previousguesses=[]    
        

    print("Welcome to Mastermind")
    print("Your goal is to deduce the correct sequence of colors")
    print("The available colors are Red (r), Green (g), Blue (b), Yellow (y), Orange (o) and White (w)")
    print("The numbers next to your guesses indicate the amount of correctly placed colors (left) and")
    print("the amount of correct colors in the wrong place (right)")


    #begin fase    
    while game_length == 0:
        g_l = input("Please select difficulty level (e/m/h): ")
        if g_l == "e":
            game_length = 3
        elif g_l == "m":
            game_length = 5
        elif g_l == "h":
            game_length = 7
        else:
            print("Please input a valid difficulty")
            print("e = Easy, m = Medium, h = Hard")
            g_l=''
            game_length = 0
    print("The answer is of length ", game_length)
    
    answer = init(game_length)


    while continue_game == True:
        guess = input("Guess? : ")
        if guess == "end":
            continue_game = False
        lguess = list(guess)
        if len(lguess) > int(game_length) or len(lguess) < int(game_length):
            print("Please make a valid guess")
            continue
        previousguesses.append(check(lguess, int(game_length), answer))
        for i in range(len(previousguesses)):
            print(previousguesses[i])
        if lguess == answer:
            print("YOU WON!")
            continue_game = False
        if len(previousguesses)>9:
            print("You lost, you took too many tries.")
            continue_game = False
    
    print("Correct answer = ", ''.join(answer))

    replay = input("Play again ? (y/n)")
    if replay == "y":
        playgame()
        
if __name__ == '__main__':
    playgame()