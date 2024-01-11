#!C:\Python311\python.exe
import os

def send_redirect(location:str) :
    print("Status: 301 Moved Permanently")
    print("Location: /uk/shop/")
    print()
    exit()

# Разбираем query string в словарь dict{name: value}
query_string = os.environ['QUERY_STRING']
query_params = { k: v for k, v in (pair.split('=') for pair in os.environ['QUERY_STRING'].split('&')) } 
titles = {
    'ru': 'Магазин работает',
    'en': 'Shop works',
    'uk': 'Магазин працює',
    'de': 'Shop funktioniert',
    'es': 'La tienda funciona',
    'fr': 'La boutique fonctionne',
}
lang = query_params.get('lang', 'uk') 
if not lang in titles:
    send_redirect('/uk/shop/')
    
title = titles[lang]

print( "Content-type: text/html; charset=cp1251" )
print( "Connection: close" )
print() # end of headers
print(f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="cp1251">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI</title>
</head>
<body>
    <h1>{title}</h2>
    <p>{lang}</p>
</body>
</html>
''')