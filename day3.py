print('''                                    _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                      ''')

print('Welcome to Treaure island. Your mission is to find the treasure.')
first = input('You are on a crossroad. Where should you turn? Type "Left" or "right" \n').lower()
if first == 'left':
    second = input('You find yourself in front of a lake. Do you swim or wait? Type "swim" or "wait" \n').lower()
    if second == 'wait':
        third = input('You are faced with three doors with different colors.Which one should will lead you to the treasure? Choose bewtween "blue", "red", "yellow" \n').lower()
        if third == 'blue':
            print('Eaten by beasts. Game over')
        elif third == 'red':
            print('Burned by fire. Game over.')
        elif third == 'yellow':
            print('Congratulations! You found the treasure!')
        else:
            print('Game over.')
    else:
        print('Game over.')
        
else:
    print('opps! Wrong choice. Game over')




