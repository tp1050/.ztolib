"""
Network
"""
uas=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36']
import requests
import re, json
from helper import UNIN, isInitialized, isUnin,tprint,disp



def getHTML(url,secure=0,format='html'):
    print("Method deprecitated do not use it")
    return loadURL(url=url,secure=secure)

def get_tor_session(verbose=0):
    disp('Getting a tor a session',verbose=verbose)
    session = requests.session()
    session.proxies =  {
                        'https': 'socks5://127.0.0.1:9050'
                        # 'https': 'socks5://127.0.0.1:9050'
                        }
                       # 'http':  'socks5h://192.168.5.17:9050',
                       #                    'https': 'socks5h://192.168.5.17:9050'
    ret=""
    success="This browser is configured to use Tor"
    try:
        ret=session.get("https://check.torproject.org/").text
        if  success in ret:
            disp("TorBala Got a session",verbose=verbose)
            return session
        else:
            disp("deadend",verbose=verbose)
    except Exception as e:
        disp(e,verbose=verbose)
    return session


def loadURL(url,secure=False,userAgent=UNIN,session=UNIN,format=UNIN,verbose=0):
    if secure:
        session=get_tor_session()
    elif isUnin(session):
            session=requests.session()
    if isUnin(userAgent):
            userAgent=uas[0]
    try:
        session.headers = {'User-Agent': userAgent}
        resp=session.get(url)
        if format=='json':
            try:
                return resp.json()
            except:
                try:
                    return json.dumps(resp.text,indent=4,sort_keys=True)
                except:
                    return '<!NO!>'
        if format=='html':
            return resp.text
        if format=='soup':
            from bs4 import BeautifulSoup as BS
            disp('dddddddddddddddddddddddddddddddddddddddddddddd',verbose=verbose)
            return BS(resp.text, 'html.parser')
        return resp
    except Exception as e:
        disp (e,verbose=verbose)



def getIPfromstring(s):
    ret=re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',str(s))
    return ret




def is_valid_ipv4_address(ipAddress):
    import socket
    try :
        binaryIP    = socket.inet_pton(socket.AF_INET, ipAddress)
        return True
    except:
        return False
    return True

def filter_ip(inlist):
    for i in inlist:
        if not is_valid_ipv4_address(i):
            inlist.remove(i)
    return inlist

def myIP(session=requests.session(),verbose=0) ->list :
    """
    Stuborn function to extract callerIP for a passed sesssion.
    """

    from helper import disp

    provider =['http://checkip.amazonaws.com/',
                'https://www.cloudflare.com/cdn-cgi/trace',
                'https://idenrrt.me/',
                'http://icanhazip.com',
                'http://httpbin.org/ip'
                ]
    ret=[]
    for p in provider:
        res="2"
        try:
            disp('trying : ' +p,verbose=verbose)
            res=loadURL(p,format="html")
            s=getIPfromstring(str(res))
            ret=ret+s
        except Exception as e:
            ret.append(e.args)
        ret=filter_ip(ret)
        ret=list(set(ret))
    return ret

def lan_ip():
    """
    returns the current machines local IP this rarly is same as the
    public IP
    This method does not account for multiple lan interfaces
    """
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return [s.getsockname()[0]]

def get_my_IP():
    ip_matrix={"inner":[],"outer":[],"misc":[]}
    ip_matrix["inner"]=lan_ip()
    ip_matrix["outer"]=myIP()
    return ip_matrix
