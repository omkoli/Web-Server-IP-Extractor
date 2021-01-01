# Web-Server-IP-Extractor
A python script to automate shodan.io queries for finding internal IPs of web servers.

![alt text](https://github.com/omkoli/Web-Server-IP-Extractor/blob/main/ipx.png)

## Introduction:
Many companies often forget to take down their internal IPs from directly accessing to their websites. These IP addresses often remain without Cloudflare protection, making a ground for DDoS Attacks. This tool automates shodan.io to find vulnerable internal IPs.

## Pre-requisites:
(Shodan Library)
To install the Shodan library:

	$ pip install shodan


Or if you don't have pip installed (which you should seriously install):

	$ easy_install shodan

## Install:

	$ git clone https://github.com/omkoli/Web-Server-IP-Extractor
	$ cd Web-Server-IP-Extractor

## Run:

	$ python3 ipx.py <search_query>


For Termux, you need root permissions,

	$ tsu
	$ python3 ipx.py <search_query>

## Contributors : 

Om Suryakant Koli (omkoli3600xt@gmail.com)

Atharva R. Hedage (atharavhedage@gmail.com)
						 
GitHub : 
- [github.com/omkoli](https://github.com/omkoli)
- [github.com/AtharavRH](https://github.com/AtharavRH)
						
LinkedIn : 
- [linkedin.com/omkoli](https://www.linkedin.com/in/omkoli/)
- [linkedin.com/atharavhedage](https://www.linkedin.com/in/atharavhedage/)
						 
Instagram  : 
- [instagram.com/0mkoli](https://www.instagram.com/0mkoli/)
- [instagram.com/atharav_rh](https://www.instagram.com/atharav_rh/)

**DISCLAIMER :-
This script is only for penetration testing and security research. I will not be responsible if you use it for any illegal activities.**
