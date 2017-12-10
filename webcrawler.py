from bs4 import BeautifulSoup
import urllib.request
import csv
import queue
file = open('C://Users//vikas yadav//Desktop//crawler.csv',"a" ,newline='')
writer = csv.writer(file ,delimiter=" ");

url = urllib.request.urlopen("http://facebook.com")
data = url.read();
soup = BeautifulSoup(data,"html.parser");
anchor = soup.findAll('a');

"""for adata in anchor:
 print (adata);
"""

print ();
q= queue.Queue();

for adata in anchor:
 #print (adata['href']);
 q.put(adata);
 #writer.writerow(adata['href']); 
file.close(); 
#print (anchor);

while  not q.empty() :
 print (q.get())
