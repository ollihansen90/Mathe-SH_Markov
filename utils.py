import random

class Markov():
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.back = len(list(dictionary.keys())[0].split(","))

    def generate(self, start="0"):
        key = self.back*"<,"[:-1]
        name = self.back*["<"]
        while key!=">":
            next_keys = self.dictionary[generate_key(name[-self.back:])]
            valliste = []
            keyliste = []
            for dictkey in next_keys.keys():
                valliste.append(next_keys[dictkey])
                keyliste.append(dictkey)
            summe = 0
            cumsum = []
            for eintrag in valliste:
                summe += eintrag
                cumsum.append(summe)
            n = random.randint(0,summe)
            i = 0
            while n>cumsum[i]:
                i += 1
            key = keyliste[i]
            name += [key]
        return name[self.back:-1]


def get_sentence(liste, lookup):
    satz = ""
    for wort in liste:
        satz += lookup["i2w"][wort] + " "
    return satz


def generate_key(keylist):
    return ",".join([str(k) for k in keylist])
