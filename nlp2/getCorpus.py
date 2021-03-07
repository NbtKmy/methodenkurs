import pandas as pd
import re
import MeCab


def getCorpus(csv_data):
    df = pd.read_csv(csv_data)
    txt_list = list(df['text'])

    corpus = ""
    for txt in txt_list:
        if type(txt) == float: # NaN soll nicht reinkommen
            continue
        else:
            corpus += str(txt)
    
    wakati = MeCab.Tagger('-F"%f[6] "  -U"%m " -E"\n" -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd') 
    newCorpus = wakati.parse(corpus)
    # print(newCorpus)
    with open('tweetsCorpus.txt', mode='w') as f:
        f.write(newCorpus)

if __name__ == "__main__":
    getCorpus('tweetsdata.csv')