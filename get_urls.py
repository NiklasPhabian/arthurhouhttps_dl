#!/usr/bin/python3

import requests
import bs4
import re
import datetime
import time
import argparse


class ArthurhouFolder:
    
    def __init__(self, year, month, day, level):
        self.session = requests.Session()
        self.url_trunk = 'https://arthurhouhttps.pps.eosdis.nasa.gov'        
        #self.login()
        self.url = None
        self.html = None
        self.make_url(year, month, day, level)
    
    def login(self, user, pwd):
        auth = requests.auth.HTTPBasicAuth(user, pwd)
        self.session.get(self.url_trunk, auth=auth)
    
    def make_url(self, year, month, day, level):        
        dataset = '/pub/gpmdata/'
        date =  '{year}/{month:02d}/{day:02d}'
        date = date.format(year=year, month=month, day=day)
        level = '/{}/'.format(level)
        self.url = self.url_trunk + dataset + date + level
    
    def download(self, user, pwd):
        downloaded = False
        auth = requests.auth.HTTPBasicAuth(user, pwd)
        while not downloaded:                
            try:
                ret = self.session.get(self.url, auth=auth)                          
            except Exception as e:
                print(e)
                print('download failed, trying again')
                time.sleep(1)                
            if ret.status_code == 200:
                self.html = ret.text   
                downloaded = True
            elif ret.status_code == 401:
                print('Got 401. Wrong user/pwd?')
                break
    
    def extract_granule_links(self, product):
        soup = bs4.BeautifulSoup(self.html, features="lxml")
        term = '{product}*.*.HDF5'.format(product=product)
        files = soup.find_all('a', href=re.compile(term))
        links = []
        for file in files:
            links.append(self.url + file.get('href'))
        return links
    

def get_urls(products, start, stop, user, pwd, level):
    urls = []
    start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
    stop = datetime.datetime.strptime(stop, '%Y-%m-%d').date()
    step = datetime.timedelta(days=1)
    iterator = start  
    while iterator + step <= stop:
        folder = ArthurhouFolder(iterator.year, iterator.month, iterator.day, level)
        folder.download(user=user, pwd=pwd)
        for product in products:
            urls += folder.extract_granule_links(product)
        iterator += step
    return urls    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get URLs from the ArthurHou server')
    parser.add_argument('--products', metavar='products', nargs='+', 
                        type=str, required=True, 
                        help='xcal product (1C.GCOMW1.AMSR2, 1C.NPP.ATMS, 1C.NOAA20.ATMS, 1C.GPM.GMI, 1C.NOAA19.MHS, 1C.METOPB.MHS, 1C.MT1.SAPHIR, 1C.F16.SSMIS, 1C.F17.SSMIS, 1C.F18.SSMIS)')    
    parser.add_argument('--level', metavar='level', required=True, type=str, 
                        help='processing level (e.g. 1A, 1B, 1C)')
    parser.add_argument('--email', metavar='email', required=True, type=str, 
                        help='Email to be used as username and password on arthurhouhttps')    
    parser.add_argument('--start', metavar='start', required=True, type=str, 
                        help='start date (yyyy-mm-dd)')
    parser.add_argument('--stop', metavar='stop', required=True, type=str, 
                        help='stop date (yyyy-mm-dd)')
    parser.add_argument('--out', metavar='out', required=False, type=str, 
                        help='the csv filename to store the links in')
    parser.set_defaults(out='urls.csv')    
    args = parser.parse_args()   
    
    user= args.email
    pwd = args.email
    
    urls = get_urls(args.products, args.start, args.stop, user, pwd, args.level)
    with open(args.out, 'a') as files_log:        
        files_log.writelines("\n".join(urls))
        files_log.write('\n')
