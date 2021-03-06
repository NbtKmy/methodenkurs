import MeCab
import mojimoji
import itertools
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import japanize_matplotlib
# %matplotlib inline

with open('./kan_pk_all.txt') as f:
    kan_all = f.read()
    tekisuto0 = kan_all.replace('\n', '')
    tekisuto = mojimoji.zen_to_han(tekisuto0, kana=False)
    sents = tekisuto.split('。')

mecab = MeCab.Tagger('-d /usr/share/mecab/dic/mecab-ipadic-neologd -Ochasen')

nouns = [[v.split()[2] for v in mecab.parse(sen).splitlines() if (len(v.split())>=3 and v.split()[3][:2]=='名詞')] for sen in sents]




# create collocation list
pair_list = [
             list(itertools.combinations(n, 2))
             for n in nouns if len(nouns) >=2
             ]

all_pairs = []
for u in pair_list:
    all_pairs.extend(u)

# definition of stopwords
stopwords = ['これ', 'こと', 'ところ', 'もの', 'わけ', 'の', 'よう', '何', 'それ', 'ふう', 'とおり', '中', '月', '日', '年', '方', '形', '的', '私']

for stopword in stopwords:
    all_pairs = [s for s in all_pairs if stopword not in s]


cnt_pairs = Counter(all_pairs)



# pick up only top 100 pairs
tops = sorted(
    cnt_pairs.items(),
    key=lambda x: x[1], reverse=True
    )[:100]

noun_1 = []
noun_2 = []
frequency = [] # frequency of the edges
nodelist = []
node_freq = [] # frequency of the nodes ; the index position is parallel to nodelist

# create dataframe
for n,f in tops:
    noun_1.append(n[0])
    noun_2.append(n[1])
    frequency.append(f)

    if n[0] not in nodelist:
        nodelist.append(n[0])
        node_freq.append(f)

        if n[1] not in nodelist:
            nodelist.append(n[1])
            node_freq.append(f)

        elif n[1] in nodelist:
            dokodoko = nodelist.index(n[1])
            node_freq[dokodoko] = node_freq[dokodoko] + f

    elif n[0] in nodelist:
        doko = nodelist.index(n[0])
        node_freq[doko] = node_freq[doko] + f

        if n[1] not in nodelist:
            nodelist.append(n[1])
            node_freq.append(f)

        elif n[1] in nodelist:
            dokodoko = nodelist.index(n[1])
            node_freq[dokodoko] = node_freq[dokodoko] + f




df = pd.DataFrame({'prev_n': noun_1, 'aft_n': noun_2, 'freq': frequency})
weighted_edges = np.array(df)

# define the color intensity of the edge through frequency
max_freq = max(frequency)
edge_col = [(0, 0.5, 0, n/max_freq) for n in frequency]



# create the graph
G = nx.Graph()

G.add_weighted_edges_from(weighted_edges)

pos = nx.spring_layout(G, k=2)
plt.figure(figsize=(20,20))
nx.draw_networkx(G,
                 pos,
                 width=5,
                 nodelist = nodelist,
                 node_shape = 'o',
                 node_color = '#BC002D',
                 node_size = [nodes*50 for nodes in node_freq], # node size = frequency of the node
                 edge_color = edge_col, # color intensity = frequency of the edge
                 font_size = 18,
                 font_color='black',
                 font_family = 'IPAexGothic')

plt.savefig('kan_pk.png')
