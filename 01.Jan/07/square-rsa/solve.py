from Crypto.Util.number import long_to_bytes
import math

# output.txt から値を読み込む
data = {}
with open("output.txt", "r") as f:
    for line in f:
        if "=" in line:
            key, val = line.split("=")
            data[key.strip()] = int(val.strip())

n = data["n"]
c = data["c"]
e = 65537

# n = p^2 なので平方根で p を取得
p = math.isqrt(n)

# n = p^k の場合のオイラー関数 phi(n) = p^(k-1) * (p-1)
phi = p * (p - 1)

# 秘密鍵 d の計算と復号
d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m).decode())
