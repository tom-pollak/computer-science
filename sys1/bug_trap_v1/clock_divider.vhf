--------------------------------------------------------------------------------
-- Copyright (c) 1995-2013 Xilinx, Inc.  All rights reserved.
--------------------------------------------------------------------------------
--   ____  ____ 
--  /   /\/   / 
-- /___/  \  /    Vendor: Xilinx 
-- \   \   \/     Version : 14.7
--  \   \         Application : sch2hdl
--  /   /         Filename : clock_divider.vhf
-- /___/   /\     Timestamp : 01/28/2021 14:13:57
-- \   \  /  \ 
--  \___\/\___\ 
--
--Command: sch2hdl -sympath /mnt/hgfs/sys1/bug_trap_v1/Src -intstyle ise -family zynq -flat -suppress -vhdl /mnt/hgfs/sys1/bug_trap_v1/clock_divider.vhf -w /mnt/hgfs/sys1/bug_trap_v1/Src/clock_divider.sch
--Design Name: clock_divider
--Device: zynq
--Purpose:
--    This vhdl netlist is translated from an ECS schematic. It can be 
--    synthesized and simulated, but it should not be modified. 
--
----- CELL CB16CE_HXILINX_clock_divider -----


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity CB16CE_HXILINX_clock_divider is
port (
    CEO : out STD_LOGIC;
    Q   : out STD_LOGIC_VECTOR(15 downto 0);
    TC  : out STD_LOGIC;
    C   : in STD_LOGIC;
    CE  : in STD_LOGIC;
    CLR : in STD_LOGIC
    );
end CB16CE_HXILINX_clock_divider;

architecture Behavioral of CB16CE_HXILINX_clock_divider is

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

entity clock_divider is
   port ( CLK     : in    std_logic; 
          CLR     : in    std_logic; 
          CLK_OUT : out   std_logic);
end clock_divider;

architecture BEHAVIORAL of clock_divider is
   attribute HU_SET     : string ;
   attribute BOX_TYPE   : string ;
   signal CNT     : std_logic_vector (15 downto 0);
   signal XLXN_1  : std_logic;
   signal XLXN_5  : std_logic;
   component CB16CE_HXILINX_clock_divider
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
   
   attribute HU_SET of XLXI_3 : label is "XLXI_3_2";
   attribute HU_SET of XLXI_4 : label is "XLXI_4_3";
begin
   XLXI_3 : CB16CE_HXILINX_clock_divider
      port map (C=>CLK,
                CE=>XLXN_5,
                CLR=>CLR,
                CEO=>XLXN_1,
                Q=>open,
                TC=>open);
   
   XLXI_4 : CB16CE_HXILINX_clock_divider
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


