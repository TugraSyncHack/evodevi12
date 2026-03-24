users = {}

def register_user(username, password):
    if username in users:
        return "Bu girişe sahip bir kullanıcı zaten mevcut."
    else:
        users[username] = password
        return f"{username} başarıyla kaydedildi."
