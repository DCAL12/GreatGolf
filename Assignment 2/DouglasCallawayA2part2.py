""" CP1200 Assignment 2 (Part 2) - 2014-Block 7
    Great Golf Game 
    Douglas Callaway
    21/07/2014

Pseudocode:

use Club class (refer to club.py)

(Club dictionary/map: Average shot strengths are measured in meters.)
CLUB_DICTIONARY = empty map 
CLUB_DICTIONARY['D'] = new instance of class Club("Driver", 100) 
CLUB_DICTIONARY['3'] = new instance of class Club("3 Iron", 60) 
CLUB_DICTIONARY['7'] = new instance of class Club("7 Iron", 30) 
CLUB_DICTIONARY['P'] = new instance of class Club("Putter", 10)

(Swing strength variations (% of average hit distance))
SHOT_STRENGTH_VARIATION_LOWER = 80
SHOT_STRENGTH_VARIATION_UPPER = 120

(Putting parameters)
SHORT_PUT_THRESHOLD_METERS = 10
MIN_PUT_DISTANCE_METERS = 1

(Hole & play attributes)
PAR = 5
HOLE_DISTANCE_FROM_TEE = 230
NUMBER_ROUNDS_MIN = 1
NUMBER_ROUNDS_MAX = 9

(Administrative attributes)
PLAYER_NAME_LENGTH_MIN = 1
PLAYER_NAME_LENGTH_MAX = 27
SCORE_OUTPUT_FILE = "scores.txt"
        
function main()
    display welcome message
    get playerFullName
    repeat while length of playerFullName < PLAYER_NAME_LENGTH_MIN 
    or > PLAYER_NAME_LENGTH_MAX
        display error message
        get playerFullName
  
    display menu
    get menuChoice as upper-case     
    repeat while menuChoice is not 'Q'
        if menuChoice is 'I'
            display instructions
            call showClubMenu()
        otherwise if menuChoice is 'V'
            call viewScores(SCORE_OUTPUT_FILE)
        otherwise if menuChoice is 'P'
            call playGolf(playerFullName)
        otherwise
            display invalid choice message
    
        display menu
        get menuChoice as upper-case
    
    display "Thanks for playing."

function showClubMenu()
    display "Club Selection:"
    for each key in CLUB_DICTIONARY keys
        display key, call getClubInfo() (from Club class)

function viewScores(fileName)
    (open the 'fileName' text file, store the names and scores in a 
        score-sorted list, then display to the user) 
    scoresContents = blank list
    open SCORE_OUTPUT_FILE as inFile for reading
    for each line in inFile
        lineElements =  formated score, formated name
        append lineElements to scoresContents
    close inFile
    sort scoresContents by ascending score
    
    for each entry in  scoresContents
        display name, score

function getValidString(minLength, maxLength, prompt, errorMessage):
    (Validate a user input string)
    display prompt
    get validString
    while length of validString < minLength or > maxLength:
            display errorMessage
            get validString
    
    return validString

function getValidInteger(lowerLimit, upperLimit, prompt, errorMessage)
    (validate that a user-input value is a valid integer within a given range)
    finished = False
    repeat while not finished
        try
            display prompt
            get validInteger
            repeat while validInteger < lowerLimit or > upperLimit
                display errorMessage
                get validInteger
            finished = True   
        
        except
            display errorMessage

    return validInteger

function playGolf(playerFullName)        
    (Play the desired number rounds of golf (1-9). Prompt the player to pick a
        club; calculate the new distanceToHole until the ball reaches the hole.)
    numberRounds = call getValidInteger(NUMBER_ROUNDS_MIN, NUMBER_ROUNDS_MAX, 
        prompt, error message)
    for each roundNumber in numberRounds  
        distanceToHole = HOLE_DISTANCE_FROM_TEE
        shotCount = 0
        display roundNumber, hole information
        call showClubMenu()

        (repeatedly prompt the player to pick a club, then calculate the 
            new distanceToHole until the ball reaches the hole)
        repeat while distanceToHole > 0
            display distanceToHole, shotCount            
            get clubSelection as upper-case
            if clubSelection is in CLUB_DICTIONARY
                call CLUB_DICTIONARY[clubSelection].setSwingStrength(SHOT_STRENGTH_VARIATION_LOWER,
                                                                    SHOT_STRENGTH_VARIATION_UPPER)
                if clubSelection is 'P' and distanceToHole < SHORT_PUT_THRESHOLD_METERS             
                    call CLUB_DICTIONARY[clubSelection].shortPut(distanceToHole, 
                                                                MIN_PUT_DISTANCE_METERS)
                otherwise
                    call CLUB_DICTIONARY[clubSelection].swing()
                
                shotDistance = call CLUB_DICTIONARY[clubSelection].getShot()
            
            otherwise
                shotDistance = 0
                display missed swing message
                call showClubMenu()
            
            display shotDistance
            distanceToHole = absolute value of (distanceToHole - shotDistance)
            shotCount = shotCount + 1     
    
        display hole completion message, shotCount
        parScore = absolute value of (shotCount - PAR)
    
        if shotCount > PAR
            display "Disappointing.", parScore
        otherwise if shotCount is PAR
            display "And that's par."
        otherwise
            display "Congratulations.", parScore
        
        (Ask the user whether to save the score.  If yes, append the score 
            and player's full name to the scores file)
        playerNames = playerFullName divided into list elements (first name, last name)
        get saveScoreToFile as upper-case (prompt user using first name)
        repeat while saveScoreToFile is not 'Y' and 'N'
            display error message
            get saveScoreToFile as upper-case
            
        if saveScoreToFile is 'Y'
            open SCORE_OUTPUT_FILE as outFile for appending
            write shotCount, playerFullName to outFile
            close outFile
            display "Score saved. New high scores:"
            call viewScores(SCORE_OUTPUT_FILE)
            
call main()
"""
import club

