-- =============================================================================================================
-- *
-- * Copyright (c) M.Freeman
-- *
-- * File Name: virtual_wires.vhd
-- *
-- * Version: V1.0
-- *
-- * Release Date:
-- *
-- * Author(s): M.Freeman
-- *
-- * Description: Single core PicoBlaze top level virtual wires 
-- *
-- * Change History:  $Author: $
-- *                  $Date: $
-- *                  $Revision: $
-- *
-- * Conditions of Use: THIS CODE IS COPYRIGHT AND IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING,
-- *                    BUT NOT LIMITED TO, ANY IMPLIED WARRANTY OF MERCHANTABILITY AND FITNESS FOR A
-- *                    PARTICULAR PURPOSE.
-- *
-- * Notes:
-- *
-- =============================================================================================================

LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL; 
USE IEEE.std_logic_arith.ALL;

LIBRARY UNISIM;
USE UNISIM.vcomponents.ALL;

ENTITY virtual_wires IS
PORT (
  clk_i         : IN  STD_LOGIC;
  rst_i         : IN  STD_LOGIC; 
  
  clk_10MHz_o   : OUT STD_LOGIC;
  
  sel_ser_i2c_o : OUT STD_LOGIC;
  sel_bus_o     : OUT STD_LOGIC_VECTOR(2 DOWNTO 0);
  
  i2c_scl_io    : INOUT  STD_LOGIC;
  i2c_sda_io    : INOUT  STD_LOGIC;
  
  LED_o         : OUT STD_LOGIC_VECTOR(1 DOWNTO 0);

  pio_A_i       : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
  pio_B_o       : OUT STD_LOGIC_VECTOR(6 DOWNTO 0);
 
  pio_C_io      : INOUT STD_LOGIC_VECTOR(7 DOWNTO 0); 
  
  pio_D_o       : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);

  pio_F_i       : IN  STD_LOGIC_VECTOR(1 DOWNTO 0);
  pio_F_o       : OUT STD_LOGIC_VECTOR(3 DOWNTO 0) ); 
  
END virtual_wires;

ARCHITECTURE virtual_wires_arch OF virtual_wires IS

  -- ##############
  -- # Components #
  -- ##############

  --
  -- Processor
  --

  COMPONENT picoblze_top_level IS
  PORT (
    clk_i         : IN  STD_LOGIC;
    rst_i         : IN  STD_LOGIC;  

    clk_10MHz_o   : OUT STD_LOGIC;

    sel_ser_i2c_o : OUT STD_LOGIC;
    sel_bus_o     : OUT STD_LOGIC_VECTOR(2 DOWNTO 0);
  
    i2c_scl_i     : IN  STD_LOGIC;
    i2c_sda_i     : IN  STD_LOGIC;
    i2c_scl_clk_o : OUT STD_LOGIC;
    i2c_scl_en_o  : OUT STD_LOGIC;
    i2c_sda_en_o  : OUT STD_LOGIC;
  
    LED_o         : OUT STD_LOGIC_VECTOR(1 DOWNTO 0);

    pio_A_i       : IN  STD_LOGIC_VECTOR(6 DOWNTO 0);
    pio_B_o       : OUT STD_LOGIC_VECTOR(6 DOWNTO 0);
 
    pio_C_dir     : OUT STD_LOGIC_VECTOR(7 DOWNTO 0); 
    pio_C_i       : IN  STD_LOGIC_VECTOR(7 DOWNTO 0);
    pio_C_o       : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
  
    pio_D_o       : OUT STD_LOGIC_VECTOR(7 DOWNTO 0);

    pio_F_i       : IN  STD_LOGIC_VECTOR(1 DOWNTO 0);
    pio_F_o       : OUT STD_LOGIC_VECTOR(3 DOWNTO 0) ); 
  END COMPONENT;

  -- ###########
  -- # Signals #
  -- ###########

  SIGNAL GND     : STD_LOGIC;
  SIGNAL VCC     : STD_LOGIC;
  SIGNAL GND_BUS : STD_LOGIC_VECTOR(7 DOWNTO 0);
  
  SIGNAL pio_C_o   : STD_LOGIC_VECTOR(7 DOWNTO 0); 
  SIGNAL pio_C_dir : STD_LOGIC_VECTOR(7 DOWNTO 0); 
  
  SIGNAL scl_clk : STD_LOGIC;
  SIGNAL scl_en  : STD_LOGIC;
  SIGNAL sda_en  : STD_LOGIC;
  
BEGIN

  --
  -- SIGNAL BUFFERS
  --
  
  i2c_scl_io  <= '0' WHEN (scl_en = '1' AND scl_clk = '0') ELSE 'Z';
  i2c_sda_io  <= '0' WHEN (sda_en = '0') ELSE 'Z';
  
  pio_C_io(0) <=  pio_C_o(0) WHEN (pio_C_dir(0) = '1') ELSE 'Z';
  pio_C_io(1) <=  pio_C_o(1) WHEN (pio_C_dir(1) = '1') ELSE 'Z';
  pio_C_io(2) <=  pio_C_o(2) WHEN (pio_C_dir(2) = '1') ELSE 'Z';
  pio_C_io(3) <=  pio_C_o(3) WHEN (pio_C_dir(3) = '1') ELSE 'Z';
  
  pio_C_io(4) <=  pio_C_o(4) WHEN (pio_C_dir(4) = '1') ELSE 'Z';
  pio_C_io(5) <=  pio_C_o(5) WHEN (pio_C_dir(5) = '1') ELSE 'Z';
  pio_C_io(6) <=  pio_C_o(6) WHEN (pio_C_dir(6) = '1') ELSE 'Z';
  pio_C_io(7) <=  pio_C_o(7) WHEN (pio_C_dir(7) = '1') ELSE 'Z';

  --
  -- COMPONENTS
  --
  
  SYSTEM : picoblze_top_level PORT MAP(
    clk_i         => clk_i,
    rst_i         => rst_i,
    clk_10MHz_o   => clk_10MHz_o,
    sel_ser_i2c_o => sel_ser_i2c_o,
    sel_bus_o     => sel_bus_o,
    i2c_scl_i     => i2c_scl_io,
    i2c_sda_i     => i2c_sda_io,
    i2c_scl_clk_o => scl_clk,
    i2c_scl_en_o  => scl_en,
    i2c_sda_en_o  => sda_en,
    LED_o         => LED_o,
    pio_A_i       => pio_A_i,
    pio_B_o       => pio_B_o,
    pio_C_dir     => pio_C_dir,
    pio_C_i       => pio_C_io,
    pio_C_o       => pio_C_o,
    pio_D_o       => pio_D_o,
    pio_F_i       => pio_F_i,
    pio_F_o       => pio_F_o );   


END virtual_wires_arch;
