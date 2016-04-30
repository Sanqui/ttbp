#!/usr/bin/python

#import core

import os

PATH = os.path.join("/home", "endorphant", "projects", "ttbp", "bin")
WWW = os.path.join(PATH, "..","www")
CONFIG = os.path.join(PATH, "config")
DATA = os.path.join(PATH, "..", "data")

BANNER = open(os.path.join(CONFIG, "banner.txt")).read()
CLOSER = "\n\tsee you later, space cowboy..."
SPACER = "\n\n\n\n"

def start():
  print(BANNER)
  print(SPACER)

  print(check_init())

  try:
    print(main_menu())
  except ValueError or SyntaxError:
    print("\n\noh no i didn't understand that")
    print(main_menu())
  except KeyboardInterrupt:
    print("\n\neject button fired")
    print(main_menu())

def stop():
  return CLOSER

def check_init():
  if os.path.exists(os.path.join(os.path.expanduser("~"),".ttbp")):
    return "welcome back, friend"
  else:
    return init()

def init():
  print(SPACER)
  return "i don't recognize you, stranger. let's make friends."

def main_menu():
  print(SPACER)

  print("how are you feeling today? ")

  ans = raw_input("your feels (enter 'none' to quit): ")

  if ans == "none":
    return stop()
  else:
    return main_menu()

#####

start()