import os
import requests

def boilerplate_answer():
  user_answer = str(input("Do you want to start over? y/n")).lower()
  if user_answer == "y" or user_answer == "n":
    if user_answer == "y":
      google_url()
    elif user_answer == "n":
      print("k, bye!")
      return
  else : 
    print("That's not a vaild answer.")
    boilerplate_answer()

def google_url():
  os.system('clear')
  print("Welcome to IsitDown.py!\nPlease write a URL or URLs you want to check. (seperated by comma)")

  user_write = str(input()).lower().split(",")
  for url in user_write:
    url = url.strip()
    if "." not in url:
      print(f"{url} is not a valid URL")
    else:
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(f"{url} is up!")
        else:
          print(f"{url} is down!")
      except:
        print(f"{url} is down!")
  boilerplate_answer()
  
google_url()