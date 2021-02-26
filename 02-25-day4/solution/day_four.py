import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower() 
  #lower: 유저가 대문자로 써도 소문자로 바꿔줌
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return #여기서 끝내버린다.
    elif answer == "y":
      main() # main함수를 실행한다.
  else: # y나 n이 아닌 알파벳을 쓴다면
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")

  urls = str(input()).lower().split(",") # split(",") = ,를 기준으로 나눔
  # urls는 input에 입력된 문자들인데 소문자로 변환시키고 콤마를 기준으로 하나씩 나뉨
  for url in urls: 
  # url이 하나씩 보이게 하기 위해서 for문 사용함
    url = url.strip() 
    # url의 양쪽 공백 지워주기(혹시 콘솔창에 여러개의 url 입력 시 띄어쓰기를 할 수도 있으니까)
    if "." not in url: 
    #url에 .이 없다면(인터넷 주소는 무조건 .이 들어가니까)
      print(url, "is not a valid URL.")
    else: 
    #url에 .이 있다 그리고
      if "http" not in url: 
      #url에 http라는 문구가 없다면
        url = f"http://{url}"
        # url에 http를 써준다
      try: 
      #예외처리(try, except문) = try except절 -> 에러 발생시 무조건 except절 실행
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else: # (if랑 이어짐) 에러가 발생하지 않고, request.status_code != 200일 때
          print(url, "is down!")
      except: #except -> 에러가 발생했을때 print(url, "is down!")
          print(url, "is down!")
  restart()

main()