from docopt import docopt
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import pprint
from colorama import Fore, Back, Style


usage = '''
 _______________________________________________________
|                                                       |
V3RM1N - Crawl Website Pages

Usage:
    vermin.py [-r] [-l] <TARGET_URL>
    vermin.py [-d] <WORDLIST> <TARGET_URL>
    
    
Options:    
    -h               Show this help message and exit
    -r               List Contents of /robots.txt
    -l               List every link in a page
    -d               Bruteforce directories
    WORDLIST         Wordlist to bruteforce directories
    TARGET_URL       URL to attack

|_______________________________________________________|
'''


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
if 'http://' not in SEARCH_URL:
    SEARCH_URL = 'http://' + SEARCH_URL
else: SEARCH_URL = arguments['<TARGET_URL>']

#print (SEARCH_URL)


#------------#
# Robots.txt #
#------------#
def get_robots():
    robots_url = SEARCH_URL + '/robots.txt'
    robots_response = requests.get(robots_url)
    if robots_response.status_code == 200:
        robots_soup = BeautifulSoup(robots_response.content, 'html.parser')
        return(robots_soup)
        
    else:
        return Exception(Fore.RED + "[-] Bad Request: Site Prohibits Crawling, Can't Access the Robots File")


#---------#
# Links   #
#---------#
def get_links():
    link_response = requests.get(SEARCH_URL)
    link_soup = BeautifulSoup(link_response.text, 'html.parser')
    
    for link in link_soup.find_all('a'):
        #if '#main' in link.get('href')
        print (Fore.BLUE + link.get('href').replace('#main', ''))

#get_links()


#-----------#
# Directory #
#-----------#
def get_directory():

    try:
        with open(arguments['<WORDLIST>'], "r", encoding='utf-8-sig') as w:
            wordlists = w.readlines()  # type List          
            for i in wordlists:                    
                word = i.rstrip()
                directory = SEARCH_URL + '/' + word
                directory_request = requests.get(directory)
                print (Fore.BLUE + '{}:{}'.format(directory, directory_request.status_code))
        
                
    except FileNotFoundError:
        return (Fore.RED + "Error: No such file on your directory")

#get_directory()


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


    print (Back.BLUE + "\nTarget URL: ", arguments['<TARGET_URL>'])
    print(Style.RESET_ALL)

    # Get user options/flags
    if  arguments["-r"]:
        print ("\nFinding Robot Files: \n")
        print(get_robots())

    if  arguments["-l"]:
        print ("\nFinding links in this page: \n")
        get_links()

    elif  arguments["-d"]:
        print ("\nFinding Hidden Directories: \n")
        print("WordList Used:",arguments['<WORDLIST>'])
        get_directory()
    





