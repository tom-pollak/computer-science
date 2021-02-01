--------------------------------------------------------------------------------
-- Copyright (c) 1995-2013 Xilinx, Inc.  All rights reserved.
--------------------------------------------------------------------------------
--   ____  ____ 
--  /   /\/   / 
-- /___/  \  /    Vendor: Xilinx 
-- \   \   \/     Version : 14.7
--  \   \         Application : sch2hdl
--  /   /         Filename : bug_trap.vhf
-- /___/   /\     Timestamp : 01/28/2021 14:13:56
-- \   \  /  \ 
--  \___\/\___\ 
--
--Command: sch2hdl -sympath /mnt/hgfs/sys1/bug_trap_v1/Src -intstyle ise -family zynq -flat -suppress -vhdl /mnt/hgfs/sys1/bug_trap_v1/bug_trap.vhf -w /mnt/hgfs/sys1/bug_trap_v1/Src/bug_trap.sch
--Design Name: bug_trap
--Device: zynq
--Purpose:
--    This vhdl netlist is translated from an ECS schematic. It can be 
--    synthesized and simulated, but it should not be modified. 
--
----- CELL CB16CE_HXILINX_bug_trap -----


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity CB16CE_HXILINX_bug_trap is
port (
    CEO : out STD_LOGIC;
    Q   : out STD_LOGIC_VECTOR(15 downto 0);
    TC  : out STD_LOGIC;
    C   : in STD_LOGIC;
    CE  : in STD_LOGIC;
    CLR : in STD_LOGIC
    );
end CB16CE_HXILINX_bug_trap;

architecture Behavioral of CB16CE_HXILINX_bug_trap is

  signal COUNT : STD_LOGIC_VECTOR(15 downto 0) := (others => '0');
  constant TERMINAL_COUNT : STD_LOGIC_VECTOR(15 downto 0) := (others => '1');
  
begin

