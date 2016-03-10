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
LIBS:001-trianglefeed-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L C C1
U 1 1 56C1C0D8
P 2700 2250
F 0 "C1" H 2725 2350 50  0000 L CNN
F 1 "C" H 2725 2150 50  0000 L CNN
F 2 "Capacitors_SMD:C_0402" H 2738 2100 50  0001 C CNN
F 3 "" H 2700 2250 50  0000 C CNN
	1    2700 2250
	0    1    1    0   
$EndComp
$Comp
L L_Small L1
U 1 1 56C1C15A
P 3000 2450
F 0 "L1" H 3030 2490 50  0000 L CNN
F 1 "L_Small" H 3030 2410 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603_HandSoldering" H 3000 2450 50  0001 C CNN
F 3 "" H 3000 2450 50  0000 C CNN
	1    3000 2450
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 56C1C1FD
P 3550 2500
F 0 "C3" H 3575 2600 50  0000 L CNN
F 1 "C" H 3575 2400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0402" H 3588 2350 50  0001 C CNN
F 3 "" H 3550 2500 50  0000 C CNN
	1    3550 2500
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 A1
U 1 1 56C1C8C2
P 4000 2250
F 0 "A1" H 4000 2350 50  0000 C CNN
F 1 "ANTENNA" V 4100 2250 50  0000 C CNN
F 2 "Measurement_Points:Measurement_Point_Square-SMD-Pad_Small" H 4000 2250 50  0001 C CNN
F 3 "" H 4000 2250 50  0000 C CNN
	1    4000 2250
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 56C1CB75
P 2700 2950
F 0 "C2" H 2725 3050 50  0000 L CNN
F 1 "C" H 2725 2850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0402" H 2738 2800 50  0001 C CNN
F 3 "" H 2700 2950 50  0000 C CNN
	1    2700 2950
	0    1    1    0   
$EndComp
$Comp
L L_Small L2
U 1 1 56C1CB7B
P 3000 3150
F 0 "L2" H 3030 3190 50  0000 L CNN
F 1 "L_Small" H 3030 3110 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603_HandSoldering" H 3000 3150 50  0001 C CNN
F 3 "" H 3000 3150 50  0000 C CNN
	1    3000 3150
	1    0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 56C1CB81
P 3550 3200
F 0 "C4" H 3575 3300 50  0000 L CNN
F 1 "C" H 3575 3100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0402" H 3588 3050 50  0001 C CNN
F 3 "" H 3550 3200 50  0000 C CNN
	1    3550 3200
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 A2
U 1 1 56C1CB96
P 4000 2950
F 0 "A2" H 4000 3050 50  0000 C CNN
F 1 "ANTENNA" V 4100 2950 50  0000 C CNN
F 2 "Measurement_Points:Measurement_Point_Square-SMD-Pad_Small" H 4000 2950 50  0001 C CNN
F 3 "" H 4000 2950 50  0000 C CNN
	1    4000 2950
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X01 P1
U 1 1 56C1CF80
P 2150 2250
F 0 "P1" H 2150 2350 50  0000 C CNN
F 1 "SMA" V 2250 2250 50  0000 C CNN
F 2 "Measurement_Points:Measurement_Point_Square-SMD-Pad_Small" H 2150 2250 50  0001 C CNN
F 3 "" H 2150 2250 50  0000 C CNN
	1    2150 2250
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X01 P2
U 1 1 56C1D014
P 2150 2950
F 0 "P2" H 2150 3050 50  0000 C CNN
F 1 "SMA" V 2250 2950 50  0000 C CNN
F 2 "Measurement_Points:Measurement_Point_Square-SMD-Pad_Small" H 2150 2950 50  0001 C CNN
F 3 "" H 2150 2950 50  0000 C CNN
	1    2150 2950
	-1   0    0    1   
$EndComp
Wire Wire Line
	2850 2250 3800 2250
Wire Wire Line
	3000 2250 3000 2350
Wire Wire Line
	3550 2250 3550 2350
Connection ~ 3000 2250
Wire Wire Line
	3000 2650 3000 2550
Connection ~ 3550 2250
Wire Wire Line
	2850 2950 3800 2950
Wire Wire Line
	3000 2950 3000 3050
Wire Wire Line
	3550 2950 3550 3050
Connection ~ 3000 2950
Wire Wire Line
	3000 3350 3000 3250
Connection ~ 3550 2950
Wire Wire Line
	2350 2250 2550 2250
Wire Wire Line
	2350 2950 2550 2950
Wire Wire Line
	3000 2650 3550 2650
Wire Wire Line
	3000 3350 3550 3350
Text Label 3000 2650 0    60   ~ 0
GND
Text Label 3000 3350 0    60   ~ 0
GND
Text Label 3550 2250 0    60   ~ 0
Ant1
Text Label 3550 2950 0    60   ~ 0
Ant2
$EndSCHEMATC
