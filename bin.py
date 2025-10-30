def max_characters_removed(S):
    stack = []
    count_removed = 0
    
    for char in S:
        if stack and stack[-1] != char:
            stack.pop()
            count_removed += 2
        else:
            stack.append(char)
    
    return count_removed

# Test cases
print(max_characters_removed("aaabc"))   
print(max_characters_removed("aaaaa"))    
print(max_characters_removed("abcdefg"))