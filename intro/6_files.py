# Python: files
def create_file1() -> None:
    filename = "file1.txt"
    file = None
    try:
        file = open(filename, mode="w", encoding="utf-8")
        file.write("Latin data\n")
        file.write("Кирилица\n")
        
    except OSError as e:
        print(e)
    else:
        file.flush()
        print("File created")
    finally:
        if file != None:
            file.close()


def read_all_text1(filename: str) -> str:
    file = None
    try:
        file = open(filename, mode="r", encoding="utf-8")
    except OSError as e:
        print(e)
    else:
        return file.read()
    finally:
        if file != None : file.close()


def create_headers(filename: str) -> None:
    try:
        with open(filename, mode="w", encoding="utf-8") as file :
            file.write("Host: localhost\r\n")
            file.write("Connection: close\r\n")
            file.write("Content-Type: text/css\r\n")
            file.write("Content-Length: 100500\r\n")
    except IOError as e:
        print("Create headers error")
    else:
        print("File created")
    finally:
        pass


def parse_headers1(filename: str) -> dict | None:
    try:
        ret = {}
        with open(filename, mode="r", encoding="utf-8") as file :
            for line in file:
                if ':' in line:
                    key, value = line.split(":")
                    ret[key.strip()] = value.strip()
            return ret
    except IOError as e:
        print("Create headers error")
    else:
        print("File readed")
    finally:
        pass


def print_headers(filename:str) -> None:
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            n = 1
            for x in file :
                print( n, x)
                n += 1
    except IOError as e:
        print("Read headers error")

def parse_headers(filename: str) -> dict | None:
    try:
        with open(filename, mode="r", encoding="utf-8") as file :
            return {k: v for k, v in (map(str.strip, line.split(":") ) for line in file.readlines() if ":" in line)}
    except IOError as e:
        print("Create headers error")
        return None

def main() -> None:
    # create_file1()
    # print(read_all_text1("file1.txt"))
    create_headers("headers.txt")
    for k, v in parse_headers("headers.txt").items():
        print(k, v)
    # print(parse_headers("headers.txt"))
    pass

if __name__ == "__main__": main()