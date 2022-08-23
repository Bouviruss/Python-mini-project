from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={gpu}&n=8000"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

