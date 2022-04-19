from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

for string in ("Name:", "Favorite Color:"):
    start_indx = html.find(string)
    text_start_indx = start_indx + len(string)

    html_tag = html[text_start_indx:].find("<")
    text_end_indx = text_start_indx + html_tag

    ret = html[text_start_indx:text_end_indx]
    print(ret.strip())
