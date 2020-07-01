import re
import urllib.request


class Result(object):
    def __init__(self, name, price, extra, link):
        self.name = name
        self.price = price
        self.extra = extra
        self.link = link


def get_WebPage(dest):
    return urllib.request.urlopen(dest).read().decode('utf-8')


def get_List(content):
    results = []
    for result in re.findall('a href="(/appartamento/affitto/[^"]*)', content):
        link = "https://www.casa.it"+result
        html = get_WebPage(link)
        try:
            Price = int(re.search('pinfo-price[^€]*€ ([0-9]+\.*[0-9]*)', html).groups()[0].strip().replace(".", ""))
        except Exception:
            Price = 0
        try:
            Extra = int(re.search('Spese condominiali<!--[^€]*€([^/]*)', html).groups()[0].strip())
        except Exception:
            Extra = 0
        results.append(Result("lol", Price, Extra, link))
    return results


if __name__ == "__main__":
    Link = input("Insert Link: ")
    #Type = (re.search('\?tr=([^&]*)', Link)).groups()[0]
    #Zone = (re.search('&geopolygon=({.*})', Link)).groups()[0]

    Results = (get_List(get_WebPage(Link)))
    for result in Results:
        print((result.price)+(result.extra))
        print(result.link)
    # get user search link
    # get list of homes
    # ask for user filters
    # sort homes
    # output an exel
