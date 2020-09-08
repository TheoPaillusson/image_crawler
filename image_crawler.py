    # import the modules - OK
import requests, re, os, shutil
from bs4 import *

    # request & access to the site - OK
print('Entrez les mots clefs de votre recherche')
search = input()
request = requests.get('https://www.flickr.com/search/?text=' + str(search))

if request.ok:
    soup = BeautifulSoup(request.content, 'html.parser')
else:
    print('Le site flickr.com ne répond pas')

    # collect datas from the html page - OK
div = str(soup.find_all('div', class_='view photo-list-photo-view requiredToShowOnServer awake'))
staticurl = re.compile(r'url\((.*)\)')

urls = staticurl.findall(div)
urls = ["https:" + s for s in urls] #add correct https before each link

    # ask the numbers of photos - OK
while True:
    try:
        nbimages = int(input('''Combien d'images souhaitez-vous ?'''))
    except ValueError:
        print("Veuillez entrer un nombre")
        continue
    if nbimages <= 0:
        print("Veuillez entrer un nombre supérieur à 0")
    else:
        break

        # dowload the number of photos we want, give them names, and stock them into a brand new folder

os.mkdir(str(search) + ' pictures')
path_source = str(os.getcwd())
path_dest = str(os.getcwd() + '\\' + str(search) + ' pictures')

i = 1

for index, links in enumerate(urls):
    if i <= nbimages:     
        img_data = requests.get(links).content
        with open(str(search) + "_" + str(index+1)+'.jpg', 'wb+') as file:
            file.write(img_data)    
        shutil.move(path_source + '\\' + str(search) + "_" + str(index+1)+'.jpg', path_dest) 
        i += 1
    else:
        break