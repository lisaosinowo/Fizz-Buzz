for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0: # The number divisible by both 3 and 5 needs to be checked first. If the number isn't divisible by both 3 and 5 then the next elif statements are checked
      print("FizzBuzz")
    elif n % 5 == 0:
       print("Buzz")
    elif n % 3 == 0:
      print("Fizz")
    else:
      print(n)
