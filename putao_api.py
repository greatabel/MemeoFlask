import urllib
import urllib.parse
import hashlib
import time
import collections
from termcolor import colored,cprint
import requests

url = 'http://api-weidu-test.ptdev.cn'

data = {"app_key":"a9973799e0dbfbb338ea573d5d76dcbd","time":"1472023028"}
data["time"] = str(int(time.time()))
secret_key = '900ced36ff5fb92abc4a37c95c823b1e'



def recursive_urlencode(d):
    """URL-encode a multidimensional dictionary.

    >>> data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
    >>> recursive_urlencode(data)
    u'a=b%26c&j=k&d[e][f%26g]=h%2Ai'
    """
    def recursion(d, base=[]):
        pairs = []
        od = collections.OrderedDict(sorted(d.items()))
        for key, value in od.items():
            new_base = base + [key]
            if hasattr(value, 'values'):
                pairs += recursion(value, new_base)
            else:
                new_pair = None
                if len(new_base) > 1:
                    first = urllib.parse.quote(new_base.pop(0))
                    rest = map(lambda x: urllib.parse.quote(x), new_base)
                    new_pair = "%s[%s]=%s" % (first, ']['.join(rest), urllib.parse.quote(str(value)))
                else:
                    new_pair = "%s=%s" % (urllib.parse.quote(str(key)), urllib.parse.quote(str(value)))
                pairs.append(new_pair)
        return pairs

    return '&'.join(recursion(d))




def create_sign(data):
    e = recursive_urlencode(data)
    print('urllib.unquote(e)=',urllib.parse.unquote(e))
    m = hashlib.md5()
    print(colored('e+secret_key=','red'),(e+secret_key))
    m.update((e+secret_key).encode('utf-8') )
    print(colored('m.hexdigest()=','red'),m.hexdigest())
    return m.hexdigest()

def user_by_openid(openid,access_token):
    user_url = 'http://api-weidu-test.ptdev.cn/server/userinfo/get?access_token='+access_token+'&open_id='+openid+'&service_id=50044'
    print("\nuser_url=",user_url)
    response = requests.get(user_url)
    print('user_by_openid end=',response.text)

if __name__ == "__main__":
    url +='/server/get/access/token'
    sign = create_sign(data)
    ts = str(int(time.time()))
    print('current time=', ts)

    # ts = "1472023028"
    # sign = "14f671f8e484ef94c65b36b89f6fa041"
    data = '{"app_key":"a9973799e0dbfbb338ea573d5d76dcbd","time":"1381429600","sign":"'+sign+'" }'
    print('url=',url)
    print('data=',data)
    # post to putao url is not working
    # response = requests.post(url, data=data)
    url +='?app_key=a9973799e0dbfbb338ea573d5d76dcbd&time='+ts+'&sign='+sign
    response = requests.get(url)
    print('end=',response.text)
    user_by_openid("0870111b0ea9f317465b209071305916e3080cce", "a38699b6108ed9e26fd69a6afbb2df7ba960572c")
