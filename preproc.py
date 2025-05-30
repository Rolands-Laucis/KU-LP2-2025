import re

def CleanSentence(s:str) -> str:
    s = s.strip().lower()
    # remove links
    s = re.sub(r'http[s]?://\S+', '', s)
    # remove xml tags and their content
    s = re.sub(r'<[^>]+>', '', s)
    # replace numbers with 0
    s = re.sub(r'\d+', '0', s)
    # s = re.sub(r'([\.,!?;:\/\\\(\)\[\]\{\}\<\>@#$%^&*])', r'  \1', s)
    # seperate punctuation and special chars with a space
    # s = re.sub(r'([^\w])', r'  \1 ', s)
    s = re.sub(r'[^a-z0-9\s]', '', s)
    # space folding
    s = re.sub(r'\s\s+', ' ', s)
    
    return s.strip()