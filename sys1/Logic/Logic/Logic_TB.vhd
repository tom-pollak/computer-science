
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Logic_Logic_sch_tb IS
END Logic_Logic_sch_tb;
ARCHITECTURE behavioral OF Logic_Logic_sch_tb IS 

   COMPONENT Logic
   PORT(           
		A	      :	IN	STD_LOGIC; 
      B	      :	IN	STD_LOGIC; 
      BUF_GATE	:	OUT	STD_LOGIC;       
		NOT_GATE	:	OUT	STD_LOGIC; 
      AND_GATE	:	OUT	STD_LOGIC;       
		OR_GATE	:	OUT	STD_LOGIC; 
      XOR_GATE	:	OUT	STD_LOGIC;       
		NAND_GATE:	OUT	STD_LOGIC; 
		NOR_GATE	:	OUT	STD_LOGIC; 
      XNOR_GATE:	OUT	STD_LOGIC);  
   END COMPONENT;

	SIGNAL A : STD_LOGIC; 
   SIGNAL B : STD_LOGIC; 
		
   SIGNAL BUF_GATE	: STD_LOGIC;       
	SIGNAL NOT_GATE	: STD_LOGIC; 
   SIGNAL AND_GATE	: STD_LOGIC;       
	SIGNAL OR_GATE	   : STD_LOGIC; 
   SIGNAL XOR_GATE	: STD_LOGIC;       
	SIGNAL NAND_GATE  : STD_LOGIC; 
	SIGNAL NOR_GATE	: STD_LOGIC; 
   SIGNAL XNOR_GATE  : STD_LOGIC; 

BEGIN

   UUT: Logic PORT MAP(
		A,
      B,
      BUF_GATE,    
		NOT_GATE, 
      AND_GATE,     
		OR_GATE,
      XOR_GATE,    
		NAND_GATE, 
		NOR_GATE,
      XNOR_GATE );

   tb : PROCESS
   BEGIN
      A <= '0'; B <= '0'; WAIT FOR 200 ns;
		A <= '0'; B <= '1'; WAIT FOR 200 ns;
		A <= '1'; B <= '0'; WAIT FOR 200 ns;
		A <= '1'; B <= '1'; WAIT FOR 200 ns;		
      WAIT; 
   END PROCESS;

END;

