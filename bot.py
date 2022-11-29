from user_commands_classes import FUNCTIONS


def decor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return 'There is no phone number. Enter name and phone.' # If user didn`t put the number, only name.
        except ValueError: 
            return 'Number must contain only numbers/the number is too short/the date is incorrect.' # If number contains letters
        except KeyError:
            return 'Wrong command. Try again.' # This command is not in the dictionary with commands. 
        except AttributeError:
            return f'You hasn`t set the b-day for this guy yet.'

    return wrapper


@decor
def handle(inp_by_user):

    inp_by_user = inp_by_user.lower().split()
    if ' '.join(inp_by_user[0:2]) == 'show all' or ' '.join(inp_by_user[0:2]) == 'good bye':
        func = ' '.join(inp_by_user[0:2])
    else:
        func = inp_by_user[0]
    args = inp_by_user[1:]

    if func in FUNCTIONS.keys():
        return FUNCTIONS[func]().command_to_execute(args)
    else:
        return f'Command {func} doesn`t exist.'

while True:
    
    user_input = input('Enter the command: ')
    user_handler = handle(user_input)
    
    if user_handler == 'Good bye!':
        print(user_handler)
        exit()
    elif user_handler:
        print(user_handler)
