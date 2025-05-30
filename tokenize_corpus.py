from os.path import join
from collections import Counter
import json

counter = Counter()
corpus_path = join('data', 'lang_corpus', 'en', 'corpus.txt')

i = 0
with open(corpus_path, 'r', encoding='utf-8') as f:
    print('Building vocab...')
    for line in f:
        tokens = line.strip().split()
        counter.update(tokens)

        i += 1
        if i % 100000 == 0:
            print(f'Processed {i} lines...', end='\r')

    # Sort tokens by frequency and assign IDs
    sorted_tokens = [token for token, _ in counter.most_common()]
    vocab = {token:idx for idx, token in enumerate(sorted_tokens)}

    # Save vocab
    with open(join('data', 'lang_corpus', 'en', 'vocab.json'), 'w', encoding='utf-8') as f:
        json.dump(vocab, f, indent=2)

i = 0
with open(corpus_path, 'r', encoding='utf-8') as f:
    with open(join('data', 'lang_corpus', 'en', 'corpus_tokens.txt'), 'w', encoding='utf-8') as out:
        print('Tokenizing corpus...')
        for line in f:
            words = line.strip().split()
            token_ids = [str(vocab[w]) for w in words if w in vocab]
            out.write(" ".join(token_ids) + "\n")

            i += 1
            if i % 100000 == 0:
                print(f'Processed {i} lines...', end='\r')
