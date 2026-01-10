import sys
from Crypto.Util.number import isPrime, long_to_bytes

# 桁数制限を解除 (10万桁程度に設定)
sys.set_int_max_str_digits(100000)

# 1. output.txt から数値を自動で読み込む
data = {}
with open("output.txt") as f:
    for line in f:
        if "=" in line:
            name, value = line.split("=")
            data[name.strip()] = int(value.strip())

n = data["n"]
e = data["e"]
c = data["c"]

# 2. n を素因数分解して phi(n) を求める
temp_n = n
phi = 1
for p in range(2, 2026):
    if isPrime(p) and temp_n % p == 0:
        count = 0
        while temp_n % p == 0:
            count += 1
            temp_n //= p
        # p^count の phi は p^(count-1) * (p-1)
        phi *= (p**(count - 1)) * (p - 1)

# 3. 秘密鍵 d を求めて復号
d = pow(e, -1, phi)
m = pow(c, d, n)

# 4. フラグを表示
print(long_to_bytes(m).decode())
