s = "ABCDEFGHIJK"
print(s)
for i in range(len(s)):
    print("[", s[i], "]", sep="", end="")
print()  # Print newline

for ch in s:
    print("<", ch, ">", sep="", end="")
print()  # Print newline    
