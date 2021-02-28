import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://www.iban.com/currency-codes" 



request = requests.get(url)
c_soup = BeautifulSoup(c_url.text, "html.parser")

def main():
  print("Hello! Please choose select a country by number:")
  country_num = c_soup.find("table", {"class":"table"})
  c_num = country_num.select("td:nth-child(4n)")
  c_name = country_num.select("td:nth-child(4n-3)")
  c_cur = country_num.select("td:nth-child(4n-1)")
  print(c_num.sorted(c_num))
  #u_num = int(input())

  #for number in c_num:
  #  countries.append(c_num.string)
    #if type(u_num) is not int:
    #  print("That wasn't a number")
main()