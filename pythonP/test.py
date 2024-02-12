APA = {} 
with open("C:\movie\python\practice\pythonP\dicdata.csv") as dictionaryData :
    content = dictionaryData.read().splitlines()
    for item in content[1:] :
       key , value= item.split(",")
       APA[key]=value
       print(APA)


userWord = input("enter your word").upper()

for char in userWord :
    print(APA[char])