

char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']

sentence = 'Welcome Back to This Tutorial'

print(set(char_list))
print(set(sentence))

print(set(char_list + list(sentence)))

unique_char =set(char_list)
unique_char.add('x')
print(unique_char)

unique_char.remove('x')
print(unique_char)
unique_char.discard('d')
print(unique_char)
#####remove 和discard区别： 如果set中不存在，remove出错，discard不出错
unique_char.clear()
print(unique_char)

unique_char = set(char_list)
print(unique_char.difference({'a','e','i'}))
print(unique_char.intersection({'a','e','i'}))