start:
    load RA red_val
	store RA 0x52B
	store RA 0x512
	store RA 0x514
	store RA 0x513
	store RA 0x4FB

    move RA 0x00
    store RA 0xfff

end:
    jump end
red_val:
	.data 0xF800