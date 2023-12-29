x = int(input("enter a number:"))
if x > 0:
  print("positive number")
  if x % 2 == 1:
    print("odd")
  else:
    print("even")
else:
  print("negative number"