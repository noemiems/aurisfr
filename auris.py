freq_threshold = 0
sound1 = 'y'
sound2 = 'u'
word_length = 5 #number of syllabless



import pandas as pd
import re

pdlex = pd.read_csv("Lexique383.tsv", sep='\t')
pdlex.to_csv('lexique.txt')

lexique = open("lexique.txt")
line = "XXX"
wordlist = []
pairlist = []

while line:
    line = lexique.readline()
    line.strip()
    if len(line) > 1:
        x = line.startswith(',ortho')
        if x == True:
            continue
        wordipa = line.split(',')[23]
        if 'E' in wordipa:
            wordipa = re.sub('E', 'ɛ', wordipa)
        if 'O' in wordipa:
            wordipa = re.sub('O', 'ɔ', wordipa)
        if 'R' in wordipa:
            wordipa = re.sub('R', 'r', wordipa)
        if 'Z' in wordipa:
            wordipa = re.sub('Z', 'ʒ', wordipa)
        if '°' in wordipa:
            wordipa = re.sub('°', 'ə', wordipa)
        if '9' in wordipa:
            wordipa = re.sub('9', 'œ', wordipa)
        word = line.split(',')[1]
        freqfilm = line.split(',')[7]
        if '.' in freqfilm:
            freq = float(freqfilm)
            wordlist.append([wordipa, word, freq])
            if freq >= float(freq_threshold):
                if len(re.findall('[-]', wordipa)) < word_length :
                    if sound1 in wordipa:
                        savedb = word
                        new = re.sub(sound1, sound2, wordipa)
                        for x in range(len(wordlist)):
                            for item in wordlist[x]:
                                if new == item:
                                    pair = [savedb, [wordlist[x][1], wordlist[x][2]]]
                                    if pair in pairlist :
                                        continue
                                    else:
                                        pairlist.append([savedb, wordlist[x][1]])
                                        print(savedb, freq, ',', wordlist[x][1], wordlist[x][2])
