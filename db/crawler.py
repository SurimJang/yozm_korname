### Requirements
## General
import json
import urllib.request as req
import math
import numpy as np
import pandas as pd
from tqdm import tqdm
#ADD: DB


### Functions

#TODO: def checker - Update data when the difference between the latest data and the present is more than one month

def collector(year='2022', gender='t', page='1'):
    """
    #TODO: year - add option (all, latest)
    #TODO: gender - add option (m, f)
    #TODO: page - add option (max)
    #TODO: Checking the data type   
    """

    def get_url(year, gender, page):
        url = "https://www.namechart.kr/_next/data/b8p-f0HrtjgJNesctd7KD/ko/chart/{y}.json?"
        if year != None:
            url = url + "year={y}".format(y=year)
        if gender == 't':
            pass
        else:
            url = url + "&gender={g}".format(g=gender)
        if page != None:
            url = url + "&page={p}".format(p=page)
        return url  

    def page_num():
        url = get_url(year, gender, page='1')
        url_open = req.urlopen(url)
        url_res = json.load(url_open)
        tot = url_res['pageProps']['data']['total']
        pnum = math.ceil(tot/50)
        return pnum

    def crawling_df(url):
        url_open = req.urlopen(url)
        url_res = json.load(url_open)
        df = pd.DataFrame.from_records(url_res['pageProps']['data']['items'])
        df['year'] = url_res['pageProps']['data']['year']
        return df[['year', 'ranking', 'name', 'total', 'male', 'female']]

    if page == 'max':
        pnum = page_num()
        urls = []
        dfs = []
        print(">> 따끈따끈한 요즘 이름 모으는 중...")
        for p in tqdm(range(1, pnum+1)):
            url = get_url(year, gender, page=p)
            df = crawling_df(url)
            urls.append(url)
            dfs.append(df)
        print(">> 총 {} pages 가져오기 성공!".format(pnum))
    return dfs


