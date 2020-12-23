# Site está acessível?
# Site: http://pudim.com.br/

import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[1;31mConexão desligada!\033[m')
else:
    print('\033[1;32mO site Pudim está acessível!\033[m')
    print(site.read()) # código fonte da página
