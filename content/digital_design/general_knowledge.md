Title: General Concepts in Digital Design
Date: 2025-05-10
Category: Digital Design
Slug: general-digital-design
Author: Tung Nguyen
Summary: Core concepts in digital logic design including timing, hazards, metastability, FSMs, and CDC.
 <!-- PELICAN_END_SUMMARY -->

## Timing Basics

- **Setup Time**: Time input must be stable **before** clock edge.
- **Hold Time**: Time input must be stable **after** clock edge.
- **Aperture Time**: `Setup + Hold` time.
- **Recovery Time**: Time async reset/set must be **inactive before** clock edge.
- **Removal Time**: Time async reset/set must be **inactive after** clock edge.
- **Metastability**: Flip-flops enter unpredictable states if timing is violated.
- **Fanout**: Number of gate inputs driven by a logic output.

## Combinational Logic

- **Hazard**: Glitches in outputs due to gate delays and improper logic design.

## Finite State Machines (FSM)

- **Encoding Styles**:
  - **Binary**
  - **Gray**
  - **One-hot**: One bit is HIGH, others LOW.
  - **One-cold**: One bit is LOW, others HIGH.

## Clock Domain Crossing (CDC)

- Transferring data between **different clock domains**
- Prevent metastability using:
  - 2/3 stage synchronizers
- To be added.