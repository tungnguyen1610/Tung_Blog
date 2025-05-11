Title: CAN network  
Date: 2025-05-11  
Category: Automotive  
Tags: Communication, CAN  
Summary: CAN communication in electric control unit (ECU).

## Introduction

The Controller Area Network (CAN) is a robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other within a vehicle without a host computer. It is widely used in automotive ECUs (Electronic Control Units) for real-time communication.

## CAN Features

- **Differential Signaling (CAN High and CAN Low):**  
  Uses two wires (CAN_H and CAN_L) for noise-resistant communication. The signal is represented using:
  - **Dominant bit:** Logical 0 (CAN_H - CAN_L ~ 2 V)
  - **Recessive bit:** Logical 1 (CAN_H - CAN_L ~ 0 V)

- **Broadcast Communication:**  
  All nodes on the CAN bus can "hear" every transmission. Nodes determine if the message is relevant by filtering IDs.

- **Arbitration Field:**  
  When multiple ECUs transmit simultaneously, CAN uses priority-based arbitration. Lower ID values have higher priority.

- **CAN Frame Structure:**
  - **Identifier (ID):** Determines the priority of the message.
  - **RTR (Remote Transmission Request):** Indicates if the frame is a data frame or a remote request.
  - **Length:** Number of bytes in the data field (0–8 for classic CAN, up to 64 in CAN FD).
  - **Payload:** The actual data being transmitted.
  - **CRC (Cyclic Redundancy Check):** Ensures data integrity.

## Components:
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
  - Two-wire twisted pair: **CAN_H** and **CAN_L**
  - Terminated at both ends with 120-ohm resistors to prevent signal reflections.

## Conclusion
CAN communication is critical in modern automotive systems for enabling reliable, prioritized, and synchronized data exchange between ECUs.

