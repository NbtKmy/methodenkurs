import pandas as pd
import mojimoji



def getCorpus(csv_data):
    df = pd.read_csv(csv_data)
    txt_list = list(df['text'])

    corpus = ""
    for txt in txt_list:
        if type(txt) == float: # NaN soll nicht reinkommen
            continue
        else:
            corpus += str(txt)
    
    corpus = corpus.replace('\n', '')
    newCorpus = mojimoji.zen_to_han(corpus, kana=False)
    # print(newCorpus)
    with open('tweets_reinText.txt', mode='w') as f:
        f.write(newCorpus)

if __name__ == "__main__":
    getCorpus('tweetsdata.csv')