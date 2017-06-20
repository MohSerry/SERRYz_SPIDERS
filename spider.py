import urllib.request
from FindLinks import LinkFinder
from domain import *
from basicFunctions import *


class Spider:
    projectName = ''
    baseURL = ''
    domainName = ''
    qFile = ''
    crawledFile = ''
    q = set()
    crawled = set()

    def __init__(self, projectName, baseURL, domainName):
        Spider.projectName = projectName
        Spider.baseURL = baseURL
        Spider.domainName = domainName
        Spider.qFile = Spider.projectName + '\queue.txt'
        Spider.crawledFile = Spider.projectName + '\crawled.txt'
        self.boot()
        self.crawlPage('spider', Spider.baseURL)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        createProjectDirectory(Spider.projectName)
        createFiles(Spider.projectName, Spider.baseURL)
        Spider.q = convert_to_set(Spider.qFile)
        Spider.crawled = convert_to_set(Spider.crawledFile)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawlPage(threadName, pageURL):
        if pageURL not in Spider.crawled:
            print(threadName + 'Spider crawling ' + pageURL)
            print('Queue ' + str(len(Spider.q)) + '     Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(pageURL))
            Spider.q.remove(pageURL)
            Spider.crawled.add(pageURL)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urllib.request.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.baseURL, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.pageLinks()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.q) or (url in Spider.crawled):
                continue
            if Spider.domainName != get_domain_name(url):
                continue
            Spider.q.add(url)

    @staticmethod
    def update_files():
        convert_to_file(Spider.q, Spider.qFile)
        convert_to_file(Spider.crawled, Spider.crawledFile)
