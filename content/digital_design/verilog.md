Title: SystemVerilog Coding Essentials
Summary: SystemVerilog concepts including assignments, procedures, and language features.
Date: 2025-05-09
Category: Digital Design
Author: Tung Nguyen
<!-- PELICAN_END_SUMMARY -->

## Assignments in SystemVerilog

- **Blocking Assignment (`=`)**: Executes sequentially.
- **Non-Blocking Assignment (`<=`)**: All updates scheduled at end of time step.

## Types of Assignments

- **Procedural Assignments**: Used in `always`, `initial`, `task`, `function`.
- **Continuous Assignments**: Assigned directly to `wire`.

> Note: `if`, `else`, and `case` must be used **within procedural blocks**.

## SystemVerilog Features

- **Classes & Inheritance**: For OOP-style modeling.
- **Randomization**: Use `rand` and `constraint` for random test generation.
- **Bit Ordering**: `[2:0]` means MSB (`2`) to LSB (`0`).

## Modules
```systemverilog
module example (
  input logic clk,
  input logic rst,
  output logic [2:0] out
);
// ...
endmodule
```

## Universal Verification Methodology (UVM) 
