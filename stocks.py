import requests
from bs4 import BeautifulSoup

r = requests.get('http://money.rediff.com/index.html')
data=r.text
soup = BeautifulSoup(data)

html1=soup.find_all('div',id='sensTab1')
#print html1[0]
html2=soup.find_all('div',id='sensTab2')
#print html2
html3=soup.find_all('div',id='div_bse_gainer')
html4=soup.find_all('div',id='div_nse_gainer')
html5=soup.find_all('div',id='div_bse_looser')
html6=soup.find_all('div',id='div_nse_gainer')
table4=html6[0].text
print (table4)
table3=html5[0].text
print (table3)
table2=html4[0].text
print (table2)
table1=html3[0].text
print (table1)
bse=html1[0].text
print (bse)
nse=html2[0].text
print (nse)
'''
html=soup.find_all('div',id='leftcontainer')
print html[0].text
'''
name_tag = soup.find_all('h2')[0].get_text()
value=soup.find_all('span', class_='black')[0].get_text()
figure=soup.find_all('span', class_='red')[0].get_text()

#print name_tag
#print value
#print figure
####
