from preproc import CleanSentence
from os.path import join
import os

base_path = join('data', 'lang_corpus', 'es')
os.makedirs(base_path, exist_ok=True)
with open(join(base_path, 'corpus.txt'), 'w', encoding='utf-8') as out:
    with open(join(base_path, 'wiki_sentences.txt'), 'r', encoding='utf-8') as f:
        i = 0
        print('Processing Spanish wiki_sentences...')
        for line in f:
            line = line.replace('\n', ' ').replace('\r', ' ').strip().replace('.', '.\n').replace('!', '!\n').replace('?', '?\n').strip()
            for l in line.split('\n'):
                l = CleanSentence(l)
                if l.count(' ') < 5:
                    continue
                out.write(l + '\n')
                # print(line)

                i += 1
                if i % 100000 == 0:
                    print(f'Processed {i} lines...', end='\r')
                    # break
            if i > 11000000:
                print(f'processed {i} lines')
                break
exit(0)

base_path = join('data', 'lang_corpus', 'en')
os.makedirs(base_path, exist_ok=True)
with open(join(base_path, 'corpus.txt'), 'w', encoding='utf-8') as out:
    with open(join(base_path, 'elsevier_oa.txt'), 'r', encoding='utf-8') as f:
        i = 0
        print('Processing Elsevier OA...')
        for line in f:
            i += 1
            if i % 100000 == 0:
                print(f'Processed {i} lines...', end='\r')
                # break
            line = line.replace('\n', ' ').replace('\r', ' ').replace('.', '.\n').replace('!', '!\n').replace('?', '?\n').strip()
            
            line = CleanSentence(line)
            if line.count(' ') < 5:
                continue
            out.write(line + '\n')

    with open(join('data', 'lang_corpus', 'en', 'wikibooks.txt'), 'r', encoding='utf-8') as f:
        i = 0
        print('Processing wikibooks...')
        text = f.read()
        text = text.replace('\n', ' ').replace('\r', ' ').replace('.', '.\n').replace('!', '!\n').replace('?', '?\n').strip()

        for line in text.split('\n'):
            i += 1
            if i % 10000 == 0:
                print(f'Processed {i} lines...', end='\r')
                # break
            line = CleanSentence(line)
            if line.count(' ') < 5:
                continue
            out.write(line + '\n')