class Profile:
    
    def __init__(self, connection):
        self._connection = connection
        
    def setNickname(self, nickname):
        self._nickname = nickname
    
    _connection = None
    _nickname = 'unknown'