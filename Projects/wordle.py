import random
print(f"Welcome to wordle python!")
# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial, smart"]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        # second letter
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
             # third letter
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
     # fourth letter
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
  # last letter
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
# check if it's 5 letters
if len(guess_word) != 5:
    print(f"That's not a five letter word!")

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
      

print(f"You used {i+1} guesses")        