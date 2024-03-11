# NECESSÁRIO INSTALAR O DATASET: pip install datasets
# ESSA FUNÇÃO SERVE PARA CRIAR UM DICIONÁRIO COM AS PALAVRAS E SUAS RESPECTIVAS POS_TAGS BASEADO NO DATASET MAC_MORPHO
# https://huggingface.co/datasets/mac_morpho
# https://medium.com/turing-talks/pos-tagging-da-teoria-%C3%A0-implementa%C3%A7%C3%A3o-eafa59c9d115

from datasets import load_dataset
import os

print("Loading dataset...")

dataset = load_dataset("mac_morpho", trust_remote_code=True)

print("===== DONE =====")

DATASET_TYPE = "train"
OUTPUT_FILE = f"datasets/dict_{DATASET_TYPE}.csv"

UNWANTED_TOKENS = [",", ".", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", '"', "'"]

df = dataset[DATASET_TYPE].to_pandas()

# Remove file if it already exists
if os.path.exists(OUTPUT_FILE):
    print(f"Found {OUTPUT_FILE}, removing...")
    os.remove(OUTPUT_FILE)
    print("===== DONE =====")

print(f"Saving {len(df)} phrases...")

# Save all words with post_tag
for i, row in df.iterrows():

    tokens = row["tokens"]
    pos_tags = row["pos_tags"]

    for token, pos_tag in zip(tokens, pos_tags):
        if token in UNWANTED_TOKENS:
            continue

        with open(OUTPUT_FILE, "a") as f:
            f.write(f"{token}|{pos_tag}\n")

print("===== DONE =====")

# Remove duplicates by joining all the pos_tags for each word
with open(OUTPUT_FILE, "r") as f:
    lines = f.readlines()

    words = {}

    print(f"Joining duplicates words from {len(lines)} lines...")

    for i, line in enumerate(lines):

        word, pos_tag = line.split("|")

        if word not in words:
            words[word] = pos_tag.strip()
        elif pos_tag.strip() not in words[word]:
            words[word] += f",{pos_tag.strip()}"

    print(f"Reduced from {len(lines)} to {len(words)} words")


with open(OUTPUT_FILE, "w") as f:
    for word, pos_tag in words.items():
        f.write(f"{word}|{pos_tag}\n")

print("===== DONE =====")
