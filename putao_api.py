import urllib
import urllib.parse
import hashlib
import time
import collections
from termcolor import colored,cprint
import requests
import json
import datetime 
from dbhelper import DBHelper

import putao_config

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
    
# def recursive_urlencode(d):
#     """URL-encode a multidimensional dictionary.

#     >>> data = {'a': 'b&c', 'd': {'e': {'f&g': 'h*i'}}, 'j': 'k'}
#     >>> recursive_urlencode(data)
#     u'a=b%26c&j=k&d[e][f%26g]=h%2Ai'
#     """
#     def recursion(d, base=[]):
#         pairs = []
#         od = collections.OrderedDict(sorted(d.items()))
#         for key, value in sorted(d.items()):
#             new_base = base + [key]
#             if hasattr(value, 'values'):
#                 pairs += recursion(value, new_base)
#             else:
#                 new_pair = None
#                 if len(new_base) > 1:
#                     first = urllib.parse.quote(new_base.pop(0))
#                     rest = map(lambda x: urllib.parse.quote(x), new_base)
#                     new_pair = "%s[%s]=%s" % (first, ']['.join(rest), urllib.parse.quote(str(value)))
#                 else:
#                     new_pair = "%s=%s" % (urllib.parse.quote(str(key)), urllib.parse.quote(str(value)))
#                 pairs.append(new_pair)
#         return pairs

#     return '&'.join(recursion(d))




def create_sign(data):
    e = recursive_urlencode(data)
    print('urllib.unquote(e)=',urllib.parse.unquote(e))
    m = hashlib.md5()
    print(colored('e+secret_key=','red'),(e+putao_config.secret_key))
    m.update((e+putao_config.secret_key).encode('utf-8') )
    print(colored('m.hexdigest()=','red'),m.hexdigest())
    return m.hexdigest()

def user_by_openid(openid,access_token,service_id):
    # user_url = 'http://api-weidu-test.ptdev.cn/server/userinfo/get?access_token='+access_token+'&open_id='+openid+'&service_id=50044'

    print("\nuser_url=",putao_config.user_url)
    # response = requests.get(user_url)
    data = {"access_token":access_token,"open_id":openid,"service_id":service_id}
    response = requests.post(putao_config.user_url, data=data)
    d = json.loads(response.text)
    return d
    # print('2:### user_by_openid end=',d)

def child_by_openid(openid,access_token,service_id):

    print("\patient_url=",putao_config.patient_url)
    # response = requests.get(user_url)
    data = {"access_token":access_token,"open_id":openid,"service_id":service_id}
    response = requests.post(putao_config.patient_url, data=data)
    d = json.loads(response.text)

    print('3:### child_by_openid end=',response.text)

    return d

def save_child_data(name,sex,birthday,imgurl,userid):
    print('get_child_picture')
    data=requests.get(imgurl)
    photo=data.content
    # newstring = photo.decode(encoding='UTF-8')
    args = {'name': name, 'sex': sex, 'birthday': birthday,'picture':''}

    args['picture'] = photo

    DB = DBHelper()
    lastid = DB.add_children(args)
    DB.add_patientuser({'patientid':lastid,'userid':userid})
    print('lastid=',lastid)
    # print('#=',photo)

def get_access_token(url):
    data = {"app_key": putao_config.app_key}
    # 防止时间超过葡萄服务器时间，所以打提前量3分钟
    data["time"] = str(int(time.time())+180000)
    sign = create_sign(data)
    print('data before:',data)
    # ts = str(int(time.time())+180000)
    # print('current time=', ts)

    # ts = "1472023028"
    # sign = "14f671f8e484ef94c65b36b89f6fa041"
    # data = {"app_key":"a9973799e0dbfbb338ea573d5d76dcbd","time":ts,"sign":sign}
    data['sign'] = sign

    print('url=',url)
    print('data=',data)
    # post to putao url is not working
    print('post:')
    response = requests.post(url, data=data)
    
    # url +='?app_key=a9973799e0dbfbb338ea573d5d76dcbd&time='+ts+'&sign='+sign
    print('url=',url)
    print('data=',data)
    # response = requests.get(url)
    print(colored('1:token end=','red'),response.text)
    d = json.loads(response.text)
    access_token = d['data']['access_token']
    return access_token

def fetch_user(openid):
    access_token = get_access_token(putao_config.access_token_url) 
    user_dic = user_by_openid(openid, access_token,putao_config.service_id)
    args = {'putao_token_uid': openid, 'putao_name': user_dic['data']['nick_name']}
    DB = DBHelper()
    newuserid = DB.add_user(args)
    print('newuserid=',newuserid)
    return newuserid

def fetch_child(openid,userid):
    access_token = get_access_token(putao_config.access_token_url)
    print('*'*10,access_token)

    # user_by_openid(openid, access_token,service_id)
    child_dic = child_by_openid(openid,access_token,putao_config.service_id)
    print('child_dic=',child_dic)
    for i,val in enumerate(child_dic['data']):
        birthday = val['child_birthday']      
        if '-' not in val['child_birthday']:
            birthday = datetime.datetime.fromtimestamp(    int(val['child_birthday'])  ).strftime('%Y-%m-%d %H:%M:%S')
        save_child_data(val['child_nickname'],val['child_gender'],
            birthday,putao_config.dev_pre_picture_url+val['child_avatar'],userid)

def fetch_user_and_child(openid):
    userid = fetch_user(openid)
    print(colored('-' * 10,'red'))
    fetch_child(openid,userid)

if __name__ == "__main__":
    fetch_user_and_child(putao_config.openid)
    # data = {'a': {'b': 'c', 'd': {'e': 'f', 'g': 'h'}}}
    # print(recursive_urlencode(data))
    # print('type:',type(data))



