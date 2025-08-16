Title: Single Cycle Processor 
Date: 2025-07-24  
Category: Digital Design  
Slug: single-cycle-processor  
Author: Tung Nguyen  
Summary: MIPS microprocessor design  
<!-- PELICAN_END_SUMMARY -->

## Introduction

This blog post explores *microarchitecture*—the specific arrangement of registers, ALUs, FSMs, memories, and other logic blocks required to implement a processor architecture.

**Reference:** *Digital Design and Computer Architecture* by David Harris

---

## 1. Architectural State and Instruction Set

- **Architectural state:** 32 general-purpose registers and a program counter (PC)  
- **Instruction set:**  
  - R-type: `add`, `sub`, `and`, `or`  
  - Memory instructions: `lw`, `sw`  
  - Branch instruction: `beq`

Example:

![State element](../images/digital_design/processor_2.png)

---

## 2. Design Path: Single-Cycle Processor

### 2.1 32-bit Datapath

**State elements:** Program counter, instruction memory, data memory, and register file.

![Datapath](../images/digital_design/processor_1.png)

- **Program Counter (PC):** A 32-bit register whose output provides the current instruction address (PC), and whose input (`PC'`) points to the next instruction address.  
- **Instruction Memory:** Has a single read port. Takes the PC as input (instruction address) and outputs a 32-bit instruction.  
- **Register File:** Has two 5-bit read address ports (`Rs`, `Rt`) and one 5-bit write address port (`Rd`). Includes a 32-bit write data input to support immediate addressing.

#### Example: Single-Cycle Datapath for `lw` Instruction

a. Instruction Fetch  
b. Operand Read (Decode)  
![Decode](../images/digital_design/processor_3.png)

c. Sign-extend the Immediate  
![Sign-extend](../images/digital_design/processor_4.png)

d. Memory Address Computation  
![Address computation](../images/digital_design/processor_5.png)

e. Write Back  
![Write back](../images/digital_design/processor_6.png)

f. Determine Next Instruction Address  
![Next PC](../images/digital_design/processor_7.png)

---

### Generalized Datapath for R-Type Instruction

![R-type Datapath](../images/digital_design/processor_8.png)

---

### 2.2 Control Unit

Control signals are generated based on the **opcode** (bits [31:26]) and **function code** (bits [5:0]) of the instruction.

![Control unit](../images/digital_design/processor_9.png)

---

### Complete Single-Cycle MIPS Processor

![Complete processor](../images/digital_design/processor_10.png)

---

## 3. Verilog Design

(*To be detailed in the following sections.*)
