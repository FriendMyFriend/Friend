import os
import sys
import time

ans = input("please select a command")

if ans == "calc" or ans == "calculator" :
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
    time.sleep(4)
    restart()
elif ans == "quit" or ans == "exit":
    quit()
elif ans == "help":
    print("calc or calculator = math helper")
    print("quit or exit = quit program")
    print("res or restart = restart program")
    print("help brings you here")
    time.sleep(5)
    # asking to close program 5 seconds later
    ask_close = input("Do you want to close program [Y/N]")
    
    if ask_close == "y" or ask_close == "Y":
      quit()
    elif ask_close == "n" or ask_close == "N":
      # do nothing to change program
    elif ask_close == "restart" or ask_close == "res":
      restart()
    else:
      ask_again_close = input("please select one y or n")
      
      if ask_again_close == "y" or "Y":
        quit()
      elif ask_again_close == "n" or "N":
        # do nothing
      elif aks_again_close == "restart" or "res":
        restart()
      else:
        time.sleep(3)
        quit()
elif ans == "res" or ans == "restart":
    restart()
else:
    print("error please type 'help' for help restarting in 10 seconds")
    time.sleep(10)
    restart()

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)
