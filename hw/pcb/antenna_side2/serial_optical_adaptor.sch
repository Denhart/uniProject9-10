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
LIBS:txb0108
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
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3930 2900 50  0001 C CNN
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
F 2 "Resistors_SMD:R_0805_HandSoldering" V 4930 2500 50  0001 C CNN
F 3 "" H 5000 2500 50  0000 C CNN
	1    5000 2500
	1    0    0    -1  
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
F 2 "Resistors_SMD:R_0805_HandSoldering" V 6430 1750 50  0001 C CNN
F 3 "" H 6500 1750 50  0000 C CNN
	1    6500 1750
	1    0    0    -1  
$EndComp
Text Label 6800 2250 0    60   ~ 0
RX
Text Label 650  3650 0    60   ~ 0
GND
Text Notes 5650 650  0    60   ~ 0
RECEIVER
Text Notes 1700 650  0    60   ~ 0
TRANSMITTER
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
	5000 2650 5000 2900
Wire Wire Line
	5000 3200 5000 3650
Connection ~ 5000 3650
Wire Wire Line
	5450 2350 5700 2350
Connection ~ 4000 750 
Wire Wire Line
	4000 3050 4000 3650
Connection ~ 4000 3650
Wire Wire Line
	5700 2150 4000 2150
Wire Wire Line
	6500 1900 6500 2250
Wire Wire Line
	6300 2250 6800 2250
Connection ~ 6500 2250
Connection ~ 1950 750 
Connection ~ 1950 3650
Connection ~ 1350 3650
Connection ~ 1350 750 
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
$Comp
L ATMEGA168PA-A IC1
U 1 1 5704B95B
P 1900 5800
F 0 "IC1" H 1150 7050 50  0000 L BNN
F 1 "ATMEGA168PA-A" H 2300 4400 50  0000 L BNN
F 2 "Housings_QFP:TQFP-32_7x7mm_Pitch0.8mm" H 1900 5800 50  0001 C CIN
F 3 "" H 1900 5800 50  0000 C CNN
	1    1900 5800
	1    0    0    -1  
$EndComp
Text Label 1000 4700 2    60   ~ 0
VCC
Text Label 1000 4800 2    60   ~ 0
VCC
Text Label 1000 6800 2    60   ~ 0
GND
Text Label 1000 6900 2    60   ~ 0
GND
Text Label 1000 7000 2    60   ~ 0
GND
Text Label 1000 5000 2    60   ~ 0
VCC
Text Label 2900 5000 0    60   ~ 0
ICSP_MOSI
Text Label 2900 5100 0    60   ~ 0
ICSP_MISO
Text Label 2900 5200 0    60   ~ 0
ICSP_SCK
Text Label 2900 5400 0    60   ~ 0
AVR_RFFE_SCLK
Text Label 2900 5300 0    60   ~ 0
AVR_RFFE_SDATA
Text Label 4550 6100 2    60   ~ 0
VCC
Text Label 4650 5100 2    60   ~ 0
GND
Text Label 4650 5700 2    60   ~ 0
AVR_RFFE_SDATA
Text Label 4650 5500 2    60   ~ 0
AVR_RFFE_SCLK
Text Label 5550 5700 0    60   ~ 0
RFFE_SDATA
Text Label 5550 5500 0    60   ~ 0
RFFE_SCLK
$Comp
L CONN_02X03 P1
U 1 1 5704F701
P 3000 4200
F 0 "P1" H 3000 4400 50  0000 C CNN
F 1 "CONN_02X03" H 3000 4000 50  0000 C CNN
F 2 "hw:CONN_02X03_SMD" H 3000 3000 50  0001 C CNN
F 3 "" H 3000 3000 50  0000 C CNN
	1    3000 4200
	1    0    0    -1  
$EndComp
Text Label 2750 4100 2    60   ~ 0
ICSP_MISO
Text Label 2750 4200 2    60   ~ 0
ICSP_SCK
Text Label 2750 4300 2    60   ~ 0
AVR_RESET
Text Label 3250 4200 0    60   ~ 0
ICSP_MOSI
Text Label 3250 4100 0    60   ~ 0
VCC
Text Label 3250 4300 0    60   ~ 0
GND
$Comp
L LP3984 U2
U 1 1 570513A1
P 5150 7000
F 0 "U2" H 5150 7350 60  0000 C CNN
F 1 "LP3984" H 5150 7250 60  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5" H 4850 6550 60  0001 C CNN
F 3 "" H 4850 6550 60  0000 C CNN
	1    5150 7000
	1    0    0    -1  
$EndComp
Text Label 5150 7400 3    60   ~ 0
GND
Text Label 4650 7100 2    60   ~ 0
Vcc
$Comp
L C C6
U 1 1 57051A38
P 5700 6750
F 0 "C6" H 5725 6850 50  0000 L CNN
F 1 "C" H 5600 6850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5738 6600 50  0001 C CNN
F 3 "" H 5700 6750 50  0000 C CNN
	1    5700 6750
	1    0    0    -1  
