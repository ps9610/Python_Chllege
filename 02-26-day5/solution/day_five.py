import os
import requests
from bs4 import BeautifulSoup

os.system("clear")


url = "https://www.iban.com/currency-codes"


countries = []
#1.requset, soup 설정
#2. 해당 url에서 table태그 찾아 변수 table로 저장, 
    # 나라 이름, 숫자, 화폐단위 들어있는 tr 태그 찾아 rows로 저장
#3. for문을 이용하여 tr들을 하나씩 나열하고
    # td 찾아서 items라는 변수로 저장
    # items 첫번째 = 국가 이름
    # items 세번째 = 화폐
#4. if문 이용하여 
  # 

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"You chose {country['name']}\nThe currency code is {country['code']}")
  except ValueError:
    print("That wasn't a number.")
    ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()

