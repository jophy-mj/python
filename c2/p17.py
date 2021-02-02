d={'manu':20,'arjun':19,'jancy':35}
l=list(d.items())
l.sort()
print("Ascending order:",l)
l=list(d.items())
l.sort(reverse=True)
print("Descending order:",l)
dict=dict(l)
print("Dictionary:",dict)
