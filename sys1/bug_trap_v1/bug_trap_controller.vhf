--------------------------------------------------------------------------------
-- Copyright (c) 1995-2013 Xilinx, Inc.  All rights reserved.
--------------------------------------------------------------------------------
--   ____  ____ 
--  /   /\/   / 
-- /___/  \  /    Vendor: Xilinx 
-- \   \   \/     Version : 14.7
--  \   \         Application : sch2hdl
--  /   /         Filename : bug_trap_controller.vhf
-- /___/   /\     Timestamp : 01/28/2021 14:13:57
-- \   \  /  \ 
--  \___\/\___\ 
--
--Command: sch2hdl -sympath /mnt/hgfs/sys1/bug_trap_v1/Src -intstyle ise -family zynq -flat -suppress -vhdl /mnt/hgfs/sys1/bug_trap_v1/bug_trap_controller.vhf -w /mnt/hgfs/sys1/bug_trap_v1/Src/bug_trap_controller.sch
--Design Name: bug_trap_controller
--Device: zynq
--Purpose:
--    This vhdl netlist is translated from an ECS schematic. It can be 
--    synthesized and simulated, but it should not be modified. 
--

library ieee;
use ieee.std_logic_1164.ALL;
use ieee.numeric_std.ALL;
library UNISIM;
use UNISIM.Vcomponents.ALL;

entity bug_trap_controller is
   port ( FIRE     : in    std_logic; 
          MODE     : in    std_logic; 
          OSC      : in    std_logic; 
          SENSOR_1 : in    std_logic; 
          SENSOR_2 : in    std_logic; 
          LED      : out   std_logic; 
          SERVO    : out   std_logic);
end bug_trap_controller;

architecture BEHAVIORAL of bug_trap_controller is
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


