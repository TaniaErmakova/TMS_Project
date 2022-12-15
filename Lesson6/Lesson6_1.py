b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode("utf-8")
print(s)
l = s.encode("Latin1")
print(l)
m = l.decode("Latin1")
print(m)
