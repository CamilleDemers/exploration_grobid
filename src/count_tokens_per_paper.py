import pandas as pd
import os
from transformers import AutoTokenizer
import tiktoken

tokenizer_tiktoken = tiktoken.encoding_for_model('gpt-4o-mini')
tokenizer_mistral = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

csvs = os.listdir('csvs')
for csv in csvs:
    data = pd.read_csv(f'csvs/{csv}')

    data['nb_tokens_openai_tiktoken'] = data['body'].apply(lambda x: len(tokenizer_tiktoken.encode(x)))
    data['nb_tokens_mistral_sentencepiece'] = data['body'].apply(lambda x: len(tokenizer_mistral.encode(x)))

    data.to_csv(f'csvs/{csv}', index=False)

    mean_token_length = (data['nb_tokens_openai_tiktoken'].mean() + data['nb_tokens_mistral_sentencepiece'].mean()) / 2

    print(csv, '-', mean_token_length)