# =============================================================================================================
# *
# * Copyright (c) Mike
# *
# * File Name: virtualBugTrap.py
# *
# * Version: V1.0
# *
# * Release Date:
# *
# * Author(s): M.Freeman
# *
# * Description: Online replacement for the Bug Trap
# *
# * Conditions of Use: THIS CODE IS COPYRIGHT AND IS SUPPLIED "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING,
# *                    BUT NOT LIMITED TO, ANY IMPLIED WARRANTY OF MERCHANTABILITY AND FITNESS FOR A
# *                    PARTICULAR PURPOSE.
# *
# * Notes: Yes i know, very bad code, cut-and-paste python at its best, a quick and dirty solution to COVID :)
# *
# =============================================================================================================

import os
import re
import sys
import subprocess
import time
import threading

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

updateSimulation = True

fpgaStateUpdate = False
trapStateUpdate = False

systemExit = False
simulationRunning = False
soundRunning = False

skipTestBench = False
skipSimpleCPU = False
windows = True

GHDL = "C:/APPS/ghdl/bin/ghdl.exe"


def periodicCall():

    global fpgaStateUpdate, systemExit

    if fpgaStateUpdate:
        print("Updating simulation")

        updateSystemState()

        if labData == 1:
            lab1()

        elif labData == 2:
            lab2()

        elif labData == 3:
            lab3()

        elif labData == 4:
            lab4()

        elif labData == 5:
            lab5()

        elif labData == 8:
            lab8()

        fpgaStateUpdate = False

    if systemExit:
        sys.exit(1)

    window.after(200, periodicCall)


def updateSystemState():
    global fpgaPushButtonData
    global fpgaSlideSwitchData
    global fpgaKeypadDigitData

    global trapInfraredSensorData
    global trapPushButtonData
    global trapToggleSwitchData

    if os.path.exists("simulation.vcd"):
        os.remove("simulation.vcd")

    if os.path.exists("fpgaRedGreenLed.dat"):
        os.remove("fpgaRedGreenLed.dat")

    if os.path.exists("fpgaSevenSegment0.dat"):
        os.remove("fpgaSevenSegment0.dat")
    if os.path.exists("fpgaSevenSegment1.dat"):
        os.remove("fpgaSevenSegment1.dat")
    if os.path.exists("fpgaSevenSegment2.dat"):
        os.remove("fpgaSevenSegment2.dat")
    if os.path.exists("fpgaSevenSegment3.dat"):
        os.remove("fpgaSevenSegment3.dat")

    if os.path.exists("trapLedServo.dat"):
        os.remove("trapLedServo.dat")

    fpgaPushButtonFile = open("fpgaPushButton.dat", "w")
    for data in fpgaPushButtonData:
        fpgaPushButtonFile.write(str(data))
    fpgaPushButtonFile.close()

    fpgaSlideSwitchFile = open("fpgaSlideSwitch.dat", "w")
    for data in fpgaSlideSwitchData:
        fpgaSlideSwitchFile.write(str(data))
    fpgaSlideSwitchFile.close()

    fpgaKeypadDigit0File = open("fpgaKeypadDigit0.dat", "w")
    if fpgaKeypadDigitData[0] == 0:
        fpgaKeypadDigit0File.write("000")
    elif fpgaKeypadDigitData[0] == 1:
        fpgaKeypadDigit0File.write("001")
    elif fpgaKeypadDigitData[0] == 2:
        fpgaKeypadDigit0File.write("010")
    elif fpgaKeypadDigitData[0] == 3:
        fpgaKeypadDigit0File.write("011")
    elif fpgaKeypadDigitData[0] == 4:
        fpgaKeypadDigit0File.write("100")
    elif fpgaKeypadDigitData[0] == 5:
        fpgaKeypadDigit0File.write("101")
    elif fpgaKeypadDigitData[0] == 6:
        fpgaKeypadDigit0File.write("110")
    elif fpgaKeypadDigitData[0] == 7:
        fpgaKeypadDigit0File.write("111")
    else:
        fpgaKeypadDigit0File.write("000")
    fpgaKeypadDigit0File.close()

    fpgaKeypadDigit1File = open("fpgaKeypadDigit1.dat", "w")
    if fpgaKeypadDigitData[1] == 0:
        fpgaKeypadDigit1File.write("000")
    elif fpgaKeypadDigitData[1] == 1:
        fpgaKeypadDigit1File.write("001")
    elif fpgaKeypadDigitData[1] == 2:
        fpgaKeypadDigit1File.write("010")
    elif fpgaKeypadDigitData[1] == 3:
        fpgaKeypadDigit1File.write("011")
    elif fpgaKeypadDigitData[1] == 4:
        fpgaKeypadDigit1File.write("100")
    elif fpgaKeypadDigitData[1] == 5:
        fpgaKeypadDigit1File.write("101")
    elif fpgaKeypadDigitData[1] == 6:
        fpgaKeypadDigit1File.write("110")
    elif fpgaKeypadDigitData[1] == 7:
        fpgaKeypadDigit1File.write("111")
    else:
        fpgaKeypadDigit1File.write("000")
    fpgaKeypadDigit1File.close()

    trapSensorSwitchFile = open("trapSensorSwitch.dat", "w")
    for data in trapInfraredSensorData:
        trapSensorSwitchFile.write(str(data))

    trapSensorSwitchFile.write(str(trapToggleSwitchData))
    trapSensorSwitchFile.write(str(trapPushButtonData))
    trapSensorSwitchFile.close()


def splat():
    if not soundRunning:
        playsound("Sounds/splat.wav")


def beep_on():
    if not soundRunning:
        playsound("Sounds/beep_on.wav")


def beep_off():
    if not soundRunning:
        playsound("Sounds/beep_off.wav")


