import random
word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False

lives = 6
correct_letters = []

########Stages##########

five = """ _______
  |/      
  |      
  |      
  |
  |      
  |
 _|___"""

four=""" ______________
  |/      |
  |      
  |      
  |       
  |      
  |
 _|___"""
 
three=""" ______________
  |/      |
  |      (_)
  |      
  |      
  |
 _|___"""
 
two = """ ______________
  |/      |
  |      (_)
  |      \|/
  |      
  |
 _|___"""
 
one = """ ______________
  |/      |
  |      (_)
  |      \|/
  |       |
  |      
  |
 _|___"""
 
 
zero =""" ______________
  |/      |
  |      (_)
  |      \|/
  |       |
  |      /\
  |
 _|___"""
 
 ############################
while not game_over:
    guess= input("Guess a letter:").lower()
    
    display = ""
    
    for letter in chosen_word:
          if letter == guess:
              display += letter
              correct_letters.append(guess)
          elif letter in correct_letters:
              display += letter
          else:
                display += "-"
    print(display)
    
    if "-" not in  display:
        game_over = True
        print("You win")
  
      
    if guess not in correct_letters:
        lives -=1
        print(f"{lives} lives left")
      
    if lives == 0:
        print(zero)
        print("Game over!")
        break
        
    if lives==5:
        print(five)
    elif lives==4:
          print(four)
    elif lives ==3:
          print(three)
    elif lives ==2:
          print(two)
    elif lives ==1:
          print(one)

