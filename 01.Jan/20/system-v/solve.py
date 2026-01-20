# ターゲットとなる flag 配列のデータ (unsigned long = 8 bytes each)
flag_raw = [
    0x9beff28796ecf3e9, 0x2335ae47c5b3ea6a,
    0x7bd30354a9dfecfe, 0x3243804702b92b8c,
    0x7caad2839ae4bf07, 0x2749c14807c2e873,
    0xbcd9c683a3ebf11c, 0x4119a527d9aa0a73
]

# 1. flagデータを16bit (2バイト) ずつのリストに変換する (Little Endian)
target_u16 = []
for val in flag_raw:
    for i in range(4):
        target_u16.append((val >> (i * 16)) & 0xFFFF)

# 2. 逆演算を行う
# 各ブロック(8要素ごと)で k = 0..7 の加算回数が適用されている
ADD_VAL = (0x1dea * 0xcafe) & 0xFFFF
original_chars = []

for i, val in enumerate(target_u16):
    # k は 8要素周期でのインデックス
    k = i % 8

    # 加算回数の計算
    num_adds = 255 - (1 << k)

    # 逆演算: (目標値 - 加算合計) mod 0x10000
    total_added = (num_adds * ADD_VAL) & 0xFFFF
    orig = (val - total_added) & 0xFFFF

    # 16bitを2つの8bit(文字)に分解
    original_chars.append(orig & 0xFF)
    original_chars.append((orig >> 8) & 0xFF)

# 3. 文字列と出力
flag_str = "".join(map(chr, original_chars))
print(f"Flag: {flag_str}")
