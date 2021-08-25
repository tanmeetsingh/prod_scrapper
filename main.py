import requests
from bs4 import BeautifulSoup
import sys
import requests
from utilities import *


sys.stdin=open("links.txt","r")
sys.stdout=open("results.txt","w",encoding="utf-8")


def Execute():
    try:
        while True:
            P={}
            url=input()
            if url=="":
                break
            r=requests.get(url)
            soup=BeautifulSoup(r.content,"html5lib")
            try:
                P['Name']=Name_and_Brand(soup)
                P['Price']=Current_price(soup)
                P['Highlights']=Specifications(soup)
                P['Image']=Image_links(soup)
                P['Details']=Full_Specifications(soup)
                P['Category']=Get_Category(soup)
                P['Rating']=Rating(soup)
                try:
                    P['Store']=Get_stores(soup)
                except:
                    P['Store']=[]
            except:
                continue
            print(P['Name'])
            print(P['Price'])
            print(P['Highlights'])
            print(P['Image'])
            print(P['Details'])
            print(P['Rating'])
            for store in P['Store']:
                store.show_store()
            print('-'*200)

    except EOFError:
        print("Successfully executed !!")


Execute()