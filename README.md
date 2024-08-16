# Test script for USB to serial converter / Raspberry Pi UART communication 
## Setup:
**Hardware:**
- Adafruit CP2102N Friend - USB to Serial Converter ([link](https://www.adafruit.com/product/5335))
- Raspberry Pi 4 or Raspberry Pi 5

**Wiring:**

| Converter | Raspberry Pi      | Note                                             |
|-----------|-------------------|--------------------------------------------------|
| GND       | 4 (GND)           |                                                  |
| CTS       |                   | not connected                                    |
| 5V        | 6 (5V)            |                                                  |
| TXD       | 10 (GPIO15 - RXD) | TXD and RXD might be swapped in some components  |
| RXD       | 8 (GPIO14 - TXD)  | TXD and RXD might be swapped in some components  |
| RTS       |                   | not connected                                    |