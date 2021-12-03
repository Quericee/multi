from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures
import urllib.request
import time

#links = open('res.txt', encoding='utf8').read().split('\n')


def load_url(url, timeout):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)


start_time = time.time()
# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     future_to_url = {executor.submit(load_url, url, 60): url for url in links}
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#         except Exception as exc:
#             print('%r generated an exception: %s' % (url, exc))
#         else:
#             print(1)
#             #print('%r page is %d bytes' % (url, len(data)))
links = open('res.txt', encoding='utf8').read().split('\n')

for url in links:
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)
print("--- %s seconds ---" % (time.time() - start_time))
