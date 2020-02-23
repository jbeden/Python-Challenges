

for i in range(100):
  x = i + 1
  if(x % 3 == 0 or x % 5 == 0):
    if(x % 3 == 0):
      print("Fizz", end="")
    if(x % 5 == 0):
      print("Buzz", end="")
    print()
  else:
    print(x)
