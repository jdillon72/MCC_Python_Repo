# Variables for numbers of bottles on the wall.
BoB_on_wall = 99

# While loop for subtracting bottles.
while BoB_on_wall > 0:
    if BoB_on_wall > 1:
        print(str(BoB_on_wall) + " bottles of beer on the wall!")
        print(str(BoB_on_wall) + " bottles of beer!")
    else:
        print(str(BoB_on_wall) + " bottle of beer on the wall!")
        print(str(BoB_on_wall) + " bottle of beer!")
    
    print("Take one down, pass it around!")
    BoB_on_wall -= 1 # Increment Count of bottles on the wall.
    
    if BoB_on_wall > 1:
        print(str(BoB_on_wall) + " bottles of beer on the wall!")
    elif BoB_on_wall > 0:
        print(str(BoB_on_wall) + " bottle of beer on the wall!")
    else: # This handles the last part of the song after the while completes.
        print("No more bottles of beer on the wall!")
    
    print() # Used to print blank line between verses.
    

