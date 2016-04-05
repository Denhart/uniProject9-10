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

#define RFFE_PORT PORTC
#define RFFE_SDATA 0
#define RFFE_SCLK 1
#define RFFE_DELAY_US 0
static inline void rffe_sdata(uint8_t x)
{
    if (x)
        RFFE_PORT |= (1 << RFFE_SDATA);
    else
        RFFE_PORT &= ~(1 << RFFE_SDATA);
}

static inline void rffe_sclk(uint8_t x)
{
    if (x)
        RFFE_PORT |= (1 << RFFE_SCLK);
    else
        RFFE_PORT &= ~(1 << RFFE_SCLK);
}

static inline void rffe_start()
{
    // Start condition
    rffe_sclk(0);
    rffe_sdata(0);
    _delay_us(RFFE_DELAY_US);

    rffe_sdata(1);
    _delay_us(RFFE_DELAY_US);

    rffe_sdata(0);
    _delay_us(RFFE_DELAY_US);
}

static inline void rffe_send_bit(uint8_t bit)
{
    rffe_sdata(bit);
    rffe_sclk(1);
    _delay_us(RFFE_DELAY_US);
    rffe_sclk(0);
    _delay_us(RFFE_DELAY_US);
}

static inline void rffe_send_slave_address(uint8_t address)
{
    int8_t i;
    for (i = 3; i >= 0; i--){
        rffe_send_bit((address >> i) & 0x01 );
    }
}

static inline void rffe_send_parity(uint8_t p)
{
    p = p ^ (p >> 4 | p << 4);
    p = p ^ (p >> 2);
    p = p ^ (p >> 1);
    p &= 1;

    rffe_send_bit(!p); // Total number of '1's == odd
}

static inline void rffe_send_byte(uint8_t byte)
{
    int8_t i;
    // Clock out data
    for (i = 7; i >= 0; i--){
        rffe_send_bit((byte >> i) & 0x01 );
    }

    // Parity
    rffe_send_parity(byte);
}

static inline void rffe_bus_park()
{
    rffe_send_bit(0);
}

void rffe_set_reg(uint8_t address, uint8_t reg, uint8_t value)
{
    rffe_start();
    rffe_send_slave_address(address);
    rffe_send_byte((0x02 << 5) | reg); // Write reg cmd
    rffe_send_byte(value);
    rffe_bus_park();
}

#define WS1040_A 0x07
#define WS1040_B 0x06
ISR (USART_RX_vect)
{
    // Code to be executed when the USART receives a byte here
    static uint8_t r;
    r = UDR0;
    switch (r) {
    case '0':
        rffe_set_reg(WS1040_A, 0x01, 0x00);
        break;
    case '1':
        rffe_set_reg(WS1040_A, 0x01, 0x01);
        break;
    case '2':
        rffe_set_reg(WS1040_A, 0x01, 0x02);
        break;
    case '3':
        rffe_set_reg(WS1040_A, 0x01, 0x03);
        break;
    case '4':
        rffe_set_reg(WS1040_A, 0x01, 0x04);
        break;
    case '5':
        rffe_set_reg(WS1040_A, 0x01, 0x05);
        break;
    case '6':
        rffe_set_reg(WS1040_A, 0x01, 0x06);
        break;
    case '7':
        rffe_set_reg(WS1040_A, 0x01, 0x07);
        break;
    case '8':
        rffe_set_reg(WS1040_A, 0x01, 0x08);
        break;
    case '9':
        rffe_set_reg(WS1040_A, 0x01, 0x09);
        break;
    case 'a':
        rffe_set_reg(WS1040_A, 0x01, 0x0a);
        break;
    case 'b':
        rffe_set_reg(WS1040_A, 0x01, 0x0b);
        break;
    case 'c':
        rffe_set_reg(WS1040_A, 0x01, 0x0c);
        break;
    case 'd':
        rffe_set_reg(WS1040_A, 0x01, 0x0d);
        break;
    case 'e':
        rffe_set_reg(WS1040_A, 0x01, 0x0e);
        break;
    case 'f':
        rffe_set_reg(WS1040_A, 0x01, 0x0f);
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
