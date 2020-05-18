import requests
from  bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date
urls=["https://in.finance.yahoo.com/quote/GOOGL/","https://in.finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

today=str(date.today())#+".csv"
csv_file=open("scrap"+today+".csv","w")
csv_writer=csv.writer((csv_file))
csv_writer.writerow(['Stock name','Current Price','Previous close','Open','Bid','Ask','Day range','52 week range','Volume','Avg Volume'])
for url in urls:
    stock=[]
    html_page=requests.get(url,headers=headers)
    soup=BeautifulSoup(html_page.content,'lxml')

    #title=soup.find("title").get_text()
    header_info=soup.find_all("div",id="quote-header-info")[0]
    stock_title=header_info.find("h1").get_text()
    stock_amt=header_info.find("div",class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()
    stock.append(stock_title)
    stock.append(stock_amt)
    table_info=soup.find_all("div",class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all('tr')

    for i in range(0,8):
        #heading=table_info[i].find_all("td")[0].get_text()
        value=table_info[i].find_all("td")[1].get_text()
        stock.append(value)
    csv_writer.writerow(stock)
    time.sleep(5)
csv_file.close()

send_mail.send(filename="scrap.csv")