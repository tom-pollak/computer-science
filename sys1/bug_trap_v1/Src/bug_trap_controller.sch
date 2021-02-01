<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="SENSOR_1" />
        <signal name="SENSOR_2" />
        <signal name="MODE" />
        <signal name="FIRE" />
        <signal name="XLXN_140" />
        <signal name="LED" />
        <signal name="SERVO" />
        <signal name="OSC" />
        <signal name="XLXN_313" />
        <signal name="XLXN_314" />
        <port polarity="Input" name="SENSOR_1" />
        <port polarity="Input" name="SENSOR_2" />
        <port polarity="Input" name="MODE" />
        <port polarity="Input" name="FIRE" />
        <port polarity="Output" name="LED" />
        <port polarity="Output" name="SERVO" />
        <port polarity="Input" name="OSC" />
        <blockdef name="buf">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="128" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="0" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="-64" x1="128" />
            <line x2="64" y1="-64" y2="0" x1="64" />
        </blockdef>
        <blockdef name="inv">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="160" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="-64" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="0" x1="128" />
            <line x2="64" y1="0" y2="-64" x1="64" />
            <circle r="16" cx="144" cy="-32" />
        </blockdef>
        <block symbolname="buf" name="XLXI_1">
            <blockpin signalname="SENSOR_1" name="I" />
            <blockpin name="O" />
        </block>
        <block symbolname="buf" name="XLXI_2">
            <blockpin signalname="SENSOR_2" name="I" />
            <blockpin name="O" />
        </block>
        <block symbolname="buf" name="XLXI_3">
            <blockpin signalname="MODE" name="I" />
            <blockpin name="O" />
        </block>
        <block symbolname="buf" name="XLXI_4">
            <blockpin signalname="FIRE" name="I" />
            <blockpin signalname="XLXN_140" name="O" />
        </block>
        <block symbolname="buf" name="XLXI_13">
            <blockpin signalname="OSC" name="I" />
            <blockpin name="O" />
        </block>
        <block symbolname="buf" name="XLXI_10">
            <blockpin signalname="XLXN_314" name="I" />
            <blockpin signalname="LED" name="O" />
        </block>
        <block symbolname="buf" name="XLXI_9">
            <blockpin signalname="XLXN_314" name="I" />
            <blockpin signalname="SERVO" name="O" />
        </block>
        <block symbolname="inv" name="XLXI_65">
            <blockpin signalname="XLXN_140" name="I" />
            <blockpin signalname="XLXN_314" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="3520" height="2720">
        <branch name="SENSOR_1">
            <wire x2="960" y1="960" y2="960" x1="848" />
        </branch>
        <instance x="960" y="992" name="XLXI_1" orien="R0" />
        <branch name="SENSOR_2">
            <wire x2="960" y1="1040" y2="1040" x1="848" />
        </branch>
        <instance x="960" y="1072" name="XLXI_2" orien="R0" />
        <branch name="MODE">
            <wire x2="960" y1="1168" y2="1168" x1="784" />
        </branch>
        <instance x="960" y="1200" name="XLXI_3" orien="R0" />
        <branch name="FIRE">
            <wire x2="960" y1="1328" y2="1328" x1="768" />
        </branch>
        <branch name="XLXN_140">
            <wire x2="1232" y1="1328" y2="1328" x1="1184" />
            <wire x2="1424" y1="1328" y2="1328" x1="1232" />
        </branch>
        <instance x="960" y="1360" name="XLXI_4" orien="R0" />
        <branch name="LED">
            <wire x2="2656" y1="1280" y2="1280" x1="2560" />
        </branch>
        <branch name="SERVO">
            <wire x2="2656" y1="1056" y2="1056" x1="2560" />
        </branch>
        <branch name="OSC">
            <wire x2="960" y1="1456" y2="1456" x1="768" />
        </branch>
        <instance x="960" y="1488" name="XLXI_13" orien="R0" />
        <instance x="2336" y="1312" name="XLXI_10" orien="R0" />
        <iomarker fontsize="28" x="848" y="960" name="SENSOR_1" orien="R180" />
        <iomarker fontsize="28" x="848" y="1040" name="SENSOR_2" orien="R180" />
        <iomarker fontsize="28" x="784" y="1168" name="MODE" orien="R180" />
        <iomarker fontsize="28" x="768" y="1328" name="FIRE" orien="R180" />
        <iomarker fontsize="28" x="768" y="1456" name="OSC" orien="R180" />
        <iomarker fontsize="28" x="2656" y="1056" name="SERVO" orien="R0" />
        <iomarker fontsize="28" x="2656" y="1280" name="LED" orien="R0" />
        <instance x="2336" y="1088" name="XLXI_9" orien="R0" />
        <instance x="1424" y="1360" name="XLXI_65" orien="R0" />
        <branch name="XLXN_314">
            <wire x2="1984" y1="1328" y2="1328" x1="1648" />
            <wire x2="2336" y1="1056" y2="1056" x1="1984" />
            <wire x2="1984" y1="1056" y2="1280" x1="1984" />
            <wire x2="1984" y1="1280" y2="1328" x1="1984" />
            <wire x2="2336" y1="1280" y2="1280" x1="1984" />
        </branch>
    </sheet>
</drawing>