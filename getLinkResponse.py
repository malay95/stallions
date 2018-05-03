import requests
from bs4 import BeautifulSoup
def getLinkResponse():
    print("which url you want to connect?")
    url = input()
    try:
        response = requests.get(url).text
        soup = BeautifulSoup(response,"html.parser")
        if response:
            print(soup)
        else:
            print("No response")
    except:
        print("Exception!")

if __name__ == "__main__":
    getLinkResponse()