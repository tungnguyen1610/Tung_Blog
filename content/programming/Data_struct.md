Title: Embedded C Structure  
Date: 2025-05-11  
Category: Programming  
Tags: struct, union, bitfield  
Summary: A detailed comparison between struct, union, and bit-field in Embedded C.


In C programming, especially within embedded systems, `struct` and `union` are user-defined data types that allow grouping variables of different types under one name. However, they differ fundamentally in how they allocate and manage memory.

---

## 🔹 Struct vs. Union

### ✅ `struct`

- Each member occupies **its own memory space**.
- Total size = **sum of all members' sizes** (plus possible padding for alignment).
- Members are stored **contiguously** in memory.

### ✅ `union`

- All members **share the same memory location**.
- Total size = **size of the largest member**.
- Only one member can hold a valid value at a time.

### 📊 Visual Comparison

![Struct vs Union](../images/programming/Struct_vs_Union.jpg)

---

## 🔸 Bit-Fields in Structures

Sometimes, we know a variable only needs a few bits (e.g., a month value ranges from 1–12). Using bit-fields helps **save memory**, which is crucial in embedded systems with limited storage.

### 📌 Syntax:

```c
struct {
    data_type member_name : width_in_bits;
};
```

### Example
```
struct date {
    int month : 4;
};
```
Bit-fields are powerful, but there are caveats:

If a field’s value exceeds its bit-width, unexpected behavior may 
occur.

In the example, when printing value of month to stdout, The output comes out to be negative. What happened behind is that the value 31 was stored in 4 bit signed integer which is equal to 1111.

