"""
This is the submission of Jodie Mullins for the Code in Place final project.

Primary Skills Used:
Print
If, Else, and Elif statements
Nesting statements
Random libary
Lists
User Input & Output
For Loop
i and range 
"""
import random

print("Inspiration Inc.")
print("Enjoy some kind energies your way today!")

strength_quotes = ["Strength does not come from physical capacity. It comes from an indomitable will. -Mahatma Gandhi", "A single twig breaks, but the bundle of twigs is strong. -Tecumseh", "You have power over your mind-not outside events. Realize this, and you will find strength. -Marcus Aurelius", "My strength is as the strength of ten, because my heart is pure. -Alfred Lord Tennyson"]

humor_quotes = ["A well-developed sense of humor is the pole that adds balance to your steps as you walk the tightrope of life. -William Arthur Ward", "A sense of humor is a major defense against minor troubles. -Mignon McLaughlin", "We are all here on earth to help others; what on earth the others are here for I don't know. -W. H. Auden"]

courage_quotes = ["The secret to happiness is freedom... And the secret to freedom is courage. -Thucydides", "Only those who will risk going too far can possibly find out how far one can go. -T. S. Eliot", "Courage is the most important of all the virtues, because without courage you can't practice any other virtue consistently. You can practice any virtue erratically, but nothing consistently without courage. -Maya Angelou", "The opposite of courage in our society is not cowardice, it is conformity. -Rollo May", "Boldness be my friend. -William Shakespeare"]

business_quotes = ["It's easy to make a buck. It's a lot tougher to make a difference. -Tom Brokaw", "A business that makes nothing but money is a poor business. -Henry Ford", "Just because something doesn't do what you planned it to do doesn't mean it's useless. -Thomas A. Edison", "Failure doesn't mean you are a failure it just means you haven't succeeded yet.-Robert H. Schuller"]

science_quotes = ["Scientific research is one of the most exciting and rewarding of occupations. -Frederick Sanger", "Research is what I'm doing when I don't know what I'm doing. -Wernher von Braun", "We can't solve problems by using the same kind of thinking we used when we created them. -Albert Einstein", "Science may have found a cure for most evils; but it has found no remedy for the worst of them all - the apathy of human beings. -Helen Keller"]

print("") #space
print("") #space
print("") #space

print("SECURE LOG-IN PAGE ")
print("+++++++++++++++++++++++++++++")
print("") #space
print("") #space
username = input("USERNAME > ")
password = input("PASSWORD > ")


print("")
print("")
print("")



if username == "Karel_Robot" and password == "R0b01!":
  print("Welcome, Karel!")
  print("")
  print("")
  print("")
  print("Glad your human could read the Captcha today!") 
  print("") #space
  print("") #space
  print("") #space
elif username == "CIP" and password == "Cod3inPlace":
  print("Welcome, wonderful volunteers of knowledge and wisdom!")
  print("")
  print("")  
  print("")
  print("You're doing great work!")
  print("") #space
  print("") #space
  print("") #space

elif username == "JoMuffins" and password == "Mull!n$":
  print("Welcome, Jodie")
  print("")
  print("")
  print("")
  print("Another day of coding, eh?")
  print("") #space
  print("") #space
  print("") #space
else:
  print("Welcome", username, "\b! May the days be kind to you!")
  print("") #space
  print("") #space
  
print("Let's take a moment to take some deep breaths and calm our nervous system a bit, shall we?")
# this will print a list of 1-10 so the user can take a moment to count breaths.
count = 10
for i in range(count):
  print(1 + i)  

print("") #space
print("") #space
print("") #space
print("") #space


name_input = input("What's your preferred name? ")
print("") #space
print("Welcome,", name_input,"\b! We are very thankful you've joined us for this time to supply you with a vote of confidence.")

print("") #space
print("") #space

print("Strength, Humor, Courage, Business, Science") 

user_goal = input("From the given list, what kind of inspiration are you looking for? ")

print("") #space
print("") #space
print("") #space
print("") #space
print("") #space
print("") #space

if user_goal == "Strength" or user_goal == "strength":
  """
  By including the "or" combinator in each exclusive if statement, I've allowed the program to be less case-sensitive for the user.
  
  Nested within this if statement, a random operator is used below to select a random quote from the the lists above, with a preference for a specific list as indicated by the user's input. A single quote will then display for the user.
  
  Both of these statements continue in trend below until the else statement.
  """

  print(random.choice(strength_quotes))
  print("") #space
  print("") #space

elif user_goal == "humor" or user_goal == "Humor":
  print(random.choice(humor_quotes))
  print("") #space
  print("") #space

elif user_goal == "Courage" or user_goal == "courage":
  print(random.choice(courage_quotes))
  print("") #space
  print("") #space

elif user_goal == "business" or user_goal == "Business":
  print(random.choice(business_quotes))
  print("") #space
  print("") #space


elif user_goal == "science" or user_goal == "Science":
  print(random.choice(science_quotes))
  print("") #space
  print("") #space


else:   #if the user does not put in any valid topic from the lists, this quote will still display for them
  print("Experience has shown, and a true philosophy will always show, that a vast, perhaps the larger portion of the truth arises from the seemingly irrelevant. -Edgar Allan Poe")
  print("") #space
  print("") #space
  print("") #space