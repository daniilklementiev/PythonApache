#!C:\Python311\python.exe
import os

envs = os.environ; # получаем все переменные окружения dict{name: value}

print( "Content-type: text/html; charset=cp1251" )
print( "Connection: close" )
print() # end of headers
with open('home.html', encoding="utf-8") as file :
    print( file.read() )

import cgi

# print("Content-type: text/html\n")

# # Забезпечення відображення обраних змінних оточення
# selected_env_vars = ["REQUEST_URI", "QUERY_STRING", "REQUEST_METHOD", "REMOTE_ADDR", "REQUEST_SCHEME"]
# for var_name in selected_env_vars:
#     print(f"{var_name}: {os.environ.get(var_name, '')}<br>")

# print("<br>")

# # Розбір рядка QUERY_STRING у словник
# query_string = os.environ.get("QUERY_STRING", "")
# query_dict = cgi.parse_qs(query_string)

# # Виведення результатів розбору
# print("Query string dictionary:<br>")
# print("{<br>")
# for key, values in query_dict.items():
#     print(f'  "{key}": {values},<br>')
# print("}<br>")