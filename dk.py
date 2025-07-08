#adding item in lists
lists=["apple","kiwi","banana"]
lists.append("orange")
print(lists)

#finding largest numer in the list

lar=[25,35,44,54,12,32]
largest =lar[0]
for num in lar:
    if num >largest:
        largest=num
print("the largest num is",largest)

#Iterate through a list of numbers and print only the positive ones

numbers=[-1,-2,-3,-4,3,5,6,7]
positive_numbers=[]
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)


#Reverse a list using a loop (without built-in functions).

number=[1,2,3,4,5]
for i in number[::-1]:
    print(i)
    
    
#Write a program to find the sum of all elements in a 2D list.

add=[1,2,3,4,5]
plus=0
for a in add:
    plus+=a
print(plus)

#Count the occurrences of a specific word in a list of strings.

def count_word_occurrences(word, string_list):
    word = word.lower()
    count = 0
    for s in string_list:
        # Split string into words and count occurrences
        words = s.lower().split()
        count += words.count(word)
    return count

# Example usage:
strings = ["This is a test", "This test is simple", "Test the function"]
word_to_count = "test"

print(count_word_occurrences(word_to_count, strings))

        




    

