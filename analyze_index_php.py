import requests
from bs4 import BeautifulSoup

def analyze_index_php(phpfile  = None):
    print("Enter port number:")
    port = input()
    print("Enter the field on which you want to make injection:")
    print("e.g. username , uname , user")
    userfield = input()
    url = "localhost:"+port + "/"+phpfile.strip()+"?"+userfield + "=" + '"' + "'" + '"'
    print("Following url will be called for sql injection")
    print(url)
    response = requests.get(url).text
    print("Response")
    print(response)
    if 'error' in response and 'syntax' in response or 'MySQL' in response:
        print('Its vulnerable')
    else:
        print('Its not vulnerable')

if __name__ == "__main__":
    print("Give name of the php file:")
    print("With path !   e.g. abc/xyz.php")
    file = input()
    analyze_index_php(file)