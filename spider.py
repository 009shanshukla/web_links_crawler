from urllib.request import urlopen
from get_links import LinkFinder
from general import*

class Spider:
	### instance variables
	base_url = ''
	project_name = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, domain_name, base_url):
		Spider.project_name = project_name
		Spider.domain_name = domain_name
		Spider.base_url = base_url
		Spider.queue_file = Spider.project_name + '/queue.txt'
		Spider.crawled_file = Spider.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page('First Spider', Spider.base_url)


	### as we are not initializind any instance of class in some functions, we can make it static 	
	@staticmethod
	def boot():
		create_proj_dir(Spider.project_name)
		create_data_file(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)	
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod	
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print(thread_name + " now crawling " + page_url)
			print("queue " + str(len(Spider.queue)) + " crawled " + str(len(Spider.crawled)))
			Spider.add_links_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()	

	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			response = urlopen(page_url)
			if response.getheader('Content-Type') == 'text/html':
				html_byte = response.read()
				html_string = html_byte.decode("utf-8")
				finder = LinkFinder(Spider.base_url, page_url)
				finder.feed(html_string)
		except:
			print("unable to crawl page")
			return set()

		return(finder.page_links())	

	@staticmethod
	def add_links_queue(links):
		for url in links:
			if url in crawled:
				continue
			if url in queue:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)
			
	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)

				
				
