#!/usr/local/bin/python3
import numpy as np
import pandas as pd
import os
import shutil
import time
from urllib.request import urlretrieve
from urllib.request import urlopen,Request
import xml.etree.ElementTree as ET


def get_news(stock_ticker):
    try:
        shutil.rmtree("news/")
    except:
        pass
    os.makedirs("news/")
    urlretrieve("http://finance.yahoo.com/rss/headline?s="+str(stock_ticker).lower(),"news/"+str(stock_ticker).lower()+".xml")
    root=ET.parse("news/"+str(stock_ticker).lower()+".xml").getroot()
    print("\nRECENT NEWS FOR "+ str(stock_ticker))
    iterable=root.iter("item")
    print("--"*30)
    count=-1
    content=[]
    for i in iterable:
        count+=1
        content.append(i[0].text)
        print("["+str(count)+"] "+i[4].text)
    print("\nREAD NEWS? (y/n):")
    decision=input()
    while(decision!="n"):
        if decision=="y":
            print("INSERT NEWS N°:",end=" ")
            num=int(input())
            print(content[num])
        print("\nREAD NEWS? (y/n):",end=" ")
        decision=input()


print("\n*** FINANCIAL NEWS READER - YAHOO RSS ***")
print("Insert stock ticker: ",end='')
tick=str(input())
get_news(tick)
