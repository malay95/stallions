# Import everything in the pwntools namespace
from pwn import *

def gotanalysis(execute_command = None,filename = "challenge",find_in_got=[],find_symbol_array=[],interactive = False):
    '''
    Get the address of all the vulnerable functions

    :param execute_command: The command to be executed or None
    :param filename: The filename to be executed or "Challenge"
    :param find_in_got: The arrays of function which are to be found in got table or empty
    :param find_symbol_array: The array of function which are to be found in symbolic table or empty
    :param interactive: The option which enables interactive shell or None
    :return: The dictionary which has function name as key and address as value
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

    # Receive the address of main
    main = io.unpack()
    address_dictionary = {}
    # Load up a copy of the ELF so we can look up its GOT and symbol table
    elf = context.binary

    # Fix up its base address.  This automatically updates all of the symbols.
    elf.address = main - elf.symbols['main']
    #Main contains address of base address

    address_dictionary["main"] = elf.address
    log.info("Main:    %x" % main)
    log.info("Address: %x" % elf.address)


    for function in find_in_got:
        where = elf.got[function]
        if where:
            log.info("Function   %s" %function)
            log.info("Where:   %x" % where)
            address_dictionary[function] = where
        else:
            log.info("Function   %s" % function)
            log.info("Not found in GOT")
    # All the function address are relative to main function
    # We want to overwrite it with the address of the function that gives us a shell
    for symbol in find_symbol_array:
        what = elf.symbols[symbol]
        if what:

            log.info("Function   %s" % function)
            log.info("Where:   %x" % where)
            address_dictionary[symbol] = what
        else:
            log.info("Function   %s" % function)
            log.info("Not found in Symbol table")

    # If we really wanted to, we could even find the address of "/bin/sh" in memory
    # binsh = elf.search("/bin/sh\x00").next()

    # For opening the shell if required

    if interactive:
        io.interactive()
    return address_dictionary



if __name__ == "__main__":
    gotanalysis(execute_command=None,filename="challenge",find_in_got=[],find_symbol_array=[],interactive=False)