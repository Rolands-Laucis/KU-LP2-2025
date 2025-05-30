from preproc import CleanSentence
from os.path import join

with open(join('data', 'lang_corpus', 'en', 'corpus.txt'), 'w', encoding='utf-8') as out:
    with open(join('data', 'lang_corpus', 'en', 'elsevier_oa.txt'), 'r', encoding='utf-8') as f:
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