process(C, CLR)
begin
  if (CLR='1') then
    COUNT <= (others => '0');
  elsif (C'event and C = '1') then
    if (CE='1') then 
      COUNT <= COUNT+1;
    end if;
  end if;
end process;

TC  <= '1' when (COUNT = TERMINAL_COUNT) else '0';
CEO <= '1' when ((COUNT = TERMINAL_COUNT) and CE='1') else '0';
Q   <= COUNT;

end Behavioral;


library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.ALL;
library UNISIM;
use UNISIM.Vcomponents.ALL;

entity bug_trap_controller_MUSER_bug_trap is
   port ( FIRE     : in    std_logic; 
          MODE     : in    std_logic; 
          OSC      : in    std_logic; 
          SENSOR_1 : in    std_logic; 
          SENSOR_2 : in    std_logic; 
          LED      : out   std_logic; 
          SERVO    : out   std_logic);
end bug_trap_controller_MUSER_bug_trap;

architecture BEHAVIORAL of bug_trap_controller_MUSER_bug_trap is
   attribute BOX_TYPE   : string ;
   signal XLXN_140 : std_logic;
   signal XLXN_314 : std_logic;
   component BUF
      port ( I : in    std_logic; 
             O : out   std_logic);
   end component;
   attribute BOX_TYPE of BUF : component is "BLACK_BOX";
   
   component INV
      port ( I : in    std_logic; 
             O : out   std_logic);
   end component;
   attribute BOX_TYPE of INV : component is "BLACK_BOX";
   
begin
   XLXI_1 : BUF
      port map (I=>SENSOR_1,
                O=>open);
   
   XLXI_2 : BUF
      port map (I=>SENSOR_2,
                O=>open);
   
   XLXI_3 : BUF
      port map (I=>MODE,
                O=>open);
   
   XLXI_4 : BUF
      port map (I=>FIRE,
                O=>XLXN_140);
   
   XLXI_9 : BUF
      port map (I=>XLXN_314,
                O=>SERVO);
   
   XLXI_10 : BUF
      port map (I=>XLXN_314,
                O=>LED);
   
   XLXI_13 : BUF
      port map (I=>OSC,
                O=>open);
   
   XLXI_65 : INV
      port map (I=>XLXN_140,
                O=>XLXN_314);
   
end BEHAVIORAL;



library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.ALL;
library UNISIM;
use UNISIM.Vcomponents.ALL;

entity clock_divider_MUSER_bug_trap is
   port ( CLK     : in    std_logic; 
          CLR     : in    std_logic; 
          CLK_OUT : out   std_logic);
end clock_divider_MUSER_bug_trap;

architecture BEHAVIORAL of clock_divider_MUSER_bug_trap is
   attribute HU_SET     : string ;
   attribute BOX_TYPE   : string ;
   signal CNT     : std_logic_vector (15 downto 0);
   signal XLXN_1  : std_logic;
   signal XLXN_5  : std_logic;
   component CB16CE_HXILINX_bug_trap
      port ( C   : in    std_logic; 
             CE  : in    std_logic; 
             CLR : in    std_logic; 
             CEO : out   std_logic; 
             Q   : out   std_logic_vector (15 downto 0); 
             TC  : out   std_logic);
   end component;
   
   component BUF
      port ( I : in    std_logic; 
             O : out   std_logic);
   end component;
   attribute BOX_TYPE of BUF : component is "BLACK_BOX";
   
   component VCC
      port ( P : out   std_logic);
   end component;
   attribute BOX_TYPE of VCC : component is "BLACK_BOX";
   
   attribute HU_SET of XLXI_3 : label is "XLXI_3_0";
   attribute HU_SET of XLXI_4 : label is "XLXI_4_1";
begin
   XLXI_3 : CB16CE_HXILINX_bug_trap
      port map (C=>CLK,
                CE=>XLXN_5,
                CLR=>CLR,
                CEO=>XLXN_1,
                Q=>open,
                TC=>open);
   
   XLXI_4 : CB16CE_HXILINX_bug_trap
      port map (C=>CLK,
                CE=>XLXN_1,
                CLR=>CLR,
                CEO=>open,
                Q(15 downto 0)=>CNT(15 downto 0),
                TC=>open);
   
   XLXI_7 : BUF
      port map (I=>CNT(6),
                O=>CLK_OUT);
   
   XLXI_11 : VCC
      port map (P=>XLXN_5);
   
end BEHAVIORAL;



library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.ALL;
library UNISIM;
use UNISIM.Vcomponents.ALL;

entity bug_trap is
   port ( clk_i         : in    std_logic; 
          pio_A_i       : in    std_logic_vector (6 downto 0); 
          rst_i         : in    std_logic; 
          LED_o         : out   std_logic_vector (1 downto 0); 
          pio_B_o       : out   std_logic_vector (6 downto 0); 
          pio_D_o       : out   std_logic_vector (7 downto 0); 
          sel_bus_o     : out   std_logic_vector (2 downto 0); 
          sel_ser_i2c_o : out   std_logic; 
          i2c_scl_io    : inout std_logic; 
          i2c_sda_io    : inout std_logic; 
          pio_C_io      : inout std_logic_vector (7 downto 0));
end bug_trap;

architecture BEHAVIORAL of bug_trap is
   signal pio_F_i       : std_logic_vector (1 downto 0);
   signal pio_F_o       : std_logic_vector (3 downto 0);
   signal XLXN_5        : std_logic;
   signal XLXN_20       : std_logic;
   component clock_divider_MUSER_bug_trap
      port ( CLK     : in    std_logic; 
             CLR     : in    std_logic; 
             CLK_OUT : out   std_logic);
   end component;
   
   component virtual_wires
      port ( clk_i         : in    std_logic; 
             rst_i         : in    std_logic; 
             pio_A_i       : in    std_logic_vector (6 downto 0); 
             pio_F_i       : in    std_logic_vector (1 downto 0); 
             clk_10MHz_o   : out   std_logic; 
             sel_ser_i2c_o : out   std_logic; 
             sel_bus_o     : out   std_logic_vector (2 downto 0); 
             LED_o         : out   std_logic_vector (1 downto 0); 
             pio_B_o       : out   std_logic_vector (6 downto 0); 
             pio_D_o       : out   std_logic_vector (7 downto 0); 
             pio_F_o       : out   std_logic_vector (3 downto 0); 
             i2c_scl_io    : inout std_logic; 
             i2c_sda_io    : inout std_logic; 
             pio_C_io      : inout std_logic_vector (7 downto 0));
   end component;
   
   component bug_trap_controller_MUSER_bug_trap
      port ( SENSOR_1 : in    std_logic; 
             SENSOR_2 : in    std_logic; 
             OSC      : in    std_logic; 
             FIRE     : in    std_logic; 
             MODE     : in    std_logic; 
             LED      : out   std_logic; 
             SERVO    : out   std_logic);
   end component;
   
begin
   CLOCK : clock_divider_MUSER_bug_trap
      port map (CLK=>XLXN_5,
                CLR=>rst_i,
                CLK_OUT=>XLXN_20);
   
   COMMS : virtual_wires
      port map (clk_i=>clk_i,
                pio_A_i(6 downto 0)=>pio_A_i(6 downto 0),
                pio_F_i(1 downto 0)=>pio_F_i(1 downto 0),
                rst_i=>rst_i,
                clk_10MHz_o=>XLXN_5,
                LED_o(1 downto 0)=>LED_o(1 downto 0),
                pio_B_o(6 downto 0)=>pio_B_o(6 downto 0),
                pio_D_o(7 downto 0)=>pio_D_o(7 downto 0),
                pio_F_o(3 downto 0)=>pio_F_o(3 downto 0),
                sel_bus_o(2 downto 0)=>sel_bus_o(2 downto 0),
                sel_ser_i2c_o=>sel_ser_i2c_o,
                i2c_scl_io=>i2c_scl_io,
                i2c_sda_io=>i2c_sda_io,
                pio_C_io(7 downto 0)=>pio_C_io(7 downto 0));
   
   CONTROLLER : bug_trap_controller_MUSER_bug_trap
      port map (FIRE=>pio_F_o(0),
                MODE=>pio_F_o(1),
                OSC=>XLXN_20,
                SENSOR_1=>pio_F_o(3),
                SENSOR_2=>pio_F_o(2),
                LED=>pio_F_i(1),
                SERVO=>pio_F_i(0));
   
end BEHAVIORAL;


