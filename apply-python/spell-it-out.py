text = list(input("Enter statement to be spelled out: "))
# text = (" " in text) = "SPACE"
# print(text)

# def spell(text):
#     for item in text:
#         # item = text(" ") = "SPACE"
#         print(item)


# spell(text)


def spell1(text):
    # space = [" "]
    for item in text:
        str_len = len(item)
        if item.isspace() == True:
            print("SPACE")
        elif (isinstance(item, str)) == True:
            print(item)
    print()
    print("How's my spelling?")       
            # return item
        
        # return item
        
        # item = text(" ") = "SPACE"
        # print(item)


spell1(text)