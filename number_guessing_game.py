import random
print('Guess the number')
p=random.randint(0,100)
#print(p)
def check(c):
    print(f"you have {c} chances to guess the number")
    for i in range(c):
      try:
        q=int(input("make a guess: "))
      except ValueError:
        print('enter valid input')
        print(f"you have {c-i-1} chances left")
        continue
      if p<q:
        print('your guess is too high')
        print(f"you have {c-i-1} chances left")
      elif p>q:
        print('your guess is too low')
        print(f"you have {c-i-1} chances left")
      elif p==q:
        print(f"Your guess is correct.you won..")
        break

a=input('choose the difficulty level....easy or hard: ')
if a.lower()=='easy':
  c=10
  check(c)
if a.lower()=='hard':
  c=5
  check(c)
print(f"The number is {p}")

