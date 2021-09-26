# # String concatenation can be done via various methods, all of which require a variable
# # Suppose you want a string that says "My favourite football team is ________"
# team = "Newcastle United" # string variable

# # Methods
# print("My favourite football team is " + team)
# print("My favourite football team is {}".format(team))
# print(f"My favourite football team is {team}")

team = input("Football team: ")
currentPlayer = input("Current player: ")
exPlayer = input("Ex Player: ")

madlib = f"My favourite football team is {team}! My favourite current player is {currentPlayer}, my favourite ex player is {exPlayer}"

print(madlib)