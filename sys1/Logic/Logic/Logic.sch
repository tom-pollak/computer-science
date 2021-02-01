<?xml version="1.0" encoding="UTF-8"?>
<drawing version="7">
    <attr value="zynq" name="DeviceFamilyName">
        <trait delete="all:0" />
        <trait editname="all:0" />
        <trait edittrait="all:0" />
    </attr>
    <netlist>
        <signal name="XLXN_3" />
        <signal name="XLXN_4" />
        <signal name="XLXN_5" />
        <signal name="XLXN_7" />
        <signal name="XLXN_8" />
        <signal name="XLXN_9" />
        <signal name="XLXN_10" />
        <signal name="XLXN_11" />
        <signal name="XLXN_12" />
        <signal name="XLXN_13" />
        <signal name="XLXN_14" />
        <signal name="XLXN_15" />
        <signal name="A" />
        <signal name="B" />
        <signal name="BUF_GATE" />
        <signal name="NOT_GATE" />
        <signal name="AND_GATE" />
        <signal name="OR_GATE" />
        <signal name="XOR_GATE" />
        <signal name="NAND_GATE" />
        <signal name="NOR_GATE" />
        <signal name="XNOR_GATE" />
        <port polarity="Input" name="A" />
        <port polarity="Input" name="B" />
        <port polarity="Output" name="BUF_GATE" />
        <port polarity="Output" name="NOT_GATE" />
        <port polarity="Output" name="AND_GATE" />
        <port polarity="Output" name="OR_GATE" />
        <port polarity="Output" name="XOR_GATE" />
        <port polarity="Output" name="NAND_GATE" />
        <port polarity="Output" name="NOR_GATE" />
        <port polarity="Output" name="XNOR_GATE" />
        <blockdef name="inv">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="160" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="-64" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="0" x1="128" />
            <line x2="64" y1="0" y2="-64" x1="64" />
            <circle r="16" cx="144" cy="-32" />
        </blockdef>
        <blockdef name="and2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="192" y1="-96" y2="-96" x1="256" />
            <arc ex="144" ey="-144" sx="144" sy="-48" r="48" cx="144" cy="-96" />
            <line x2="64" y1="-48" y2="-48" x1="144" />
            <line x2="144" y1="-144" y2="-144" x1="64" />
            <line x2="64" y1="-48" y2="-144" x1="64" />
        </blockdef>
        <blockdef name="buf">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-32" y2="-32" x1="0" />
            <line x2="128" y1="-32" y2="-32" x1="224" />
            <line x2="128" y1="0" y2="-32" x1="64" />
            <line x2="64" y1="-32" y2="-64" x1="128" />
            <line x2="64" y1="-64" y2="0" x1="64" />
        </blockdef>
        <blockdef name="or2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="192" y1="-96" y2="-96" x1="256" />
            <arc ex="192" ey="-96" sx="112" sy="-48" r="88" cx="116" cy="-136" />
            <arc ex="48" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <line x2="48" y1="-144" y2="-144" x1="112" />
            <arc ex="112" ey="-144" sx="192" sy="-96" r="88" cx="116" cy="-56" />
            <line x2="48" y1="-48" y2="-48" x1="112" />
        </blockdef>
        <blockdef name="xor2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="60" y1="-128" y2="-128" x1="0" />
            <line x2="208" y1="-96" y2="-96" x1="256" />
            <arc ex="44" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <arc ex="64" ey="-144" sx="64" sy="-48" r="56" cx="32" cy="-96" />
            <line x2="64" y1="-144" y2="-144" x1="128" />
            <line x2="64" y1="-48" y2="-48" x1="128" />
            <arc ex="128" ey="-144" sx="208" sy="-96" r="88" cx="132" cy="-56" />
            <arc ex="208" ey="-96" sx="128" sy="-48" r="88" cx="132" cy="-136" />
        </blockdef>
        <blockdef name="nand2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="216" y1="-96" y2="-96" x1="256" />
            <circle r="12" cx="204" cy="-96" />
            <line x2="64" y1="-48" y2="-144" x1="64" />
            <line x2="144" y1="-144" y2="-144" x1="64" />
            <line x2="64" y1="-48" y2="-48" x1="144" />
            <arc ex="144" ey="-144" sx="144" sy="-48" r="48" cx="144" cy="-96" />
        </blockdef>
        <blockdef name="nor2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="64" y1="-128" y2="-128" x1="0" />
            <line x2="216" y1="-96" y2="-96" x1="256" />
            <circle r="12" cx="204" cy="-96" />
            <arc ex="192" ey="-96" sx="112" sy="-48" r="88" cx="116" cy="-136" />
            <arc ex="112" ey="-144" sx="192" sy="-96" r="88" cx="116" cy="-56" />
            <arc ex="48" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <line x2="48" y1="-48" y2="-48" x1="112" />
            <line x2="48" y1="-144" y2="-144" x1="112" />
        </blockdef>
        <blockdef name="xnor2">
            <timestamp>2000-1-1T10:10:10</timestamp>
            <line x2="64" y1="-64" y2="-64" x1="0" />
            <line x2="60" y1="-128" y2="-128" x1="0" />
            <arc ex="44" ey="-144" sx="48" sy="-48" r="56" cx="16" cy="-96" />
            <arc ex="64" ey="-144" sx="64" sy="-48" r="56" cx="32" cy="-96" />
            <line x2="64" y1="-144" y2="-144" x1="128" />
            <line x2="64" y1="-48" y2="-48" x1="128" />
            <arc ex="128" ey="-144" sx="208" sy="-96" r="88" cx="132" cy="-56" />
            <arc ex="208" ey="-96" sx="128" sy="-48" r="88" cx="132" cy="-136" />
            <circle r="8" cx="220" cy="-96" />
            <line x2="256" y1="-96" y2="-96" x1="228" />
            <line x2="60" y1="-28" y2="-28" x1="60" />
        </blockdef>
        <block symbolname="inv" name="XLXI_4">
            <blockpin signalname="A" name="I" />
            <blockpin signalname="NOT_GATE" name="O" />
        </block>
        <block symbolname="buf" name="XLXI_3">
            <blockpin signalname="A" name="I" />
            <blockpin signalname="BUF_GATE" name="O" />
        </block>
        <block symbolname="and2" name="XLXI_2">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="AND_GATE" name="O" />
        </block>
        <block symbolname="or2" name="XLXI_5">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="OR_GATE" name="O" />
        </block>
        <block symbolname="xor2" name="XLXI_6">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="XOR_GATE" name="O" />
        </block>
        <block symbolname="nand2" name="XLXI_7">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="NAND_GATE" name="O" />
        </block>
        <block symbolname="xnor2" name="XLXI_9">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="XNOR_GATE" name="O" />
        </block>
        <block symbolname="nor2" name="XLXI_8">
            <blockpin signalname="B" name="I0" />
            <blockpin signalname="A" name="I1" />
            <blockpin signalname="NOR_GATE" name="O" />
        </block>
    </netlist>
    <sheet sheetnum="1" width="2720" height="1760">
        <branch name="A">
            <wire x2="1008" y1="144" y2="144" x1="768" />
            <wire x2="1008" y1="144" y2="272" x1="1008" />
            <wire x2="1264" y1="272" y2="272" x1="1008" />
            <wire x2="1008" y1="272" y2="400" x1="1008" />
            <wire x2="1008" y1="400" y2="544" x1="1008" />
            <wire x2="1232" y1="544" y2="544" x1="1008" />
            <wire x2="1008" y1="544" y2="704" x1="1008" />
            <wire x2="1232" y1="704" y2="704" x1="1008" />
            <wire x2="1008" y1="704" y2="864" x1="1008" />
            <wire x2="1232" y1="864" y2="864" x1="1008" />
            <wire x2="1008" y1="864" y2="1040" x1="1008" />
            <wire x2="1232" y1="1040" y2="1040" x1="1008" />
            <wire x2="1008" y1="1040" y2="1216" x1="1008" />
            <wire x2="1232" y1="1216" y2="1216" x1="1008" />
            <wire x2="1008" y1="1216" y2="1376" x1="1008" />
            <wire x2="1232" y1="1376" y2="1376" x1="1008" />
            <wire x2="1264" y1="400" y2="400" x1="1008" />
        </branch>
        <branch name="B">
            <wire x2="960" y1="208" y2="208" x1="768" />
            <wire x2="960" y1="208" y2="608" x1="960" />
            <wire x2="1232" y1="608" y2="608" x1="960" />
            <wire x2="960" y1="608" y2="768" x1="960" />
            <wire x2="1232" y1="768" y2="768" x1="960" />
            <wire x2="960" y1="768" y2="928" x1="960" />
            <wire x2="1232" y1="928" y2="928" x1="960" />
            <wire x2="960" y1="928" y2="1104" x1="960" />
            <wire x2="1232" y1="1104" y2="1104" x1="960" />
            <wire x2="960" y1="1104" y2="1280" x1="960" />
            <wire x2="1232" y1="1280" y2="1280" x1="960" />
            <wire x2="960" y1="1280" y2="1440" x1="960" />
            <wire x2="1232" y1="1440" y2="1440" x1="960" />
        </branch>
        <instance x="1264" y="432" name="XLXI_4" orien="R0" />
        <instance x="1264" y="304" name="XLXI_3" orien="R0" />
        <instance x="1232" y="672" name="XLXI_2" orien="R0" />
        <instance x="1232" y="832" name="XLXI_5" orien="R0" />
        <instance x="1232" y="992" name="XLXI_6" orien="R0" />
        <instance x="1232" y="1168" name="XLXI_7" orien="R0" />
        <instance x="1232" y="1504" name="XLXI_9" orien="R0" />
        <instance x="1232" y="1344" name="XLXI_8" orien="R0" />
        <branch name="BUF_GATE">
            <wire x2="1520" y1="272" y2="272" x1="1488" />
        </branch>
        <branch name="NOT_GATE">
            <wire x2="1520" y1="400" y2="400" x1="1488" />
        </branch>
        <branch name="AND_GATE">
            <wire x2="1520" y1="576" y2="576" x1="1488" />
        </branch>
        <branch name="OR_GATE">
            <wire x2="1520" y1="736" y2="736" x1="1488" />
        </branch>
        <branch name="XOR_GATE">
            <wire x2="1520" y1="896" y2="896" x1="1488" />
        </branch>
        <branch name="NAND_GATE">
            <wire x2="1520" y1="1072" y2="1072" x1="1488" />
        </branch>
        <branch name="NOR_GATE">
            <wire x2="1520" y1="1248" y2="1248" x1="1488" />
        </branch>
        <branch name="XNOR_GATE">
            <wire x2="1504" y1="1408" y2="1408" x1="1488" />
            <wire x2="1520" y1="1408" y2="1408" x1="1504" />
        </branch>
        <iomarker fontsize="28" x="768" y="144" name="A" orien="R180" />
        <iomarker fontsize="28" x="768" y="208" name="B" orien="R180" />
        <iomarker fontsize="28" x="1520" y="272" name="BUF_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="400" name="NOT_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="576" name="AND_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="736" name="OR_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="896" name="XOR_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="1072" name="NAND_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="1248" name="NOR_GATE" orien="R0" />
        <iomarker fontsize="28" x="1520" y="1408" name="XNOR_GATE" orien="R0" />
    </sheet>
</drawing>