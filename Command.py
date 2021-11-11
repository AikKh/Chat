import jsonpickle
from Cesar import Cesar

class Command(object):
    
    cesar = Cesar()
    
    def __init__(self, cmd : str, msg : str):
        self._cmd = cmd
        self._msg = self.cesar.encrypt(msg, 1)
    
    _cmd = None
    _msg = None
    
    @staticmethod
    def CreateCommand(cmd, msg):
        
        command = Command(cmd, msg)
        return jsonpickle.encode(command)
    
    
    def getMessage(self):
        return self.cesar.encrypt(self._msg, -1) 
                
        
        