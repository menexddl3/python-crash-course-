#List of three people to invite to dinner
names = ['sean', 'mike', 'zabron']
print(f"Hi {names[0].title()} you are invited to dinner!")
print(f"Hi {names[1].title()} you are invited to dinner!")
print(f"Hi {names[2].title()} you are invited to dinner!")

#Change the guest list
print(f"{names[1].title()} can't make it to dinner")
unavailable = 'mike'
names.remove(unavailable)
names.append('lisa')
print(f"Hi {names[2].title()} you are invited to dinner!")

#More guests
print("I'm inviting more guests, found a bigger table")
names.insert(0, 'jake')
names.insert(2, 'fadzai')
names.append('zavier')
print(f"Hi {names[0].title()} you are invited to dinner!")
print(f"Hi {names[1].title()} you are invited to dinner!")
print(f"Hi {names[2].title()} you are invited to dinner!")
print(f"Hi {names[3].title()} you are invited to dinner!")
print(f"Hi {names[4].title()} you are invited to dinner!")
print(f"Hi {names[5].title()} you are invited to dinner!")

#Shrinking guest list
print("I can only invite two people for dinner")
print(f"I'm sorry to say, you are no longer invited {names.pop().title()}")
print(f"I'm sorry to say, you are no longer invited {names.pop().title()}")
print(f"I'm sorry to say, you are no longer invited {names.pop().title()}")
print(f"I'm sorry to say, you are no longer invited {names.pop().title()}")
print(f"{names[0].title()} you are still invited")
print(f"{names[1].title()} you are still invited")

#deleting last two names in the list
print(names)
del names[1], names[0]
print(names)
