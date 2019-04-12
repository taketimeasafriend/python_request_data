import requests

url = "http://maintao.com/2019/meet-my-sisters"

url2 = "http://51world.win/the_old_man_and_the_sea/about_author.html"

response = requests.get(url)

response.encoding = "utf-8"
# print(response.text)
# print(response.content.decode())

with open("maintao.html", "w", encoding="utf-8") as f:
    f.write(response.text)
    print("finished.")
