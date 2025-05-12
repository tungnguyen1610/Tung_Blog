Title: CAN network  
Date: 2025-05-11  
Category: Automotive  
Tags: Communication, CAN  
Summary: CAN communication in electric control unit (ECU).

## Introduction

The Controller Area Network (CAN) is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other within a vehicle without a host computer. It is widely used in automotive ECUs (Electronic Control Units) for real-time communication.

## CAN Features

- **Differential Signaling (CAN High and CAN Low):**  
  Uses two wires (CAN_H and CAN_L) for noise-resistant communication The signal is represented using:
  <ul>
    <li>Dominant bit: Logical 0 (CAN_H - CAN_L ~ 2 V)</li>
    <li>Recessive bit: Logical 1 (CAN_H - CAN_L ~ 0 V)</li>
  </ul>

- **Broadcast Communication:**  
  All nodes on the CAN bus can "hear" every transmission. Nodes determine if the message is relevant by filtering IDs.

- **Arbitration Field:**  
  When multiple ECUs transmit simultaneously, CAN uses priority-based arbitration. Lower ID values have higher priority.

- **CAN Frame Structure:**
  <ul>
    <li><strong>Identifier (ID):</strong> Determines the priority of the message.</li>
    <li><strong>RTR (Remote Transmission Request):</strong> Indicates if the frame is a data frame or a remote request.</li>
    <li><strong>Length:</strong> Number of bytes in the data field (0–8 for classic CAN, up to 64 in CAN FD).</li>
    <li><strong>Payload:</strong> The actual data being transmitted.</li>
    <li><strong>CRC (Cyclic Redundancy Check):</strong> Ensures data integrity.</li>
  </ul>


## General CAN set-up:
- **Microcontroller (MCU):**
  - Has dedicated CAN controller hardware.
  - Communicates using two digital lines:
    - **CAN_TX**: Transmit line from MCU to the CAN transceiver.
    - **CAN_RX**: Receive line from the CAN transceiver to the MCU.

- **CAN Transceiver:**
  - Converts digital signals (TX/RX) from the microcontroller into differential voltages on the CAN bus (CAN_H and CAN_L).
  - Also converts bus voltages back to digital signals for the MCU.
  - Ensures compliance with ISO 11898 (physical layer spec).

- **CAN Bus:**
  - Two-wire twisted pair: **CAN_H** and **CAN_L** to reduce EMC. 
  - Terminated at both ends with 120-ohm resistors to prevent signal reflections.

## CAN Bus Error
Error handling is vital to the robustness of CAN.

1. Bit Error (Transmitter)
  Node transmit a dominant/recessive bit but read backs opposite level

2. Bit stuffing Error (Receiver)
  Detecting a sequence of 6 bits of the same logical level 

3. Form error (Receiver):
  Detects bit of invalid logical level in the SOF/EOF fields or ACK/CRC delimiters

4. ACK error (Transmitter):
  Node transmits a CAN message, but the ACK slot is not made dominant by receivers

5. CRC Error (Receiver):
  Node calculates a CAN message CRC that differs from the transmitted CRC field value

