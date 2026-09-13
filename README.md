# Firmware Development for PIC32-Based High-Voltage DC Power Supply (200V, 5 kW) with Dual HMIs

## Overview

This repository contains the firmware, control interface scripts, schematics, and documentation for a high-voltage, high-power DC supply system (200V, 5 kW). Developed as part of a larger power electronics project, this subsystem enables full control and monitoring of a programmable power supply via two independent Human-Machine Interfaces (HMIs):

1. **Hardware HMI:** A dedicated external touch-screen terminal (DWIN DMG48270C043_03WTR) communicating over UART.
2. **Desktop Software GUI:** A cross-platform Python application designed primarily for Windows (and adaptable to Linux/macOS) to enable host-based monitoring and remote operation over Serial/UART.

---

## System Architecture & Components

- **Microcontroller:** Microchip PIC32MM0256GPM064
- **Programmable Power Supply:** XP Power HPL5K0TS200 (5 kW, 0–200 VDC output configurable via I2C interface)
- **Hardware Touch Terminal:** DWIN DMG48270C043_03WTR (4.3-inch Smart UART TFT LCD Display)
- **Desktop Software Application:** Custom Python GUI compiled for standalone host execution (`.exe`)

---

## Software & Hardware Toolchain

### Software Tools
- **Embedded Development IDE:** Microchip MPLAB X IDE
- **C Compiler:** Microchip MPLAB XC32 Compiler (`xc32-gcc`)
- **Python IDE:** PyCharm
- **GUI Designer:** DWIN DGUS_V7647 (Display UI design and asset compilation)

### Hardware & Debugging Tools
- **Programmer / Debugger:** Microchip PICkit 5
- **Measurement & Test Equipment:** Digital Storage Oscilloscope, External Low-Voltage Bench Power Supply, Digital Multimeter

---

## Technical Documentation & References

### PIC32 Microcontroller
- [PIC32MM0256GPM064 docs](https://www.microchip.com/en-us/product/pic32mm0256gpm064)

### Programmable Power Supply
- [HPL5K0TS200 docs](https://www.xppower.com/product/HPL5K0-Series)

### Human-Machine Interfaces
- [DWIN DMG48270C043_03WTR docs](https://www.dwin-global.com/4-3-inch-hmi-uart-lcm-dmg48270c043_03w-commercial-grade-product/)

---

## How to Build & Flash

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/MuhammadHarisMasoom/pic32-5kw-dc-power-supply.git](https://github.com/MuhammadHarisMasoom/pic32-5kw-dc-power-supply.git)
