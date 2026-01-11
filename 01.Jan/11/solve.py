import hashlib
import string
import re
import ast

# 1. original_code.py の中身を読み込む
with open('original_code.py', 'r') as f:
    content = f.read()

# 
try:
    actual_code = ast.literal_eval(content.strip())
    if isinstance(actual_code, bytes):
        actual_code = actual_code.decode()
except:
    actual_code = content

# 2. 正規表現でリスト h の中身 (ハッシュ値のリスト) を抽出する
# 文字列中の['hash', 'hash', ...]の部分を探します
match = re.search(r"h\s*=\s*(\[.*?\])", actual_code, re.DOTALL)
if not match:
    print("ハッシュリストが見つかりませんでした。")
    exit()

#
h = ast.literal_eval(match.group(1))

# 文字列のリストに変換
# h_raw = match.group(1)
# h = [val.strip().strip("'") for val in h_raw.split(',')]

# 3. ハッシュの逆引き辞書を作成
chars = string.ascii_lowercase + "_"
lookup = {hashlib.sha256(c.encode()).hexdigest(): c for c in chars}

# 4. フラグを復元
flag_content = "".join([lookup[val] for val in h])
print(f"Alpaca{{{flag_content}}}")
