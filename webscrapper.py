import bs4
import urllib.request
url='websitelink here'
sauce = urllib.request.urlopen(url).read()

soup = bs4.BeautifulSoup(sauce,"html.parser")



print(soup.prettify())
