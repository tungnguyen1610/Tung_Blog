Title: General Concepts in Digital Design
Date: 2025-07-24
Category: Digital Design
Slug: single-cycle-processor
Author: Tung Nguyen
Summary: MIPS micro-processor design
 <!-- PELICAN_END_SUMMARY -->
## Introduction
This blog covers microarchitecture which is the specific arrangement of registers, ALU, FSMs, memories and other logic building blocks needed to implement an architecture.

Reference: Digital Design and Computer Architecture (David Harris)

1. Architectural state and Instruction set
Architectural state: 32 registers and PC
Instruction set: R type (add, sub, and, or), memory instruction (lw,sw) and branches (beq)
For eg:
![State element](../images/digital_design/processor_2.png)

2. Design path (single-cycle processor)
2.1 32 bit Datapath
State element: Program counter, memories (instruction and ), registers.

![State element](../images/digital_design/processor_1.png)

Program counter: 32 bit register. Its output PC, current address instruction. Its input, PC', points to next address instruction

Instruction memory: single read port. It takes PC (address of instruction) -> output: 32 bit instruction

Register file: 2 read ports, and one write port. It takes 5 bit address input ports specifying one of 32 registers as Rs (source opperands). The write port
takes a 5-bit address input, A3; a 32-bit write data input (for immediate addressing).

Single cycle datapth of "lw" instruction
a instruction fetch
b Read opperand (decode)

![State element](../images/digital_design/processor_3.png)
c Sign-extend the immediate

![State element](../images/digital_design/processor_4.png)
d Memory address computation
![State element](../images/digital_design/processor_5.png)
e Write back
![State element](../images/digital_design/processor_6.png)
f. Determine next address instruction
![State element](../images/digital_design/processor_7.png)

Generalized datapath for R-type instruction
![State element](../images/digital_design/processor_8.png)

2.2 Control unit
Control signal: based on opcode and funct fields of insutrction ( bit [31:26], and bit [5:0])
![State element](../images/digital_design/processor_9.png)

Complete single-cycle of MIPS processor.
![State element](../images/digital_design/processor_10.png)

3. Verilog design