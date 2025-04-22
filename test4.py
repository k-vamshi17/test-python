def simpleArraySum(n):
  k=[]
  z=0
  for i in n:
    k.append(int(i))
  for i in k:
    z+=i
  print(z)
n=input("Enter Values:").split()
simpleArraySum(n)