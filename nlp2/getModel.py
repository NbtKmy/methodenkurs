from gensim.models import word2vec
import logging

def createModel(corp):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = word2vec.LineSentence(corp)
    model = word2vec.Word2Vec(sentences,
        sg=1,
        size=100,
        min_count=1,
        window=10,
        hs=1) # # use skip-gram & hierarchical softmax
    
    model.save('tweetsOlympic.model')

if __name__ == "__main__":
    createModel('tweetsCorpus.txt')