# Club dictionary/map: Average shot strengths are measured in meters.
CLUB_DICTIONARY = {'D' : club.Club("Driver", 100),\
                   'P' : club.Club("Putter", 10),\
                   '7' : club.Club("7 Iron", 30),\
                   '3' : club.Club("3 Iron", 60),\
                  }

# Swing strength variations (% of average hit distance)
SHOT_STRENGTH_VARIATION_LOWER = 80
SHOT_STRENGTH_VARIATION_UPPER = 120

# Putting parameters
SHORT_PUT_THRESHOLD_METERS = 10
MIN_PUT_DISTANCE_METERS = 1

# Hole attributes
PAR = 5
HOLE_DISTANCE_FROM_TEE = 230
NUMBER_ROUNDS_MIN = 1
NUMBER_ROUNDS_MAX = 9

# Administrative attributes
PLAYER_NAME_LENGTH_MIN = 1
PLAYER_NAME_LENGTH_MAX = 27
SCORE_OUTPUT_FILE = "scores.txt"
MENU = "\nGolf!\n(I)nstructions\n(V)iew scores\n(P)lay round\n(Q)uit"
INSTRUCTIONS = "Instructions: It's golf on your console. Each shot will vary in distance around its average."
    
def main():
    """Prompt the user for menu selections until he/she chooses to quit."""
    print("Let's play great golf, CP1200 style!")
    print("Written by Douglas Callaway, July 2014")
    
    playerFullName = getValidString(PLAYER_NAME_LENGTH_MIN, PLAYER_NAME_LENGTH_MAX, 
                                    "Please enter your name: ", 
                                    "Your name can not be blank and must be <= " +
                                    str(PLAYER_NAME_LENGTH_MAX) + " characters")
    print(MENU)
    menuChoice = input(">>>").upper()
  
    while menuChoice != 'Q':
        if menuChoice == 'I':
            print(INSTRUCTIONS)
            showClubMenu()    
        elif menuChoice == 'V':
            viewScores(SCORE_OUTPUT_FILE)
        elif menuChoice == 'P':
            playGolf(playerFullName)
        else:
            print("Invalid menu choice.")
    
        print(MENU)
        menuChoice = input(">>>").upper()
    
    print("Thanks for playing.")

def showClubMenu():
    """Display all available clubs and associated distances."""
    print("Club selection:")
    #List all clubs in the dictionary by key, name, and distance
    for key in CLUB_DICTIONARY.keys():
        print(str(key), "for", CLUB_DICTIONARY[key].getClubInfo())
  
def viewScores(fileName=SCORE_OUTPUT_FILE):
    """Display the saved high scores.
    
     Open the 'scores' text file, store the names and scores 
     in a score-sorted list, then display to the user.
    """
    scoresContents = []
    inFile = open(fileName, "r")
    for line in inFile:
        lineElements = (line.strip()).split(',')
        # format the score to take up 2 spaces and the name to take up 
        # PLAYER_NAME_LENGTH_MAX spaces
        lineElements = [format(int(lineElements[0]), '2'), 
                        format((lineElements[1]).lstrip(), 
                               str(PLAYER_NAME_LENGTH_MAX) + 's')]
        scoresContents.append(lineElements)
    inFile.close()
    scoresContents.sort()
    
    for entry in scoresContents:
        print(entry[1], entry[0])

