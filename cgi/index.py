#!C:\Python311\python.exe
import os

envs = os.environ; # получаем все переменные окружения dict{name: value}

print( "Content-type: text/html; charset=cp1251" )
print( "Connection: close" )
print() # end of headers
with open('home.html', encoding="utf-8") as file :
    print( file.read() )

# import cgi
# import MySQLdb
    
# print("Content-type: text/html\n")

# selected_env_vars = ["REQUEST_URI", "QUERY_STRING", "REQUEST_METHOD", "REMOTE_ADDR", "REQUEST_SCHEME"]
# for var_name in selected_env_vars:
#     print(f"{var_name}: {os.environ.get(var_name, '')}<br>")

# print("<br>")

# query_string = os.environ.get("QUERY_STRING", "")
# query_dict = cgi.parse_qs(query_string)

# print("Query string dictionary:<br>")
# print("{<br>")
# for key, values in query_dict.items():
#     print(f'  "{key}": {values},<br>')
# print("}<br>")
    

# db_host = "your_db_host"
# db_user = "your_db_user"
# db_password = "your_db_password"


# db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password)
# cursor = db.cursor()

# sql_query = "SHOW DATABASES"
# cursor.execute(sql_query)
# databases = cursor.fetchall()

# print("<html><head><title>Database List</title></head><body>")
# print("<h1>Database List:</h1>")
# print("<table border='1'>")
# print("<tr><th>Database Name</th></tr>")

# for database in databases:
#     print(f"<tr><td>{database[0]}</td></tr>")

# print("</table></body></html>")

# cursor.close()
# db.close()