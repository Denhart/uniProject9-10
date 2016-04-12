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

#define RFFE_DDR DDRB
#define RFFE_PORT PORTB
#define RFFE_SDATA 6
#define RFFE_SCLK 7

// RFFE_XY, X=SCLK, Y=SDATA
#define RFFE_HH (1<<RFFE_SCLK)|(1<<RFFE_SDATA)
#define RFFE_HL (1<<RFFE_SCLK)|(0<<RFFE_SDATA)
#define RFFE_LH (0<<RFFE_SCLK)|(1<<RFFE_SDATA)
#define RFFE_LL (0<<RFFE_SCLK)|(0<<RFFE_SDATA)

uint8_t rffe_parity(uint8_t p)
{
    p = p ^ (p >> 4 | p << 4);
    p = p ^ (p >> 2);
    p = p ^ (p >> 1);
    p &= 1;

    return !p;  // Total #1's = odd
    /* return p; // Total #1's = even */
}

void rffe_variable_to_rffe(uint8_t input, uint8_t *output, uint8_t start, uint8_t len)
{
    int8_t i, j;
    for (i = len-1, j = start; i >= 0; i--, j++)
        output[j] = ((input >> i) & 0x01) ? RFFE_HH : RFFE_HL;
}

void rffe_set_reg(uint8_t address, uint8_t reg, uint8_t value)
{
    uint8_t rffe_command[24];
    uint8_t sclk_pin = (1 << RFFE_SCLK);
    uint8_t reg_command;

    // BUILD COMMAND ///////////////////////////////////////////////////////////
    // The reason for splitting BUILD and SEND in two parts is to have
    // consistent timing when clocking out the RFFE protocol.

    // 0:      Start: SDATA pulse while SCLK low
    // 1--4:   Address of chip
    // 5--12:  Write register command (0x02, 3 MSb) + register number (5 LSb)
    // 13:     Parity of previous byte
    // 14--21: Value of register (8 bit)
    // 22:     Parity of previous byte
    // 23:     Bus park: Clock out a 0 bit
    reg_command = (0x02 << 5) | reg;

    //                    From          To             Start  Length
    rffe_variable_to_rffe(address,      rffe_command,  1,     4);      // Slave address
    rffe_variable_to_rffe(reg_command,  rffe_command,  5,     8);      // Register command + register
    rffe_variable_to_rffe(value,        rffe_command,  14,    8);      // Value of register

    rffe_command[0] = RFFE_LH;                                         // Start condition
    rffe_command[13] = rffe_parity(reg_command) ? RFFE_HH : RFFE_HL;   // Parity: Register command + register
    rffe_command[22] = rffe_parity(value) ? RFFE_HH : RFFE_HL;         // Parity: Value of register
    rffe_command[23] = RFFE_HL;                                        // Bus park

    // SEND COMMAND ////////////////////////////////////////////////////////////
    RFFE_PORT = rffe_command[0]; // Start
    RFFE_PORT = RFFE_LL;
    RFFE_PORT = rffe_command[1]; // Slave address
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[2];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[3];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[4];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[5]; // Write Register Command
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[6];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[7];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[8]; // Register number
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[9];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[10];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[11];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[12];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[13]; // Parity
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[14]; // Value
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[15];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[16];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[17];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[18];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[19];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[20];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[21];
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[22]; // Parity
    RFFE_PORT &= ~ sclk_pin;
    RFFE_PORT = rffe_command[23]; // Bus park
    RFFE_PORT &= ~ sclk_pin;

}

#define WS1040_A 0x07
#define WS1040_B 0x06
static uint8_t ws1040_address = WS1040_A;
static uint8_t ws1040_reg = 0x01;
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
    case 'x':
        ws1040_reg = 0x01;
        break;
    case 'y':
        ws1040_reg = 0x02;
        break;
    case 'z':
        ws1040_reg = 0x03;
        break;
    case 't':
        ws1040_reg = 0x04;
        break;
    case '0':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x00);
        break;
    case '1':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x01);
        break;
    case '2':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x02);
        break;
    case '3':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x03);
        break;
    case '4':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x04);
        break;
    case '5':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x05);
        break;
    case '6':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x06);
        break;
    case '7':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x07);
        break;
    case '8':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x08);
        break;
    case '9':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x09);
        break;
    case 'a':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0a);
        break;
    case 'b':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0b);
        break;
    case 'c':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0c);
        break;
    case 'd':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0d);
        break;
    case 'e':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0e);
        break;
    case 'f':
        rffe_set_reg(ws1040_address, ws1040_reg, 0x0f);
        break;
    }
}

int main (void) 
{
    RFFE_DDR = (1<<RFFE_SCLK) | (1<<RFFE_SDATA); // Output for RFFE
    RFFE_PORT = 0x00;

    usart0_init();
    while (1) {

    }
}
