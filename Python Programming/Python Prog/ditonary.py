number = input("Number: ")
formattedString = {
    "1": "one",
    "2": "Two",
    "3": "Three"
}
emptySt = ""
for item in number:
    emptySt += formattedString.get(item, "") + " "
print(emptySt)
