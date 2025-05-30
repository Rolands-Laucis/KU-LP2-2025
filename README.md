---
language:
- en
- uk
- ru
- de
- zh
- am
- ar
- hi
- es
- it
- fr
- he
- ja
- tt
license: openrail++
size_categories:
- 10K<n<100K
task_categories:
- text-generation
dataset_info:
  features:
  - name: toxic_sentence
    dtype: string
  - name: neutral_sentence
    dtype: string
  splits:
  - name: en
    num_bytes: 47435
    num_examples: 400
  - name: ru
    num_bytes: 89453
    num_examples: 400
  - name: uk
    num_bytes: 78106
    num_examples: 400
  - name: de
    num_bytes: 86818
    num_examples: 400
  - name: es
    num_bytes: 56868
    num_examples: 400
  - name: am
    num_bytes: 133489
    num_examples: 400
  - name: zh
    num_bytes: 79089
    num_examples: 400
  - name: ar
    num_bytes: 85237
    num_examples: 400
  - name: hi
    num_bytes: 107518
    num_examples: 400
  download_size: 489288
  dataset_size: 764013
configs:
- config_name: default
  data_files:
  - split: en
    path: data/en-*
  - split: ru
    path: data/ru-*
  - split: uk
    path: data/uk-*
  - split: de
    path: data/de-*
  - split: es
    path: data/es-*
  - split: am
    path: data/am-*
  - split: zh
    path: data/zh-*
  - split: ar
    path: data/ar-*
  - split: hi
    path: data/hi-*
tags:
- toxic
---
**Multilingual Text Detoxification with Parallel Data**

