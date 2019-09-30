'''
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?
You are given a string P that denotes the new order of letters in the English dictionary. 
You need to print the smallest lexicographic string made from the given string S.

#####constraints#####
 1 <= T <= 1000
Length (P) = 26
1 <= length (S) <= 100
All characters in the string S, P are in lowercase

#####input_format#####
The first line contains number of test cases T
The second line has the string P
The third line has the string S


#####test_case#####
Example 1
Input
1
polikujmnhytgbvfredcxswqaz
abcd
Output
bcda
'''

n = int(input())
value=[] ;key = []
for i in range(n):
    value.append(input())
    key.append(input())
for i in range(n):
    index=[]
    s=''
    t = list(key[i])
    for j in t:
            index.append(value[i].index(j))
    index.sort()
    for j in index:
        s+=''.join(value[i][j])
print(s)
