text = list(input("Enter statement to be spelled out: "))

def spell(text):
    # space = [" "]
    for item in text:
        # str_len = len(item)
        if item.isspace() == True:
            print("SPACE")
        elif (isinstance(item, str)) == True:
            print(item)
    print()
    print("How's my spelling?")


spell(text)