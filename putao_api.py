import urllib
import urllib.parse
import hashlib
import time
import collections
from termcolor import colored,cprint
import requests

url = 'http://api-weidu-test.ptdev.cn'

data = {"app_key":"a9973799e0dbfbb338ea573d5d76dcbd","time":"1472023028"}
data["time"] = str(int(time.time())+180000)
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

def user_by_openid(openid,access_token,service_id):
    # user_url = 'http://api-weidu-test.ptdev.cn/server/userinfo/get?access_token='+access_token+'&open_id='+openid+'&service_id=50044'
    user_url = 'http://api-weidu-test.ptdev.cn/server/userinfo/get'
    print("\nuser_url=",user_url)
    # response = requests.get(user_url)
    data = {"access_token":access_token,"open_id":openid,"service_id":service_id}
    response = requests.post(user_url, data=data)

    print('2:### user_by_openid end=',response.text)

def child_by_openid(openid,access_token,service_id):
    child_url = 'http://api-weidu-test.ptdev.cn/server/get/child'
    print("\child_url=",child_url)
    # response = requests.get(user_url)
    data = {"access_token":access_token,"open_id":openid,"service_id":service_id}
    response = requests.post(child_url, data=data)

    print('3:### child_by_openid end=',response.text)

def get_child_picture(imgurl):
    print('get_child_picture')
    data=requests.get(imgurl)
    photo=data.content
    # newstring = photo.decode(encoding='UTF-8')
    args = {'name': 'abel', 'sex': 0, 'birthday': '2015-12-12 00:00:00','picture':''}

    args['picture'] = photo
    from dbhelper import DBHelper
    DB = DBHelper()
    DB.add_children(args)
    # print('#=',photo)



if __name__ == "__main__":
    url +='/server/get/access/token'
    sign = create_sign(data)
    ts = str(int(time.time())+180000)
    print('current time=', ts)

    # ts = "1472023028"
    # sign = "14f671f8e484ef94c65b36b89f6fa041"
    data = {"app_key":"a9973799e0dbfbb338ea573d5d76dcbd","time":ts,"sign":sign}
    print('url=',url)
    print('data=',data)
    # post to putao url is not working
    print('post:')
    response = requests.post(url, data=data)
    
    # url +='?app_key=a9973799e0dbfbb338ea573d5d76dcbd&time='+ts+'&sign='+sign
    print('url=',url)
    print('data=',data)
    # response = requests.get(url)
    print('1:token end=',response.text)
    user_by_openid("0870111b0ea9f317465b209071305916e3080cce", "8098a705fc949938f8475884762c27d47c6df941","50044")
    child_by_openid("0870111b0ea9f317465b209071305916e3080cce", "8098a705fc949938f8475884762c27d47c6df941","50044")
    get_child_picture('http://weidu.file.dev.putaocloud.com/file/66aca9bae95ddd5b8c0cf7ad6e96edfe8fcb29d5.jpg')
