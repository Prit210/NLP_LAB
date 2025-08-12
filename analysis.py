# Corpus Statistics Calculation

# Read tokenized files
with open("sentences.txt", 'r', encoding='utf-8') as f:
    tokenized_sentences = [line.strip() for line in f if line.strip()]

with open("words.txt", 'r', encoding='utf-8') as f:
    tokenized_words = [line.strip() for line in f if line.strip()]


# i. Total number of sentences
total_sentences = len(tokenized_sentences)

# ii. Total number of words
total_words = len(tokenized_words)

# iii. Total number of characters (excluding whitespace)
total_characters = sum(len(token) for token in tokenized_words)

# iv. Average Sentence Length
avg_sentence_length = total_words / total_sentences if total_sentences else 0

# v. Average Word Length
avg_word_length = total_characters / total_words if total_words else 0

# vi. Type/Token Ratio
unique_tokens = len(set(tokenized_words))
ttr = unique_tokens / total_words if total_words else 0

# 📊 Print Results
print(" Statistics")
print(f"Total Sentences           : {total_sentences}")
print(f"Total Words               : {total_words}")
print(f"Total Characters          : {total_characters}")
print(f"Average Sentence Length   : {avg_sentence_length:.2f} words/sentence")
print(f"Average Word Length       : {avg_word_length:.2f} chars/word")
print(f"Type/Token Ratio (TTR)    : {ttr:.4f}")
