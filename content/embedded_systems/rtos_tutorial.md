Title: STM32 Startup Sequence  
Date: 2025-05-09  
Category: Embedded Systems  
Tags: stm32, microcontroller, startup, reset, IVT  
Slug: stm32-startup  
Summary: Understand the power-on and startup sequence of STM32 microcontrollers.

## Introduction

In this article, we'll explore how an STM32 microcontroller starts up after power-on or reset — from the first instruction to the start of your `main()` function.

---

## Microcontroller Startup Basics

A microcontroller begins execution from a known **reset vector address**. For ARM Cortex-M cores (used in STM32 devices), this involves the **Interrupt Vector Table (IVT)**:

- **IVT Location**: At the start of the memory map (e.g., `0x08000000` for Flash)
- **First Entry**: Initial **Stack Pointer** (SP)
- **Second Entry**: Address of the **Reset Handler** (i.e., where execution starts)

These values are set by the **linker script** and provided in `stm32xxx_flash.ld`.

---

## STM32 Startup Sequence

Here’s the typical STM32 boot and startup process:

1. **Reset Handler** (2nd entry in the IVT) is called
2. **Boot Configuration**: Determines whether to boot from:
   - Flash (default for user code)
   - System memory (bootloader)
   - SRAM (for debugging/testing)
3. **SystemInit()** is usually called (by CMSIS) early to:
   - Set up clock sources (HSE/PLL)
   - Configure low-level registers (via `system_stm32fxxx.c`)
4. **C Runtime Initialization**:
   - **Data Section Init**: Copies initialized variables from Flash to RAM
   - **BSS Section Init**: Zeros out uninitialized global/static variables
5. **Static Constructors**: Run C++ constructors if any
6. `main()` function is finally called

---

## Visual Summary

```text
[Power On / Reset]
       ↓
[IVT @ 0x08000000]
  - SP (entry 0)
  - Reset_Handler (entry 1)
       ↓
[SystemInit()]
       ↓
[Initialize .data and .bss]
       ↓
[Run static constructors]
       ↓
[main()]
```