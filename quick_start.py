import requests
from parsel import Selector

URL = 'https://europharma.kz/en/nestle-smes-nan-3-optipro-molchnaya-dlya-detey-s-12-mesyatsev-800-g'

r = requests.get(URL)
s = Selector(r.text)

title = s.css('h1::text').get()
print(title)

price = s.xpath('//*[@class="product__price-value"]/text()').get()
print(price)

brand = s.css('.characteristic__list')[1].css('dt::text').get()
print(brand)

data = s.css('dt::text').getall()   # returns a list of all results
print(list(filter(lambda a: not '\n' in a, data)))

# No AttributeError raised unlike in bs4
assert s.xpath('//a[biba="biba-biba"]').get() is None

link1 = s.xpath('//a[@class="product__eclub eclub-price"]/@href').get()
print(link1)

link2 = s.css('a.product__eclub.eclub-price').attrib['href']
print(link2)

assert link1 == link2