$EndComp
$Comp
L C C5
U 1 1 57051AAA
P 4600 6750
F 0 "C5" H 4625 6850 50  0000 L CNN
F 1 "C" H 4625 6650 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 4638 6600 50  0001 C CNN
F 3 "" H 4600 6750 50  0000 C CNN
	1    4600 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 6900 5750 6900
Connection ~ 5700 6900
Wire Wire Line
	4550 6900 4650 6900
Connection ~ 4600 6900
Text Label 5750 6900 0    60   ~ 0
Vrffe
Text Label 4550 6900 2    60   ~ 0
Vcc
Text Label 4600 6600 0    60   ~ 0
GND
Text Label 5700 6600 0    60   ~ 0
GND
Text Label 2900 6300 0    60   ~ 0
RX
$Comp
L R R7
U 1 1 57052AAB
P 3250 6150
F 0 "R7" V 3330 6150 50  0000 C CNN
F 1 "100k" V 3250 6150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3180 6150 50  0001 C CNN
F 3 "" H 3250 6150 50  0000 C CNN
	1    3250 6150
	0    1    1    0   
$EndComp
Wire Wire Line
	2900 6150 3100 6150
Wire Wire Line
	3400 6150 3550 6150
Text Label 3550 6150 0    60   ~ 0
VCC
Wire Wire Line
	3050 6150 3050 6050
Connection ~ 3050 6150
Text Label 3050 6050 0    60   ~ 0
AVR_RESET
$Comp
L C C1
U 1 1 5705321A
P 950 4150
F 0 "C1" H 975 4250 50  0000 L CNN
F 1 "C" H 975 4050 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 988 4000 50  0001 C CNN
F 3 "" H 950 4150 50  0000 C CNN
	1    950  4150
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5705327C
P 1200 4150
F 0 "C2" H 1225 4250 50  0000 L CNN
F 1 "C" H 1225 4050 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 1238 4000 50  0001 C CNN
F 3 "" H 1200 4150 50  0000 C CNN
	1    1200 4150
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 570532CD
P 1450 4150
F 0 "C3" H 1475 4250 50  0000 L CNN
F 1 "C" H 1475 4050 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 1488 4000 50  0001 C CNN
F 3 "" H 1450 4150 50  0000 C CNN
	1    1450 4150
	1    0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 5705332F
P 1700 4150
F 0 "C4" H 1725 4250 50  0000 L CNN
F 1 "C" H 1725 4050 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 1738 4000 50  0001 C CNN
F 3 "" H 1700 4150 50  0000 C CNN
	1    1700 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	800  4300 2000 4300
Connection ~ 950  4300
Connection ~ 1200 4300
Connection ~ 1450 4300
Connection ~ 1700 4300
Text Label 800  4300 2    60   ~ 0
VCC
Text Label 1700 4000 0    60   ~ 0
GND
Text Label 1450 4000 0    60   ~ 0
GND
Text Label 1200 4000 0    60   ~ 0
GND
Text Label 950  4000 0    60   ~ 0
GND
Text Label 4250 4000 2    60   ~ 0
VCC
Text Label 4250 4100 2    60   ~ 0
GND
$Comp
L CONN_01X01 P3
U 1 1 57055043
P 5350 4100
F 0 "P3" H 5350 4200 50  0000 C CNN
F 1 "CONN_01X01" V 5450 4100 50  0000 C CNN
F 2 "hw:CONN_01X01_SMD" H 5350 4100 50  0001 C CNN
F 3 "" H 5350 4100 50  0000 C CNN
	1    5350 4100
	1    0    0    -1  
$EndComp
Text Label 5150 4100 2    60   ~ 0
VCC
Text Label 7650 6000 2    60   ~ 0
Vrffe
Text Label 7650 5900 2    60   ~ 0
RFFE_SDATA
Text Label 7650 5800 2    60   ~ 0
RFFE_SCLK
Wire Wire Line
	6500 750  6450 750 
Wire Wire Line
	6500 750  6500 1600
Connection ~ 6500 750 
$Comp
L CONN_01X04 P4
U 1 1 5705755A
P 7850 5950
F 0 "P4" H 7850 6200 50  0000 C CNN
F 1 "CONN_01X04" V 7950 5950 50  0000 C CNN
F 2 "hw:CONN_01X04_SMD" H 7850 5950 50  0001 C CNN
F 3 "" H 7850 5950 50  0000 C CNN
	1    7850 5950
	1    0    0    -1  
$EndComp
Text Label 7650 6100 2    60   ~ 0
GND
$Comp
L CONN_01X02 P2
U 1 1 57058EE6
P 4450 4050
F 0 "P2" H 4450 4200 50  0000 C CNN
F 1 "Battery" V 4550 4050 50  0000 C CNN
F 2 "antenna_side:Batt" H 4450 4050 50  0001 C CNN
F 3 "" H 4450 4050 50  0000 C CNN
	1    4450 4050
	1    0    0    -1  
