from os.path import join
import os
import pickle
from collections import Counter

for n in range(2, 6):
    c = Counter()
    l = 0
    print(f'Training {n}-gram model...')

    # load corpus
    with open(join('data', 'lang_corpus', 'en', 'corpus_tokens.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            # read tokens from the file
            tokens = list(map(int, line.strip().split()))
            
            # pad tokens for n-gram generation
            tokens = [-1] * (n - 1) + tokens + [-1] * (n - 1) #pad with the -1 token, bcs i want the ngram model to handle sentence boundaries

            # create examples for n-grams by sliding a window of size n
            for i in range(n, len(tokens) + 1):
                ngram = tuple(tokens[i - n:i])
                c[ngram] += 1
            
            l += 1
            if l % 100000 == 0:
                print(f'Processed {l} lines...', end='\r')

            # if l > 5000000:
            #     print('ran into max lines')
            #     break
            # exit(0)

    # Save the model
    output_dir = join('models', 'ngrams')
    os.makedirs(output_dir, exist_ok=True)
    model_path = join(output_dir, f'{n}-gram.pkl')
    with open(model_path, 'wb') as model_file:
        pickle.dump(c, model_file)
    print(f'Model saved to {model_path}')