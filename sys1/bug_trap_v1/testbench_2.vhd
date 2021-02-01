-- =============================================================================================================
-- *
-- * Copyright (c) Mike
-- *
-- * File Name: testbench_2.vhd
-- *
-- * Version: V1.0
-- *
-- * Release Date:
-- *
-- * Author(s): M.Freeman
-- *
-- * Description: testbench
-- *
-- * Conditions of Use: THIS CODE IS COPYRIGHT AND IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING,
-- *                    BUT NOT LIMITED TO, ANY IMPLIED WARRANTY OF MERCHANTABILITY AND FITNESS FOR A
-- *                    PARTICULAR PURPOSE.
-- *
-- * Notes: 
-- * 
-- =============================================================================================================

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use STD.textio.all;
use ieee.std_logic_textio.all;
 
entity testbench_2 is
  generic (   
    trapSensorSwitchData : string := "trapSensorSwitch.dat";
    trapLedServoState    : string := "trapLedServo.dat" );
end testbench_2;
 
architecture testbench_2_arch of testbench_2 is

  component bug_trap_controller is
  port ( 
    FIRE     : in    std_logic; 
    MODE     : in    std_logic; 
    OSC      : in    std_logic; 
    SENSOR_1 : in    std_logic; 
    SENSOR_2 : in    std_logic; 
    LED      : out   std_logic; 
    SERVO    : out   std_logic);
  end component;
 
  constant trapSensorData_WIDTH    : natural := 4;
  constant trapLedServoState_WIDTH : natural := 2;
 
  signal inputSignals  : std_logic_vector(trapSensorData_WIDTH-1 downto 0);
  signal outputSignals : std_logic_vector(trapLedServoState_WIDTH-1 downto 0);

  signal FIRE     : std_logic; 
  signal MODE     : std_logic; 
  signal OSC      : std_logic; 
  signal SENSOR_1 : std_logic; 
  signal SENSOR_2 : std_logic; 
  signal LED      : std_logic; 
  signal SERVO    : std_logic; 

begin

  uut: bug_trap_controller port map( 
    FIRE     => FIRE,
    MODE     => MODE,
    OSC      => OSC,
    SENSOR_1 => SENSOR_1,
    SENSOR_2 => SENSOR_2,
    LED      => LED,
    SERVO    => SERVO );

  -- INPUTS
  -- B7 : NU
  -- B6 : NU
  -- B5 : NU
  -- B4 : NU
  -- B3 : BACK INFRA-RED  (Triggered=0)
  -- B2 : FRONT INFRA-RED (Triggered=0)
  -- B1 : TOGGLE          (Up=0)
  -- B0 : PUSH BUTTON     (Pushed=0)

  -- OUTPUTS
  -- B7 : NU
  -- B6 : NU
  -- B5 : NU
  -- B4 : NU
  -- B3 : NU
  -- B2 : NU
  -- B1 : LED   (Off=0)
  -- B0 : SERVO (Up=0)

  FIRE     <= inputSignals(0);
  MODE     <= inputSignals(1);
  SENSOR_2 <= inputSignals(2);
  SENSOR_1 <= inputSignals(3);
  OSC      <= '1';

  outputSignals(0) <= SERVO;
  outputSignals(1) <= LED;

  tb: process
    file inputDataFile : text;
    file outputDataFile : text;

    variable inputDataLine : line;
    variable outputDataLine : line;
	
    variable inputData : std_logic_vector(trapSensorData_WIDTH-1 downto 0);
     
  begin
 
    file_open(inputDataFile, trapSensorSwitchData, read_mode);
    file_open(outputDataFile, trapLedServoState, write_mode);
 
    while not endfile(inputDataFile) 
    loop
      readline(inputDataFile, inputDataLine);
      read(inputDataLine, inputData);
 
      inputSignals <= inputData;	

	   	wait for 100 ns;
      write(outputDataLine, inputSignals, right, trapSensorData_WIDTH);
      write(outputDataLine, String'(" - "));
      write(outputDataLine, outputSignals, right, trapLedServoState_WIDTH);
      writeline(output, outputDataLine);

      write(outputDataLine, outputSignals, right, trapLedServoState_WIDTH);
      writeline(outputDataFile, outputDataLine);
			wait for 100 ns;

    end loop;
 
    file_close(inputDataFile);
    file_close(outputDataFile);
     
    wait;
  end process;
 
end testbench_2_arch;
