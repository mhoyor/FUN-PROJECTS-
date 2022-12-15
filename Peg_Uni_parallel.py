
#Code for playing both in parallel versions:

#Program to play both unicorn and Pegasus in parallel - Multiprocessing 
from multiprocessing import Pool
import time
import logging
from peg_game import play_Unicorn_Pegasus

def logger_setup(path):
    logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
        filename="./" + path + ".log",
        filemode='a')
    logger = logging.getLogger(path)
    return logger

logger = logger_setup('code_execution')

def test_function(name):
    st = time.time()
    play_Unicorn_Pegasus(name)
    logger.info(f'multiprocessing time taken for {name} : {time.time() - st}')

def testing_multiprocessing(names): 
    with Pool(len(names)) as p:
        p.map(test_function,[name for name in names])
    
if __name__ == '__main__':
    names = ['unicorn', 'pegasus']
    testing_multiprocessing(names)

#Function used to play unicorn/Pegasus dice game:
import random
 
def play_Unicorn_Pegasus(game):
    """ start the game you  
            selected unicorn or pegasus.
        Roll a dice until 
            all the body parts of a unicorn or pegasus is collected."""
    bodyCount = 0
    tailCount = 0
    legCount = 0
    headCount = 0
    eyeCount = 0
    mouthCount = 0
    hornCount = 0
    wingCount = 0
    rolls = 0
    horn_rolls_count = 0
    wing_rolls_count= 0
    diceRoll = 0
    while (diceRoll!=1):
        diceRoll = random.randint(1,8)
        print('output of rolling a dice ', rolls+1 ,'times is',diceRoll)
        if (diceRoll == 8):
            horn_rolls_count += 1
        if (diceRoll == 7):
            wing_rolls_count+= 1
        rolls +=1
    bodyCount += 1
    print('Body collected')
    print('Rolls to get body is: ',rolls)
    dice = True
    while (dice):
        diceRoll = random.randint(1,8)
        print('output of a dice roll ', rolls+1 ,'times is',diceRoll)
        rolls +=1
        if (diceRoll == 8):
            horn_rolls_count += 1
        if (diceRoll == 7):
            wing_rolls_count+= 1
        if (diceRoll == 2 and tailCount == 0):
            tailCount += 1
            print("we have ",tailCount," tail ")
        elif(diceRoll == 3 and legCount < 4):
            legCount += 1
            print("we have ",legCount," leg ")
        elif(diceRoll == 4 and headCount == 0):
            headCount += 1
            print("we have ",headCount," head ")
        elif(diceRoll == 5 and headCount == 1 and eyeCount < 2):            
            eyeCount += 1
            print("we have ",eyeCount," eye ")
        elif(diceRoll == 6 and headCount == 1 and mouthCount < 1):
            mouthCount += 1
            print("we have ",mouthCount," mouth ")
        elif(diceRoll == 8 and headCount == 1 and game == "unicorn" and hornCount < 1 ):
            hornCount += 1
            print("we have ",hornCount," horn ")
        elif(diceRoll == 7 and headCount == 1 and wingCount < 2 and game == "pegasus"):
            wingCount += 1
            print("we have ",wingCount," wing ")
        elif(bodyCount == 1 and tailCount == 1 and legCount == 4 and
           headCount == 1 and eyeCount == 2 and mouthCount == 1 and hornCount == 1):
            dice = False
            print('All body parts of Unicorn collected')
            print("collected : body-1,tail-1,leg-4,head-1,eye-2,mouth-1,horn-1")
            print('Rolls to get all body parts of a Unicorn: ',rolls)
            print('number of times wings was gotten while rolling the dice in the game:',wing_rolls_count)
            print('number of times horn was gotten while rolling the dice in the game:',horn_rolls_count)
        elif(bodyCount == 1 and tailCount == 1 and legCount == 4 and
           headCount == 1 and eyeCount == 2 and mouthCount == 1 and wingCount == 2):
            dice = False
            print('All body parts of Pegasus collected') 
            print("collected : body-1,tail-1,leg-4,head-1,eye-2,mouth-1,wing-2")
            print('Rolls to get all body parts of a Pegasus: ',rolls)
            print('number of times wings was gotten while rolling the dice in the game:',wing_rolls_count)
            print('number of times horn was gotten while rolling the dice in the game:',horn_rolls_count)
        else:
            print("dice roll not valid")
    return()

if __name__ == '__main__':
    pass