from re import search,IGNORECASE
import requests
from json import loads
import concurrent.futures
#so sad,hackerrank can't use aiohttp/pycurl

def getMovies(year, query):
    url = f'https://jsonmock.hackerrank.com/api/movies?Year={year}&page=1'
    a = requests.get(url)
    q = query.replace('*','.*')
    total = loads(a.text)['total']+1
    urlList = [f'{url[:-1]}{x}' for x in range(1,total)]
    def load_url(url, timeout):
        return requests.get(url, timeout = timeout)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        future_to_url = {executor.submit(load_url, url, 10): url for url in urlList}
        res = []
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            data = future.result()
            for k in loads(data.text)['data']:
                if search(rf'^{q}$',k['Title'],IGNORECASE):
                    res.append([url[url.find('page=')+5:],k['imdbID'],k['Title']])
        return [i[1:] for i in sorted(res, key=lambda x:int(x[0]))]
