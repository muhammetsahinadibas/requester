import requests

print("""
 ____                            _
|  _ \ ___  __ _ _   _  ___  ___| |_ ___ _ __
| |_) / _ \/ _` | | | |/ _ \/ __| __/ _ \ '__|
|  _ <  __/ (_| | |_| |  __/\__ \ ||  __/ |
|_| \_\___|\__, |\__,_|\___||___/\__\___|_|
              |_|

------------------------------------------
| Developer: Muhammet Sahin Adibas       |
| Twitter: twitter.com/muhammetadibas    |
| Blog: muhammetsahinadibas.com.tr       |
| Github: github.com/muhammetsahinadibas |
------------------------------------------
""")

url = input("Enter the URL you want to request: ")

fuzz_url_question = input("\nDo you want to add a number increasing by the amount of the request into the URL ? (Yes=1 , No=2): ")
if(fuzz_url_question == "1"):
    enter_fuzz_url_question = input("      |------> Enter FUZZ URL ( Example: https://example.com/user.php?id=FUZZ ): ")

number_of_requests = int(input("\nEnter the number of requests: "))

content_question = input("\nDo you want the content of the site ? (Yes=1 , No=2): ")

value_question = input("\nAre there any values you want the site to have in it ? (Yes=1 , No=2): ")
if(value_question == "1"):
    enter_value_question = input("      |------> Enter the value you want to search: ")
    letters_value_question = input("      |------> Do you want to make all letters in the site uppercase or lowercase ? (Upper=1, Lower=2, Do not change=3): ")


# ------------------------------------ Events ------------------------------------


print("\n \nStarted !! Please wait.")

if(content_question == "1" and value_question == "2"):
    if(fuzz_url_question == "1"):
        for i in range(number_of_requests):
            new_url = enter_fuzz_url_question.replace("FUZZ",str(i)) 
            r = requests.get(new_url)
            print("\n \n + |------> " + new_url + "\n" + r.text) 
            
    if(fuzz_url_question == "2"):
        for i in range(number_of_requests):
            r = requests.get(url)
            print("\n \n + |------> " + url + "\n" + r.text)


if(value_question == "1"):
    if(fuzz_url_question == "1"):
        for i in range(number_of_requests):
            new_url = enter_fuzz_url_question.replace("FUZZ",str(i)) 

            r = requests.get(new_url)

            if(letters_value_question == "1"):
                data = r.text.upper()
            elif(letters_value_question == "2"):
                data = r.text.lower()
            elif(letters_value_question == "3"):
                data = r.text

            if enter_value_question in data:
                print("\n + " + "'" + enter_value_question + "'" + " Found! |------> " + new_url)

    if(fuzz_url_question == "2"):
        for i in range(number_of_requests):

            r = requests.get(url)

            if(letters_value_question == "1"):
                data = r.text.upper()
            elif(letters_value_question == "2"):
                data = r.text.lower()
            elif(letters_value_question == "3"):
                data = r.text
                
            if enter_value_question in data:
                print("\n + "  + "'" + enter_value_question + "'" +  " Found! |------> " + url)


if(content_question == "2" and value_question == "2"):
    if(fuzz_url_question == "1"):
        for i in range(number_of_requests):
            new_url = enter_fuzz_url_question.replace("FUZZ",str(i)) 
            r = requests.get(new_url)
        print("\n \nSuccessful!")

    if(fuzz_url_question == "2"):
        for i in range(number_of_requests):
            r = requests.get(url)
        print("\n \nSuccessful!")
