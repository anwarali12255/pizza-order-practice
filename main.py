print("Welcome to Python Pizza Dileveriea!")
size = input('what size pizza do you want? S, M or L ')
add_pepperconi= input("do you want pepperconi? Y or N ")
extra_cheeze= input("do you want extra cheeze? Y or N ")
bill=0
if size=='S':
  bill+=15
  if add_pepperconi=='Y':
    bill+=2
  if extra_cheeze=='Y':
    bill+=1
elif size=='M':
  bill+=20
  if add_pepperconi=='Y':
    bill+=3
  if extra_cheeze=='Y':
    bill+=1
elif size=='L':
  bill+=25
  if add_pepperconi=='Y':
    bill+=3
  if extra_cheeze=='Y':
    bill+=1
print(f'your final bill is ${bill} ')
