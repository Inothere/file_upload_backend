class User(object):
    def __init__(self, id, username, password):
        self.username = username
        self.password = password
        self.id = id
    
    def __str__(self):
        return 'User(\'{}\')'.format(self.username)
    

