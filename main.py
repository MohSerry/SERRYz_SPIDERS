import threading
from queue import Queue
from spider import Spider
from domain import *
from basicFunctions import *

print("WELCOME TO SERRYz SPIDER!")

Target = input("Enter Target URL ")
PROJECT_NAME = get_domain_name(Target)
HOMEPAGE = Target
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS =  input("How many spiders do you want: ")
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def createSpiders():
    for _ in range(int(NUMBER_OF_THREADS)):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in convert_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = convert_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


createSpiders()
crawl()
