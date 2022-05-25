def deaf_grandma():
    goodbye = 0
    response = input("HEY KID!")
    while goodbye != 2:
        if response == "GOODBYE!" and goodbye == 0:
            response = input("LEAVING SO SOON?")
            goodbye = 1
        if(response == "GOODBYE!" and goodbye == 1):
            print("LATER, SKATER!")
            return
        if response.isupper() == True:
            response = input("NO, NOT SINCE 1946!")
        if response == "":
            response = input('WHAT?!')
        if response != "" and response.isupper() == False:
            response = input('SPEAK UP, KID!')
        

deaf_grandma()
