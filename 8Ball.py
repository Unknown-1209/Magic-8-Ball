import random

responses = ["Very doubtful.", "Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Without a doubt.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good."]

name = input("What is toue name: ")
question = input("Asks a yes or no question: ")
answer = random.choice(responses)


if len(question) == 0:
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
elif len(name) == 0:
  print(f"Question: {question} \nMagic 8-Ball says: {answer}")
elif len(name) > 0:
  print(f"{name} asks: {question} \nMagic 8-Ball's says: {answer}")
else:
  print(f"{name} asks: {question} \nMagic 8-Ball's says: {answer}")
