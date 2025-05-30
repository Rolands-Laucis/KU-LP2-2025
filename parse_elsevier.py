# import os
import json
from glob import glob

i = 0

# Write all sentences to the output file
with open('./data/lang_corpus/en/elsevier_oa.txt', 'w', encoding='utf-8') as out:
    # Walk through the directory to find all JSON files
    files = glob('./data/lang_corpus/en/elsevier_oa/*.json')
    total_files = len(files)
    print(f"Total files to process: {total_files}")
    for file in files:
        with open(file, 'r', encoding='utf-8') as json_file:
            try:
                data = json.load(json_file)
                # Extract sentences from "body_text"
                if "body_text" in data:
                    for obj in data["body_text"]:
                        if "sentence" in obj:
                            s = obj["sentence"]
                            if len(s) > 50:
                                out.write(s + '\n')
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {file}")
        i += 1
        if i % 100 == 0:
            print(f"Processed {round(i*100/total_files, 2)}% files...", end='\r')
