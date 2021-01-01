lethalskid_txt = """
\033[0;34
__        _______ ____    ____  _____ ______     _______ ____    ___ ____  
\ \      / / ____| __ )  / ___|| ____|  _ \ \   / / ____|  _ \  |_ _|  _ \ 
 \ \ /\ / /|  _| |  _ \  \___ \|  _| | |_) \ \ / /|  _| | |_) |  | || |_) |
  \ V  V / | |___| |_) |  ___) | |___|  _ < \ V / | |___|  _ <   | ||  __/ 
   \_/\_/  |_____|____/  |____/|_____|_| \_\ \_/  |_____|_| \_\ |___|_|    
                                                                           
 _______  _______ ____      _    ____ _____ ___  ____  
| ____\ \/ /_   _|  _ \    / \  / ___|_   _/ _ \|  _ \ 
|  _|  \  /  | | | |_) |  / _ \| |     | || | | | |_) |
| |___ /  \  | | |  _ <  / ___ \ |___  | || |_| |  _ < 
|_____/_/\_\ |_| |_| \_\/_/   \_\____| |_| \___/|_| \_\
						     

\033[0m

\033[1;32m 
Contributors : Om Suryakant Koli (omkoli3600xt@gmail.com)
	     : Atharva R. Hedage (atharavhedage@gmail.com)
      GitHub : github.com/omkoli
             : github.com/AtharavRH
\033[0m
                                                                           
\033[1;31m** Only for Testing and Penetration purposes **\033[0m


"""
import shodan
import sys
import os.path

file_exists = os.path.isfile("API_KEY.txt")

if file_exists:
    print("\033[1;32mAPI_KEY has been already saved\033[0m")


else:
    fh = open("API_KEY.txt", "w")
    print("\033[1;32mEnter your API_KEY\033[0m")
    SHODAN_API_KEY = input()
    fh.write(SHODAN_API_KEY)
    fh.close()
    fh = open("API_KEY.txt", "r")
    SHODAN_API_KEY = fh.read()

print("\033[1;33mDo you want to edit the saved API_KEY?\033[0m <Y/N>")
choice = input().lower()

if choice == "y":
    fh = open("API_KEY.txt", "w")
    print("\033[1;32mEnter the API_KEY you want to save and use\033[0m")
    SHODAN_API_KEY = input()
    fh.write(SHODAN_API_KEY)
    fh.close()
    fh = open("API_KEY.txt", "r")
    SHODAN_API_KEY = fh.read()


if choice == "n":
    fh = open("API_KEY.txt", "r")
    SHODAN_API_KEY = fh.read()


api = shodan.Shodan(SHODAN_API_KEY)

if len(sys.argv) < 2:
    print("Usage :python3 ipx.py <query search>")
    print("Example: python3 ipx.py apache")
    sys.exit(0)

try:
    query = sys.argv[1]
    results = api.search(query)

    print(lethalskid_txt)
    for result in results["matches"]:
        print(result["ip_str"], end=" ")
        print(result["org"])


except shodan.APIError as oeps:
    print("[⚠️] \033[0;31mError: %s \033[0m" % (oeps))

except shodan.APIerror as e:
    print(e)

