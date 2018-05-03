import requests
from bs4 import BeautifulSoup
import analyze_index_php as a

def getformfields(filename = "index.html"):
    content  = ""
    with open(filename,'r') as f:
        content += f.read()
    soup = BeautifulSoup(content,'html.parser')
    formTags = soup.find_all('form')
    i = 0
    for form in formTags:

        print("------------")
        print("Form number " + str(i))

        i += 1
        input_tags = form.find_all('input')
        for one_input_tag in input_tags:
            print(one_input_tag["name"])
        try:
            print("action:     " + form["action"])
            print("Calling Now action:")
            a.analyze_index_php(form["action"])

        except:

            print("No action specified")

        # print("Enter port number :")

        # print(input_tags)

    # print(formTags)
    # print(soup)

if __name__ ==  "__main__":
    getformfields()