def lab1():
    print("LAB 1")

    if windows:
        process = subprocess.Popen(
            GHDL + " -a --work=unisim --ieee=synopsys ../Logic.vhf",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
    else:
        process = subprocess.Popen(
            ['ghdl -a --work=unisim --ieee=synopsys LAB1/Logic.vhf'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
    stdout, stderr = process.communicate()
    print("Analysis : Logic " + " " + stdout + " " + stderr)

    debugText.configure(state=tk.NORMAL)
    debugText.insert(tk.END,
                     "Analysis : Logic " + " " + stdout + " " + stderr + "\n")
    debugText.see(tk.END)
    debugText.update()
    debugText.configure(state=tk.DISABLED)

    if windows:
        pass
    else:
        process = subprocess.Popen(
            ['ghdl -e --work=unisim --ieee=synopsys Logic'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
        stdout, stderr = process.communicate()
        print("Compile : Logic " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Compile : Logic " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

    if not skipTestBench:
        if windows:
            process = subprocess.Popen(
                GHDL +
                " -a --work=unisim --ieee=synopsys Lab1/testbench_1.vhd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen(
                ['ghdl -a --work=unisim --ieee=synopsys LAB1/testbench_1.vhd'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        stdout, stderr = process.communicate()
        print("Analysis : testbench " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "Analysis : testbench_1 " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            pass
        else:
            process = subprocess.Popen(
                ['ghdl -e --work=unisim --ieee=synopsys testbench_1'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            stdout, stderr = process.communicate()
            print("Compile : testbench " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Compile : testbench " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

    if windows:
        process = subprocess.Popen(
            GHDL +
            " -r --work=unisim --ieee=synopsys testbench_1 --vcd=simulation.vcd",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
    else:
        process = subprocess.Popen([
            'ghdl -r --work=unisim --ieee=synopsys testbench_1 --vcd=simulation.vcd'
        ],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True)
    stdout, stderr = process.communicate()
    print("Run : testbench " + " " + stdout + " " + stderr)

    debugText.configure(state=tk.NORMAL)
    debugText.insert(tk.END, "                 HG   GR\n")
    debugText.insert(tk.END,
                     "Run : testbench " + " " + stdout + " " + stderr + "\n")
    debugText.see(tk.END)
    debugText.update()
    debugText.configure(state=tk.DISABLED)

    try:
        fpga = Image.open("Images/FPGA/fpga.png")

        fpgaRedGreenLedFile = open("fpgaRedGreenLed.dat", "r")
        data = str(fpgaRedGreenLedFile.read())
        fpgaRedGreenLedFile.close()

        if data[1] == '1':
            fpga_red = Image.open("Images/FPGA/LEDS/red.png")
            fpga.paste(fpga_red, (0, 0), fpga_red.convert('RGBA'))

        if data[0] == '1':
            fpga_green = Image.open("Images/FPGA/LEDS/green.png")
            fpga.paste(fpga_green, (0, 0), fpga_green.convert('RGBA'))

        fpgaImage = ImageTk.PhotoImage(fpga)

        label1.config(image=fpgaImage)
        label1.image = fpgaImage
        label1.pack()

        print("Finished")
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Finished\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

    except IOError as e:
        print("I/O error{0}: {1}".format(e.errno, e.strerror))

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return

    except:
        print("Unexpected error:", sys.exc_info()[0])
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Unexpected error:", sys.exc_info()[0] + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return


def lab2WorkerThread():

    global trapStateUpdate

    signalBlockStart = False

    osc_Symbol = ""
    sensor_1_Symbol = ""
    sensor_2_Symbol = ""
    mode_Symbol = ""
    fire_Symbol = ""
    servo_Symbol = ""
    led_Symbol = ""

    sensor_1_State = False
    sensor_2_State = False
    mode_State = False
    fire_State = False
    servo_State = False
    led_State = False

    timeBlockStart = False
    timeBlockUpdate = False

    simulationTime = 0
    lastSimulationTime = 0

    lastTriggerTime = 0
    simulationStepTime = 0

    vcdFileName = "simulation.vcd"

    try:
        vcdFile = open(vcdFileName, "r")

        for line in vcdFile.readlines():
            if "module" in line:
                signalBlockStart = False

            if "testbench_2a" in line:
                signalBlockStart = True

            if signalBlockStart:
                if "osc" in line:
                    osc_Symbol = line.split(" ")[3]
                elif "sensor_1" in line:
                    sensor_1_Symbol = line.split(" ")[3]
                elif "sensor_2" in line:
                    sensor_2_Symbol = line.split(" ")[3]
                elif "mode" in line:
                    mode_Symbol = line.split(" ")[3]
                elif "fire" in line:
                    fire_Symbol = line.split(" ")[3]
                elif "servo" in line:
                    servo_Symbol = line.split(" ")[3]
                elif "led" in line:
                    led_Symbol = line.split(" ")[3]

                timeBlockStart = True
                data = re.sub('[\r\n]+', '', line)
                lastSimulationTime = simulationTime
                simulationTime = int(data[1:]) / 1000000000000

                if timeBlockUpdate:
                    timeBlockUpdate = False

                    if lastTriggerTime == 0:
                        simulationStepTime = lastSimulationTime
                    else:
                        simulationStepTime = lastSimulationTime - lastTriggerTime

                    lastTriggerTime = lastSimulationTime

                    total = 0
                    if not sensor_1_State:
                        total = total + 4
                    if not sensor_2_State:
                        total = total + 8
                    if mode_State:
                        total = total + 2
                    if not fire_State:
                        total = total + 1

                    fpga = Image.open("Images/FPGA/fpga.png")
                    inputSignals = "0000"

                    if total == 0:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
                        inputSignals = "0000"
                    elif total == 1:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
                        inputSignals = "0001"
                    elif total == 2:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
                        inputSignals = "0010"
                    elif total == 3:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
                        inputSignals = "0011"
                    elif total == 4:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
                        inputSignals = "0100"
                    elif total == 5:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
                        inputSignals = "0101"
                    elif total == 6:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
                        inputSignals = "0110"
                    elif total == 7:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
                        inputSignals = "0111"
                    elif total == 8:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
                        inputSignals = "1000"
                    elif total == 9:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
                        inputSignals = "1001"
                    elif total == 10:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
                        inputSignals = "1010"
                    elif total == 11:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
                        inputSignals = "1011"
                    elif total == 12:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
                        inputSignals = "1100"
                    elif total == 13:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
                        inputSignals = "1101"
                    elif total == 14:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
                        inputSignals = "1110"
                    else:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")
                        inputSignals = "1111"

                    fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

                    total = 0
                    if servo_State:
                        total = total + 1
                        if not sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_e.png")
                        elif sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_f.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False

                        elif not sensor_1_State and sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_b.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False
                        else:
                            trap = Image.open("Images/TRAP/trap_closed_m.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False
                    else:
                        if not sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_e.png")
                        elif sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_f.png")
                        elif not sensor_1_State and sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_b.png")
                        else:
                            trap = Image.open("Images/TRAP/trap_open_m.png")

                    if sensor_1_State:
                        trapInfraredSensor_A_State.set(1)
                    else:
                        trapInfraredSensor_A_State.set(0)

                    if sensor_2_State:
                        trapInfraredSensor_B_State.set(1)
                    else:
                        trapInfraredSensor_B_State.set(0)

                    if mode_State:
                        trapPushButtonState.set(1)
                    else:
                        trapPushButtonState.set(0)

                    if fire_State:
                        trapToggleSwitchState.set(1)
                    else:
                        trapToggleSwitchState.set(0)

                    if led_State:
                        total = total + 2
                        led = Image.open("Images/TRAP/LED/led_on.png")
                    else:
                        led = Image.open("Images/TRAP/LED/led_off.png")

                    trap.paste(led, (0, 0), led.convert('RGBA'))

                    if mode_State:
                        switch = Image.open("Images/TRAP/SWITCH/toggle_up.png")
                    else:
                        switch = Image.open(
                            "Images/TRAP/SWITCH/toggle_down.png")

                    trap.paste(switch, (0, 0), switch.convert('RGBA'))
                    outputSignals = "00"

                    if total == 0:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
                        outputSignals = "00"
                    elif total == 1:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
                        outputSignals = "01"
                    elif total == 2:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
                        outputSignals = "10"
                    else:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
                        outputSignals = "11"

                    fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

                    fpgaImage = ImageTk.PhotoImage(fpga)
                    trapImage = ImageTk.PhotoImage(trap)

                    label1.config(image=fpgaImage)
                    label1.image = fpgaImage
                    label1.pack()

                    label2.config(image=trapImage)
                    label2.image = trapImage
                    label2.pack()

                    debugText.configure(state=tk.NORMAL)
                    debugText.insert(
                        tk.END,
                        "Step :" + " " + inputSignals + "  " + outputSignals +
                        " - " + str(simulationStepTime / 1000.0) + "s\n")
                    debugText.see(tk.END)
                    debugText.update()
                    debugText.configure(state=tk.DISABLED)

                    if trapSimulationModeState.get() == 0:
                        while not trapStateUpdate:
                            time.sleep(0.5)
                        trapStateUpdate = False
                    else:
                        time.sleep(simulationStepTime / 1000.0)

            if timeBlockStart:
                data = re.sub('[\r\n]+', '', line)

                if servo_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        servo_State = True
                    else:
                        servo_State = False

                if led_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        led_State = True
                    else:
                        led_State = False

                if sensor_1_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        sensor_1_State = True
                    else:
                        sensor_1_State = False

                if sensor_2_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        sensor_2_State = True
                    else:
                        sensor_2_State = False

                if mode_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        mode_State = True
                    else:
                        mode_State = False

                if fire_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        fire_State = True
                    else:
                        fire_State = False

        print("Finished")
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Finished\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

    except IOError as e:
        print("I/O error{0}: {1}".format(e.errno, e.strerror))

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return

    except:
        print("Unexpected error:", sys.exc_info()[0])
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Unexpected error:", sys.exc_info()[0] + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return


def lab2():
    print("LAB 2")

    if testCaseData == 0:
        if windows:
            process = subprocess.Popen(
                GHDL +
                " -a --work=unisim --ieee=synopsys ../bug_trap_controller.vhf",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -a --work=unisim --ieee=synopsys LAB2/bug_trap_controller.vhf'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Analysis : bug_trap_controller " + " " + str(stdout) + " " + str(stderr))

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Analysis : bug_trap_controller " + " " + stdout + " " +
            stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            pass
        else:
            process = subprocess.Popen(
                ['ghdl -e --work=unisim --ieee=synopsys bug_trap_controller'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            stdout, stderr = process.communicate()
            print("Compile : bug_trap_controller " + " " + stdout + " " +
                  stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Compile : bug_trap_controller " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_2.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB2/testbench_2.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_2 " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : testbench_2 " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_2'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_2 " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_2 " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_2 --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_2 --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_2 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "                   BFTP   LS\n")
        debugText.insert(
            tk.END, "Run : testbench_2 " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            total = (trapInfraredSensorData[0] *
                     8) + (trapInfraredSensorData[1] *
                           4) + (trapToggleSwitchData * 2) + trapPushButtonData

            fpga = Image.open("Images/FPGA/fpga.png")

            if total == 0:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif total == 1:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif total == 2:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif total == 3:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif total == 4:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif total == 5:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif total == 6:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif total == 7:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            elif total == 8:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
            elif total == 9:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
            elif total == 10:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
            elif total == 11:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
            elif total == 12:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
            elif total == 13:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
            elif total == 14:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            trapLedServoFile = open("trapLedServo.dat", "r")
            data = str(trapLedServoFile.read())
            trapLedServoFile.close()

            total = 0
            if data[1] == '1':
                total = total + 1
                if trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_closed_e.png")
                elif trapInfraredSensorData[1] == 0 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_closed_f.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False

                elif trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 0:
                    trap = Image.open("Images/TRAP/trap_closed_b.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False

                else:
                    trap = Image.open("Images/TRAP/trap_closed_m.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False
            else:
                if trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_open_e.png")
                elif trapInfraredSensorData[1] == 0 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_open_f.png")
                elif trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 0:
                    trap = Image.open("Images/TRAP/trap_open_b.png")
                else:
                    trap = Image.open("Images/TRAP/trap_open_m.png")

            if data[0] == '1':
                total = total + 2
                led = Image.open("Images/TRAP/LED/led_on.png")
            else:
                led = Image.open("Images/TRAP/LED/led_off.png")

            trap.paste(led, (0, 0), led.convert('RGBA'))

            if trapToggleSwitchData == 0:
                switch = Image.open("Images/TRAP/SWITCH/toggle_up.png")
            else:
                switch = Image.open("Images/TRAP/SWITCH/toggle_down.png")

            trap.paste(switch, (0, 0), switch.convert('RGBA'))

            if total == 0:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif total == 1:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif total == 2:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)
            trapImage = ImageTk.PhotoImage(trap)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            label2.config(image=trapImage)
            label2.image = trapImage
            label2.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    elif testCaseData == 1:

        try:
            source_file = open("./Lab2/1/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : " + file_name + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys ' + file_name],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_2a.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB2/testbench_2a.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_2a " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_2a " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_2a'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_2a " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_2a " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_2a --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_2a --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_2a " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "Run : testbench_2a " + " " + stdout + " " + stderr + "\n\n")
        debugText.insert(tk.END, "       BFTP  LS\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = True
        thread1 = threading.Thread(target=lab2WorkerThread)
        thread1.setDaemon(1)
        thread1.start()


def lab3():
    print("LAB 3")

    if testCaseData == 0:
        if windows:
            process = subprocess.Popen(
                GHDL + " -a --work=unisim --ieee=synopsys ../top_level.vhf",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen(
                ['ghdl -a --work=unisim --ieee=synopsys LAB3/top_level.vhf'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        stdout, stderr = process.communicate()
        print("Analysis : top_level " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "Analysis : top_level " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            pass
        else:
            process = subprocess.Popen(
                ['ghdl -e --work=unisim --ieee=synopsys top_level'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            stdout, stderr = process.communicate()
            print("Compile : top_level " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Compile : top_level " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_3.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB3/testbench_3.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_3 " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : testbench_3 " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_3'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_3 " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_3 " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_3 --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_3 --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_3 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END,
                         "                   HGFEDCBA   GFEDCBA   GR\n")
        debugText.insert(
            tk.END, "Run : testbench_3 " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            fpgaSevenSegmentFile = open("fpgaSevenSegment0.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            fpga = Image.open("Images/FPGA/fpga.png")

            if data == "1000000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif data == "1111001":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif data == "0100100":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif data == "0110000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif data == "0011001":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif data == "0010010":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif data == "0000010":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif data == "1111000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            elif data == "0000000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
            elif data == "0011000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
            elif data == "0001000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
            elif data == "0000011":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
            elif data == "0000110":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
            elif data == "0100001":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
            elif data == "0000110":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            fpgaRedGreenLedFile = open("fpgaRedGreenLed.dat", "r")
            data = str(fpgaRedGreenLedFile.read())
            fpgaRedGreenLedFile.close()

            if data[1] == '1':
                fpga_red = Image.open("Images/FPGA/LEDS/red.png")
                fpga.paste(fpga_red, (0, 0), fpga_red.convert('RGBA'))

            if data[0] == '1':
                fpga_green = Image.open("Images/FPGA/LEDS/green.png")
                fpga.paste(fpga_green, (0, 0), fpga_green.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    elif testCaseData == 1:

        if windows:
            process = subprocess.Popen(
                GHDL + " -a --work=unisim --ieee=synopsys ../top_level.vhf",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen(
                ['ghdl -a --work=unisim --ieee=synopsys LAB3/top_level.vhf'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        stdout, stderr = process.communicate()
        print("Analysis : top_level " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "Analysis : top_level " + " " + stdout + " " + stderr + "\n")
        debugText.configure(state=tk.DISABLED)

        if windows:
            pass
        else:
            process = subprocess.Popen(
                ['ghdl -e --work=unisim --ieee=synopsys top_level'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            stdout, stderr = process.communicate()
            print("Compile : top_level " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Compile : top_level " + " " + stdout + " " + stderr + "\n")
            debugText.configure(state=tk.DISABLED)

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_3a.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB3/testbench_3a.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_3a " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_3a " + " " + stdout + " " +
                stderr + "\n")
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_3a'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_3a " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_3a " + " " + stdout + " " +
                    stderr + "\n")
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_3a --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_3a --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_3 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "                    HGFEDCBA   GFEDCBA   GFEDCBA   GFEDCBA\n")
        debugText.insert(
            tk.END, "Run : testbench_3a " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            fpgaSevenSegmentFile = open("fpgaSevenSegment0.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            fpga = Image.open("Images/FPGA/fpga.png")

            if data == "1000000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif data == "1111001":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif data == "0100100":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif data == "0110000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif data == "0011001":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif data == "0010010":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif data == "0000010":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif data == "1111000":
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_x.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment1.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif data == "1111001":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif data == "0100100":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            elif data == "0110000":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
            elif data == "0011001":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_4.png")
            elif data == "0010010":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_5.png")
            elif data == "0000010":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_6.png")
            elif data == "1111000":
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_7.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_x.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment2.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_0.png")
            elif data == "1111001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_1.png")
            elif data == "0100100":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_2.png")
            elif data == "0110000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_3.png")
            elif data == "0011001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_4.png")
            elif data == "0010010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_5.png")
            elif data == "0000010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_6.png")
            elif data == "1111000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_7.png")
            else:
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_x.png")

            fpga.paste(digit_2, (0, 0), digit_2.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return


def lab4():
    print("LAB 4")

    if testCaseData == 0:
        if windows:
            process = subprocess.Popen(
                GHDL + " -a --work=unisim --ieee=synopsys ../full_adder.vhf",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen(
                ['ghdl -a --work=unisim --ieee=synopsys LAB4/full_adder.vhf'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        stdout, stderr = process.communicate()
        print("Analysis : full_adder " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "Analysis : full_adder " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            pass
        else:
            process = subprocess.Popen(
                ['ghdl -e --work=unisim --ieee=synopsys full_adder'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
            stdout, stderr = process.communicate()
            print("Compile : full_adder " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Compile : full_adder " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_4.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB4/testbench_4.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_4 " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : testbench_4 " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_4'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_4 " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_4 " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_4 --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_4 --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_4 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "                   DCBA   GR \n")
        debugText.insert(
            tk.END, "Run : testbench_4 " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            fpga = Image.open("Images/FPGA/fpga.png")

            if fpgaSlideSwitchData[3] == 1:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_on.png")
            else:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_off.png")
            fpga.paste(sw0, (0, 0), sw0.convert('RGBA'))
            if fpgaSlideSwitchData[2] == 1:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_on.png")
            else:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_off.png")
            fpga.paste(sw1, (0, 0), sw1.convert('RGBA'))
            if fpgaSlideSwitchData[1] == 1:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_on.png")
            else:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_off.png")
            fpga.paste(sw2, (0, 0), sw2.convert('RGBA'))
            if fpgaSlideSwitchData[0] == 1:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_on.png")
            else:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_off.png")
            fpga.paste(sw3, (0, 0), sw3.convert('RGBA'))

            fpgaRedGreenLedFile = open("fpgaRedGreenLed.dat", "r")
            data = str(fpgaRedGreenLedFile.read())
            fpgaRedGreenLedFile.close()

            if data[1] == '1':
                fpga_red = Image.open("Images/FPGA/LEDS/red.png")
                fpga.paste(fpga_red, (0, 0), fpga_red.convert('RGBA'))

            if data[0] == '1':
                fpga_green = Image.open("Images/FPGA/LEDS/green.png")
                fpga.paste(fpga_green, (0, 0), fpga_green.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    elif testCaseData == 1:

        try:
            source_file = open("./Lab4/1/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_4a.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB4/testbench_4a.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_4a " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_4a " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_4a'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_4a" + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_4a " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_4a --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_4a --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_4a " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "                    -A-   -B-   DCBA   GFEDCBA   GFEDCBA\n")
        debugText.insert(
            tk.END, "Run : testbench_4a " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            fpga = Image.open("Images/FPGA/fpga.png")

            if fpgaSlideSwitchData[3] == 1:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_on.png")
            else:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_off.png")
            fpga.paste(sw0, (0, 0), sw0.convert('RGBA'))
            if fpgaSlideSwitchData[2] == 1:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_on.png")
            else:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_off.png")
            fpga.paste(sw1, (0, 0), sw1.convert('RGBA'))
            if fpgaSlideSwitchData[1] == 1:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_on.png")
            else:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_off.png")
            fpga.paste(sw2, (0, 0), sw2.convert('RGBA'))
            if fpgaSlideSwitchData[0] == 1:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_on.png")
            else:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_off.png")
            fpga.paste(sw3, (0, 0), sw3.convert('RGBA'))

            if fpgaKeypadDigitData[0] == 0:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif fpgaKeypadDigitData[0] == 1:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif fpgaKeypadDigitData[0] == 2:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif fpgaKeypadDigitData[0] == 3:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif fpgaKeypadDigitData[0] == 4:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif fpgaKeypadDigitData[0] == 5:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif fpgaKeypadDigitData[0] == 6:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif fpgaKeypadDigitData[0] == 7:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_x.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            if fpgaKeypadDigitData[1] == 0:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif fpgaKeypadDigitData[1] == 1:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif fpgaKeypadDigitData[1] == 2:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            elif fpgaKeypadDigitData[1] == 3:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
            elif fpgaKeypadDigitData[1] == 4:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_4.png")
            elif fpgaKeypadDigitData[1] == 5:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_5.png")
            elif fpgaKeypadDigitData[1] == 6:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_6.png")
            elif fpgaKeypadDigitData[1] == 7:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_7.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_x.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment2.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_0.png")
            elif data == "1111001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_1.png")
            elif data == "0100100":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_2.png")
            elif data == "0110000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_3.png")
            elif data == "0011001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_4.png")
            elif data == "0010010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_5.png")
            elif data == "0000010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_6.png")
            elif data == "1111000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_7.png")
            else:
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_x.png")

            fpga.paste(digit_2, (0, 0), digit_2.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment3.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_0.png")
            elif data == "1111001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_1.png")
            elif data == "0100100":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_2.png")
            elif data == "0110000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_3.png")
            elif data == "0011001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_4.png")
            elif data == "0010010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_5.png")
            elif data == "0000010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_6.png")
            elif data == "1111000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_7.png")
            else:
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_x.png")

            fpga.paste(digit_3, (0, 0), digit_3.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    elif testCaseData == 2:

        try:
            source_file = open("./Lab4/2/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_4b.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB4/testbench_4b.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_4b " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_4b " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_4b'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_4b" + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_4b " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_4b --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_4b --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_4b " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END,
            "                    -A-   -B-   DCBA   GFEDCBA   GFEDCBA\n")
        debugText.insert(
            tk.END, "Run : testbench_4b " + " " + stdout + " " + stderr + "\n")
        debugText.update()
        debugText.see(tk.END)
        debugText.configure(state=tk.DISABLED)

        try:
            fpga = Image.open("Images/FPGA/fpga.png")

            if fpgaSlideSwitchData[3] == 1:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_on.png")
            else:
                sw0 = Image.open("Images/FPGA/SWITCHES/sw0_off.png")
            fpga.paste(sw0, (0, 0), sw0.convert('RGBA'))
            if fpgaSlideSwitchData[2] == 1:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_on.png")
            else:
                sw1 = Image.open("Images/FPGA/SWITCHES/sw1_off.png")
            fpga.paste(sw1, (0, 0), sw1.convert('RGBA'))
            if fpgaSlideSwitchData[1] == 1:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_on.png")
            else:
                sw2 = Image.open("Images/FPGA/SWITCHES/sw2_off.png")
            fpga.paste(sw2, (0, 0), sw2.convert('RGBA'))
            if fpgaSlideSwitchData[0] == 1:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_on.png")
            else:
                sw3 = Image.open("Images/FPGA/SWITCHES/sw3_off.png")
            fpga.paste(sw3, (0, 0), sw3.convert('RGBA'))

            if fpgaKeypadDigitData[0] == 0:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif fpgaKeypadDigitData[0] == 1:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif fpgaKeypadDigitData[0] == 2:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif fpgaKeypadDigitData[0] == 3:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif fpgaKeypadDigitData[0] == 4:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif fpgaKeypadDigitData[0] == 5:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif fpgaKeypadDigitData[0] == 6:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif fpgaKeypadDigitData[0] == 7:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_x.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            if fpgaKeypadDigitData[1] == 0:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif fpgaKeypadDigitData[1] == 1:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif fpgaKeypadDigitData[1] == 2:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            elif fpgaKeypadDigitData[1] == 3:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
            elif fpgaKeypadDigitData[1] == 4:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_4.png")
            elif fpgaKeypadDigitData[1] == 5:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_5.png")
            elif fpgaKeypadDigitData[1] == 6:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_6.png")
            elif fpgaKeypadDigitData[1] == 7:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_7.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_x.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment2.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_0.png")
            elif data == "1111001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_1.png")
            elif data == "0100100":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_2.png")
            elif data == "0110000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_3.png")
            elif data == "0011001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_4.png")
            elif data == "0010010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_5.png")
            elif data == "0000010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_6.png")
            elif data == "1111000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_7.png")
            else:
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_x.png")

            fpga.paste(digit_2, (0, 0), digit_2.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment3.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_0.png")
            elif data == "1111001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_1.png")
            elif data == "0100100":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_2.png")
            elif data == "0110000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_3.png")
            elif data == "0011001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_4.png")
            elif data == "0010010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_5.png")
            elif data == "0000010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_6.png")
            elif data == "1111000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_7.png")
            else:
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_x.png")

            fpga.paste(digit_3, (0, 0), digit_3.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    elif testCaseData == 3:

        try:
            source_file = open("./Lab4/3/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_4c.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB4/testbench_4c.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_4c " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_4c " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_4c'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_4c" + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_4c " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_4c --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_4c --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_4c " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "                    -A-   -B-   GFEDCBA   GFEDCBA\n")
        debugText.insert(
            tk.END, "Run : testbench_4c " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            fpga = Image.open("Images/FPGA/fpga.png")

            if fpgaKeypadDigitData[0] == 0:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif fpgaKeypadDigitData[0] == 1:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif fpgaKeypadDigitData[0] == 2:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif fpgaKeypadDigitData[0] == 3:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif fpgaKeypadDigitData[0] == 4:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif fpgaKeypadDigitData[0] == 5:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif fpgaKeypadDigitData[0] == 6:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif fpgaKeypadDigitData[0] == 7:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_x.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            if fpgaKeypadDigitData[1] == 0:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif fpgaKeypadDigitData[1] == 1:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif fpgaKeypadDigitData[1] == 2:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            elif fpgaKeypadDigitData[1] == 3:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
            elif fpgaKeypadDigitData[1] == 4:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_4.png")
            elif fpgaKeypadDigitData[1] == 5:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_5.png")
            elif fpgaKeypadDigitData[1] == 6:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_6.png")
            elif fpgaKeypadDigitData[1] == 7:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_7.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_x.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment2.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_0.png")
            elif data == "1111001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_1.png")
            elif data == "0100100":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_2.png")
            elif data == "0110000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_3.png")
            elif data == "0011001":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_4.png")
            elif data == "0010010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_5.png")
            elif data == "0000010":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_6.png")
            elif data == "1111000":
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_7.png")
            else:
                digit_2 = Image.open("Images/FPGA/SEVENSEG/2_x.png")

            fpga.paste(digit_2, (0, 0), digit_2.convert('RGBA'))

            fpgaSevenSegmentFile = open("fpgaSevenSegment3.dat", "r")
            data = str(fpgaSevenSegmentFile.read()).strip("\n")
            fpgaSevenSegmentFile.close()

            if data == "1000000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_0.png")
            elif data == "1111001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_1.png")
            elif data == "0100100":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_2.png")
            elif data == "0110000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_3.png")
            elif data == "0011001":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_4.png")
            elif data == "0010010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_5.png")
            elif data == "0000010":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_6.png")
            elif data == "1111000":
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_7.png")
            else:
                digit_3 = Image.open("Images/FPGA/SEVENSEG/3_x.png")

            fpga.paste(digit_3, (0, 0), digit_3.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return


def lab5WorkerThread():

    global trapStateUpdate

    signalBlockStart = False

    osc_Symbol = ""
    sensor_1_Symbol = ""
    sensor_2_Symbol = ""
    mode_Symbol = ""
    fire_Symbol = ""
    servo_Symbol = ""
    led_Symbol = ""

    sensor_1_State = False
    sensor_2_State = False
    mode_State = False
    fire_State = False
    servo_State = False
    led_State = False

    timeBlockStart = False
    timeBlockUpdate = False

    simulationTime = 0
    lastSimulationTime = 0

    lastTriggerTime = 0
    simulationStepTime = 0

    vcdFileName = "simulation.vcd"

    try:
        vcdFile = open(vcdFileName, "r")

        for line in vcdFile.readlines():
            if "module" in line:
                signalBlockStart = False

            if "testbench_5" in line:
                signalBlockStart = True

            if signalBlockStart:
                if "osc" in line:
                    osc_Symbol = line.split(" ")[3]
                elif "sensor_1" in line:
                    sensor_1_Symbol = line.split(" ")[3]
                elif "sensor_2" in line:
                    sensor_2_Symbol = line.split(" ")[3]
                elif "mode" in line:
                    mode_Symbol = line.split(" ")[3]
                elif "fire" in line:
                    fire_Symbol = line.split(" ")[3]
                elif "servo" in line:
                    servo_Symbol = line.split(" ")[3]
                elif "led" in line:
                    led_Symbol = line.split(" ")[3]

                timeBlockStart = True
                data = re.sub('[\r\n]+', '', line)
                lastSimulationTime = simulationTime
                simulationTime = int(data[1:]) / 1000000000000

                if timeBlockUpdate:
                    timeBlockUpdate = False

                    if lastTriggerTime == 0:
                        simulationStepTime = lastSimulationTime
                    else:
                        simulationStepTime = lastSimulationTime - lastTriggerTime

                    lastTriggerTime = lastSimulationTime

                    total = 0
                    if not sensor_1_State:
                        total = total + 4
                    if not sensor_2_State:
                        total = total + 8
                    if mode_State:
                        total = total + 2
                    if not fire_State:
                        total = total + 1

                    fpga = Image.open("Images/FPGA/fpga.png")
                    inputSignals = "0000"

                    if total == 0:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
                        inputSignals = "0000"
                    elif total == 1:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
                        inputSignals = "0001"
                    elif total == 2:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
                        inputSignals = "0010"
                    elif total == 3:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
                        inputSignals = "0011"
                    elif total == 4:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
                        inputSignals = "0100"
                    elif total == 5:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
                        inputSignals = "0101"
                    elif total == 6:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
                        inputSignals = "0110"
                    elif total == 7:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
                        inputSignals = "0111"
                    elif total == 8:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
                        inputSignals = "1000"
                    elif total == 9:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
                        inputSignals = "1001"
                    elif total == 10:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
                        inputSignals = "1010"
                    elif total == 11:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
                        inputSignals = "1011"
                    elif total == 12:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
                        inputSignals = "1100"
                    elif total == 13:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
                        inputSignals = "1101"
                    elif total == 14:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
                        inputSignals = "1110"
                    else:
                        digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")
                        inputSignals = "1111"

                    fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

                    total = 0
                    if servo_State:
                        total = total + 1
                        if not sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_e.png")
                        elif sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_f.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False

                        elif not sensor_1_State and sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_closed_b.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False
                        else:
                            trap = Image.open("Images/TRAP/trap_closed_m.png")
                            soundRunning = True
                            thread2 = threading.Thread(target=splat)
                            thread2.setDaemon(1)
                            thread2.start()
                            soundRunning = False
                    else:
                        if not sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_e.png")
                        elif sensor_1_State and not sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_f.png")
                        elif not sensor_1_State and sensor_2_State:
                            trap = Image.open("Images/TRAP/trap_open_b.png")
                        else:
                            trap = Image.open("Images/TRAP/trap_open_m.png")

                    if sensor_1_State:
                        trapInfraredSensor_A_State.set(1)
                    else:
                        trapInfraredSensor_A_State.set(0)

                    if sensor_2_State:
                        trapInfraredSensor_B_State.set(1)
                    else:
                        trapInfraredSensor_B_State.set(0)

                    if fire_State:
                        trapPushButtonState.set(0)
                    else:
                        trapPushButtonState.set(1)

                    if mode_State:
                        trapToggleSwitchState.set(1)
                    else:
                        trapToggleSwitchState.set(0)

                    if led_State:
                        total = total + 2
                        led = Image.open("Images/TRAP/LED/led_on.png")
                    else:
                        led = Image.open("Images/TRAP/LED/led_off.png")

                    trap.paste(led, (0, 0), led.convert('RGBA'))

                    if mode_State:
                        switch = Image.open("Images/TRAP/SWITCH/toggle_up.png")
                    else:
                        switch = Image.open(
                            "Images/TRAP/SWITCH/toggle_down.png")

                    trap.paste(switch, (0, 0), switch.convert('RGBA'))

                    outputSignals = "00"
                    if total == 0:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
                        outputSignals = "00"
                    elif total == 1:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
                        outputSignals = "01"
                    elif total == 2:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
                        outputSignals = "10"
                    else:
                        digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
                        outputSignals = "11"

                    print("Sim : " + inputSignals + " - " + outputSignals +
                          " - " + str(lastSimulationTime))

                    fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

                    fpgaImage = ImageTk.PhotoImage(fpga)
                    trapImage = ImageTk.PhotoImage(trap)

                    label1.config(image=fpgaImage)
                    label1.image = fpgaImage
                    label1.pack()

                    label2.config(image=trapImage)
                    label2.image = trapImage
                    label2.pack()

                    debugText.configure(state=tk.NORMAL)
                    debugText.insert(
                        tk.END,
                        "Step :" + " " + inputSignals + "  " + outputSignals +
                        " - " + str(simulationStepTime / 1000.0) + "s\n")
                    debugText.see(tk.END)
                    debugText.update()
                    debugText.configure(state=tk.DISABLED)

                    if trapSimulationModeState.get() == 0:
                        while not trapStateUpdate:
                            time.sleep(0.5)
                        trapStateUpdate = False
                    else:
                        time.sleep(simulationStepTime / 1000.0)

            if timeBlockStart:
                data = re.sub('[\r\n]+', '', line)

                if servo_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        servo_State = True
                    else:
                        servo_State = False

                if led_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        led_State = True
                    else:
                        led_State = False

                if sensor_1_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        sensor_1_State = True
                    else:
                        sensor_1_State = False

                if sensor_2_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        sensor_2_State = True
                    else:
                        sensor_2_State = False

                if mode_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "1":
                        mode_State = True
                    else:
                        mode_State = False

                if fire_Symbol == data[1:]:
                    timeBlockUpdate = True
                    if data[0] == "0":
                        fire_State = True
                    else:
                        fire_State = False

        print("Finished")
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Finished\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

    except IOError as e:
        print("I/O error{0}: {1}".format(e.errno, e.strerror))

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return

    except:
        print("Unexpected error:", sys.exc_info()[0])
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Unexpected error:", sys.exc_info()[0] + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)
        return


def lab5():
    print("LAB 5")

    if testCaseData == 0:

        try:
            source_file = open("./Lab5/0/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_5.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB5/testbench_5.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_5 " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : testbench_5 " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_5'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_5 " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_5 " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_5 --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_5 --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_5 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Run : testbench_5 " + " " + stdout + " " + stderr + "\n")
        debugText.insert(tk.END, "       BFTP  LS\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = True
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif testCaseData == 1:

        try:
            source_file = open("./Lab5/1/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_5a.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB5/testbench_5a.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_5a " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_5a " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_5a'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_5a " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_5a " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_5a --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_5a --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_5a " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Run : testbench_5a " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = True
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif testCaseData == 2:

        try:
            source_file = open("./Lab5/2/files.txt", "r")
        except IOError:
            print("Error: Input file does not exist.")
            return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys ../testbench_5b.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB5/testbench_5b.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_5b " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : testbench_5b " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_5b'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_5b " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_5b " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_5b --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_5b --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_5b " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Run : testbench_5b " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = True
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()


def lab8WorkerThread():

    global trapStateUpdate

    sensor_1_State = False
    sensor_2_State = False
    mode_State = False
    fire_State = False
    servo_State = False
    led_State = False

    simulationTime = 0
    lastSimulationTime = 0
    simulationStepTime = 0

    logFileName = "trapData.log"

    testTime = 0
    lastTestTime = 0

    lastLine = ""

    multipleTimes = False

    print("LAB8 THREAD")
    logFile = open(logFileName, "r")

    for line in logFile.readlines():

        testTime = round(int(line.split(" ")[2]) / 100000000000.0, 1)
        if testTime == lastTestTime:
            multipleTimes = True
            lastLine = line
            continue

        lastTestTime = testTime
        if multipleTimes:
            line = lastLine
            multipleTimes = False

        inputSignals = line.split(" ")[0]

        if inputSignals[0] == '1':
            sensor_1_State = False
        else:
            sensor_1_State = True

        if inputSignals[1] == '1':
            sensor_2_State = False
        else:
            sensor_2_State = True

        if inputSignals[2] == '1':
            mode_State = True
        else:
            mode_State = False

        if inputSignals[3] == '1':
            fire_State = False
        else:
            fire_State = True

        outputSignals = line.split(" ")[1]

        if outputSignals[0] == '1':
            servo_State = True
        else:
            servo_State = False

        if outputSignals[1] == '1':
            led_State = True
        else:
            led_State = False

        simulationTime = round(int(line.split(" ")[2]) / 100000000000.0, 1)

        if lastSimulationTime == 0:
            simulationStepTime = simulationTime
        else:
            simulationStepTime = simulationTime - lastSimulationTime

        lastSimulationTime = simulationTime

        total = 0
        if not sensor_1_State:
            total = total + 4
        if not sensor_2_State:
            total = total + 8
        if mode_State:
            total = total + 2
        if not fire_State:
            total = total + 1

        fpga = Image.open("Images/FPGA/fpga.png")
        inputSignals = "0000"

        if total == 0:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            inputSignals = "0000"
        elif total == 1:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            inputSignals = "0001"
        elif total == 2:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            inputSignals = "0010"
        elif total == 3:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            inputSignals = "0011"
        elif total == 4:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            inputSignals = "0100"
        elif total == 5:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            inputSignals = "0101"
        elif total == 6:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            inputSignals = "0110"
        elif total == 7:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            inputSignals = "0111"
        elif total == 8:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
            inputSignals = "1000"
        elif total == 9:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
            inputSignals = "1001"
        elif total == 10:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
            inputSignals = "1010"
        elif total == 11:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
            inputSignals = "1011"
        elif total == 12:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
            inputSignals = "1100"
        elif total == 13:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
            inputSignals = "1101"
        elif total == 14:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
            inputSignals = "1110"
        else:
            digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")
            inputSignals = "1111"

        fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

        total = 0
        if servo_State:
            total = total + 1
            if not sensor_1_State and not sensor_2_State:
                trap = Image.open("Images/TRAP/trap_closed_e.png")
            elif sensor_1_State and not sensor_2_State:
                trap = Image.open("Images/TRAP/trap_closed_f.png")
                soundRunning = True
                thread2 = threading.Thread(target=splat)
                thread2.setDaemon(1)
                thread2.start()
                soundRunning = False

            elif not sensor_1_State and sensor_2_State:
                trap = Image.open("Images/TRAP/trap_closed_b.png")
                soundRunning = True
                thread2 = threading.Thread(target=splat)
                thread2.setDaemon(1)
                thread2.start()
                soundRunning = False
            else:
                trap = Image.open("Images/TRAP/trap_closed_m.png")
                soundRunning = True
                thread2 = threading.Thread(target=splat)
                thread2.setDaemon(1)
                thread2.start()
                soundRunning = False
        else:
            if not sensor_1_State and not sensor_2_State:
                trap = Image.open("Images/TRAP/trap_open_e.png")
            elif sensor_1_State and not sensor_2_State:
                trap = Image.open("Images/TRAP/trap_open_f.png")
            elif not sensor_1_State and sensor_2_State:
                trap = Image.open("Images/TRAP/trap_open_b.png")
            else:
                trap = Image.open("Images/TRAP/trap_open_m.png")

        if sensor_1_State:
            trapInfraredSensor_A_State.set(1)
        else:
            trapInfraredSensor_A_State.set(0)

        if sensor_2_State:
            trapInfraredSensor_B_State.set(1)
        else:
            trapInfraredSensor_B_State.set(0)

        if fire_State:
            trapPushButtonState.set(0)
        else:
            trapPushButtonState.set(1)

        if mode_State:
            trapToggleSwitchState.set(1)
        else:
            trapToggleSwitchState.set(0)

        if led_State:
            total = total + 2
            led = Image.open("Images/TRAP/LED/led_on.png")
        else:
            led = Image.open("Images/TRAP/LED/led_off.png")

        trap.paste(led, (0, 0), led.convert('RGBA'))

        if mode_State:
            switch = Image.open("Images/TRAP/SWITCH/toggle_up.png")
        else:
            switch = Image.open("Images/TRAP/SWITCH/toggle_down.png")

        trap.paste(switch, (0, 0), switch.convert('RGBA'))

        outputSignals = "00"
        if total == 0:
            digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            outputSignals = "00"
        elif total == 1:
            digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            outputSignals = "01"
        elif total == 2:
            digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            outputSignals = "10"
        else:
            digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")
            outputSignals = "11"

        print("Sim : " + inputSignals + " - " + outputSignals + " - " +
              str(lastSimulationTime))

        fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

        fpgaImage = ImageTk.PhotoImage(fpga)
        trapImage = ImageTk.PhotoImage(trap)

        label1.config(image=fpgaImage)
        label1.image = fpgaImage
        label1.pack()

        label2.config(image=trapImage)
        label2.image = trapImage
        label2.pack()

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Step :" + " " + inputSignals + "  " + outputSignals +
            " - " + str(simulationStepTime) + "s\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if trapSimulationModeState.get() == 0:
            while not trapStateUpdate:
                time.sleep(0.5)
            trapStateUpdate = False
        else:
            time.sleep(simulationStepTime)

    debugText.configure(state=tk.NORMAL)
    debugText.insert(tk.END, "Finished\n")
    debugText.see(tk.END)
    debugText.update()
    debugText.configure(state=tk.DISABLED)


def lab8():
    global skipSimpleCPU

    print("LAB 8")

    if testCaseData == 0:

        if skipSimpleCPU:
            try:
                source_file = open("./Lab8/0/files-mem.txt", "r")
            except IOError:
                print("Error: Input file does not exist.")
                return
        else:
            try:
                source_file = open("./Lab8/0/files.txt", "r")
                skipSimpleCPU = True
            except IOError:
                print("Error: Input file does not exist.")
                return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys -Wno-hide ../testbench_8.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB8/testbench_8.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_8 " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END,
                "Analysis : testbench_8 " + " " + stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_8'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_8 " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_8 " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Starting simulation, please wait ...\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_8 --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_8 --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_8 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "                   BFTP   LS\n")
        debugText.insert(
            tk.END, "Run : testbench_8 " + " " + stdout + " " + stderr + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        try:
            total = (trapInfraredSensorData[0] *
                     8) + (trapInfraredSensorData[1] *
                           4) + (trapToggleSwitchData * 2) + trapPushButtonData

            fpga = Image.open("Images/FPGA/fpga.png")

            if total == 0:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_0.png")
            elif total == 1:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_1.png")
            elif total == 2:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_2.png")
            elif total == 3:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_3.png")
            elif total == 4:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_4.png")
            elif total == 5:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_5.png")
            elif total == 6:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_6.png")
            elif total == 7:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_7.png")
            elif total == 8:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_8.png")
            elif total == 9:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_9.png")
            elif total == 10:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_a.png")
            elif total == 11:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_b.png")
            elif total == 12:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_c.png")
            elif total == 13:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_d.png")
            elif total == 14:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_e.png")
            else:
                digit_0 = Image.open("Images/FPGA/SEVENSEG/0_f.png")

            fpga.paste(digit_0, (0, 0), digit_0.convert('RGBA'))

            trapLedServoFile = open("trapLedServo.dat", "r")
            data = str(trapLedServoFile.read())
            trapLedServoFile.close()

            total = 0
            if data[1] == '1':
                total = total + 1
                if trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_closed_e.png")
                elif trapInfraredSensorData[1] == 0 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_closed_f.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False

                elif trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 0:
                    trap = Image.open("Images/TRAP/trap_closed_b.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False

                else:
                    trap = Image.open("Images/TRAP/trap_closed_m.png")
                    soundRunning = True
                    thread2 = threading.Thread(target=splat)
                    thread2.setDaemon(1)
                    thread2.start()
                    soundRunning = False
            else:
                if trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_open_e.png")
                elif trapInfraredSensorData[1] == 0 and trapInfraredSensorData[
                        0] == 1:
                    trap = Image.open("Images/TRAP/trap_open_f.png")
                elif trapInfraredSensorData[1] == 1 and trapInfraredSensorData[
                        0] == 0:
                    trap = Image.open("Images/TRAP/trap_open_b.png")
                else:
                    trap = Image.open("Images/TRAP/trap_open_m.png")

            if data[0] == '1':
                total = total + 2
                led = Image.open("Images/TRAP/LED/led_on.png")
            else:
                led = Image.open("Images/TRAP/LED/led_off.png")

            trap.paste(led, (0, 0), led.convert('RGBA'))

            if trapToggleSwitchData == 0:
                switch = Image.open("Images/TRAP/SWITCH/toggle_up.png")
            else:
                switch = Image.open("Images/TRAP/SWITCH/toggle_down.png")

            trap.paste(switch, (0, 0), switch.convert('RGBA'))

            if total == 0:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_0.png")
            elif total == 1:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_1.png")
            elif total == 2:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_2.png")
            else:
                digit_1 = Image.open("Images/FPGA/SEVENSEG/1_3.png")

            fpga.paste(digit_1, (0, 0), digit_1.convert('RGBA'))

            fpgaImage = ImageTk.PhotoImage(fpga)
            trapImage = ImageTk.PhotoImage(trap)

            label1.config(image=fpgaImage)
            label1.image = fpgaImage
            label1.pack()

            label2.config(image=trapImage)
            label2.image = trapImage
            label2.pack()

            print("Finished")
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Finished\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        except IOError as e:
            print("I/O error{0}: {1}".format(e.errno, e.strerror))

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "I/O error{0}: {1}".format(e.errno, e.strerror) + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

        except:
            print("Unexpected error:", sys.exc_info()[0])
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "Unexpected error:",
                             sys.exc_info()[0] + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)
            return

    if testCaseData == 1:

        if skipSimpleCPU:
            try:
                source_file = open("./Lab8/1/files-mem.txt", "r")
            except IOError:
                print("Error: Input file does not exist.")
                return
        else:
            try:
                source_file = open("./Lab8/1/files.txt", "r")
                skipSimpleCPU = True
            except IOError:
                print("Error: Input file does not exist.")
                return

        for file_name in source_file:
            if windows:
                process = subprocess.Popen(
                    GHDL + " -a --work=unisim --ieee=synopsys -Wno-hide ../" +
                    file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen(
                    "ghdl -a --work=unisim --ieee=synopsys ../" + file_name,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : " + file_name + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis : " + file_name.replace("\n", "") + " " +
                stdout + " " + stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    'ghdl -e --work=unisim --ieee=synopsys ' +
                    file_name.split('.')[0],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : " + file_name + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : " + file_name + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)
        source_file.close()

        if not skipTestBench:
            if windows:
                process = subprocess.Popen(
                    GHDL +
                    " -a --work=unisim --ieee=synopsys -Wno-hide  ../testbench_8a.vhd",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
            else:
                process = subprocess.Popen([
                    'ghdl -a --work=unisim --ieee=synopsys LAB8/testbench_8a.vhd'
                ],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           shell=True)
            stdout, stderr = process.communicate()
            print("Analysis : testbench_8a " + " " + stdout + " " + stderr)

            debugText.configure(state=tk.NORMAL)
            debugText.insert(
                tk.END, "Analysis :  testbench_8a " + " " + stdout + " " +
                stderr + "\n")
            debugText.see(tk.END)
            debugText.update()
            debugText.configure(state=tk.DISABLED)

            if windows:
                pass
            else:
                process = subprocess.Popen(
                    ['ghdl -e --work=unisim --ieee=synopsys testbench_8a'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True)
                stdout, stderr = process.communicate()
                print("Compile : testbench_8a " + " " + stdout + " " + stderr)

                debugText.configure(state=tk.NORMAL)
                debugText.insert(
                    tk.END, "Compile : testbench_8a " + " " + stdout + " " +
                    stderr + "\n")
                debugText.see(tk.END)
                debugText.update()
                debugText.configure(state=tk.DISABLED)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "Starting simulation, please wait ...\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        if windows:
            process = subprocess.Popen(
                GHDL +
                " -r --work=unisim --ieee=synopsys testbench_8a --vcd=simulation.vcd",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        else:
            process = subprocess.Popen([
                'ghdl -r --work=unisim --ieee=synopsys testbench_8a --vcd=simulation.vcd'
            ],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       shell=True)
        stdout, stderr = process.communicate()
        print("Run : testbench_5 " + " " + stdout + " " + stderr)

        debugText.configure(state=tk.NORMAL)
        debugText.insert(
            tk.END, "Run : testbench_8a " + " " + stdout + " " + stderr + "\n")
        debugText.insert(tk.END, "       BFTP  LS\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = True
        thread1 = threading.Thread(target=lab8WorkerThread)
        thread1.setDaemon(1)
        thread1.start()


def callback_lab(event):

    global labData, labDataPrev

    print("callback lab select! - " + event)

    if labState.get() == "Off":
        labData = 0
        updateImages()
        testCase.configure(state=tk.DISABLED)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.DISABLED)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labState.get() == "1":
        labData = 1
        testCase.configure(state=tk.DISABLED)
        updateFpgaPushButtonFrame(tk.NORMAL)
        updateTrapFrame(tk.DISABLED)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labState.get() == "2":
        labData = 2
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

        trapRerunButton.configure(state=tk.DISABLED)

    elif labState.get() == "3":
        labData = 3
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.NORMAL)
        updateTrapFrame(tk.DISABLED)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labState.get() == "4":
        labData = 4
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.DISABLED)
        updateFpgaSlideSwitchFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labState.get() == "5":
        labData = 5
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.DISABLED)
        updateTrapControlFrame(tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)
        updateTrapSimulationModeFrame(tk.NORMAL)

    elif labState.get() == "8":
        labData = 8
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

        trapRerunButton.configure(state=tk.DISABLED)
        updateTrapSimulationModeFrame(tk.DISABLED)

    elif labState.get() == "9":
        labData = 9
    else:
        labData = 0

    if labData != labDataPrev:
        labDataPrev = labData
        soundRunning = True
        if labData == 0:
            thread2 = threading.Thread(target=beep_off)
        else:
            thread2 = threading.Thread(target=beep_on)
        thread2.setDaemon(1)
        thread2.start()
        soundRunning = False


def callback_testCase(event):

    global testCaseData, testCaseDataPrev, fpgaStateUpdate

    if event == "1":
        testCaseData = 1
    elif event == "2":
        testCaseData = 2
    elif event == "3":
        testCaseData = 3
    elif event == "4":
        testCaseData = 4
    elif event == "5":
        testCaseData = 5
    elif event == "8":
        testCaseData = 8
    elif event == "9":
        testCaseData = 9
    else:
        testCaseData = 0

    print("callback testCase_Update click!")
    print(str(testCaseData))

    if testCaseData != testCaseDataPrev:
        testCaseDataPrev = testCaseData

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "TTC = " + str(testCaseData) + "\n")
        debugText.configure(state=tk.DISABLED)

    if labData == 0:
        pass
    elif labData == 1:
        pass
    elif labData == 2 and testCaseData == 0:
        updateTrapInfraredSensorFrame(tk.NORMAL)
        updateTrapPushButtonFrame(tk.NORMAL)
        updateTrapToggleSwitchFrame(tk.NORMAL)
        updateTrapSimulationModeFrame(tk.DISABLED)

        trapRerunButton.configure(state=tk.DISABLED)
        updateTrapSimulationModeFrame(tk.DISABLED)

    elif labData == 2 and testCaseData == 1:
        updateTrapInfraredSensorFrame(tk.DISABLED)
        updateTrapPushButtonFrame(tk.DISABLED)
        updateTrapToggleSwitchFrame(tk.DISABLED)
        updateTrapSimulationModeFrame(tk.NORMAL)

        trapRerunButton.configure(state=tk.NORMAL)
        updateTrapSimulationModeFrame(tk.NORMAL)

    elif labData == 3 and testCaseData == 0:
        updateFpgaPushButtonFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labData == 3 and testCaseData == 1:
        updateFpgaPushButtonFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labData == 4 and testCaseData == 0:
        testCase.configure(state=tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

    elif labData == 4 and testCaseData == 1:
        testCase.configure(state=tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.NORMAL)

        fpgaSlideSwitch_Update.configure(state=tk.DISABLED)

    elif labData == 4 and testCaseData == 2:
        testCase.configure(state=tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.NORMAL)
        updateFpgafpgaKeypadDigitFrame(tk.NORMAL)

        fpgaSlideSwitch_Update.configure(state=tk.DISABLED)

    elif labData == 4 and testCaseData == 3:
        testCase.configure(state=tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.NORMAL)

        fpgaSlideSwitch_Update.configure(state=tk.DISABLED)

    elif labData == 5 and testCaseData == 0:
        updateTrapInfraredSensorFrame(tk.DISABLED)
        updateTrapPushButtonFrame(tk.DISABLED)
        updateTrapToggleSwitchFrame(tk.DISABLED)
        updateTrapControlFrame(tk.NORMAL)
        updateTrapSimulationModeFrame(tk.NORMAL)

    elif labData == 5 and testCaseData == 1:
        updateTrapInfraredSensorFrame(tk.DISABLED)
        updateTrapPushButtonFrame(tk.DISABLED)
        updateTrapToggleSwitchFrame(tk.DISABLED)
        updateTrapControlFrame(tk.NORMAL)
        updateTrapSimulationModeFrame(tk.NORMAL)

    elif labData == 5 and testCaseData == 2:
        updateTrapInfraredSensorFrame(tk.DISABLED)
        updateTrapPushButtonFrame(tk.DISABLED)
        updateTrapToggleSwitchFrame(tk.DISABLED)
        updateTrapControlFrame(tk.NORMAL)
        updateTrapSimulationModeFrame(tk.NORMAL)

    elif labData == 8 and testCaseData == 0:
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)

        trapRerunButton.configure(state=tk.DISABLED)
        updateTrapSimulationModeFrame(tk.DISABLED)

    elif labData == 8 and testCaseData == 1:
        testCase.configure(state=tk.NORMAL)
        updateFpgaPushButtonFrame(tk.DISABLED)
        updateTrapFrame(tk.DISABLED)
        updateTrapControlFrame(tk.NORMAL)
        updateFpgaSlideSwitchFrame(tk.DISABLED)
        updateFpgafpgaKeypadDigitFrame(tk.DISABLED)
        updateTrapSimulationModeFrame(tk.NORMAL)


def callback_reset():

    print("callback reset click!")

    updateImages()

    debugText.configure(state=tk.NORMAL)
    debugText.delete('1.0', tk.END)
    debugText.insert(tk.END, "Reset ...\n")
    debugText.configure(state=tk.DISABLED)

    if labData == 1:
        updateFpgaPushButtonFrame(tk.NORMAL)

    elif labData == 2:
        updateTrapFrame(tk.NORMAL)

    elif labData == 5:
        updateTrapFrame(tk.NORMAL)


def callback_exit():

    global systemExit

    print("callback exit click!")
    systemExit = True


def callback_fpgaPushButton_Update():

    global fpgaPushButtonDataPrev, fpgaPushButtonData, fpgaStateUpdate

    fpgaPushButtonData = [1, 1, 1, 1, 1, 1, 1, 1]
    if fpgaPushButton_A_State.get() == 1:
        fpgaPushButtonData[7] = 0
    if fpgaPushButton_B_State.get() == 1:
        fpgaPushButtonData[6] = 0
    if fpgaPushButton_C_State.get() == 1:
        fpgaPushButtonData[5] = 0
    if fpgaPushButton_D_State.get() == 1:
        fpgaPushButtonData[4] = 0
    if fpgaPushButton_E_State.get() == 1:
        fpgaPushButtonData[3] = 0
    if fpgaPushButton_F_State.get() == 1:
        fpgaPushButtonData[2] = 0
    if fpgaPushButton_G_State.get() == 1:
        fpgaPushButtonData[1] = 0
    if fpgaPushButton_H_State.get() == 1:
        fpgaPushButtonData[0] = 0

    print("callback fpgaPushButton_Update click!")
    print(str(fpgaPushButtonData))

    if fpgaPushButtonData != fpgaPushButtonDataPrev:
        fpgaPushButtonDataPrev = fpgaPushButtonData

        fpgaStateUpdate = True

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "FPB = " + str(fpgaPushButtonData) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)


def callback_fpgaSlideSwitch_Update():

    global fpgaSlideSwitchDataPrev, fpgaSlideSwitchData, fpgaStateUpdate

    fpgaSlideSwitchData = [0, 0, 0, 0]
    if fpgaSlideSwitch_A_State.get() == 1:
        fpgaSlideSwitchData[3] = 1
    if fpgaSlideSwitch_B_State.get() == 1:
        fpgaSlideSwitchData[2] = 1
    if fpgaSlideSwitch_C_State.get() == 1:
        fpgaSlideSwitchData[1] = 1
    if fpgaSlideSwitch_D_State.get() == 1:
        fpgaSlideSwitchData[0] = 1

    print("callback fpgaSlideSwitch_Update click!")
    print(str(fpgaSlideSwitchData))

    if fpgaSlideSwitchData != fpgaSlideSwitchDataPrev:
        fpgaSlideSwitchDataPrev = fpgaSlideSwitchData

        fpgaStateUpdate = True

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "FSS = " + str(fpgaSlideSwitchData) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)


def callback_fpgaKeypadDigit(event):
    print("callback fpgaKeypadDigit select! - " + event)


def callback_fpgaKeypad_Update():

    global fpgaKeypadDigitDataPrev, fpgaKeypadDigitData, fpgaStateUpdate

    callback_fpgaSlideSwitch_Update()

    fpgaKeypadDigitData = [0, 0]

    if fpgaKeypadDigit_A_State.get() == "0":
        fpgaKeypadDigitData[0] = 0
    elif fpgaKeypadDigit_A_State.get() == "1":
        fpgaKeypadDigitData[0] = 1
    elif fpgaKeypadDigit_A_State.get() == "2":
        fpgaKeypadDigitData[0] = 2
    elif fpgaKeypadDigit_A_State.get() == "3":
        fpgaKeypadDigitData[0] = 3
    elif fpgaKeypadDigit_A_State.get() == "4":
        fpgaKeypadDigitData[0] = 4
    elif fpgaKeypadDigit_A_State.get() == "5":
        fpgaKeypadDigitData[0] = 5
    elif fpgaKeypadDigit_A_State.get() == "6":
        fpgaKeypadDigitData[0] = 6
    elif fpgaKeypadDigit_A_State.get() == "7":
        fpgaKeypadDigitData[0] = 7
    else:
        fpgaKeypadDigitData[0] = 0

    if fpgaKeypadDigit_B_State.get() == "0":
        fpgaKeypadDigitData[1] = 0
    elif fpgaKeypadDigit_B_State.get() == "1":
        fpgaKeypadDigitData[1] = 1
    elif fpgaKeypadDigit_B_State.get() == "2":
        fpgaKeypadDigitData[1] = 2
    elif fpgaKeypadDigit_B_State.get() == "3":
        fpgaKeypadDigitData[1] = 3
    elif fpgaKeypadDigit_B_State.get() == "4":
        fpgaKeypadDigitData[1] = 4
    elif fpgaKeypadDigit_B_State.get() == "5":
        fpgaKeypadDigitData[1] = 5
    elif fpgaKeypadDigit_B_State.get() == "6":
        fpgaKeypadDigitData[1] = 6
    elif fpgaKeypadDigit_B_State.get() == "7":
        fpgaKeypadDigitData[1] = 7
    else:
        fpgaKeypadDigitData[1] = 0

    print("callback fpgaKeypad_Update click!")
    print(str(fpgaKeypadDigitData))

    if fpgaKeypadDigitData != fpgaKeypadDigitDataPrev:
        fpgaKeypadDigitDataPrev = fpgaKeypadDigitData

        fpgaStateUpdate = True

        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "FKP = " + str(fpgaKeypadDigitData) + "\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)


def callback_trapData_Update():

    global fpgaStateUpdate

    global trapInfraredSensorDataPrev, trapInfraredSensorData
    global trapPushButtonDataPrev, trapPushButtonData
    global trapToggleSwitchDataPrev, trapToggleSwitchData

    if testCaseData == 0:

        trapInfraredSensorData = [1, 1]
        if trapInfraredSensor_A_State.get() == 1:
            trapInfraredSensorData[0] = 0
        if trapInfraredSensor_B_State.get() == 1:
            trapInfraredSensorData[1] = 0

        if trapInfraredSensorData != trapInfraredSensorDataPrev:
            print("callback trapInfraredSensor_Update click!")
            print(str(trapInfraredSensorData))

            trapInfraredSensorDataPrev = trapInfraredSensorData
            fpgaStateUpdate = True

            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END,
                             "TIR = " + str(trapInfraredSensorData) + " ")
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if trapPushButtonState.get() == 0:
            trapPushButtonData = 0
        else:
            trapPushButtonData = 1

        if trapPushButtonData != trapPushButtonDataPrev:
            print("callback trapPushButton_Update click!")
            print(str(trapPushButtonData))

            trapPushButtonDataPrev = trapPushButtonData
            fpgaStateUpdate = True

            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "TPB = " + str(trapPushButtonData) + " ")
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if trapToggleSwitchState.get() == 0:
            trapToggleSwitchData = 0
        else:
            trapToggleSwitchData = 1

        if trapToggleSwitchData != trapToggleSwitchDataPrev:
            print("callback trapToggleSwitch_Update click!")
            print(str(trapToggleSwitchData))

            trapToggleSwitchDataPrev = trapToggleSwitchData
            fpgaStateUpdate = True

            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "TTS = " + str(trapToggleSwitchData))
            debugText.update()
            debugText.configure(state=tk.DISABLED)

        if fpgaStateUpdate:
            debugText.configure(state=tk.NORMAL)
            debugText.insert(tk.END, "\n")
            debugText.update()
            debugText.configure(state=tk.DISABLED)

    elif testCaseData == 1:
        fpgaStateUpdate = True
    elif testCaseData == 2:
        fpgaStateUpdate = True

    if updateSimulation:
        fpgaStateUpdate = True


def callback_trapData_Rerun():

    print("callback trapData_Rerun click! " + str(labData) + " " +
          str(testCaseData))

    if labData == 0:
        pass
    elif labData == 1:
        pass
    elif labData == 2 and testCaseData == 1:
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "       BFTP  SL\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = 1
        thread1 = threading.Thread(target=lab2WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif labData == 5 and testCaseData == 0:
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "       BFTP  SL\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = 1
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif labData == 5 and testCaseData == 1:
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "       BFTP  SL\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = 1
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif labData == 5 and testCaseData == 2:
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "       BFTP  SL\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = 1
        thread1 = threading.Thread(target=lab5WorkerThread)
        thread1.setDaemon(1)
        thread1.start()

    elif labData == 8 and testCaseData == 0:
        debugText.configure(state=tk.NORMAL)
        debugText.insert(tk.END, "       BFTP  SL\n")
        debugText.see(tk.END)
        debugText.update()
        debugText.configure(state=tk.DISABLED)

        simulationRunning = 1
        thread1 = threading.Thread(target=lab8WorkerThread)
        thread1.setDaemon(1)
        thread1.start()


def callback_trapSimulationMode_Update():

    global trapStateUpdate

    print("callback trapSimulationMode_Update click!")
    trapStateUpdate = True


def updateImages():
    fpga = Image.open("Images/fpga.png")
    fpgaImage = ImageTk.PhotoImage(fpga)
    label1.config(image=fpgaImage)
    label1.image = fpgaImage
    label1.pack()

    trap = Image.open("Images/trap.png")
    trapImage = ImageTk.PhotoImage(trap)
    label2.config(image=trapImage)
    label2.image = trapImage
    label2.pack()


def updateFpgaPushButtonFrame(newState):
    global fpgaPushButtonDataPrev, fpgaPushButtonData

    fpgaPushButton_Update.configure(state=newState)
    fpgaPushButton_A.configure(state=newState)
    fpgaPushButton_B.configure(state=newState)
    fpgaPushButton_C.configure(state=newState)
    fpgaPushButton_D.configure(state=newState)
    fpgaPushButton_E.configure(state=newState)
    fpgaPushButton_F.configure(state=newState)
    fpgaPushButton_G.configure(state=newState)
    fpgaPushButton_H.configure(state=newState)

    fpgaPushButtonData = [1, 1, 1, 1, 1, 1, 1, 1]
    fpgaPushButtonDataPrev = [2, 2, 2, 2, 2, 2, 2, 2]

    fpgaPushButton_A_State.set(0)
    fpgaPushButton_B_State.set(0)
    fpgaPushButton_C_State.set(0)
    fpgaPushButton_D_State.set(0)
    fpgaPushButton_E_State.set(0)
    fpgaPushButton_F_State.set(0)
    fpgaPushButton_G_State.set(0)
    fpgaPushButton_H_State.set(0)


def updateFpgaSlideSwitchFrame(newState):

    global fpgaSlideSwitchDataPrev, fpgaSlideSwitchData

    fpgaSlideSwitch_Update.configure(state=newState)
    fpgaSlideSwitch_A.configure(state=newState)
    fpgaSlideSwitch_B.configure(state=newState)
    fpgaSlideSwitch_C.configure(state=newState)
    fpgaSlideSwitch_D.configure(state=newState)

    fpgaSlideSwitchData = [0, 0, 0, 0]
    fpgaSlideSwitchDataPrev = [2, 2, 2, 2]

    fpgaSlideSwitch_A_State.set(0)
    fpgaSlideSwitch_B_State.set(0)
    fpgaSlideSwitch_C_State.set(0)
    fpgaSlideSwitch_D_State.set(0)


def updateFpgafpgaKeypadDigitFrame(newState):

    global fpgaKeypadDigitDataPrev, fpgaKeypadDigitData

    fpgaKeypadDigit_A.config(state=newState)
    fpgaKeypadDigit_B.config(state=newState)
    fpgaKeypad_Update.config(state=newState)

    fpgaKeypadDigitData = [0, 0]
    fpgaKeypadDigitDataPrev = [8, 8]

    fpgaKeypadDigit_A_State.set("0")
    fpgaKeypadDigit_B_State.set("0")


def updateTrapFrame(newState):
    updateTrapInfraredSensorFrame(newState)
    updateTrapPushButtonFrame(newState)
    updateTrapToggleSwitchFrame(newState)
    updateTrapControlFrame(newState)
    updateTrapSimulationModeFrame(newState)


def updateTrapInfraredSensorFrame(newState):

    global trapInfraredSensorData, trapInfraredSensorDataPrev

    trapInfraredSensor_A_State.set(0)
    trapInfraredSensor_B_State.set(0)

    trapInfraredSensorData = [1, 1]
    trapInfraredSensorDataPrev = [2, 2]

    trapInfraredSensor_A.configure(state=newState)
    trapInfraredSensor_B.configure(state=newState)


def updateTrapPushButtonFrame(newState):

    global trapPushButtonData, trapPushButtonDataPrev

    trapPushButtonState.set(1)

    trapPushButtonData = 1
    trapPushButtonDataPrev = 2

    trapPushButton_A.configure(state=newState)
    trapPushButton_B.configure(state=newState)


def updateTrapToggleSwitchFrame(newState):

    global trapToggleSwitchData, trapToggleSwitchDataPrev

    trapToggleSwitchState.set(1)

    trapToggleSwitchData = 0
    trapToggleSwitchDataPrev = 2

    trapToggleSwitch_A.configure(state=newState)
    trapToggleSwitch_B.configure(state=newState)


def updateTrapControlFrame(newState):
    trapUpdateButton.configure(state=newState)
    trapRerunButton.configure(state=newState)


def updateTrapSimulationModeFrame(newState):

    global trapSimulationModeData, trapSimulationModePrev

    trapSimulationModeState.set(1)

    trapSimulationModeData = 0
    trapSimulationModePrev = 2

    trapSimulationMode_A.configure(state=newState)
    trapSimulationMode_B.configure(state=newState)
    trapSimulationMode_Update.configure(state=newState)


window = tk.Tk()
window.geometry('1024x700')
window.title("Virtual Bug Trap")
window.resizable(0, 0)

fpgaFrame = tk.LabelFrame(window, text="FPGA Board")
fpga = Image.open("Images/fpga.png")
fpgaImage = ImageTk.PhotoImage(fpga)

label1 = tk.Label(fpgaFrame, image=fpgaImage)
label1.pack()
fpgaFrame.place(x=10, y=10)

trapFrame = tk.LabelFrame(window, text="Bug Trap")
trap = Image.open("Images/trap.png")
trapImage = ImageTk.PhotoImage(trap)

label2 = tk.Label(trapFrame, image=trapImage)
label2.pack()
trapFrame.place(x=10, y=370)

debugFrame = tk.LabelFrame(window, text="Debug Panel")

debugText = tk.Text(debugFrame, width=79, height=11)
debugText.insert(tk.END, "Running ...\n")
debugText.configure(state=tk.DISABLED)
debugText.pack(side=tk.LEFT, padx=5, pady=5)

debugFrame.place(x=430, y=170)

systemFrame = tk.LabelFrame(window, text="System Control")

resetButton = tk.Button(systemFrame, text="Reset", command=callback_reset)
exitButton = tk.Button(systemFrame, text="Exit", command=callback_exit)

resetButton.pack(side=tk.LEFT, padx=10, pady=10)
exitButton.pack(side=tk.LEFT, padx=10, pady=10)

systemFrame.place(x=854, y=440)

labFrame = tk.LabelFrame(window, text="Lab")

labState = tk.StringVar()
labState.set("Off")

labData = 0
labDataPrev = 99

lab = tk.OptionMenu(labFrame,
                    labState,
                    "Off",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "8",
                    "9",
                    command=callback_lab)

lab.pack(side=tk.LEFT, padx=10, pady=9)
labFrame.place(x=430, y=10)

testCaseFrame = tk.LabelFrame(window, text="Test-case")

testCase_State = tk.StringVar()
testCase_State.set("0")

testCaseData = 0
testCaseDataPrev = 5

testCase = tk.OptionMenu(testCaseFrame,
                         testCase_State,
                         "0",
                         "1",
                         "2",
                         "3",
                         "4",
                         command=callback_testCase)
testCase.config(state=tk.DISABLED)
testCase.pack(side=tk.LEFT, padx=9, pady=9)

testCaseFrame.pack(side=tk.RIGHT)

testCaseFrame.place(x=530, y=10)

fpgaPushButtonFrame = tk.LabelFrame(window, text="FPGA Push Buttons")

fpgaPushButton_A_State = tk.IntVar()
fpgaPushButton_B_State = tk.IntVar()
fpgaPushButton_C_State = tk.IntVar()
fpgaPushButton_D_State = tk.IntVar()
fpgaPushButton_E_State = tk.IntVar()
fpgaPushButton_F_State = tk.IntVar()
fpgaPushButton_G_State = tk.IntVar()
fpgaPushButton_H_State = tk.IntVar()

fpgaPushButton_A_State.set(0)
fpgaPushButton_B_State.set(0)
fpgaPushButton_C_State.set(0)
fpgaPushButton_D_State.set(0)
fpgaPushButton_E_State.set(0)
fpgaPushButton_F_State.set(0)
fpgaPushButton_G_State.set(0)
fpgaPushButton_H_State.set(0)

fpgaPushButtonData = [1, 1, 1, 1, 1, 1, 1, 1]
fpgaPushButtonDataPrev = [2, 2, 2, 2, 2, 2, 2, 2]

fpgaPushButton_A = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="A",
                                  variable=fpgaPushButton_A_State,
                                  state=tk.DISABLED)
fpgaPushButton_B = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="B",
                                  variable=fpgaPushButton_B_State,
                                  state=tk.DISABLED)
fpgaPushButton_C = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="C",
                                  variable=fpgaPushButton_C_State,
                                  state=tk.DISABLED)
fpgaPushButton_D = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="D",
                                  variable=fpgaPushButton_D_State,
                                  state=tk.DISABLED)
fpgaPushButton_E = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="E",
                                  variable=fpgaPushButton_E_State,
                                  state=tk.DISABLED)
fpgaPushButton_F = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="F",
                                  variable=fpgaPushButton_F_State,
                                  state=tk.DISABLED)
fpgaPushButton_G = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="G",
                                  variable=fpgaPushButton_G_State,
                                  state=tk.DISABLED)
fpgaPushButton_H = tk.Checkbutton(fpgaPushButtonFrame,
                                  text="H",
                                  variable=fpgaPushButton_H_State,
                                  state=tk.DISABLED)

fpgaPushButton_Update = tk.Button(fpgaPushButtonFrame,
                                  text="Update",
                                  command=callback_fpgaPushButton_Update,
                                  state=tk.DISABLED)

fpgaPushButton_H.pack(side=tk.LEFT)
fpgaPushButton_G.pack(side=tk.LEFT)
fpgaPushButton_F.pack(side=tk.LEFT)
fpgaPushButton_E.pack(side=tk.LEFT)
fpgaPushButton_D.pack(side=tk.LEFT)
fpgaPushButton_C.pack(side=tk.LEFT)
fpgaPushButton_B.pack(side=tk.LEFT)
fpgaPushButton_A.pack(side=tk.LEFT)

fpgaPushButton_Update.pack(side=tk.LEFT, padx=20, pady=10)

fpgaPushButtonFrame.place(x=620, y=10)

fpgaSlideSwitchFrame = tk.LabelFrame(window, text="FPGA Slide Switches")

fpgaSlideSwitch_A_State = tk.IntVar()
fpgaSlideSwitch_B_State = tk.IntVar()
fpgaSlideSwitch_C_State = tk.IntVar()
fpgaSlideSwitch_D_State = tk.IntVar()

fpgaSlideSwitchData = [0, 0, 0, 0]
fpgaSlideSwitchDataPrev = [2, 2, 2, 2]

fpgaSlideSwitch_A = tk.Checkbutton(fpgaSlideSwitchFrame,
                                   text="A",
                                   variable=fpgaSlideSwitch_A_State,
                                   state=tk.DISABLED)
fpgaSlideSwitch_B = tk.Checkbutton(fpgaSlideSwitchFrame,
                                   text="B",
                                   variable=fpgaSlideSwitch_B_State,
                                   state=tk.DISABLED)
fpgaSlideSwitch_C = tk.Checkbutton(fpgaSlideSwitchFrame,
                                   text="C",
                                   variable=fpgaSlideSwitch_C_State,
                                   state=tk.DISABLED)
fpgaSlideSwitch_D = tk.Checkbutton(fpgaSlideSwitchFrame,
                                   text="D",
                                   variable=fpgaSlideSwitch_D_State,
                                   state=tk.DISABLED)

fpgaSlideSwitch_Update = tk.Button(fpgaSlideSwitchFrame,
                                   text="Update",
                                   command=callback_fpgaSlideSwitch_Update,
                                   state=tk.DISABLED)

fpgaSlideSwitch_D.pack(side=tk.LEFT)
fpgaSlideSwitch_C.pack(side=tk.LEFT)
fpgaSlideSwitch_B.pack(side=tk.LEFT)
fpgaSlideSwitch_A.pack(side=tk.LEFT)

fpgaSlideSwitch_Update.pack(side=tk.LEFT, padx=20, pady=10)

fpgaSlideSwitchFrame.place(x=430, y=90)

fpgaKeypadFrame = tk.LabelFrame(window, text="FPGA Keypad")

fpgaKeypadDigit_A_State = tk.StringVar()
fpgaKeypadDigit_A_State.set("0")

fpgaKeypadDigit_B_State = tk.StringVar()
fpgaKeypadDigit_B_State.set("0")

fpgaKeypadDigitData = [0, 0]
fpgaKeypadDigitDataPrev = [8, 8]

fpgaKeypadDigit_A = tk.OptionMenu(fpgaKeypadFrame,
                                  fpgaKeypadDigit_A_State,
                                  "0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  "7",
                                  command=callback_fpgaKeypadDigit)
fpgaKeypadDigit_B = tk.OptionMenu(fpgaKeypadFrame,
                                  fpgaKeypadDigit_B_State,
                                  "0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  "7",
                                  command=callback_fpgaKeypadDigit)

fpgaKeypadDigit_A.config(state=tk.DISABLED)
fpgaKeypadDigit_B.config(state=tk.DISABLED)

fpgaKeypad_Update = tk.Button(fpgaKeypadFrame,
                              text="Update",
                              command=callback_fpgaKeypad_Update,
                              state=tk.DISABLED)

fpgaKeypadDigit_A.pack(side=tk.LEFT, padx=5)
fpgaKeypadDigit_B.pack(side=tk.LEFT)

fpgaKeypad_Update.pack(side=tk.LEFT, padx=20, pady=10)

fpgaKeypadFrame.place(x=700, y=90)

trapControlFrame = tk.LabelFrame(window, text="Trap")

trapUpdateButton = tk.Button(trapControlFrame,
                             text="Update",
                             command=callback_trapData_Update,
                             state=tk.DISABLED)
trapRerunButton = tk.Button(trapControlFrame,
                            text="Rerun",
                            command=callback_trapData_Rerun,
                            state=tk.DISABLED)

trapUpdateButton.pack(side=tk.LEFT, padx=10, pady=10)
trapRerunButton.pack(side=tk.LEFT, padx=10, pady=10)

trapControlFrame.place(x=580, y=440)

trapInfraredSensorFrame = tk.LabelFrame(window, text="Trap Infra-red Sensors")

trapInfraredSensor_A_State = tk.IntVar()
trapInfraredSensor_B_State = tk.IntVar()

trapInfraredSensor_A_State.set(0)
trapInfraredSensor_B_State.set(0)

trapInfraredSensorData = [1, 1]
trapInfraredSensorDataPrev = [2, 2]

trapInfraredSensor_A = tk.Checkbutton(trapInfraredSensorFrame,
                                      text="Back",
                                      variable=trapInfraredSensor_A_State,
                                      state=tk.DISABLED)
trapInfraredSensor_B = tk.Checkbutton(trapInfraredSensorFrame,
                                      text="Front",
                                      variable=trapInfraredSensor_B_State,
                                      state=tk.DISABLED)

trapInfraredSensor_A.pack(side=tk.LEFT, padx=5, pady=10)
trapInfraredSensor_B.pack(side=tk.LEFT, padx=5, pady=10)

trapInfraredSensorFrame.place(x=580, y=370)

trapPushButtonFrame = tk.LabelFrame(window, text="Trap Push Button")

trapPushButtonState = tk.IntVar()
trapPushButtonState.set(1)

trapPushButtonData = 1
trapPushButtonDataPrev = 2

trapPushButton_A = tk.Radiobutton(trapPushButtonFrame,
                                  text="On",
                                  variable=trapPushButtonState,
                                  value=0,
                                  state=tk.DISABLED)
trapPushButton_B = tk.Radiobutton(trapPushButtonFrame,
                                  text="Off",
                                  variable=trapPushButtonState,
                                  value=1,
                                  state=tk.DISABLED)

trapPushButton_A.pack(side=tk.LEFT, padx=5, pady=10)
trapPushButton_B.pack(side=tk.LEFT, padx=5, pady=10)

trapPushButtonFrame.place(x=890, y=370)

trapToggleSwitchFrame = tk.LabelFrame(window, text="Trap Toggle Switch")

trapToggleSwitchState = tk.IntVar()
trapToggleSwitchState.set(1)

trapToggleSwitchData = 0
trapToggleSwitchDataPrev = 2

trapToggleSwitch_A = tk.Radiobutton(trapToggleSwitchFrame,
                                    text="On",
                                    variable=trapToggleSwitchState,
                                    value=0,
                                    state=tk.DISABLED)
trapToggleSwitch_B = tk.Radiobutton(trapToggleSwitchFrame,
                                    text="Off",
                                    variable=trapToggleSwitchState,
                                    value=1,
                                    state=tk.DISABLED)

trapToggleSwitch_A.pack(side=tk.LEFT, padx=5, pady=10)
trapToggleSwitch_B.pack(side=tk.LEFT, padx=5, pady=10)

trapToggleSwitchFrame.place(x=745, y=370)

trapSimulationModeFrame = tk.LabelFrame(window, text="Trap Simulation Mode")

trapSimulationModeState = tk.IntVar()
trapSimulationModeState.set(1)

trapSimulationMode_A = tk.Radiobutton(trapSimulationModeFrame,
                                      text="Manual",
                                      variable=trapSimulationModeState,
                                      value=0,
                                      state=tk.DISABLED)
trapSimulationMode_B = tk.Radiobutton(trapSimulationModeFrame,
                                      text="Automatic",
                                      variable=trapSimulationModeState,
                                      value=1,
                                      state=tk.DISABLED)

trapSimulationMode_A.pack(side=tk.LEFT, padx=5, pady=10)
trapSimulationMode_B.pack(side=tk.LEFT, padx=5, pady=10)

trapSimulationMode_Update = tk.Button(
    trapSimulationModeFrame,
    text="Step",
    command=callback_trapSimulationMode_Update,
    state=tk.DISABLED)
trapSimulationMode_Update.pack(side=tk.LEFT, padx=20, pady=10)

trapSimulationModeFrame.place(x=580, y=520)

periodicCall()
window.mainloop()
