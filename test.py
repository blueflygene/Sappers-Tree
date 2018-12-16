import requests
import random
import os
import json
import string
import numpy
import scipy


#inject rans into form
chars = string.ascii_letters + string.digits + '!%$^&&()&*'

random.seed  = (os.urandom(1024))

#use the names json file
names = json.loads(open('names.json').read())

#URL for the injection
url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

#create the injection loop
for name in names:
	    name_extra = ''.join(random.choice(string.digits))

	    username = name.lower() + name_extra + '@yahoo.com'
	    password = ''.join(random.choice(chars) for i in range(8))

	    requests.post(url, allow_redirects=False, data={
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	    })

print('sending username %s and password %s') % (username, password)








        
        













    



    

