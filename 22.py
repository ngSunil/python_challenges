# Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically.
s = input('Please enter the sentence: ')
s_list = s.split(' ')
my_dic = {}
for word in set(s_list):
    my_dic[word] = s_list.count(word)
print(my_dic.items())
print (dict(sorted(my_dic.items(), key=lambda item: item[0])))