##############################################################################
# Programming Excercise 17
#
# Allow a user to keep a running journal of field notes.  
# Each time the program starts, ask the user if they want to read the journal or add an entry.

# If they want to read it, print the entire contents of the file to the screen.
# they want to add an entry, ask them to type a series of lines of text 
# and terminate with the work "QUIT" on a single line.  

# Ensure that the entire contents of the journal are preserved!
#############################################################################

filename = 'notes.txt'

# return 0 for read/print and 1 for add entry
def prompt_action() :
    text = input("Please type 'print' to print your journal to the screen or 'add' to add an entry:  ")
    if text.lower() == 'add':
        return 1
    else:
        return 0

def print_journal() :

    #==============================================================
    # Check if the file exists, otherwise we get an error on open
    import os
    import os.path
    if os.path.isfile(filename) == False:
        print("Sorry, the file doesn't exist!")
        return
    #==============================================================
    
    journal = open(filename, 'r')
    for line in journal:
        print(line[:-1])
    journal.close()


def add() :
    journal = open(filename, 'a')
    done = False
    print("OK, go ahead an start typing.  When you are done, type QUIT on a single line")
    while done == False:
        text = input("> ")
        if text == 'QUIT':
            journal.close()
            return
        else :
            journal.write(text + '\n')

choice = prompt_action()
if choice == 0:
    print_journal()
else:
    add()
