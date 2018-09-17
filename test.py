l = [ x*x for x in range(1,11) if x % 2 == 0]
print(l)

l = [ x+y for x in '123' for y in '123' if x != y]
print(l)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
