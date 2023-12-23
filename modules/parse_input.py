from model.decorators.input_error import input_error

@input_error
def parse_input(user_input):
    """Parses entered by user command.
    The command splits on 'cmd' - action that user wants the program to do,
    and 'args' - data on which the action is performed.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args