require 'prime'

# ターゲットとなる文字列
target = "Coufhlj@bixm|UF\\JCjP^P<".bytes

# 23個の素数
primes = Prime::Generator23.new.take(23)

# 逆算 (Target XOR Primes)
flag = target.zip(primes).map { |t, p| (t ^ p).chr }.join

puts flag
