import requests
from parsel import Selector, css2xpath

URL = 'https://europharma.kz/en/nestle-smes-nan-3-optipro-molchnaya-dlya-detey-s-12-mesyatsev-800-g'

r = requests.get(URL)
s = Selector(r.text)

full_links = s.xpath('//a/@href').re(r'^[https].+')
print(full_links, len(full_links))

first_match = s.css('span::text').re_first('[\d]+[\s]?[\d]+')
print(first_match)

for p in s.xpath('//div').xpath('.//p'):  # extracts all <p> inside
    print(p.get())

print('CSS to XPath:', css2xpath('div.container span#main'))
