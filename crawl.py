from crawler import DynamicRequest
from crawler.parser import namechart_parser
from pprint import pprint

url_list = {
        '2022': {
            'url': 'https://www.namechart.kr/chart/2022',
            'parser': 'namechart_parser'
            }
        }

request = DynamicRequest()

for key in url_list.keys():
    info = url_list[key]

    url = info['url']
    callback = eval(info['parser'])

    data = request.get(url, callback=callback)

    pprint(data)

