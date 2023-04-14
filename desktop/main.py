import os
import sys

ask = input("Enter math symbol for problem")

if ask == "+":
  numa = input("Enter a number")
  numb = input("Enter another number")
  
  print(numa + numb)
elif ask == "-":
  numc = input("Enter a number")
  numd = input("Enter another number")
  
  print(numc - numd)
elif ask == "*":
  nume = input("Enter a number")
  numf = input("Enter another number")
  
  print(nume * numf)
elif ask == "/":
  numg = input("Enter a number")
  numh = input("Enter another number")
  
  print(numg / numh)
elif ask == "help":
  print("+ for add")
  print("- for subtract")
  print("/ for divide")
  print("* for multiply")
else:
  print("Sorry not a command please type 'help' for help")

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)
