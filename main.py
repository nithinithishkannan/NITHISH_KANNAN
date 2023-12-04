from bs4 import BeautifulSoup as bs
import requests
import html5lib

urlt = 'https://results.eci.gov.in/ResultAcGenMay2023/ConstituencywiseS1034.htm?ac=34'
r = requests.get(urlt)
dt = bs(r.text,"html5lib")
d = dt.findAll('tr')
hd = 0
with open("table2.csv","w") as fl:
    for tr in d:
        #print (str(tr))
        if "th" in str(tr) and hd == 0:
            hd = 1
            th = tr.findAll('th')
            th = [i.text for i in th]
            th = ','.join(th)
            print (th)
            fl.write("%s\n"%(th))
        else:
            td = tr.findAll('td')
            td = [i.text for i in td]
            if len(td) != 0:
                td[-1] = str(td[-1]).replace(",", "")
            else:
                continue

            td = ','.join(td)
            print(td)
            fl.write("%s\n" % (td))
            # print ("\n")
