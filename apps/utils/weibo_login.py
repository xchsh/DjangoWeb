# author: xchsh
# 授权回调页：http://47.92.87.172:8000/complete/weibo/

def get_auth_url():
    weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
    #redirect_url = 'http://47.92.87.172:8000/complete/weibo/'
    redirect_uri = 'https://api.weibo.com/oauth2/default.html'
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_rul}".format(client_id=1075632994, re_rul=redirect_uri)

    print(auth_url)



def get_access_token(code = ""):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": '1075632994',
        "client_secret": 'e636329177627dd12f78f682267d6037',
        "grant_type": 'authorization_code',
        "code": code,
        "redirect_uri": 'https://api.weibo.com/oauth2/default.html'
    })
    pass

#b'{"access_token":"2.00wyew7GQRPnKBdc5f1e17e304zzEx","remind_in":"157679999","expires_in":157679999,"uid":"5894962290","isRealName":"false"}'

def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={access_token}&uid={uid}".format(access_token=access_token, uid=uid)
    print(user_url)



if __name__ == "__main__":
    get_auth_url()
    get_access_token(code="3a403020182ce8f2d535c25fb691a065")
    get_user_info(access_token="2.00wyew7GQRPnKBdc5f1e17e304zzEx", uid="5894962290")