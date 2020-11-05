s = input('Enter the sentence:')
words = s.split()
n_words = []

for word in words:
    if word[-1]=='.':
        n_words.append((word[:-1][::-1]+'.'))
    else:
        n_words.append(word[::-1])

print(' '.join(n_words))