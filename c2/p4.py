def word_count(str):
    counts=dict()
    words=str.split()
    for w in words:
        if w in counts:
            counts[w]+=1
        else:
            counts[w]=1
    return counts
print(word_count('a friend in need is a friend in deed.'))

