// References
// [1] http://deans-avr-tutorials.googlecode.com/svn/trunk/InterruptUSART/Output/InterruptUSART.pdf
// [2] http://www.embedds.com/programming-avr-usart-with-avr-gcc-part-2/

#define F_CPU 8000000UL
#include <stdint.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

void usart0_init()
{
    // Disable global interrupts
    cli();

    // Normal asyncronous
    // BAUD rate gen
    // Down-counter/prescaler running at FOSC

    // UBBRn = FOSC/(16*BAUD) - 1
    // = 51 for 9600 at 8MHz
    //
    // Must have U2Xn = 0 (double speed off)
    UBRR0 = 51; // Baud rate register

    // UMSELn bit in UCSRnC (0 for async)
    UCSR0C &= ~(1 << UMSEL00); // Asyncronous

    UCSR0B |= (1 << RXCIE0) | (1 << RXEN0); // Interrupt, enable rx

    // Set frame format to 8 data bits, no parity, 1 stop bit
    UCSR0C |= (1<<UCSZ01)|(1<<UCSZ00);

    // Enable global interrupts
    sei();
}

// RFFE_XY, X=SCLK, Y=SDATA
#define RFFE_HH 0b00000011
#define RFFE_HL 0b00000010
#define RFFE_LH 0b00000001
#define RFFE_LL 0b00000000

#define RFFE_PORT PORTC
#define RFFE_SDATA 0
#define RFFE_SCLK 1
#define RFFE_DELAY_US 0

uint8_t rffe_parity(uint8_t p)
{
    p = p ^ (p >> 4 | p << 4);
    p = p ^ (p >> 2);
    p = p ^ (p >> 1);
    p &= 1;

    return !p;
}

void rffe_set_reg(uint8_t address, uint8_t reg, uint8_t value)
{
    uint8_t rffe_command[24];
    uint8_t sclk_pin = (1 << RFFE_SCLK);
    int8_t i, j;
    uint8_t byte;

    // BUILD COMMAND ///////////////////////////////////////////////////////////
    // 0:      Start: SDATA pulse while SCLK low
    rffe_command[0] = RFFE_LH; 

    // 1--4:   Address of chip
    for (i = 3, j = 1; i >= 0; i--, j++)
        rffe_command[j] = ((address >> i) & 0x01) ? RFFE_HH : RFFE_HL;

    // 5--12:  Write register command (0x02, 3 MSb) + register number (5 LSb)
    byte = (0x02 << 5) | reg;
    for (i = 7, j = 5; i >= 0; i--, j++)
        rffe_command[j] = ((byte >> i) & 0x01) ? RFFE_HH : RFFE_HL;

    // 13:     Parity of previous byte
    rffe_command[13] = rffe_parity(byte) ? RFFE_HH : RFFE_HL;

    // 14--21: Value of register (8 bit)
    for (i = 7, j = 14; i >= 0; i--, j++)
        rffe_command[j] = ((value >> i) & 0x01) ? RFFE_HH : RFFE_HL;

    // 22:     Parity of previous byte
    rffe_command[22] = rffe_parity(value) ? RFFE_HH : RFFE_HL;

    // 23:     Bus park: Clock out a 0 bit
    rffe_command[23] = RFFE_HL;

    // SEND COMMAND ////////////////////////////////////////////////////////////
    PORTC = rffe_command[0]; // Start
    PORTC = RFFE_LL;
    PORTC = rffe_command[1]; // Slave address
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[2];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[3];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[4];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[5]; // Write Register Command
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[6];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[7];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[8]; // Register number
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[9];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[10];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[11];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[12];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[13]; // Parity
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[14]; // Value
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[15];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[16];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[17];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[18];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[19];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[20];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[21];
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[22]; // Parity
    PORTC &= ~ sclk_pin;
    PORTC = rffe_command[23]; // Bus park
    PORTC &= ~ sclk_pin;

}

#define WS1040_A 0x07
#define WS1040_B 0x06
static uint8_t ws1040_address = WS1040_A;
ISR (USART_RX_vect)
{
    // Code to be executed when the USART receives a byte here
    static uint8_t r;
    r = UDR0;
    switch (r) {
    case 'A':
        ws1040_address = WS1040_A;
        break;
    case 'B':
        ws1040_address = WS1040_B;
        break;
    case '0':
        rffe_set_reg(ws1040_address, 0x01, 0x00);
        break;
    case '1':
        rffe_set_reg(ws1040_address, 0x01, 0x01);
        break;
    case '2':
        rffe_set_reg(ws1040_address, 0x01, 0x02);
        break;
    case '3':
        rffe_set_reg(ws1040_address, 0x01, 0x03);
        break;
    case '4':
        rffe_set_reg(ws1040_address, 0x01, 0x04);
        break;
    case '5':
        rffe_set_reg(ws1040_address, 0x01, 0x05);
        break;
    case '6':
        rffe_set_reg(ws1040_address, 0x01, 0x06);
        break;
    case '7':
        rffe_set_reg(ws1040_address, 0x01, 0x07);
        break;
    case '8':
        rffe_set_reg(ws1040_address, 0x01, 0x08);
        break;
    case '9':
        rffe_set_reg(ws1040_address, 0x01, 0x09);
        break;
    case 'a':
        rffe_set_reg(ws1040_address, 0x01, 0x0a);
        break;
    case 'b':
        rffe_set_reg(ws1040_address, 0x01, 0x0b);
        break;
    case 'c':
        rffe_set_reg(ws1040_address, 0x01, 0x0c);
        break;
    case 'd':
        rffe_set_reg(ws1040_address, 0x01, 0x0d);
        break;
    case 'e':
        rffe_set_reg(ws1040_address, 0x01, 0x0e);
        break;
    case 'f':
        rffe_set_reg(ws1040_address, 0x01, 0x0f);
        break;
    }
}

int main (void) 
{
    DDRC = 0x03; // PC0, PC1 = output for RFFE
    PORTC = 0x00;

    usart0_init();
    while (1) {

    }
}
