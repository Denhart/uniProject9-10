EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:if-d91
LIBS:if-e97
LIBS:adg3300
LIBS:lp3984
LIBS:cp2102
LIBS:serial_optical_adaptor-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Serial to optical adaptor"
Date "2016-04-04"
Rev "1.0"
Comp "16gr1051"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R1
U 1 1 57025223
P 4000 2900
F 0 "R1" V 4080 2900 50  0000 C CNN
F 1 "100k" V 4000 2900 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 3930 2900 50  0001 C CNN
F 3 "" H 4000 2900 50  0000 C CNN
	1    4000 2900
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 57025332
P 5000 2500
F 0 "R2" V 5080 2500 50  0000 C CNN
F 1 "47k" V 5000 2500 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 4930 2500 50  0001 C CNN
F 3 "" H 5000 2500 50  0000 C CNN
	1    5000 2500
	1    0    0    -1  
$EndComp
$Comp
L POT RV1
U 1 1 570253FB
P 5000 2950
F 0 "RV1" H 5000 2850 50  0000 C CNN
F 1 "10k" H 5000 2950 50  0000 C CNN
F 2 "hw:smd_murrata_trimmer_pvz3a" H 5000 2950 50  0001 C CNN
F 3 "" H 5000 2950 50  0000 C CNN
	1    5000 2950
	0    1    1    0   
$EndComp
$Comp
L LM393 U1
U 1 1 57025466
P 6000 2250
F 0 "U1" H 6150 2400 50  0000 C CNN
F 1 "LM393" H 6250 2100 50  0000 C CNN
F 2 "SMD_Packages:SOIC-8-N" H 6000 2250 50  0001 C CNN
F 3 "" H 6000 2250 50  0000 C CNN
	1    6000 2250
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5702575B
P 6500 1750
F 0 "R3" V 6580 1750 50  0000 C CNN
F 1 "1k" V 6500 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 6430 1750 50  0001 C CNN
F 3 "" H 6500 1750 50  0000 C CNN
	1    6500 1750
	1    0    0    -1  
$EndComp
Text Label 6800 2250 0    60   ~ 0
RX
$Comp
L R R4
U 1 1 57025951
P 1350 1400
F 0 "R4" V 1430 1400 50  0000 C CNN
F 1 "4k7" V 1350 1400 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 1280 1400 50  0001 C CNN
F 3 "" H 1350 1400 50  0000 C CNN
	1    1350 1400
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 570259EE
P 1350 3000
F 0 "R5" V 1430 3000 50  0000 C CNN
F 1 "4k7" V 1350 3000 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 1280 3000 50  0001 C CNN
F 3 "" H 1350 3000 50  0000 C CNN
	1    1350 3000
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 57025B06
P 2650 1100
F 0 "R6" V 2730 1100 50  0000 C CNN
F 1 "100" V 2650 1100 50  0000 C CNN
F 2 "Resistors_SMD:R_0603_HandSoldering" V 2580 1100 50  0001 C CNN
F 3 "" H 2650 1100 50  0000 C CNN
	1    2650 1100
	1    0    0    -1  
$EndComp
$Comp
L LM393 U1
U 2 1 57025B92
P 2050 2250
F 0 "U1" H 2200 2400 50  0000 C CNN
F 1 "LM393" H 2300 2100 50  0000 C CNN
F 2 "SMD_Packages:SOIC-8-N" H 2050 2250 50  0001 C CNN
F 3 "" H 2050 2250 50  0000 C CNN
	2    2050 2250
	1    0    0    -1  
$EndComp
Text Label 1000 2350 0    60   ~ 0
TX
Text Label 650  3650 0    60   ~ 0
GND
Text Label 650  750  0    60   ~ 0
Vdd
Text Notes 5650 650  0    60   ~ 0
RECEIVER
Text Notes 1700 650  0    60   ~ 0
TRANSMITTER
$Comp
L IF-E97 D1
U 1 1 57029DC9
P 2650 1500
F 0 "D1" H 2650 1600 50  0000 C CNN
F 1 "IF-E97" H 2650 1350 50  0000 C CNN
F 2 "hw:IF-E97" H 2650 1500 60  0001 C CNN
F 3 "" H 2650 1500 60  0000 C CNN
	1    2650 1500
	0    1    1    0   
$EndComp
$Comp
L IF-D91 D2
U 1 1 57029E87
P 4000 1500
F 0 "D2" H 4000 1600 50  0000 C CNN
F 1 "IF-D91" H 4000 1350 50  0000 C CNN
F 2 "hw:IF-D91" H 4000 1500 60  0001 C CNN
F 3 "" H 4000 1500 60  0000 C CNN
	1    4000 1500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	650  750  7200 750 
Wire Wire Line
	650  3650 7200 3650
Wire Wire Line
	5000 2350 5000 750 
Connection ~ 5000 750 
Wire Wire Line
	5000 2650 5000 2700
