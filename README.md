# stallions
Library for using in the attack defense CTFs
Using the library for connecting and automating the process in a CTF. In a normal CTF, a team is given a virtual machine which contains multiple services which have some vulnerbility. A team has to attack those vulnerability to find a flag in another teams VM. We have created a library which you can use to make it easy for attacking and defencing. There are functions for backing up the whole CTF so that you don't loose the points when you cant revert the changes you made. 

We have multiple functions which span over different types of vulnerabilities like web, binary files, C, Global offset table, etc. We have developed command line programs which you can use stand alone. 

Dependencies needed: 
  1. Python 3
  2. Pwntools
  3. Beautifulsoup 
  4. swpag.clients.
Download each dependencies using pip. 

How to run each Function. 
1. takebackup(source, destination) 
  use it in your python file as specified above or use it as command line "./backup.py source destination"
  example:   ./backup.py 
