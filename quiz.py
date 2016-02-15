# Fill in  the blank quiz by Michael Speranza
# The following are some test strings to pass in to the play_game function.
gameeasy = """The 1 was invented in the late 20th century. A 2 makes requests via the
internet to a 3,using a protocol called 4. The server responds with files that
your 5 displays."""

gamemedium = '''1 documents are the heart of the web, made up of 2 content and
3 to other HTML documents. 4 is the skeleton of every webpage on the internet,
and with just links, you can travel to many other areas of the 5'''

gamehard = '''Computers are 1. Despite being dumb, they are very 2.
People say they are dumb because when receiving input, computers can be
very 3, meaning that they take what we say for what it is, and cannot complete
any mising information. Misunderstanding our 4 instructions is easy if the human
is not 5 '''

# answer keys to know if the user input is correct
answereasy = ['0','internet','browser','server','http','browser']

answermedium = ['0','HTML','text','links','HTML','internet']

answerhard = ['0','dumb','powerful','literal','unclear','clear']


def difficulty():
    """Prompts the user for what diffuclty they want to play on,
    and returns the correct game/answers"""
    difficulty = raw_input("Choose difficulty easy,medium, or hard:")
    correct_answer = 0
    while correct_answer < 1:
        if difficulty != ('easy' and 'medium' and 'hard'):
            difficulty = raw_input('enter a valid input with no spaces:easy,medium,hard:')
        else:
            correct_answer = correct_answer + 1
    if difficulty == "easy":
        game = gameeasy
        answers = answereasy
    elif difficulty == "medium":
        game = gamemedium
        answers = answermedium
    else:
        difficulty == "hard"
        game = gamehard
        answers = answerhard
    return game,answers

game,answers = difficulty()


def play_game(game,answers): 
    ''' Plays a full fill in the
    blank quiz game that prompts
    the user for a word to fill in
    the blank and offers 2 tries'''
    answer_index = 1
    while answer_index < len(answers):
        print game
        user_input = raw_input('Fill in the blank for ' + str(answer_index) + ' here:')
        if user_input == answers[answer_index]:
            game = game.replace(str(answer_index),user_input)
            answer_index += 1
    return "Congratulations on finishing!!"     
        
          
print play_game(game, answers)       