Wire Wire Line
	5000 3200 5000 3650
Connection ~ 5000 3650
Wire Wire Line
	5450 2350 5450 2950
Wire Wire Line
	5450 2350 5700 2350
Connection ~ 4000 750 
Wire Wire Line
	4000 3050 4000 3650
Connection ~ 4000 3650
Wire Wire Line
	5700 2150 4000 2150
Wire Wire Line
	5450 2950 5150 2950
Wire Wire Line
	6500 1900 6500 2250
Wire Wire Line
	6300 2250 6800 2250
Connection ~ 6500 2250
Wire Wire Line
	1950 1950 1950 750 
Connection ~ 1950 750 
Wire Wire Line
	1950 2550 1950 3650
Connection ~ 1950 3650
Wire Wire Line
	1350 3150 1350 3650
Connection ~ 1350 3650
Wire Wire Line
	1350 1250 1350 750 
Connection ~ 1350 750 
Wire Wire Line
	1350 1550 1350 2850
Wire Wire Line
	1350 2150 1750 2150
Connection ~ 1350 2150
Wire Wire Line
	1750 2350 1000 2350
Wire Wire Line
	2650 2250 2350 2250
Wire Wire Line
	2650 950  2650 750 
Connection ~ 2650 750 
Wire Wire Line
	5900 3650 5900 2550
Connection ~ 5900 3650
Wire Wire Line
	5900 1950 5900 750 
Connection ~ 5900 750 
Wire Wire Line
	4000 1300 4000 750 
Wire Wire Line
	4000 1700 4000 2750
Connection ~ 4000 2150
Wire Wire Line
	2650 1250 2650 1300
Wire Wire Line
	2650 1700 2650 2250
Wire Wire Line
	6500 750  6450 750 
Wire Wire Line
	6500 750  6500 1600
Connection ~ 6500 750 
$Comp
L CP2102 U2
U 1 1 57057D88
P 4050 5450
F 0 "U2" H 4050 5350 50  0000 C CNN
F 1 "CP2102" H 4050 5550 50  0000 C CNN
F 2 "Housings_DFN_QFN:QFN-28-1EP_5x6mm_Pitch0.5mm" H 4050 5450 60  0001 C CNN
F 3 "" H 4050 5450 60  0000 C CNN
	1    4050 5450
	1    0    0    -1  
$EndComp
Text Label 3500 6400 3    60   ~ 0
GND
Text Label 1800 5400 0    60   ~ 0
D+
Text Label 1800 5500 0    60   ~ 0
D-
Text Label 1800 5600 0    60   ~ 0
Vbus
Text Label 1800 5300 0    60   ~ 0
GND
Text Label 1400 5100 0    60   ~ 0
GND
Text Label 2700 5000 2    60   ~ 0
D+
Text Label 2700 5100 2    60   ~ 0
D-
Text Label 4400 4500 1    60   ~ 0
Vbus
Text Label 2700 5200 2    60   ~ 0
RST
Text Label 4600 4500 1    60   ~ 0
Vdd
Text Label 5400 5600 0    60   ~ 0
SUSP1
Text Label 5400 5700 0    60   ~ 0
SUSP2
Text Label 4500 4500 1    60   ~ 0
Vbus
Text Label 5400 5000 0    60   ~ 0
DTR
Text Label 5400 5100 0    60   ~ 0
DSR
Text Label 5400 5200 0    60   ~ 0
TX
Text Label 5400 5300 0    60   ~ 0
RX
Text Label 5400 5400 0    60   ~ 0
RTS
Text Label 5400 5500 0    60   ~ 0
CTS
Text Label 5400 5800 0    60   ~ 0
RI
Text Label 5400 5900 0    60   ~ 0
DCD
Text Label 7300 4400 2    60   ~ 0
GND
Text Label 7300 4800 2    60   ~ 0
RX
Text Label 7300 4700 2    60   ~ 0
TX
Text Label 7300 4600 2    60   ~ 0
Vdd
$Comp
L USB_B P1
U 1 1 5705E8AC
P 1500 5400
F 0 "P1" H 1700 5200 50  0000 C CNN
F 1 "USB_B" H 1450 5600 50  0000 C CNN
F 2 "Connect:USB_B" V 1450 5300 50  0001 C CNN
F 3 "" V 1450 5300 50  0000 C CNN
	1    1500 5400
	0    -1   -1   0   
$EndComp
Text Label 2800 5400 2    60   ~ 0
GND
$Comp
L CONN_01X06 P2
U 1 1 570621E4
P 7500 4650
F 0 "P2" H 7500 5000 50  0000 C CNN
F 1 "CONN_01X06" V 7600 4650 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x06" H 7500 4650 50  0001 C CNN
F 3 "" H 7500 4650 50  0000 C CNN
	1    7500 4650
	1    0    0    -1  
$EndComp
$EndSCHEMATC
