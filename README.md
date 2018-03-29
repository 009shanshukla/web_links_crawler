# Overview

WEB_LINKS_CRAWLER is multi-threaded website spider written in Python. It first open the homepage of the website, then collects all the links of the same domain of website and collects it onto a text file(Crwaled).  Basically purpose of this tool is to gather links **links only**. Whole Data Analytics, Data harvesting and search algorithms are written as a seperate program.

### Requirements

- python3
- htmlparser library
- sys library

## Remember

At the start of the program a directory will be created as the same name of domain name and two text files will be created (queue.txt and crawled.txt). 

- Queue File will contain all the links that has yet to be visited.
- Crawled File will contain all the links that has been visited.

### Specification 

- same links will not be visited twice.(Only stored once in the files)
- Every will link will be updated into files simultaneously, in the case of sudden failure of program, it can be re-start from the links where it would stop. 
