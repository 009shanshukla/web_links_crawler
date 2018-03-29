import os


### each website you crawal, is a seperate project(if not created)
def create_proj_dir(directory):
	if not os.path.exists(directory):
		print("creating project " + directory)
		os.makedirs(directory)

### create queue and crawled file(if not created)
def create_data_file(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

### create new file and write
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()		
		
### add data into existing file
def append_to_file(path, data):
	with open(path, 'a') as f:
		f.write(data + '\n')
		f.close()

### delete the content of file
def delete_content(path):
	with open(path, 'w') as f:
		pass

### convert file content into set
def file_to_set(file_name):
	links = set()
	with open(file_name, 'rt') as f:
		for line in f:
			links.add(line.replace('\n', ''))
	return links
	

### convert set links into file
def set_to_file(links, file_name):
	delete_content(file_name)
	for link in sorted(links):
		append_to_file(file_name, link)
