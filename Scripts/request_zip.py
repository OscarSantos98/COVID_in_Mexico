from bs4 import BeautifulSoup
import requests
import sys
import zipfile

# Web Scrapping
source = requests.get('https://www.gob.mx/salud/documentos/datos-abiertos-152127').text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())
div_article = soup.find('div',class_='article-body bottom-buffer')
downloads = []
for link in div_article.find_all('a', string = 'VER'):
    downloads.append(link['href'])
# first_link = div_article.find_all('a', string = 'VER')[0]['href']
print('These are the download links of the website:')
for download in downloads:
    print(download)
updated_database_link = downloads[0]

# Download
r = requests.get(updated_database_link)
if r.ok:
    print('You have downloaded the database succesfully')
else:
    print('Something went wrong')
    sys.exit()

# Save the zip file
with open('datos_abiertos_covid19.zip','wb') as f:  # write bytes mode
    f.write(r.content)

# Open zip file
with zipfile.ZipFile('datos_abiertos_covid19.zip','r') as data_zip:  # read mode
    print('The following file is within the zip file:')
    print(data_zip.namelist())
    data_zip.extractall('Data')
    print('Data succesfully extracted')