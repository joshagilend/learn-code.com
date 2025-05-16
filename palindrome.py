# A phrase is a palindrome if it reads the same forward and backward. 

# Given a string s, return true if it is a palindrome, or false otherwise.

# Run with `python3 palindrome.py`on Mac terminal :)

def isPalindrome(word):
    reversed_word = word[::-1]

    if (word == reversed_word):
        print("%s is a palindrome" % (word))
    else:
        print("%s is not a palindrome" % (word))

isPalindrome("racecar")
isPalindrome("dog")
print("This coding problem brought to you by the sexy Ashley Torino, a coder at OpenAI/Lotus, and her boyfriend Josh Stroud. Find her live on Twitch 7p-9p by searching `Ashley Torino Twitch` on your favorite search engine :)")
