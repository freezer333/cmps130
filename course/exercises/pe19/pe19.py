##############################################################################
# Programming Excercise 19
#
# Create a function called `removeDuplicates` which accepts a list 
# modified that list such that all duplicates are removes. 
#############################################################################



def removeDuplicates(collection):
    uniques = []
    for x in collection:
        if x not in uniques:
            uniques.append(x)
    
    # the del command will remove specific things from 
    # the collection.  The [:] notation gives us the entire
    # list, so this will remove everything.
    # REMEMBER, we can't just re-assign collection to [], because
    # collection is just a name - we need to change the actual object
    # it is bound to.  So doing collection = [] just binds it to another 
    # empty list - it doesn't make the original empty!
    del collection[:]
    collection.extend(uniques)


test = [1, 2, 2, 3, 4, 4, 5, 1, 2, 3, 4, 5, 2]
removeDuplicates(test)
print(test)



