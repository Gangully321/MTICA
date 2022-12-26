def extract_vowel(s):
    temp_vowel=''
    for i in s:
        print("i=",i)
        if i in 'AEIOUaeiou':
            print("i:",i,"temp_vowel:",temp_vowel)
    return temp_vowel
inp=input()
a=extract_vowel(inp)
print("vowels:",a)







    
