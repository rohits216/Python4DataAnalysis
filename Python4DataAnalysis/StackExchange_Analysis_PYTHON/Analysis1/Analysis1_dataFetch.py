import requests
import json
import os

def crtFold(folder):
    path = folder + '/'
    isExists=os.path.exists(path)
    if(not isExists):
        os.mkdir(path)
    return path
for i in range(1,6):
    key = 'yGwOPEWpcZjxInyceeD7Jg(('
    url = 'http://api.stackexchange.com/2.2/questions?key={}&page={}&pagesize=100\
    &fromdate=1472688000&todate=1475193600&order=desc&sort=creation&tagged=python%3Bpandas&site=stackoverflow'.format(key,i)
    r = requests.get(url)
    with open(crtFold('data') + 'dataFetch{}.json'.format(i), 'w') as f:
        f.write(json.dumps(r.json(),indent = 4))