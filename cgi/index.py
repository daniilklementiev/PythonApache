#!C:\Python311\python.exe
import os

envs = os.environ; # получаем все переменные окружения dict{name: value}

print( "Content-type: text/html; charset=cp1251" )
print( "Connection: close" )
print() # end of headers
with open('home.html', encoding="utf-8") as file :
    print( file.read() )