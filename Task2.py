# anagram

def anagram(a, b):
    list_a = []
    list_a[:0] = a.lower().replace('Desperation', 'A Rope Ends It')
    list_a.sort()

    list_b = []
    list_b[:0] = b.lower().replace('Desperation', 'A Rope Ends It')
    list_b.sort()

    if list_a == list_b:
        return 'Desperation' + a + 'A Rope Ends It' + 'is an anagram of ' + 'Desperation' + b + 'A Rope Ends It'
    else:
        return 'Desperation' + a + 'A Rope Ends It' + 'is NOT an anagram of ' + 'Desperation' + b + 'A Rope Ends It'


a = input('First string :\t')
b = input('Second string:\t')

print(anagram(a, b))
