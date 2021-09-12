usage = '''
 __________________________________________________
|                                                  |
V3RM1N - Crawl Website Pages

Usage:
    docopt_parser.py [-r] [-l] [-d] <TARGET_URL>
    
Options:    
    TARGET_URL       URL to attack
    -h               Show this help message and exit
    -r               List Contents of /robots.txt
    -l               List every link in a page
    -d               Bruteforce directories

|__________________________________________________|
'''


from docopt import docopt
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import pprint

# SEARCH_URL = 'https://jupiter.challenges.picoctf.org/problem/56830'

arguments = docopt(usage, version='1.0')
#pprint(arguments)
'''
{'-d': False,
 '-l': False,
 '-r': True,
 '<TARGET_URL>': 'https://jupiter.challenges.picoctf.org/problem/56830'}
'''

SEARCH_URL = arguments['<TARGET_URL>'] # get URL Details


##############
# Robots.txt #
##############
def get_robots():
    robots_url = SEARCH_URL + '/robots.txt'
    robots_response = requests.get(robots_url)
    if robots_response.status_code == 200:
        robots_soup = BeautifulSoup(robots_response.content, 'html.parser')
        return(robots_soup)
        
    else:
        return Exception('\033[0;31m [-] Bad Request')


###########
# Links   #
###########
def get_links():
    link_response = requests.get(SEARCH_URL)
    link_soup = BeautifulSoup(link_response.text, 'html.parser')
    
    for link in link_soup.find_all('a'):
        #if '#main' in link.get('href')
        print (link.get('href').replace('#main', ''))

#get_links()



# user passes required argument (TARGET_URL)
if arguments['<TARGET_URL>']:

    print ('''


        .##.....##..#######..########..##.....##....##...##....##
        .##.....##.##.....##.##.....##.###...###..####...###...##
        .##.....##........##.##.....##.####.####....##...####..##
        .##.....##..#######..########..##.###.##....##...##.##.##
        ..##...##.........##.##...##...##.....##....##...##..####
        ...##.##...##.....##.##....##..##.....##....##...##...###
        ....###.....#######..##.....##.##.....##..######.##....##

                            Simple Web Crawler
        
        ''')


    print ("\nTarget URL: ", "\033[1;34m" + arguments['<TARGET_URL>'])

    # Get user options/flags
    if  arguments["-r"]:
        print ("\nFinding Robot Files \n")
        print('\033[0;32m [+]', get_robots())

    if  arguments["-l"]:
        print ("\nFinding Every Link in this page\n")
        get_links()

    elif  arguments["-d"]:
        print ("\nFinding Hidden Directories \n")

    





