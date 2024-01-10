print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
comboName = name1 + name2
lowername = comboName.lower()
L = lowername.count("l")
O = lowername.count("o")
V = lowername.count("v")
E = lowername.count("e")
Love_score = L + O + V + E

T = lowername.count("t")
R = lowername.count("r")
U = lowername.count("u")
E = lowername.count("e")
True_score = T + R + U + E

Score = int(str(True_score) + str(Love_score))
if Score < 10 or Score > 90:
  print(f"Your score is {Score}, you go together like coke and mentos.")
elif 40 < Score < 50:
  print(f"Your score is {Score}, you are alright together.")
else: 
  print(f"Your score is {Score}.")
