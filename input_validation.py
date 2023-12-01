def input_validation(user_input,limit):
    #user_input=int(user_input)
    if user_input.isnumeric():
        user_input=int(user_input)
    else :
        return False
    if  int(user_input)<1 or int(user_input) > limit:
        return False
    else :
        return True
#

