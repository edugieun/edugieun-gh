import requests
# from bs4 import BeautifulSoup
# from bs4 import SoupStrainer

req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
raw = req.text
raw = str(raw)
start = 0
end = 0
for i in range(len(raw)):
    if raw[i] == '<' and raw[i+1] == 't' and raw[i+2] == 'a' and raw[i+3] == 'b' and raw[i+4] == 'l' and raw[i+5] == 'e':
        start = i
    if raw[i] == '<' and raw[i+1] == '/' and raw[i+2] == 't' and raw[i+3] == 'a' and raw[i+4] == 'b' and raw[i+5] == 'l':
        end = i + 8
        break
table_ele = raw[start:end]
print(table_ele)

# req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
# raw = req.text
# html_source = BeautifulSoup(raw, 'html.parser')
# codes = html_source.select('table.highlight.tab-size.js-file-line-container')
# codes = codes[0]
# print(codes)
# codes = str(codes)

# # print(codes[0])

# # html_source = bs.find('table')


# # codes = codes[0]
# # codes = BeautifulSoup(codes)
# # print(codes)

# # import requests
# from xml.dom import minidom

# # req = requests.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
# # raw = req.text
# a = '<a>awda</a>'
# a = codes
# # print(a)
# xmlraw = minidom.parseString(a)
# td_list = xmlraw.getElementsByTagName('table') 
# print(td_list[0].toxml())

# # import urllib.request
# # from urllib.parse import urlparse

# # a = urllib.request.urlopen("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py/")
# # print(a.read().decode("utf-8"))
