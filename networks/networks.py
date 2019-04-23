#import socket, argparse
#from datetime import datetime

#Max_bytes = 65535

#def server(port):
#    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock.bind(("localhost", port))
#    print("Listening at {}".format(sock.getsockname))
#    while True:
#        data, address = sock.recvfrom(Max_bytes)
#        text = data.decode("ascii")
#        print("The client at {} says {!r}".format(address, text))
#        text = "Your data was {} bytes long".format(len(data))
#        data = text.encode("ascii")
#        sock.sendto(data, address)


#def client(port):
#    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    text = "The time is {}".format(datetime.now())
#    data = text.encode("ascii")
#    sock.sendto(data, ("127.0.0.1", port))
#    print("The OS assigned me the address {}".format(sock.getsockname))
#    data, address = sock.recvfrom(Max_bytes)
#    text = data.decode("ascii")
#    print("The server {} replied {!r}".format(address, text))


#if __name__ == "__main__":
#    choices = {'client':client, 'server':server}
#    parser = argparse.ArgumentParser(description = "Send and receive UDP locally")
#    parser.add_argument('role', choices = choices, help = 'which role to play')
#    parser.add_argument('-p', metavar = 'PORT', type = int, default = 1060, help = "UDP port (default 1060)")
#    args = parser.parse_args()
#    function = choices[args.role]
#    function(args.p)

import requests as re


class Spyder:
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    def __init__(self):
        self.session = re.Session()
    def login(self, username = "15279706155", password = "project1"):
        form = {
            'username': username,
            'password': password,
            'checkhash': '',
            }
        html = self.session.post('http://www.pigai.org/index.php?a=login', headers = Spyder.head, data = form)
        return html;
    def modify_password(self):
        return self.session.get("http://www.pigai.org/?a=modifyPassword", headers = Spyder.head)
    def get_ready_for_writing(self):
        html = self.session.get("http://www.pigai.org/index.php?c=v2&a=write&eid=89543084&rid=10", headers = Spyder.head)
        self.eid = 89543084
        return html
    def post_article(self, article = ""):
        form = {
            'utContent': 'why%20am%20i%20so%20handsome%20why%20am%20i%20so%20,handsome%20why%3F',
            'utTitle': '%E8%87%AA%E6%B5%8B%E7%BB%83%E4%B9%A0',
            "bzold" : '',
            'bz':'',
            'fileName': '',
            'filePath':'' ,
            'rid': '10',
            'eid': '',
            'type': '0',
            'utype': '',
            'gao': '1',
            'uncheck': '',
            'tiku_id': '0',
            'engine': '',
            'fromCode': '754973'
            
            }
        html = self.session.post("http://www.pigai.org/index.php?c=ajax&a=postSave", headers = Spyder.head, data = form)
        return html#从这开始！！！！
spi = Spyder()
response = spi.login()
response2 = spi.get_ready_for_writing()
print(response2.getRequestURL())
print(spi.eid)