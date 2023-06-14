
def spell():
    text = input("Enter statement to be spelled out: ")

    for item in text:
        # 1. Using for loop and conditions statements:
        if item.isspace() == True:
            print("SPACE")
        else:
            print(item)

        # 2. Using replace() function to replace spaces in text:
        # space_replace = item.replace(" ", "SPACE")
        # print(space_replace)

    print()
    print("How's my spelling?")


spell()