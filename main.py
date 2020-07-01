import re
import urllib.request

#declared object Result, an item of the list that will ultimatelly be shown to the user or exported to excel
class Result(object):
    def __init__(self, name, price, extra, link):
        self.name = name
        self.price = price
        self.extra = extra
        self.link = link

#get webpage as string
def get_WebPage(dest):
    return urllib.request.urlopen(dest).read().decode('utf-8')

#this is where the magic happens
def get_List(content):
    results = []
    for result in re.findall('a href="(/appartamento/affitto/[^"]*)', content):
        link = "https://www.casa.it"+result
        html = get_WebPage(link)
        try:
            Price = int(re.search('pinfo-price[^€]*€ ([0-9]+\.*[0-9]*)', html).groups()[0].strip().replace(".", "")) #gets the price of a listing
        except Exception:
            Price = 0
        try:
            regex = '<div[^<>][^<>]*>.*spese condominiali .*?€.*?([0-9]+).*?<\/div>|Spese condominiali<!--[^€]*€([^/]*)' #regex to find the Spese Condominiali of a listing either in the appropiate section or the description TODO! More corner cases
            Extra = int(re.search(regex, html, re.IGNORECASE).groups()[0].strip())
        except Exception:
            Extra = 0
        results.append(Result("lol", Price, Extra, link))
    return results


if __name__ == "__main__":
    Link = input("Insert Link: ")
    #Type = (re.search('\?tr=([^&]*)', Link)).groups()[0]
    #Zone = (re.search('&geopolygon=({.*})', Link)).groups()[0]
    #TODO Ask for how many pages and process n pages
    #TODO Implement other sites
    Results = (get_List(get_WebPage(Link)))
    for result in Results:
        print((result.price)+(result.extra))
        print(result.link)
    # get user search link
    # get list of homes
    # ask for user filters
    # sort homes
    # output an exel
