from bs4 import BeautifulSoup
import requests
import re

resp = requests.get('https://wikipedia.org/')
html = resp.text

a = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
print(a)

soup = BeautifulSoup(html, 'lxml')
tags = soup('a', 'other-project-link')
#print(tags)

print([tag['href'] for tag in tags])


html = """<!DOCTYPE html>
<html lang="en">
    <head>
        <title>test page</title>
    </head>
    <body class="mybody" id="js-body">
        <p class="text odd"> first <b>bold</b> paragraph</p>
        <p class="text even"> second <a href="https://mail.ru">link</a></p>
        <p class="text odd"> third <a id="paragraph"><b>bold link</b></a></p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
# всякие поиски по html
print(soup.prettify())

print(soup.p.b.string)
print(soup.p['class'])
print(soup.p.b.parent)
print([tag.name for tag in soup.p.b.parents])
print(soup.p.contents)

print(soup.p.b.find_parent(id="js-body").name)
print(soup.p.b.find_parent("body")['id'])
print(soup.p.find_next_sibling(class_='odd'))
print(soup.p.find_next_siblings())
print(soup.p.find('b'))
print(soup.find(id='js-body')['class'])
print(soup.find_all(name='p', class_='text odd')) # в параметрах важен порядок слов
print(soup.select('p.text.odd')) # css селектор - чтобы порядок слов не влиял
print(soup.select('p:nth-of-type(3)'))
print(soup.select('a > b'))

# +регулярки
print([i.name for i in soup.find_all(name=re.compile('^b'))])
print([i for i in soup(['a', 'b'])])

# можно менять сам html
tag = soup.b

tag.name = 'i'
tag['id'] = 'myid'
tag.string = 'italic'
print(soup.p)

# Распарсим странцу новостей мейла
results = requests.get('https://news.mail.ru/')
html = results.text
soup = BeautifulSoup(html, 'lxml')


a = [
    (section.string,
     [
         link.string for link in section.find_parents()[4].find_all('span', 'link__text')
     ]
     ) for section in soup.find_all(name='span', class_='hdr__inner')
]
print(a)