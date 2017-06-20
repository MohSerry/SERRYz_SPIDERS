from urllib import parse
from html.parser import HTMLParser

class LinkFinder(HTMLParser):

    def __init__(self, baseURL, pageURL):
        super().__init__()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseURL, value)
                    self.links.add(url)

    def pageLinks(self):
        return self.links

    def error(self, message):
        pass
