from persistence import Persistence
from openid import OpenId


def login(username, password):
    print("Efetuando login...")
    openId = OpenId(username, password)
    
    if not openId.is_authenticated():
        print("Invalid username or password")
        exit()

    print("Seja bem-vindo ao DHuO Data " + username)
    print("Workspace padrão: " + openId.get_workspace())
    
    persistence = Persistence();
    persistence.save_username(username)
    persistence.save_password(password)
    persistence.save_workspace(openId.get_workspace())