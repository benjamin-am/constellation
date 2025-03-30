import os
import re
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from typing import Dict, List, Counter as CounterType



def markdown_plaintext(file_path: str) -> List[str]:
    # Read the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()  # Read line by line
    return content

