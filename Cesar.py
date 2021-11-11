class Cesar():

    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    
    def keySign(self, key):
        if key > 0:
            return 1
        elif key < 0:
            return -1
        else:
            return 0

    def encrypt(self, txt: str, key):
        res = ''

        for i in txt:
            if i == ' ':
                res+=' '
                continue
            
            res += self.alpha[(self.alpha.find(i) + (key + self.keySign(key))) % len(self.alpha)]
            
        return res

    