$EndComp
$Comp
L R R10
U 1 1 57058461
P 6850 4450
F 0 "R10" V 6930 4450 50  0000 C CNN
F 1 "R" V 6850 4450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 6780 4450 50  0001 C CNN
F 3 "" H 6850 4450 50  0000 C CNN
	1    6850 4450
	1    0    0    -1  
$EndComp
$Comp
L R R11
U 1 1 570584AE
P 7050 4450
F 0 "R11" V 7130 4450 50  0000 C CNN
F 1 "R" V 7050 4450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 6980 4450 50  0001 C CNN
F 3 "" H 7050 4450 50  0000 C CNN
	1    7050 4450
	1    0    0    -1  
$EndComp
Text Label 6850 4300 0    60   ~ 0
GND
Text Label 7050 4300 0    60   ~ 0
GND
Text Label 7050 4600 0    60   ~ 0
GND
Text Label 6850 4600 0    60   ~ 0
GND
$Comp
L R R12
U 1 1 57065C86
P 7250 4450
F 0 "R12" V 7330 4450 50  0000 C CNN
F 1 "R" V 7250 4450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 7180 4450 50  0001 C CNN
F 3 "" H 7250 4450 50  0000 C CNN
	1    7250 4450
	1    0    0    -1  
$EndComp
Text Label 7250 4300 0    60   ~ 0
GND
Text Label 7250 4600 0    60   ~ 0
GND
$Comp
L TXB0108 U3
U 1 1 5720905D
P 5100 5550
F 0 "U3" H 5100 4850 60  0000 C CNN
F 1 "TXB0108" H 5100 4950 60  0000 C CNN
F 2 "Housings_SSOP:TSSOP-20_4.4x6.5mm_Pitch0.65mm" H 4850 5500 60  0001 C CNN
F 3 "" H 4850 5500 60  0000 C CNN
	1    5100 5550
	-1   0    0    1   
$EndComp
Text Label 5650 6100 0    60   ~ 0
Vrffe
Wire Wire Line
	5550 5100 5750 5100
$Comp
L C C8
U 1 1 5720BC67
P 5900 5100
F 0 "C8" H 5925 5200 50  0000 L CNN
F 1 "C" H 5925 5000 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5938 4950 50  0001 C CNN
F 3 "" H 5900 5100 50  0000 C CNN
	1    5900 5100
	0    1    1    0   
$EndComp
Text Label 6050 5100 0    60   ~ 0
GND
Wire Wire Line
	5650 5100 5650 5000
Connection ~ 5650 5100
Text Label 5650 5000 0    60   ~ 0
Vrffe
$Comp
L C C9
U 1 1 5720D0CC
P 5900 5900
F 0 "C9" H 5925 6000 50  0000 L CNN
F 1 "0.1pF" V 5800 5800 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 5938 5750 50  0001 C CNN
F 3 "" H 5900 5900 50  0000 C CNN
	1    5900 5900
	0    1    1    0   
$EndComp
Text Label 6050 5900 0    60   ~ 0
GND
Wire Wire Line
	5550 5900 5750 5900
Wire Wire Line
	5650 5900 5650 6100
Connection ~ 5650 5900
Wire Wire Line
	4650 5900 4500 5900
$Comp
L C C7
U 1 1 5720D574
P 4350 5900
F 0 "C7" H 4375 6000 50  0000 L CNN
F 1 "0.1pF" H 4375 5800 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 4388 5750 50  0001 C CNN
F 3 "" H 4350 5900 50  0000 C CNN
	1    4350 5900
	0    1    1    0   
$EndComp
Wire Wire Line
	4550 5900 4550 6100
Connection ~ 4550 5900
Text Label 4200 5900 2    60   ~ 0
GND
$Comp
L R R4
U 1 1 572190BF
P 5000 3050
F 0 "R4" V 5080 3050 50  0000 C CNN
F 1 "R" V 5000 3050 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 4930 3050 50  0001 C CNN
F 3 "" H 5000 3050 50  0000 C CNN
	1    5000 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 2750 5450 2750
Connection ~ 5450 2750
Connection ~ 5000 2750
Wire Wire Line
	5450 2750 5450 2350
$Comp
L C C10
U 1 1 5721D69B
P 2000 4150
F 0 "C10" H 2025 4250 50  0000 L CNN
F 1 "C" H 2025 4050 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 2038 4000 50  0001 C CNN
F 3 "" H 2000 4150 50  0000 C CNN
	1    2000 4150
	1    0    0    -1  
$EndComp
Text Label 2000 4000 0    60   ~ 0
GND
Text Label 6100 7500 0    60   ~ 0
Vrffe
$Comp
L C C11
U 1 1 5721EC42
P 6000 7350
F 0 "C11" H 6025 7450 50  0000 L CNN
F 1 "C" H 6025 7250 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 6038 7200 50  0001 C CNN
F 3 "" H 6000 7350 50  0000 C CNN
	1    6000 7350
	1    0    0    -1  
$EndComp
Text Label 6000 7200 0    60   ~ 0
GND
Wire Wire Line
	6100 7500 6000 7500
Text Label 650  750  0    60   ~ 0
VCC
$EndSCHEMATC
