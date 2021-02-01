<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="pio_F_o(3:0)" />
        <signal name="pio_A_i(6:0)" />
        <signal name="pio_F_i(1:0)" />
        <signal name="pio_F_i(1)" />
        <signal name="pio_F_i(0)" />
        <signal name="pio_F_o(0)" />
        <signal name="pio_F_o(1)" />
        <signal name="pio_F_o(2)" />
        <signal name="pio_F_o(3)" />
        <signal name="XLXN_20" />
        <signal name="pio_D_o(7:0)" />
        <signal name="pio_B_o(6:0)" />
        <signal name="LED_o(1:0)" />
        <signal name="sel_bus_o(2:0)" />
        <signal name="sel_ser_i2c_o" />
        <signal name="XLXN_5" />
        <signal name="clk_i" />
        <signal name="rst_i" />
        <signal name="pio_C_io(7:0)" />
        <signal name="i2c_scl_io" />
        <signal name="i2c_sda_io" />
        <port polarity="Input" name="pio_A_i(6:0)" />
        <port polarity="Output" name="pio_D_o(7:0)" />
        <port polarity="Output" name="pio_B_o(6:0)" />
        <port polarity="Output" name="LED_o(1:0)" />
        <port polarity="Output" name="sel_bus_o(2:0)" />
        <port polarity="Output" name="sel_ser_i2c_o" />
        <port polarity="Input" name="clk_i" />
        <port polarity="Input" name="rst_i" />
        <port polarity="BiDirectional" name="pio_C_io(7:0)" />
        <port polarity="BiDirectional" name="i2c_scl_io" />
        <port polarity="BiDirectional" name="i2c_sda_io" />
        <blockdef name="clock_divider">
            <timestamp>2019-6-19T15:13:45</timestamp>
            <rect width="256" x="64" y="-128" height="128" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-96" y2="-96" x1="320" />
        </blockdef>
        <blockdef name="virtual_wires">
            <timestamp>2019-6-25T6:27:0</timestamp>
            <rect width="304" x="64" y="-640" height="640" />
            <line x2="0" y1="-608" y2="-608" x1="64" />
            <line x2="0" y1="-416" y2="-416" x1="64" />
            <rect width="64" x="0" y="-236" height="24" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <rect width="64" x="0" y="-44" height="24" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="432" y1="-608" y2="-608" x1="368" />
            <line x2="432" y1="-544" y2="-544" x1="368" />
            <rect width="64" x="368" y="-492" height="24" />
            <line x2="432" y1="-480" y2="-480" x1="368" />
            <rect width="64" x="368" y="-428" height="24" />
            <line x2="432" y1="-416" y2="-416" x1="368" />
            <rect width="64" x="368" y="-364" height="24" />
            <line x2="432" y1="-352" y2="-352" x1="368" />
            <rect width="64" x="368" y="-300" height="24" />
            <line x2="432" y1="-288" y2="-288" x1="368" />
            <rect width="64" x="368" y="-236" height="24" />
            <line x2="432" y1="-224" y2="-224" x1="368" />
            <line x2="432" y1="-160" y2="-160" x1="368" />
            <line x2="432" y1="-96" y2="-96" x1="368" />
            <rect width="64" x="368" y="-44" height="24" />
            <line x2="432" y1="-32" y2="-32" x1="368" />
        </blockdef>
        <blockdef name="bug_trap_controller">
            <timestamp>2019-10-14T13:33:27</timestamp>
            <line x2="0" y1="-288" y2="-288" x1="64" />
            <line x2="0" y1="-224" y2="-224" x1="64" />
            <line x2="0" y1="-160" y2="-160" x1="64" />
            <line x2="0" y1="-96" y2="-96" x1="64" />
            <line x2="0" y1="-32" y2="-32" x1="64" />
            <line x2="384" y1="-32" y2="-32" x1="320" />
            <rect width="256" x="64" y="-320" height="332" />
            <line x2="384" y1="-288" y2="-288" x1="320" />
        </blockdef>
        <block symbolname="clock_divider" name="CLOCK">
            <blockpin signalname="XLXN_5" name="CLK" />
            <blockpin signalname="rst_i" name="CLR" />
            <blockpin signalname="XLXN_20" name="CLK_OUT" />
        </block>
        <block symbolname="virtual_wires" name="COMMS">
            <blockpin signalname="clk_i" name="clk_i" />
            <blockpin signalname="rst_i" name="rst_i" />
            <blockpin signalname="pio_A_i(6:0)" name="pio_A_i(6:0)" />
            <blockpin signalname="pio_F_i(1:0)" name="pio_F_i(1:0)" />
            <blockpin signalname="XLXN_5" name="clk_10MHz_o" />
            <blockpin signalname="sel_ser_i2c_o" name="sel_ser_i2c_o" />
            <blockpin signalname="sel_bus_o(2:0)" name="sel_bus_o(2:0)" />
            <blockpin signalname="LED_o(1:0)" name="LED_o(1:0)" />
            <blockpin signalname="pio_B_o(6:0)" name="pio_B_o(6:0)" />
            <blockpin signalname="pio_D_o(7:0)" name="pio_D_o(7:0)" />
            <blockpin signalname="pio_F_o(3:0)" name="pio_F_o(3:0)" />
            <blockpin signalname="i2c_scl_io" name="i2c_scl_io" />
            <blockpin signalname="i2c_sda_io" name="i2c_sda_io" />
            <blockpin signalname="pio_C_io(7:0)" name="pio_C_io(7:0)" />
        </block>
        <block symbolname="bug_trap_controller" name="CONTROLLER">
            <blockpin signalname="pio_F_o(3)" name="SENSOR_1" />
            <blockpin signalname="pio_F_o(2)" name="SENSOR_2" />
            <blockpin signalname="XLXN_20" name="OSC" />
            <blockpin signalname="pio_F_o(0)" name="FIRE" />
            <blockpin signalname="pio_F_o(1)" name="MODE" />
            <blockpin signalname="pio_F_i(1)" name="LED" />
            <blockpin signalname="pio_F_i(0)" name="SERVO" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <branch name="pio_A_i(6:0)">
            <wire x2="1632" y1="1296" y2="1296" x1="1440" />
        </branch>
        <branch name="pio_F_i(1:0)">
            <attrtext style="alignment:SOFT-BCENTER;fontsize:28;fontname:Arial" attrname="Name" x="1872" y="1664" type="branch" />
            <wire x2="1344" y1="1488" y2="1664" x1="1344" />
            <wire x2="1872" y1="1664" y2="1664" x1="1344" />
            <wire x2="2240" y1="1664" y2="1664" x1="1872" />
            <wire x2="2240" y1="1664" y2="1872" x1="2240" />
            <wire x2="2240" y1="1872" y2="2128" x1="2240" />
            <wire x2="2240" y1="2128" y2="2160" x1="2240" />
            <wire x2="1632" y1="1488" y2="1488" x1="1344" />
        </branch>
        <branch name="pio_F_o(3:0)">
            <attrtext style="alignment:SOFT-BCENTER;fontsize:28;fontname:Arial" attrname="Name" x="1888" y="1600" type="branch" />
            <wire x2="1888" y1="1600" y2="1600" x1="1488" />
            <wire x2="2528" y1="1600" y2="1600" x1="1888" />
            <wire x2="1488" y1="1600" y2="1872" x1="1488" />
            <wire x2="1488" y1="1872" y2="1936" x1="1488" />
            <wire x2="1488" y1="1936" y2="2000" x1="1488" />
            <wire x2="1488" y1="2000" y2="2064" x1="1488" />
            <wire x2="1488" y1="2064" y2="2112" x1="1488" />
            <wire x2="2528" y1="1296" y2="1296" x1="2064" />
            <wire x2="2528" y1="1296" y2="1600" x1="2528" />
        </branch>
        <branch name="pio_F_i(1)">
            <wire x2="2144" y1="2128" y2="2128" x1="2064" />
        </branch>
        <branch name="pio_F_i(0)">
            <wire x2="2144" y1="1872" y2="1872" x1="2064" />
        </branch>
        <branch name="pio_F_o(0)">
            <wire x2="1680" y1="2064" y2="2064" x1="1584" />
        </branch>
        <branch name="pio_F_o(1)">
            <wire x2="1680" y1="2000" y2="2000" x1="1584" />
        </branch>
        <branch name="pio_F_o(2)">
            <wire x2="1680" y1="1936" y2="1936" x1="1584" />
        </branch>
        <branch name="pio_F_o(3)">
            <wire x2="1680" y1="1872" y2="1872" x1="1584" />
        </branch>
        <bustap x2="1584" y1="2064" y2="2064" x1="1488" />
        <bustap x2="1584" y1="2000" y2="2000" x1="1488" />
        <bustap x2="1584" y1="1936" y2="1936" x1="1488" />
        <bustap x2="1584" y1="1872" y2="1872" x1="1488" />
        <bustap x2="2144" y1="2128" y2="2128" x1="2240" />
        <bustap x2="2144" y1="1872" y2="1872" x1="2240" />
        <branch name="XLXN_20">
            <wire x2="1680" y1="2128" y2="2128" x1="1664" />
            <wire x2="1664" y1="2128" y2="2272" x1="1664" />
            <wire x2="2640" y1="2272" y2="2272" x1="1664" />
            <wire x2="2640" y1="608" y2="608" x1="2064" />
            <wire x2="2640" y1="608" y2="2272" x1="2640" />
        </branch>
        <iomarker fontsize="28" x="1344" y="912" name="clk_i" orien="R180" />
        <branch name="pio_D_o(7:0)">
            <wire x2="2080" y1="1232" y2="1232" x1="2064" />
            <wire x2="2208" y1="1232" y2="1232" x1="2080" />
        </branch>
        <branch name="pio_B_o(6:0)">
            <wire x2="2080" y1="1168" y2="1168" x1="2064" />
            <wire x2="2208" y1="1168" y2="1168" x1="2080" />
        </branch>
        <branch name="LED_o(1:0)">
            <wire x2="2080" y1="1104" y2="1104" x1="2064" />
            <wire x2="2208" y1="1104" y2="1104" x1="2080" />
        </branch>
        <branch name="sel_bus_o(2:0)">
            <wire x2="2080" y1="1040" y2="1040" x1="2064" />
            <wire x2="2208" y1="1040" y2="1040" x1="2080" />
        </branch>
        <branch name="sel_ser_i2c_o">
            <wire x2="2080" y1="976" y2="976" x1="2064" />
            <wire x2="2208" y1="976" y2="976" x1="2080" />
        </branch>
        <branch name="clk_i">
            <wire x2="1360" y1="912" y2="912" x1="1344" />
            <wire x2="1632" y1="912" y2="912" x1="1360" />
        </branch>
        <branch name="rst_i">
            <wire x2="1520" y1="672" y2="672" x1="1344" />
            <wire x2="1520" y1="672" y2="1104" x1="1520" />
            <wire x2="1632" y1="1104" y2="1104" x1="1520" />
            <wire x2="1680" y1="672" y2="672" x1="1520" />
        </branch>
        <instance x="1680" y="704" name="CLOCK" orien="R0">
        </instance>
        <branch name="XLXN_5">
            <wire x2="1616" y1="608" y2="768" x1="1616" />
            <wire x2="2176" y1="768" y2="768" x1="1616" />
            <wire x2="2176" y1="768" y2="912" x1="2176" />
            <wire x2="1664" y1="608" y2="608" x1="1616" />
            <wire x2="1680" y1="608" y2="608" x1="1664" />
            <wire x2="2176" y1="912" y2="912" x1="2064" />
        </branch>
        <iomarker fontsize="28" x="1344" y="672" name="rst_i" orien="R180" />
        <iomarker fontsize="28" x="1440" y="1296" name="pio_A_i(6:0)" orien="R180" />
        <branch name="pio_C_io(7:0)">
            <wire x2="2176" y1="1488" y2="1488" x1="2064" />
            <wire x2="2192" y1="1488" y2="1488" x1="2176" />
        </branch>
        <iomarker fontsize="28" x="2192" y="1488" name="pio_C_io(7:0)" orien="R0" />
        <iomarker fontsize="28" x="2208" y="1232" name="pio_D_o(7:0)" orien="R0" />
        <iomarker fontsize="28" x="2208" y="1168" name="pio_B_o(6:0)" orien="R0" />
        <iomarker fontsize="28" x="2208" y="1104" name="LED_o(1:0)" orien="R0" />
        <iomarker fontsize="28" x="2208" y="1040" name="sel_bus_o(2:0)" orien="R0" />
        <iomarker fontsize="28" x="2208" y="976" name="sel_ser_i2c_o" orien="R0" />
        <instance x="1632" y="1520" name="COMMS" orien="R0">
        </instance>
        <branch name="i2c_scl_io">
            <wire x2="2080" y1="1360" y2="1360" x1="2064" />
            <wire x2="2208" y1="1360" y2="1360" x1="2080" />
        </branch>
        <branch name="i2c_sda_io">
            <wire x2="2080" y1="1424" y2="1424" x1="2064" />
            <wire x2="2208" y1="1424" y2="1424" x1="2080" />
        </branch>
        <iomarker fontsize="28" x="2208" y="1360" name="i2c_scl_io" orien="R0" />
        <iomarker fontsize="28" x="2208" y="1424" name="i2c_sda_io" orien="R0" />
        <instance x="1680" y="2160" name="CONTROLLER" orien="R0">
        </instance>
    </sheet>
</drawing>