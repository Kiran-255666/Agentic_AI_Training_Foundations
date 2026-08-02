import re            # lets us split and search text using patterns
import collections   # gives us defaultdict, handy for counting things later

text_corpus = (  # the raw block of text this whole script works on
    "Remote work is highly productive. The organization supports Slack, Microsoft Teams, "
    "and other tools! However, IT security requires a corporate VPN. Don't connect "
    "on public Wi-Fi."
)

print("Part 1: Sentence Segmentation")
sentences = re.split(r'(?<=[.!?])\s+', text_corpus)  # split after . ! or ? followed by a space, keeping the punctuation attached
for idx, sentence in enumerate(sentences):
    print(f"Sentence {idx+1}: {sentence}")

print("\nPart 2: Word Tokenization")  # \n adds a blank line so this section is visually separate
target_sentence = sentences[1]  # pick sentence 2 (index 1) to run tokenization tests on
print(f"Target: '{target_sentence}'")
naive_tokens = target_sentence.split()  # the simplest possible tokenizer: just split on whitespace
print(f"Naive Tokens ({len(naive_tokens)}): {naive_tokens}")

regex_tokens = re.findall(r"\w+(?:'\w+)?|[.!?,]", target_sentence)  # grabs words (keeping contractions like don't whole) and punctuation as separate tokens
print(f"Regex Tokens ({len(regex_tokens)}): {regex_tokens}")

print("\nPart 3: Normalization & Stopword Removal")
stopwords = {"is", "and", "other", "a", "on"}  # small, common words we don't care about for this exercise
normalized_tokens = [token.lower() for token in regex_tokens]  # lowercase everything so 'The' and 'the' count as the same word
cleaned_tokens = [
    token for token in normalized_tokens
    if token not in stopwords and token.isalnum()  # drop stopwords and drop anything that isn't purely letters/numbers (so punctuation gets removed here)
]
print(f"Original Regex Tokens: {regex_tokens}")
print(f"Cleaned Tokens: {cleaned_tokens}")

print("\nPart 4: Byte Pair Encoding (BPE) Concept")
word_corpus = [  # each word broken into single characters, with </w> marking the end of the word
    "l o o k </w>",
    "l o o k s </w>",
    "l o o k i n g </w>",
    "c o o k </w>"
]
print(f"Initial Vocabulary: {word_corpus}")


def get_pair_statistics(corpus):
    # counts how often every neighboring pair of symbols shows up across all words
    pairs = collections.defaultdict(int)  # stores pair frequencies
    for word in corpus:
        symbols = word.split()  # break the word back into its individual symbols
        for i in range(len(symbols) - 1):  # walk through the word one pair at a time
            pairs[(symbols[i], symbols[i + 1])] += 1  # tally this pair
    return pairs


def merge_character_pair(pair, corpus):
    # takes the winning pair and glues it together everywhere it appears
    merged_corpus = []
    bigram = ' '.join(pair)        # rebuild the pair as it currently looks, e.g. 'o o'
    merged_str = ''.join(pair)     # and how it should look after merging, e.g. 'oo'
    pattern = re.compile(r'(?<!\S)' + re.escape(bigram) + r'(?!\S)')  # only match the pair as whole tokens, not inside longer symbols
    for word in corpus:
        new_word = pattern.sub(merged_str, word)
        merged_corpus.append(new_word)
    return merged_corpus


num_merges = 3  # run three merge rounds to watch "look" gradually form
for i in range(num_merges):
    pair_stats = get_pair_statistics(word_corpus)
    if not pair_stats:
        break
    best_pair = max(pair_stats, key=pair_stats.get)  # pick the most frequent pair this round
    word_corpus = merge_character_pair(best_pair, word_corpus)
    print(f"Iteration {i+1}: merges {best_pair}, frequency {pair_stats[best_pair]} -> {word_corpus}")