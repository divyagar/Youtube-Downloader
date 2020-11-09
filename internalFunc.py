from urllib import request
import re
res = request.urlopen('https://www.youtube.com/results?search_query=naach-meri-rani')
pattern = re.compile(r'\"videoId\":\"(.){11}\"')
search_results = pattern.finditer(str(res.read()))
for result in search_results:
    string = result.group()[11:-1]
    print("https://www.youtube.com/watch?v={}".format(string))