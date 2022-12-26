def removeVowels(s):
    temp=''
    for i in s:
        if i not in 'AEIOUaeiou':
            temp+=i
    return temp
str1=input()
a=removeVowels(str1)
print("string",str1,"\nwithout vowel is ",a)







    
