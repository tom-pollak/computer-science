<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="pio_A_i(6:0)" />
        <signal name="pio_F_i(1:0)" />
        <signal name="pio_F_o(3:0)" />
        <signal name="XLXN_24(3:0)" />
        <signal name="pio_F_i(1)" />
        <signal name="pio_F_i(0)" />
        <signal name="pio_F_o(0)" />
        <signal name="pio_F_o(1)" />
        <signal name="pio_F_o(2)" />
        <signal name="pio_F_o(3)" />
        <signal name="XLXN_31" />
        <signal name="XLXN_20" />
        <signal name="pio_D_o(7:0)" />
        <signal name="pio_B_o(6:0)" />
        <signal name="LED_o(1:0)" />
        <signal name="sel_bus_o(2:0)" />
        <signal name="sel_ser_i2c_o" />
        <signal name="clk_i" />
        <signal name="rst_i" />
        <signal name="XLXN_5" />
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
            <wire x2="1504" y1="1264" y2="1264" x1="1312" />
        </branch>
        <branch name="pio_F_i(1:0)">
            <attrtext style="alignment:SOFT-BCENTER;fontsize:28;fontname:Arial" attrname="Name" x="1744" y="1632" type="branch" />
            <wire x2="1216" y1="1456" y2="1632" x1="1216" />
            <wire x2="1744" y1="1632" y2="1632" x1="1216" />
            <wire x2="2112" y1="1632" y2="1632" x1="1744" />
            <wire x2="2112" y1="1632" y2="1840" x1="2112" />
            <wire x2="2112" y1="1840" y2="2096" x1="2112" />
            <wire x2="2112" y1="2096" y2="2128" x1="2112" />
            <wire x2="1504" y1="1456" y2="1456" x1="1216" />
        </branch>
        <branch name="pio_F_o(3:0)">
            <attrtext style="alignment:SOFT-BCENTER;fontsize:28;fontname:Arial" attrname="Name" x="1760" y="1568" type="branch" />
            <wire x2="1760" y1="1568" y2="1568" x1="1360" />
            <wire x2="2400" y1="1568" y2="1568" x1="1760" />
            <wire x2="1360" y1="1568" y2="1840" x1="1360" />
            <wire x2="1360" y1="1840" y2="1904" x1="1360" />
            <wire x2="1360" y1="1904" y2="1968" x1="1360" />
            <wire x2="1360" y1="1968" y2="2032" x1="1360" />
            <wire x2="1360" y1="2032" y2="2080" x1="1360" />
            <wire x2="2400" y1="1264" y2="1264" x1="1936" />
            <wire x2="2400" y1="1264" y2="1568" x1="2400" />
        </branch>
        <branch name="pio_F_i(1)">
            <wire x2="2016" y1="2096" y2="2096" x1="1936" />
        </branch>
        <branch name="pio_F_i(0)">
            <wire x2="2016" y1="1840" y2="1840" x1="1936" />
        </branch>
        <branch name="pio_F_o(0)">
            <wire x2="1552" y1="2032" y2="2032" x1="1456" />
        </branch>
        <branch name="pio_F_o(1)">
            <wire x2="1552" y1="1968" y2="1968" x1="1456" />
        </branch>
        <branch name="pio_F_o(2)">
            <wire x2="1552" y1="1904" y2="1904" x1="1456" />
        </branch>
        <branch name="pio_F_o(3)">
            <wire x2="1552" y1="1840" y2="1840" x1="1456" />
        </branch>
        <bustap x2="1456" y1="2032" y2="2032" x1="1360" />
        <bustap x2="1456" y1="1968" y2="1968" x1="1360" />
        <bustap x2="1456" y1="1904" y2="1904" x1="1360" />
        <bustap x2="1456" y1="1840" y2="1840" x1="1360" />
        <bustap x2="2016" y1="2096" y2="2096" x1="2112" />
        <bustap x2="2016" y1="1840" y2="1840" x1="2112" />
        <branch name="XLXN_20">
            <wire x2="1552" y1="2096" y2="2096" x1="1536" />
            <wire x2="1536" y1="2096" y2="2240" x1="1536" />
            <wire x2="2512" y1="2240" y2="2240" x1="1536" />
            <wire x2="2512" y1="576" y2="576" x1="1936" />
            <wire x2="2512" y1="576" y2="2240" x1="2512" />
        </branch>
        <branch name="pio_D_o(7:0)">
            <wire x2="1952" y1="1200" y2="1200" x1="1936" />
            <wire x2="2080" y1="1200" y2="1200" x1="1952" />
        </branch>
        <branch name="pio_B_o(6:0)">
            <wire x2="1952" y1="1136" y2="1136" x1="1936" />
            <wire x2="2080" y1="1136" y2="1136" x1="1952" />
        </branch>
        <branch name="LED_o(1:0)">
            <wire x2="1952" y1="1072" y2="1072" x1="1936" />
            <wire x2="2080" y1="1072" y2="1072" x1="1952" />
        </branch>
        <branch name="sel_bus_o(2:0)">
            <wire x2="1952" y1="1008" y2="1008" x1="1936" />
            <wire x2="2080" y1="1008" y2="1008" x1="1952" />
        </branch>
        <branch name="sel_ser_i2c_o">
            <wire x2="1952" y1="944" y2="944" x1="1936" />
            <wire x2="2080" y1="944" y2="944" x1="1952" />
        </branch>
        <branch name="clk_i">
            <wire x2="1232" y1="880" y2="880" x1="1216" />
            <wire x2="1504" y1="880" y2="880" x1="1232" />
        </branch>
        <branch name="rst_i">
            <wire x2="1392" y1="640" y2="640" x1="1216" />
            <wire x2="1392" y1="640" y2="1072" x1="1392" />
            <wire x2="1504" y1="1072" y2="1072" x1="1392" />
            <wire x2="1552" y1="640" y2="640" x1="1392" />
        </branch>
        <instance x="1552" y="672" name="CLOCK" orien="R0">
        </instance>
        <branch name="XLXN_5">
            <wire x2="1488" y1="576" y2="736" x1="1488" />
            <wire x2="2048" y1="736" y2="736" x1="1488" />
            <wire x2="2048" y1="736" y2="880" x1="2048" />
            <wire x2="1536" y1="576" y2="576" x1="1488" />
            <wire x2="1552" y1="576" y2="576" x1="1536" />
            <wire x2="2048" y1="880" y2="880" x1="1936" />
        </branch>
        <branch name="pio_C_io(7:0)">
            <wire x2="2048" y1="1456" y2="1456" x1="1936" />
            <wire x2="2064" y1="1456" y2="1456" x1="2048" />
        </branch>
        <instance x="1504" y="1488" name="COMMS" orien="R0">
        </instance>
        <branch name="i2c_scl_io">
            <wire x2="1952" y1="1328" y2="1328" x1="1936" />
            <wire x2="2080" y1="1328" y2="1328" x1="1952" />
        </branch>
        <branch name="i2c_sda_io">
            <wire x2="1952" y1="1392" y2="1392" x1="1936" />
            <wire x2="2080" y1="1392" y2="1392" x1="1952" />
        </branch>
        <instance x="1552" y="2128" name="CONTROLLER" orien="R0">
        </instance>
        <iomarker fontsize="28" x="1216" y="880" name="clk_i" orien="R180" />
        <iomarker fontsize="28" x="1216" y="640" name="rst_i" orien="R180" />
        <iomarker fontsize="28" x="1312" y="1264" name="pio_A_i(6:0)" orien="R180" />
        <iomarker fontsize="28" x="2064" y="1456" name="pio_C_io(7:0)" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1200" name="pio_D_o(7:0)" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1136" name="pio_B_o(6:0)" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1072" name="LED_o(1:0)" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1008" name="sel_bus_o(2:0)" orien="R0" />
        <iomarker fontsize="28" x="2080" y="944" name="sel_ser_i2c_o" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1328" name="i2c_scl_io" orien="R0" />
        <iomarker fontsize="28" x="2080" y="1392" name="i2c_sda_io" orien="R0" />
    </sheet>
</drawing>