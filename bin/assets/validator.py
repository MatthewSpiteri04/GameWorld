def main_menu(input):
    try:
        int_input = int(input)
        if int_input > 2 or int_input < 1:
            return False
        else:
            return True
    except ValueError:
        return False
    

def multiplayer_menu(input):
    try:
        int_input = int(input)
        if int_input != 1:
            return False
        else:
            return True
    except ValueError:
        return False
    
def rps(input):
    try:
        int_input = int(input)
        if int_input < 1 or int_input > 3:
            return False
        else:
            return True
    except ValueError:
        return False