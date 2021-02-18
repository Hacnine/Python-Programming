message = input(">")
splitMessage = message.split(" ")
emoijis = {
    ":)": "😊",
    ":(": "😒"
}
holderString = ""
for word in splitMessage:
    holderString += emoijis.get(word, word) + " "
print(holderString)
