# -*- coding:utf-8 -*-
import time
import string
'''
    userpw2.py.
    7.1 中管理名字-密码的键值对数据的程序有关。
    (a) 修改那个脚本,使它能记录用户上次的登录日期和时间(用time模块),并与用户密码一起保存起来。
        程序的界面有要求用户输入用户名和密码的提示。无论户名是否成功登录,都应有提示, 在户名成功登录后,应更新相应用户的上次登录时间戳。
        如果本次登录与上次登录在时间上相差不超过4个小时,则通知该用户: “You already logged in at: <last_ login_timestamp>.”
    (b) 添加一个“管理”菜单,其中有以下两项:
    (1) 删除一个用户 (2) 显示系统中所有用户的名字和他们的密码的清单。
    (e) 要求用户名不区分大小写。
    (f) 加强对用户名的限制,不允许符号和空白符。
    (g) 合并“新用户”和“老用户”两个选项。如果一个新用户试图用一个不存在的用户名登录, 询问该用户是否是新用户,如果回答是肯定的,就创建该帐户。否则,按照老用户的方式登录。
'''

db = {'fanyuhao': ['wahty0673']}
AllStrings = string.letters + string.digits


def newer():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.get(name):
            prompt = 'name taken, try another!'
            continue
        else:
            for key in name:
                if key not in AllStrings:
                    print 'name should not have space or symbol'
                    break
            else:
                pwd = raw_input('password:')
                db[name] = [pwd]
                break


def olduser():
    name = raw_input('login:').lower()
    if not db.get(name): newer()
    pwd = raw_input('password:')
    password = db.get(name)[0]
    if time.clock() >= 4*3600:
        if password == pwd:
            print 'welcome'
            localtime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
            db[name] = [password, localtime]
            print db[name]
        else:
            print 'login incorrect'
    else:
        print 'You already logged in at: <last_ login_timestamp>.'


def delete_user():
    username = raw_input('input name that you want to delete:')
    if username in db:
        del db[username]
    else:
        print 'sorry,there is no this user!'


def show_users():
    for name, password in db.iteritems():
        print 'name:%s,password:%s' % (name, password)


def showmenu():
    prompt = """
    (E) Existing User Login
    (D) delet a user
    (S) show all users
    (Q) Quit
    """
    Done = False
    while not Done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip().lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
                print '\nYou picked %s' % choice
            if choice not in 'neqsd':
                print 'invalid option,try again!'
            else:
                chosen = True
        if choice == 'n': newer()
        if choice == 'e': olduser()
        if choice == 'q': Done = True
        if choice == 'd': delete_user()
        if choice == 's': show_users()

if __name__ == '__main__':
    showmenu()
