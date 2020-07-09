# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
  print("Hi! Welcome to the applying to college checklist chatbot.")


# Choose a response based on the user's input.
def process_input(answer):
  # Define a list of possible ways the user might say hello.
  greetings = ["hi", "hello", "hey", "hey there", "sup"]

  # Define a list of possible ways the user might say bye.
  farewells = ["bye", "see ya", "goodbye", "quit", "exit"]

  if is_valid_input(answer, farewells):
    say_goodbye()
    return True # The user wants to exit!
  elif is_valid_input(answer, greetings):
    say_greeting()
  else:
    say_default()
  return False # The chatbot will continue asking for user input.


# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

# Display a farewell message to the user.
def say_goodbye():
  print("Bye! Good luck!")


# Display a default message to the user.
def say_default():
  print("Sorry, I don't understand what you mean! Try again?")


# Check if user_input matches one of the elements
#  in valid_responses.
def is_valid_input(user_input, valid_responses):
  for item in valid_responses:
    if user_input == item:
      # If you find a matching response, the input is
      #  valid for this kind of response.
      return True
  # If you didn't find a matching response, after
  #  going through the entire list, the input
  #  isn't valid for this kind of response.
  return False


# a function to answer a quick yes/no response
def yes_no(answer, answer_yes, answer_no):
  if answer == 'yes':
    print(answer_yes)
  elif answer == 'no':
    print(answer_no)
  else:
    say_default()
    answer = input("")
    yes_no(answer, answer_yes, answer_no)
    

# the junior set of questions
def junior():
  print ("Now’s the time to start exploring and deep diving into your interests! Keep an open mind and explore things that catch your eye. You don’t need to have it all figured out yet!")
  print('\n')
  answer = input("What are you interested in? (Type 'not sure' if you don't know yet.) ")
  if (answer == "not sure"):
    print ("That's okay! Get involved in your friends' clubs or explore interesting career paths online. Find mentors or people you look up to for advice on their interests!") 
  else:
    print ("That's great to hear! Try deep diving into a topic, conducting your own research, or getting involved in the things you are interested in. You're never too young to start!")
  print('\n')
  answer = input("Have you taken your SAT/ACTs yet and do you like your scores? ")
  yes_no(answer, "Amazing! You're ahead of the game on this one.", "Now is a great time to double down on studying. Spend a little bit of time every day for a couple months and the test will be a piece of cake.")
  print('\n')
  answer = input("That's about it! Would you like more info? ")
  yes_no(answer, "Some more things to think about: AP/IB tests, forming good relationships with your teachers, and reading A LOT!", "Alright, don't forget to enjoy your junior year!")

# the senior set of questions
def senior():
  print ("You’re super close! Let’s make sure you have everything you need in order to apply this fall.")
  print('\n')
  answer = input("Have you taken your SAT/ACTs yet and do you like your scores? ")
  yes_no(answer, "Amazing! You're all set in this department.", "Make sure you have a plan to take your tests before Early Action (usually October or November) and Regular Decision (usually December or January).")
  print('\n')
  answer = input("Rate how hard you feel your senior year courses will be out of 10. ")
  if 10 >= float(answer) > 5:
    print("That sounds perfect! Colleges like to see you challenging yourself. Make sure you still have time to enjoy your senior year, though.")
  elif 5 >= float(answer) > 0:
    print("Hmm...depending on the circumstances, I would take a couple harder but fun courses, if possible! It all depends on what is best for you, though.")
  print('\n')
  answer = input("Do you have some colleges in mind? ")
  yes_no(answer, "Yay! Make sure you have a healthy list of sure-fire safeties, safeties, matches, and reaches to apply to.", "Time to start researching colleges! Have a healthy mix of safeties, matches, and reaches but make sure you love ALL of them.")
  print('\n')
  answer = input("Have you started your application essays yet?")
  yes_no(answer, "Fabulous! Good luck on those essays, and don't forget about supplements.", "No worries! I would suggest starting on them at least a couple months before you have to apply.")
  print('\n')
  answer = input("On a scale of 1 to 10, how are you feeling so far? 1 = really stressed, 10 = overall positive ")
  if 10 >= float(answer) >= 7:
    print("Glad to hear you're doing well!")
  elif 7 > float(answer) > 3:
    print("This is a natural response. This is a super stressful time for seniors everywhere! It helps to find a community of people who can support you right now.")
  elif 3 >= float(answer) >= 0:
    print("Sorry you're feeling that way 😢 this is a super difficult time for a lot of people. Reach out to someone who can support you, like a counselor or parent.")
  else:
    say_default()
  print('\n')
  print("Thank you for interacting with this chatbot. Some final thoughts: don't forget to enjoy your senior year and form positive, lasting habits!")
  print('\n')
  print("Press enter to exit.")


# --- Put your main program below! ---
def main():
  done = False # Use this to keep track of when the user wants to exit.
  while not done:
    answer = input('Will you be a junior or senior this fall?')
    if answer == 'junior':
      junior()
      print('\n')
      answer = input('Press enter to exit.')
      done = True
    elif answer == 'senior':
      senior()
      print('\n')
      answer = input('Press enter to exit.')
      done = True
    else:
      say_default()


# DON'T TOUCH! Setup code that runs your main() function.
intro()
if __name__ == "__main__":
  main()