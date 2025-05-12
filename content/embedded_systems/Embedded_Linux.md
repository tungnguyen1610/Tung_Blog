Title: Intro to Embedded Linux  
Date: 2025-05-12 
Category: Embedded Systems  
Tags: Beaglebone Black, SoC, Linux, Bootloader  
Slug: intro-linux  
Summary: Learn the basics of Embedded Linux boot-up using Beaglebone Black.
<!-- PELICAN_END_SUMMARY -->

## Introduction

Why is Linux so pervasive? Why does something as seemingly simple as a smart TV need to run something as complex as Linux just to stream video?

The answer is functionality. Linux is open-source, and it offers a robust scheduler, a powerful networking stack, support for USB, Wi-Fi, Bluetooth, various storage types, multimedia devices, and much more. It checks all the boxes needed in a modern embedded device.

In this article, we'll explore the **startup process** of an embedded Linux system, using the well-known **Beaglebone Black** as an example. Devices like the Raspberry Pi follow a similar boot process, so these principles apply across many embedded platforms.

For a deeper dive into every layer of Embedded Linux—from bootloader to kernel, device trees, and driver development—I recommend the book **"Mastering Embedded Linux Programming"**.

---

## 1. Boot Process Overview

The boot process of an embedded Linux system typically involves the following stages:

### 🔹 Phase 1: ROM Code (Primary Bootloader)

This is the very first code that runs after power-on or reset. It is stored **on-chip** in the SoC and is called **ROM code**. Its job is to load a small portion of code from pre-defined sources into **SRAM**.

For example, Texas Instruments (TI) Sitara and OMAP processors may attempt to load this code (commonly named `MLO`) from:

- NAND flash
- SPI-connected flash
- MMC devices like eMMC or SD cards

Once loaded into SRAM, the ROM code jumps to the **SPL (Secondary Program Loader)**.

---

### 🔹 Phase 2: MLO (Secondary Bootloader)

This second-stage bootloader configures basic hardware like the memory controller. It then reads `u-boot.img` from a partition and prepares the system to run a full bootloader (U-Boot).

#### 📦 Example: Flashing from SD Card to eMMC on TI AM3358

```bash
#debug_over_display=tty0
source=/dev/mmcblk0
destination=/dev/mmcblk1
rfs_partition=single
rfs_rootfs_type=ext4
rfs_rootfs_startmb=4
bootloader=/opt/u-boot/bb-u-boot-am57xx-evm/install-mmcblk1.sh
flash_back=bbai-emmc-to-microsd
```
### 🔹 Phase 3: Full bootloader
At this stage, a full bootloader such as U-Boot is running. Its role is to:
- Load the Linux kernel into DRAM
- Pass essential information to the kernel

This includes:
- Hardware details, including: based address, working mode, interrupt line, etc.
- Kernel command-line arguments
Optional:
- Device Tree Blob (DTB): Describes hardware layout (memory, I/O, interrupts, etc.)
- Initial RAM filesystem (initramfs)

The kernel uses this information to initialize drivers and mount the root filesystem.
