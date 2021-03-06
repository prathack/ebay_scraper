import urllib.request as urllib
import time
import lxml
import csv
from bs4 import BeautifulSoup as b
def enterProduct(name):
    splitted = name.split()
    mainProduct = '+'.join(splitted)
    return mainProduct
def totalPages(pages):
    if pages < 200:
        return pages
def startCrawl():
    search_string = enterProduct(name)
    r = totalPages(pages)
    with open(str(filename)+'.csv', 'w',encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1,r+1):
            print("*******************Titles and Prices On Page: "+str(i)+"************************")
            try:
                url="http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw="+str(search_string)+"&_pgn="+str(i)+"&_skc=100&rt=nc"
                html = b(urllib.urlopen(url).read(),"lxml")
                titles = html.findAll('a',{'class':'vip'})
                prices = html.findAll('span',{'class':'bold'})
                for (i,j) in zip(titles,prices):
                    title,price = i.text,j.text[1:]
                    writer.writerow({'Title':title, 'Price':price})
            except:
                pass
            
def info():
    print("""
              E-BAY TITLE AND PRICES SCRAPER(V1.0) BY PRATHAP
              FACEBOOK : FB.COM/PRATHACK
              TWITTER  : TWITTER.COM/PRATHACK
              GITHUB   : GITHUB.COM/PRATHACK
              WEBSITE  : PYTHONGUI.COM

                USSAGE : 1.Run the code on python 3 IDLE.
                         2.Enter the product name
                         3.Enter how many pages to scrape 
    """)
info()
try:
    name = input("Enter the Product Name: ")
    pages = int(input("Enter How many pages to be scraped ( less than 200): "))
    filename = input("Please, Name Your Output CSV File(without .csv): ")
    enterProduct(name)
    totalPages(pages)
    startCrawl()
except:
    print("Please give the details properly !!!")
