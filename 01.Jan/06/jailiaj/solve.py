def make_palindrome_code(code):
    return code + "#" + code[::-1]

# 1. 実行したいコードを定義
code = 'print(open("flag.txt").read())'

# 2. Pythonに完全な回文を作らせる
payload = make_palindrome_code(code)

# 3. 確認
print(f"Payload: {payload}")
print(f"Is Pailndrome? : {payload == payload[::-1]}")
