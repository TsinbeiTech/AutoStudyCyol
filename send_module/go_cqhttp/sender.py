import requests

sess = requests.session()
user_id = ""
access_token = ""
api_url = ""
group_id = ""
at_user = ""

def set_api_url(url):
    global api_url
    api_url = url

def set_access_token(token):
    global access_token
    access_token = token

def set_group_id(id):
    global group_id
    group_id = id
    
def set_at_user(user):
    global at_user
    at_user = user
    
def set_user_id(id):
    global user_id
    user_id = id

def send(title, content) -> dict:
    global at_user
    empty = group_id == ""
    noat = at_user == ""
    if empty:
            resp = sess.post(url=f"{api_url}/send_private_msg?access_token={access_token}", data={
                'user_id': f"{user_id}",
                'message': f"{title}\n\n{content}"
            })
    else:
        if noat:
               at_user = user_id
        resp = sess.post(url=f"{api_url}/send_group_msg?access_token={access_token}", data={
                'group_id': f"{group_id}",
                'message': f"[CQ:at,qq={at_user}]\n\n{title}\n\n{content}" if not noat else f"{title}\n\n{content}"
            })
    res = resp.json()
    success = res['status'] == "ok"
    return {
        'success': success,
        'message': res['msg'] if not success else '发送成功'
    }
