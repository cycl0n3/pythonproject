import bs4


exampleFile = open('data/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html5lib")

elems = exampleSoup.select('#author')

print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print('-'*20)

pElems = exampleSoup.select('p')

print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