def getValidString(minLength=1, maxLength=100, 
                    prompt="Enter a valid string: ", 
                    errorMessage="Invalid Input."):
    """Validate a user input string.

    Keyword arguments:
    minLength -- the minimum acceptable length (default 1)
    maxLength -- the maximum acceptable length (default 100)
    prompt -- string to prompt the user (default "Enter a valid string: ")
    errorMessage -- for invalid input (default "Invalid Input.")
    """
    validString = input(prompt)
    while len(validString) < minLength or len(validString) > maxLength:
            print(errorMessage)
            validString = input(prompt)
    
    return validString
            
def getValidInteger(lowerLimit=1, upperLimit=9, 
                    prompt="Enter a valid integer: ", 
                    errorMessage="Invalid Input."):
    """Validate a user input integer.

    Keyword arguments:
    lowerLimit -- the minimum acceptable value (default 1)
    upperLimit -- the maximum acceptable value (default 9)
    prompt -- string to prompt the user (default "Enter a valid integer: ")
    errorMessage -- for invalid input (default "Invalid Input.")
    """
    finished = False
    while not finished:
        try:
            validInteger = int(input(prompt))
            while validInteger < lowerLimit or validInteger > upperLimit:
                print(errorMessage)
                validInteger = int(input(prompt))
            finished = True   
        
        except:
            print(errorMessage)

    return validInteger

def playGolf(playerFullName):
    """Play the desired number rounds of golf (1-9). 
    
    Prompt the player to pick a club; 
    calculate the new distanceToHole until the ball reaches the hole;
    allow user to save score
    """        
    numberRounds = getValidInteger(NUMBER_ROUNDS_MIN, NUMBER_ROUNDS_MAX, 
                                   "How many rounds would you like to play? (1-9) ",
                                   "Invalid number of rounds.")
    for roundNumber in range(numberRounds):  
        distanceToHole = HOLE_DISTANCE_FROM_TEE
        shotCount = 0
        print("\nRound", roundNumber + 1)
        print("This hole is a", str(HOLE_DISTANCE_FROM_TEE) + "m", "par", PAR)
        showClubMenu()

        while distanceToHole > 0:
            print("You are", str(distanceToHole) + "m", "from the hole, after",
                  shotCount, "shot/s")       
            
            clubSelection = (input("Choose club: ")).upper()
            if clubSelection in CLUB_DICTIONARY:
                CLUB_DICTIONARY[clubSelection].setSwingStrength(SHOT_STRENGTH_VARIATION_LOWER,
                                                                SHOT_STRENGTH_VARIATION_UPPER)
                if clubSelection == 'P' and distanceToHole < SHORT_PUT_THRESHOLD_METERS:             
                    CLUB_DICTIONARY[clubSelection].shortPut(distanceToHole, 
                                                            MIN_PUT_DISTANCE_METERS)
                else:
                    CLUB_DICTIONARY[clubSelection].swing()
                
                shotDistance = CLUB_DICTIONARY[clubSelection].getShot()
            
            else:
                shotDistance = 0
                print("Invalid club selection = air swing :(")
                showClubMenu()
                
            print("Your shot went " + str(shotDistance) + "m")
            distanceToHole = abs(distanceToHole - shotDistance)
            shotCount += 1     
    
        print("Clunk... After", shotCount, "hits, the ball is in the hole!")
        parScore = abs(shotCount - PAR)
        if shotCount > PAR:
            print("Disappointing. You are", parScore, "over par.")
        elif shotCount == PAR:
            print("And that's par.")
        else:
            print("Congratulations. You are", parScore, "under par.")
        
        """
        Ask the user, by his/her first name, whether to save the score.  
        If yes, append the score and player's full name to the scores file.
        """
        playerNames = playerFullName.split()
        saveScoreToFile = (input("Would you like to save your score, " + 
                                 playerNames[0] + "? (Y/N) ")).upper()
        while saveScoreToFile != 'Y' and saveScoreToFile != 'N':
            print("Please enter Y or N")
            saveScoreToFile = (input("Would you like to save your score, " + 
                                     playerNames[0] + "? (Y/N) ")).upper()
        if saveScoreToFile == 'Y':
            outFile = open(SCORE_OUTPUT_FILE, "a")
            outFile.write(str(shotCount) + ", " + playerFullName + '\n')
            outFile.close()
            print("Score saved. New high scores:")
            viewScores(SCORE_OUTPUT_FILE)
            
main()