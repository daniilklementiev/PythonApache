import json

def create_json_file() :
    try:
        with open("data.json", mode="w", encoding="utf-8") as file:
            file.write('''
                    {   
                        "str": "Hello, World!",
                       "digital": 1213,
                       "float": 1.456,
                       "bool1": true,
                       "null": null,
                       "obj": {
                            "bool0":false,
                            "str":"Hello, World!"
                       },
                       "arr": [1,2,3,4,5]
                    }
                        ''')
            # json.dump({"name": "John", "age": 30}, file)
    except:
        print("Create json file error")
    else:
        print("File created")
    finally:
        pass


def print_json_file(filename:str) -> None:
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            j = json.load(file)
        print(type(j), j)
        for k in j:
            print(k, j[k], type(j[k]))
        j['cyr'] = 'Привет, Мир!'
        print( '=================' )
        print(json.dumps(j))
        print(json.dumps(j, ensure_ascii=False, indent=4))    
    except:
        print("Read json file error")
    else:
        print("File readed")
    finally:
        pass


def main() -> None:
    # create_json_file()
    print_json_file("data.json")
    pass

if __name__ == "__main__": main()