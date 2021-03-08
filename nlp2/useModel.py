from gensim.models import word2vec

def useModel(w):

    model = word2vec.Word2Vec.load('tweetsOlympic.model')
    words = model.wv.most_similar(positive=[w])

    res = 'Similar words to ' + w
    for word in words:
        res = res + '\n' + word[0] + ': ' + str(word[1])

    print(res)

if __name__ == "__main__":
    useModel('コロナ')