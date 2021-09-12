
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

Finding Robot Files 

 [+] User-agent: *
Disallow: /wp-admin/
Disallow: /wp-content/plugins/
Disallow: /content-override.php
```
## Collaboration

__TO-DO__  

- Include a `-d` option that bruteforces directories using a file that contains common directory names and outputs found directories.
  
- Generate an output file to save found resources from commands.



