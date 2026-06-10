# Automatic Next Word Prediction using Bigram Model (Using File)

import nltk
from nltk.util import ngrams
from collections import Counter
import string

# --------------------------
# 1. Read Text from File
# --------------------------

# Make sure you have a file named "data.txt" in the same folder
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# --------------------------
# 2. Text Preprocessing
# --------------------------

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize (split into words)
tokens = text.split()

# --------------------------
# 3. Create Bigrams
# --------------------------
bigrams = list(ngrams(tokens, 2))
# Count frequency of bigrams
bigram_freq = Counter(bigrams)

# --------------------------
# 4. Prediction Function
# --------------------------

def predict_next_word(word):
    candidates = [pair for pair in bigram_freq if pair[0] == word]
    
    if not candidates:
        return "No prediction available"
    
    # Select the most frequent next word
    next_word = max(candidates, key=lambda pair: bigram_freq[pair])[1]
    return next_word

# --------------------------
# 5. User Input Loop
# --------------------------

print("\n--- Automatic Next Word Prediction ---")
print("Type 'exit' to stop\n")

while True:
    user_input = input("Enter a word: ").lower()
    
    if user_input == "exit":
        print("Program stopped.")
        break
    
    prediction = predict_next_word(user_input)
    print("Predicted next word:", prediction)
    print()