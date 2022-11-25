from crawler import DynamicRequest
from crawler.parser import *
from pprint import pprint
import time
start = time.process_time()

url_list = {
        '2022': {
            'url': 'https://www.namechart.kr/chart/2022',
            'parser': 'namechart_parser_greedy'
            }
        }

request = DynamicRequest()

for key in url_list.keys():
    info = url_list[key]

    url = info['url']
    callback = eval(info['parser'])

    data = request.get(url, callback=callback)

print("No. Loaded: ", len(data))
pprint(data[0])

elapsed = time.process_time() - start
print("Elapsed time: " + time.strftime("%H:%M:%S.{}".format(str(elapsed % 1)[2:])[:12], time.gmtime(elapsed)))
