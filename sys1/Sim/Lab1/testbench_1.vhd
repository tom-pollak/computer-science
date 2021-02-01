-- =============================================================================================================
-- *
-- * Copyright (c) Mike
-- *
-- * File Name: testbench_1.vhd
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
 
entity testbench_1 is
  generic (   
    fpgaPushButtonData   : string  := "fpgaPushButton.dat";
    fpgaRedGreenLedState : string  := "fpgaRedGreenLed.dat" );
end testbench_1;
 
architecture testbench_1_arch of testbench_1 is

  component Logic is
  port ( 
    SW0   : in    std_logic; 
    SW1   : in    std_logic; 
    GREEN : out   std_logic; 
    RED   : out   std_logic);
  end component;
 
  constant fpgaPushButtonData_WIDTH   : natural := 8;
  constant fpgaRedGreenLedState_WIDTH : natural := 2;
 
  signal inputSignals : std_logic_vector(fpgaPushButtonData_WIDTH-1 downto 0);
  signal outputSignals : std_logic_vector(fpgaRedGreenLedState_WIDTH-1 downto 0);

  signal SW0   : std_logic; 
  signal SW1   : std_logic; 
  signal GREEN : std_logic; 
  signal RED   : std_logic; 

begin

  uut: Logic port map( 
    SW0   => SW0,
    SW1   => SW1,
    GREEN => GREEN,
    RED   => RED );

  SW0 <= inputSignals(7);
  SW1 <= inputSignals(6);

  outputSignals(0) <= RED;
  outputSignals(1) <= GREEN;

  tb: process
    file inputDataFile  : text;
    file outputDataFile : text;

    variable inputDataLine  : line;
    variable outputDataLine : line;
	
    variable inputData : std_logic_vector(fpgaPushButtonData_WIDTH-1 downto 0);
     
  begin
 
    file_open(inputDataFile, fpgaPushButtonData,  read_mode);
    file_open(outputDataFile, fpgaRedGreenLedState, write_mode);
 
    while not endfile(inputDataFile) loop
      readline(inputDataFile, inputDataLine);
      read(inputDataLine, inputData);
 
      inputSignals <= inputData;	

	   	wait for 100 ns;
      write(outputDataLine, inputSignals(7 downto 6), right, fpgaRedGreenLedState_WIDTH);
      write(outputDataLine, String'(" - "));
      write(outputDataLine, outputSignals, right, fpgaRedGreenLedState_WIDTH);
      writeline(output, outputDataLine);

      write(outputDataLine, outputSignals, right, fpgaRedGreenLedState_WIDTH);
      writeline(outputDataFile, outputDataLine);
			wait for 100 ns;

    end loop;
 
    file_close(inputDataFile);
    file_close(outputDataFile);
     
    wait;
  end process;
 
end testbench_1_arch;
