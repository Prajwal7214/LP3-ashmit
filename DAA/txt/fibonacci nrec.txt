n = int(input("Enter the number of terms : "))
if(n <= 0):
  print("Enter a valid positive number !")
else:
  a,b = 0,1
  print("Fibonacci Sequence is : ")
  for i in range(n):
    print(a);
    a,b = b,a+b
