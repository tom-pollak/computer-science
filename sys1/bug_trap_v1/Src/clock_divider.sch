<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="XLXN_1" />
        <signal name="CLK" />
        <signal name="CLR" />
        <signal name="XLXN_5" />
        <signal name="CNT(15:0)" />
        <signal name="CNT(6)" />
        <signal name="CLK_OUT" />
        <port polarity="Input" name="CLK" />
        <port polarity="Input" name="CLR" />
        <port polarity="Output" name="CLK_OUT" />
        <blockdef name="cb16ce">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="320" y1="-192" y2="-192" x1="384" />
            <rect width="64" x="320" y="-268" height="24" />
            <line x2="320" y1="-256" y2="-256" x1="384" />
            <line x2="64" y1="-192" y2="-192" x1="0" />
            <line x2="64" y1="-32" y2="-32" x1="192" />
            <line x2="192" y1="-64" y2="-32" x1="192" />
            <line x2="64" y1="-128" y2="-144" x1="80" />
            <line x2="80" y1="-112" y2="-128" x1="64" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="320" y1="-128" y2="-128" x1="384" />
            <rect width="256" x="64" y="-320" height="256" />
        </blockdef>
        <blockdef name="buf">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="128" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="0" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="-64" x1="128" />
            <line x2="64" y1="-64" y2="0" x1="64" />
        </blockdef>
        <blockdef name="vcc">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-64" x1="64" />
            <line x2="64" y1="0" y2="-32" x1="64" />
            <line x2="32" y1="-64" y2="-64" x1="96" />
        </blockdef>
        <block symbolname="cb16ce" name="XLXI_3">
            <blockpin signalname="CLK" name="C" />
            <blockpin signalname="XLXN_5" name="CE" />
            <blockpin signalname="CLR" name="CLR" />
            <blockpin signalname="XLXN_1" name="CEO" />
            <blockpin name="Q(15:0)" />
            <blockpin name="TC" />
        </block>
        <block symbolname="cb16ce" name="XLXI_4">
            <blockpin signalname="CLK" name="C" />
            <blockpin signalname="XLXN_1" name="CE" />
            <blockpin signalname="CLR" name="CLR" />
            <blockpin name="CEO" />
            <blockpin signalname="CNT(15:0)" name="Q(15:0)" />
            <blockpin name="TC" />
        </block>
        <block symbolname="buf" name="XLXI_7">
            <blockpin signalname="CNT(6)" name="I" />
            <blockpin signalname="CLK_OUT" name="O" />
        </block>
        <block symbolname="vcc" name="XLXI_11">
            <blockpin signalname="XLXN_5" name="P" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="1760" height="1360">
        <instance x="528" y="656" name="XLXI_3" orien="R0" />
        <instance x="528" y="1136" name="XLXI_4" orien="R0" />
        <branch name="XLXN_1">
            <wire x2="432" y1="688" y2="944" x1="432" />
            <wire x2="528" y1="944" y2="944" x1="432" />
            <wire x2="1024" y1="688" y2="688" x1="432" />
            <wire x2="1024" y1="464" y2="464" x1="912" />
            <wire x2="1024" y1="464" y2="688" x1="1024" />
        </branch>
        <branch name="CLK">
            <wire x2="352" y1="528" y2="528" x1="176" />
            <wire x2="528" y1="528" y2="528" x1="352" />
            <wire x2="352" y1="528" y2="1008" x1="352" />
            <wire x2="528" y1="1008" y2="1008" x1="352" />
        </branch>
        <branch name="CLR">
            <wire x2="288" y1="624" y2="624" x1="176" />
            <wire x2="288" y1="624" y2="1104" x1="288" />
            <wire x2="528" y1="1104" y2="1104" x1="288" />
            <wire x2="528" y1="624" y2="624" x1="288" />
        </branch>
        <branch name="XLXN_5">
            <wire x2="352" y1="256" y2="464" x1="352" />
            <wire x2="528" y1="464" y2="464" x1="352" />
        </branch>
        <branch name="CNT(15:0)">
            <wire x2="1072" y1="880" y2="880" x1="912" />
            <wire x2="1072" y1="880" y2="976" x1="1072" />
            <wire x2="1072" y1="976" y2="1024" x1="1072" />
        </branch>
        <bustap x2="1168" y1="976" y2="976" x1="1072" />
        <instance x="1216" y="1008" name="XLXI_7" orien="R0" />
        <branch name="CNT(6)">
            <wire x2="1216" y1="976" y2="976" x1="1168" />
        </branch>
        <branch name="CLK_OUT">
            <wire x2="1504" y1="976" y2="976" x1="1440" />
        </branch>
        <instance x="288" y="256" name="XLXI_11" orien="R0" />
        <iomarker fontsize="28" x="1504" y="976" name="CLK_OUT" orien="R0" />
        <iomarker fontsize="28" x="176" y="528" name="CLK" orien="R180" />
        <iomarker fontsize="28" x="176" y="624" name="CLR" orien="R180" />
    </sheet>
</drawing>