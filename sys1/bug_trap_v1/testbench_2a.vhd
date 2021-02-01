
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

LIBRARY UNISIM;
USE UNISIM.Vcomponents.ALL;

ENTITY testbench_2a IS
END testbench_2a;

ARCHITECTURE testbench_2a_arch OF testbench_2a IS 

  COMPONENT bug_trap_controller
  PORT( 
    OSC    	 :	IN	 STD_LOGIC; 
    SENSOR_1 :	IN	 STD_LOGIC; 
    SENSOR_2 :	IN	 STD_LOGIC; 
    MODE	   :	IN  STD_LOGIC; 
    FIRE	   :	IN  STD_LOGIC; 
    SERVO	   :	OUT STD_LOGIC; 
    LED	     :	OUT STD_LOGIC);
  END COMPONENT;

  SIGNAL OSC	    :	STD_LOGIC := '0';
  SIGNAL SENSOR_1	:	STD_LOGIC := '1';
  SIGNAL SENSOR_2	:	STD_LOGIC := '1';
  SIGNAL MODE	    :	STD_LOGIC := '0';
  SIGNAL FIRE	    :	STD_LOGIC := '1';
  SIGNAL SERVO	  :	STD_LOGIC;
  SIGNAL LED	    :	STD_LOGIC;

BEGIN

  UUT: bug_trap_controller PORT MAP(
    OSC => OSC, 
	  SENSOR_1 => SENSOR_1, 
	  SENSOR_2 => SENSOR_2, 
	  MODE => MODE, 
	  FIRE => FIRE, 
	  SERVO => SERVO, 
	  LED => LED );
	
  clock : PROCESS
  BEGIN
    for i in 0 to 15
	 loop
      OSC <= '0'; wait for 400 ms; 
      OSC <= '1'; wait for 400 ms; 	
    end loop;
	 wait;
  END PROCESS;
  
  tb : PROCESS
  BEGIN
   SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 1000 ms;

   SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '0';
	 FIRE     <= '1';
	 wait for 1000 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '0';
	 FIRE     <= '0';
	 wait for 1000 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 1000 ms;

	 SENSOR_1 <= '0';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 2000 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 1000 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '0';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 2000 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';

	 SENSOR_1 <= '0';
	 SENSOR_2 <= '0';
	 MODE     <= '1';
	 FIRE     <= '1';
	 wait for 2500 ms;

	 SENSOR_1 <= '1';
	 SENSOR_2 <= '1';
	 MODE     <= '1';
	 FIRE     <= '1';

	 wait;
  END PROCESS;

END;
