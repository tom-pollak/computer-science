start:
	move RB 0x40 # start of file
	rol RB
	rol RB
	rol RB
	rol RB

	move RD 0x64 # start of destination file
	rol RD
	rol RD
	rol RD
	rol RD

loop:
	load RA (RB)
	rol RA
	rol RA
	rol RA
	store RA blue

	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	store RA red

	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	store RA green
	
	load RA blue
	and RA 0xF8 # get blue value
	store RA blue # store in acc
	
	load RA red
	and RA 0xF8 # get red value
	store RA red
	
	addm RA red
	addm RA red # red value * 3
	
	addm RA blue # + blue value
	
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
	rol RA
	rol RA
	store RA acc # ror 3
	
	load RA green
	and RA 0xFC # get green value
	
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
	rol RA
	rol RA
	rol RA
	rol RA # ror 1
	addm RA acc # acc (red * 3 + blue)>>3 + (green value)>>1
	store RA acc
	
	
	move RA RB # check to save or not using source bit address (% 2)
	and RA 0x01
	jumpnz save
	load RA acc
	store RA pix_val # save as lower bit
	jump increment
	
save:
	load RA acc
	rol RA # rotate pixel data to upper bit
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	rol RA
	store RA acc
	load RA pix_val
	addm RA acc  # save the two pixel values
	store RA (RD) # store pixel val
	
	move RA 0
	store RA pix_val # 0 pix_val
	add RD 1

increment:
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
pix_val:
	.data 0x00
end:
	.data 0x640
red:
	.data 0x00
green:
	.data 0x00
blue:
	.data 0x00