def reverse_words_in_string(string1):
    words=string1.split(" ")
    result = ' '.join(words[::-1])
    return result
print(reverse_words_in_string(string1=""))