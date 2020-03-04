class Affine(object):
    DIE = 128
    KEY = None

    def __init__(self):
        pass

    def encryptChar(self, char):
        K1, K2, kI = self.KEY
        return chr((K1 * ord(char) + K2) % self.DIE)

    def encrypt(self, string, key):
        self.KEY = key
        return "".join(map(self.encryptChar, string))

    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        return chr(KI * (ord(char) - K2) % self.DIE)

    def decrypt(self, string, key):
        self.KEY = key
        return "".join(map(self.decryptChar, string))
