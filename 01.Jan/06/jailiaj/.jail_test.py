# 調査用：jail.py を一時的に書き換えてみる
s = input("> ")
print(f"DEBUG: s     = '{s}'")
print(f"DEBUG: rev_s = '{s[::-1]}'")
assert s == s[::-1], "Not a palindrome!"
eval(s)
