start:
	move RB 0x40 # start of file
	rol RB
	rol RB
	rol RB
	rol RB

loop:
	load RA (RB)
	store RA nibble1
	
	rol RA
	rol RA
	rol RA
	rol RA # rotate 4th nibble to start
	store RA nibble4
	
	rol RA
	rol RA
	rol RA
	rol RA # rotate 3rd nibble to start
	store RA nibble3

	rol RA
	rol RA
	rol RA
	rol RA # move 2nd nibble to start position
	store RA nibble2
	
	
	load RA nibble2
	and RA 0x0F
	store RA acc
	
	load RA nibble1
	and RA 0x0F # get first nibble
	rol RA
	rol RA
	rol RA
	rol RA # move to 2nd position
	addm RA acc
	store RA acc

	load RA nibble4
	and RA 0xF
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA # move to 3rd position
	addm RA acc
	store RA acc
	
	load RA nibble3
	and RA 0xF
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA # move to 4th position
	addm RA acc
	store RA acc
	
	move RA 0xFF
	
	subm RA acc
	store RA (RB) # store pixel
	
	add RB 1
	move RA RB
	subm RA end # if pixel pointer reaches EOF
	jumpz trap
	jump loop

trap:
	move RA 0x00
	store RA 0xFFF
	jump trap

acc:
	.data 0x00
end:
	.data 0x640
nibble1:
	.data 0x00
nibble2:
	.data 0x00
nibble3:
	.data 0x00
nibble4:
	.data 0x00