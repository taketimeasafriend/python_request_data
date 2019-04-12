import requests
import json


# 1-cookie into douban
url = "https://www.douban.com/people/74334545/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
           "Cookie":"here is the Cookie......ll=\"108288\"; bid......"}

response = requests.get(url,headers=headers)
response.encoding = "utf-8"

with open("douban.html","w",encoding="utf-8") as f:
    f.write(response.text)
    print("douban.html finished.")

# 2-json for douban
url2 = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1554807676565"
headers2 = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
           "Referer":"https://m.douban.com/tv/american"}

response = requests.get(url2,headers=headers2)
json_str = json.loads(response.text)
print(json_str)

with open("douban.txt","w",encoding="utf-8") as f2:
    f2.write(json.dumps(json_str,ensure_ascii=False,indent=2))
    print("douban.txt finished.")
