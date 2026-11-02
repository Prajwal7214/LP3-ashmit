def fibonacci(n):
  if(n <= 1):
    return n;
  return fibonacci(n-1) + fibonacci(n-2)

a = int(input("Enter the number of terms : "))
if(a < 0):
  print("Enter a valid positive number !")
else:
  print("fibonacci sequence is : ")
  for i in range(a):
    print(fibonacci(i))
