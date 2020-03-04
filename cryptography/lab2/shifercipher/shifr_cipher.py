class ShiferCipher:
    llst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']
    blst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z']

    def encryptCaesar(self, msg, shift):
        ret = ""
        for x in msg:
            if x in self.llst:
                ind = self.llst.index(x) % len(self.llst)
                ret += self.llst[(ind + shift) % len(self.llst)]
            elif x in self.blst:
                ind = self.blst.index(x) % len(self.llst)
                ret += self.blst[(ind + shift) % len(self.llst)]
            else:
                ret += x
        return ret

    def decryptCaesar(self, msg, shift):
        ret = ""
        for x in msg:
            if x in self.llst:
                ind = self.llst.index(x)
                ret += self.llst[ind - shift]
            elif x in self.blst:
                ind = self.blst.index(x)
                ret += self.blst[ind - shift]
            else:
                ret += x
        return ret
