def palindrome(word, index=0):
    if index == round(len(word) / 2):
        return f"{word} is a palindrome"
    else:
        if word[index] == word[len(word) - index - 1]:
            pass
        else:
            return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

