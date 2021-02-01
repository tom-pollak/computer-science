
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Logic_Logic_sch_tb IS
END Logic_Logic_sch_tb;
ARCHITECTURE behavioral OF Logic_Logic_sch_tb IS 

   COMPONENT Logic
   PORT(           
		SW0	:	IN	STD_LOGIC; 
      SW1	:	IN	STD_LOGIC; 
      GREEN	:	OUT	STD_LOGIC; 
		RED	:	OUT	STD_LOGIC);
   END COMPONENT;

   SIGNAL SW0	 :	STD_LOGIC;
   SIGNAL SW1	 :	STD_LOGIC;
	SIGNAL GREEN :	STD_LOGIC;
   SIGNAL RED	 :	STD_LOGIC;

BEGIN

   UUT: Logic PORT MAP(
		SW0   => SW0, 
		SW1   => SW1, 
		GREEN => GREEN, 
		RED   => RED
   );

-- *** Test Bench - User Defined Section ***
   tb : PROCESS
   BEGIN
		SW1 <= '0'; SW0 <= '0'; WAIT FOR 100 ns;
		SW1 <= '0'; SW0 <= '1'; WAIT FOR 100 ns;
		SW1 <= '1'; SW0 <= '0'; WAIT FOR 100 ns;
		SW1 <= '1'; SW0 <= '1'; WAIT FOR 100 ns;		
      WAIT; -- will wait forever
   END PROCESS;
-- *** End Test Bench - User Defined Section ***

END;

