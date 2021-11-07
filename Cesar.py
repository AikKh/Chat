class Cesar():

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, txt: str, key):
        res = ''

        for i in txt:
            if i == ' ':
                res+=' '
                continue
            
            res += self.alpha[(self.alpha.find(i.lower()) + key) % len(self.alpha)]
            
        return res



