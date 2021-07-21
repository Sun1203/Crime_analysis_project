class userjoindto:

    def __init__(self, newuserid, newuserpw, newusername):
        self.userid = newuserid
        self.userpw = newuserpw
        self.username = newusername

    def getUserid(self):
        return self.userid

    def getUserpw(self):
        return self.userpw

    def getUsername(self):
        return self.username

    def __str__(self):
        return 'Id : ' + self.userid + 'PW : ' + self.userpw + 'Name : ' + self.username 

class logindto:

    def __init__(self, nid, npw):
        self.userid = nid
        self.userpw = npw

    def getNid(self):
        return self.userid

    def getNpw(self):
        return self.userpw
    
    def __str__(self):
        return 'Nid : ' + self.userid + 'Npw : ' + self.userpw