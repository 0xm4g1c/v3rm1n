
## V3RM1N


Simple CLI (Command Line Interface) that Enumerates websites for Robots.txt paths, Links and hidden Directories. The tool was built to automate the Enumearation process in web-based Capture The Flag (CTF) challenges.

The tool is for Educational Purposes __ONLY!__. Do not Crawl websites if you are not permitted. 


## Usage

Clone this GitHub Repository into a directory of your choice and install required modules:

```
➜ git clone https://github.com/NuhMohammed/v3rm1n
➜ pip install -r requirements.txt
```

Change into installation directory and use as follows

```
➜  python3 vermin.py -h
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
```

#### Example

Users provide a URL to attack by parsing an argument. For instance to query `/robots.txt` file in a page, we pass the `-r` argument:

```
➜ python3 vermin.py -r https://www.geeksforgeeks.org/  



        .##.....##..#######..########..##.....##....##...##....##
        .##.....##.##.....##.##.....##.###...###..####...###...##
        .##.....##........##.##.....##.####.####....##...####..##
        .##.....##..#######..########..##.###.##....##...##.##.##
        ..##...##.........##.##...##...##.....##....##...##..####
        ...##.##...##.....##.##....##..##.....##....##...##...###
        ....###.....#######..##.....##.##.....##..######.##....##

                            Simple Web Crawler
        
        

Target URL:  https://www.geeksforgeeks.org/

Finding Robot Files: 

 [+] User-agent: *
Disallow: /wp-admin/
Disallow: /wp-content/plugins/
Disallow: /content-override.php
```
## Collaboration

__TO-DO__  

- [x] Include a `-d` option that bruteforces directories using a file that contains common directory names and outputs found directories.
  
- [ ] Generate an output file to save results from commands.