[![COLING2025](https://img.shields.io/badge/COLING%202025-b31b1b)](https://aclanthology.org/2025.coling-main.535/) 
[![CLEF2024](https://img.shields.io/badge/CLEF%202024-b31b1b)](https://ceur-ws.org/Vol-3740/paper-223.pdf) 

This is the multilingual parallel dataset for the text detoxification task. Prepared for TextDetox Shared Task. 

📰 **Updates**

**[2025]** The second edition of TextDetox shared task! [webpage](https://pan.webis.de/clef25/pan25-web/text-detoxification.html)

**[2025]** We extend our data to new languages! Now also included: Italian, French, Hebrew, Hinglish, Japanese, Tatar. Check our [test](https://huggingface.co/datasets/textdetox/multilingual_paradetox_test) part.

**[2025]** We dived into the explainability of our data in our new [COLING paper](https://huggingface.co/papers/2412.11691)!

**[2024]** You can check additional releases for [Ukrainian ParaDetox](https://huggingface.co/datasets/textdetox/uk_paradetox) and [Spanish ParaDetox](https://huggingface.co/datasets/textdetox/es_paradetox) from NAACL 2024!

**[2024]** **April, 23rd, update: We are realsing the parallel train set! The test part for the final phase of the competition is available [here](https://huggingface.co/datasets/textdetox/multilingual_paradetox_test)!!!**

**[2022]** You can also check previously created training corpora: [English ParaDetox](https://huggingface.co/datasets/s-nlp/paradetox) from ACL 2022 and [Russian ParaDetox](https://huggingface.co/datasets/s-nlp/ru_paradetox).

**[2022]** The first release for [CLEF TextDetox 2024](https://pan.webis.de/clef24/pan24-web/text-detoxification.html) shared task.
For each of 9 languages, we collected 1k pairs of toxic<->detoxified instances splitted into two parts: dev (400 pairs) and test (600 pairs).

## Toxic Samples Sources

The list of the sources for the original toxic sentences:
* English: [Jigsaw](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge), [Unitary AI Toxicity Dataset](https://github.com/unitaryai/detoxify)
* Russian: [Russian Language Toxic Comments](https://www.kaggle.com/datasets/blackmoon/russian-language-toxic-comments), [Toxic Russian Comments](https://www.kaggle.com/datasets/alexandersemiletov/toxic-russian-comments)
* Ukrainian: [Ukrainian Twitter texts](https://github.com/saganoren/ukr-twi-corpus)
* Spanish: [Detecting and Monitoring Hate Speech in Twitter](https://www.mdpi.com/1424-8220/19/21/4654), [Detoxis](https://rdcu.be/dwhxH), [RoBERTuito: a pre-trained language model for social media text in Spanish](https://aclanthology.org/2022.lrec-1.785/)
* German: [GemEval 2018, 2021](https://aclanthology.org/2021.germeval-1.1/)
* Amhairc: [Amharic Hate Speech](https://github.com/uhh-lt/AmharicHateSpeech)
* Arabic: [OSACT4](https://edinburghnlp.inf.ed.ac.uk/workshops/OSACT4/)
* Hindi: [Hostility Detection Dataset in Hindi](https://competitions.codalab.org/competitions/26654#learn_the_details-dataset), [Overview of the HASOC track at FIRE 2019: Hate Speech and Offensive Content Identification in Indo-European Languages](https://dl.acm.org/doi/pdf/10.1145/3368567.3368584?download=true)
* Italian: [AMI](https://github.com/dnozza/ami2020), [HODI](https://github.com/HODI-EVALITA/HODI_2023), [Jigsaw Multilingual Toxic Comment](https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification/overview)
* French: [FrenchToxicityPrompts](https://europe.naverlabs.com/research/publications/frenchtoxicityprompts-a-large-benchmark-for-evaluating-and-mitigating-toxicity-in-french-texts/), [Jigsaw Multilingual Toxic Comment](https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification/overview)
* Hebrew: [Hebrew Offensive Language Dataset](https://github.com/NataliaVanetik/HebrewOffensiveLanguageDatasetForTheDetoxificationProject/tree/main)
* Hinglish: [Hinglish Hate Detection](https://github.com/victor7246/Hinglish_Hate_Detection/blob/main/data/raw/trac1-dataset/hindi/agr_hi_dev.csv)
* Japanese: posts from [2chan](https://huggingface.co/datasets/p1atdev/open2ch)
* Tatar: ours.

## Citation
If you would like to acknowledge our work, please, cite the following manuscripts:

```
@inproceedings{dementieva-etal-2025-multilingual,
    title = "Multilingual and Explainable Text Detoxification with Parallel Corpora",
    author = "Dementieva, Daryna  and
      Babakov, Nikolay  and
      Ronen, Amit  and
      Ayele, Abinew Ali  and
      Rizwan, Naquee  and
      Schneider, Florian  and
      Wang, Xintong  and
      Yimam, Seid Muhie  and
      Moskovskiy, Daniil Alekhseevich  and
      Stakovskii, Elisei  and
      Kaufman, Eran  and
      Elnagar, Ashraf  and
      Mukherjee, Animesh  and
      Panchenko, Alexander",
    editor = "Rambow, Owen  and
      Wanner, Leo  and
      Apidianaki, Marianna  and
      Al-Khalifa, Hend  and
      Eugenio, Barbara Di  and
      Schockaert, Steven",
    booktitle = "Proceedings of the 31st International Conference on Computational Linguistics",
    month = jan,
    year = "2025",
    address = "Abu Dhabi, UAE",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.coling-main.535/",
    pages = "7998--8025",
    abstract = "Even with various regulations in place across countries and social media platforms (Government of India, 2021; European Parliament and Council of the European Union, 2022), digital abusive speech remains a significant issue. One potential approach to address this challenge is automatic text detoxification, a text style transfer (TST) approach that transforms toxic language into a more neutral or non-toxic form. To date, the availability of parallel corpora for the text detoxification task (Logacheva et al., 2022; Atwell et al., 2022; Dementieva et al., 2024a) has proven to be crucial for state-of-the-art approaches. With this work, we extend parallel text detoxification corpus to new languages{---}German, Chinese, Arabic, Hindi, and Amharic{---}testing in the extensive multilingual setup TST baselines. Next, we conduct the first of its kind an automated, explainable analysis of the descriptive features of both toxic and non-toxic sentences, diving deeply into the nuances, similarities, and differences of toxicity and detoxification across 9 languages. Finally, based on the obtained insights, we experiment with a novel text detoxification method inspired by the Chain-of-Thoughts reasoning approach, enhancing the prompting process through clustering on relevant descriptive attributes."
}
```

```
@inproceedings{dementieva2024overview,
  title={Overview of the Multilingual Text Detoxification Task at PAN 2024},
  author={Dementieva, Daryna and Moskovskiy, Daniil and Babakov, Nikolay and Ayele, Abinew Ali and Rizwan, Naquee and Schneider, Frolian and Wang, Xintog and Yimam, Seid Muhie and Ustalov, Dmitry and Stakovskii, Elisei and Smirnova, Alisa and Elnagar, Ashraf and Mukherjee, Animesh and Panchenko, Alexander},
  booktitle={Working Notes of CLEF 2024 - Conference and Labs of the Evaluation Forum},
  editor={Guglielmo Faggioli and Nicola Ferro and Petra Galu{\v{s}}{\v{c}}{\'a}kov{\'a} and Alba Garc{\'i}a Seco de Herrera},
  year={2024},
  organization={CEUR-WS.org}
}
```

```
@inproceedings{DBLP:conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24,
  author       = {Janek Bevendorff and
                  Xavier Bonet Casals and
                  Berta Chulvi and
                  Daryna Dementieva and
                  Ashaf Elnagar and
                  Dayne Freitag and
                  Maik Fr{\"{o}}be and
                  Damir Korencic and
                  Maximilian Mayerl and
                  Animesh Mukherjee and
                  Alexander Panchenko and
                  Martin Potthast and
                  Francisco Rangel and
                  Paolo Rosso and
                  Alisa Smirnova and
                  Efstathios Stamatatos and
                  Benno Stein and
                  Mariona Taul{\'{e}} and
                  Dmitry Ustalov and
                  Matti Wiegmann and
                  Eva Zangerle},
  editor       = {Nazli Goharian and
                  Nicola Tonellotto and
                  Yulan He and
                  Aldo Lipani and
                  Graham McDonald and
                  Craig Macdonald and
                  Iadh Ounis},
  title        = {Overview of {PAN} 2024: Multi-author Writing Style Analysis, Multilingual
                  Text Detoxification, Oppositional Thinking Analysis, and Generative
                  {AI} Authorship Verification - Extended Abstract},
  booktitle    = {Advances in Information Retrieval - 46th European Conference on Information
                  Retrieval, {ECIR} 2024, Glasgow, UK, March 24-28, 2024, Proceedings,
                  Part {VI}},
  series       = {Lecture Notes in Computer Science},
  volume       = {14613},
  pages        = {3--10},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-56072-9\_1},
  doi          = {10.1007/978-3-031-56072-9\_1},
  timestamp    = {Fri, 29 Mar 2024 23:01:36 +0100},
  biburl       = {https://dblp.org/rec/conf/ecir/BevendorffCCDEFFKMMPPRRSSSTUWZ24.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

# Corresponding Contact

[Daryna Dementieva](https://huggingface.co/dardem)