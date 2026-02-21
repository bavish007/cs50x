# Week 4 Memory

## 🎯 Overview

This week dives deep into the lower-level details of how computer memory works. Moving away from the abstractions of higher-level languages, we explore the fundamental building blocks of data storage and manipulation.

**Key Learning Outcomes:**

1. **Memory & Pointers:** Understanding how data is stored in memory (addresses) and how to direct the computer to specific locations using pointers (`&` and `*` operators).
2. **Manual Memory Management:** Learning to allocate (`malloc`) and deallocate (`free`) memory dynamically, and the importance of avoiding memory leaks (using tools like Valgrind).
3. **Data Representation:** Gaining insight into how images and files are constructed from raw bytes (pixels, hexadecimal) and how to manipulate them directly.

## 📚 Documentation & Resources

| Document | Type | Location |
| :--- | :---: | :--- |
| **Notes** | Markdown | [Notes.md](./Lecture/Notes.md) |
| **Call Stacks** | PDF | [call_stacks.pdf](./Lecture/Additional%20Concepts/call_stacks.pdf) |
| **Custom Types** | PDF | [custom_types.pdf](./Lecture/Additional%20Concepts/custom_types.pdf) |
| **Dynamic Memory Allocation** | PDF | [dynamic_memory_allocation.pdf](./Lecture/Additional%20Concepts/dynamic_memory_allocation.pdf) |
| **File Pointers** | PDF | [file_pointers.pdf](./Lecture/Additional%20Concepts/file_pointers.pdf) |
| **Hexadecimal** | PDF | [hexadecimal.pdf](./Lecture/Additional%20Concepts/hexadecimal.pdf) |
| **Pointers** | PDF | [pointers.pdf](./Lecture/Additional%20Concepts/pointers.pdf) |
| **Lecture 4 Slides** | PPTX | [CS50 2025 - Lecture 4 - Memory.pptx](./Lecture/Resources/CS50%202025%20-%20Lecture%204%20-%20Memory.pptx) |
| **Lecture 4 PDF** | PDF | [lecture4.pdf](./Lecture/Resources/lecture4.pdf) |
| **Source Code PDF** | PDF | [src4.pdf](./Lecture/Source%20Code/src4.pdf) |

## 🗂️ Complete File Index

* **Lecture**
  * 📂 **Additional Concepts**
    * 📄 [`call_stacks.pdf`](./Lecture/Additional%20Concepts/call_stacks.pdf)
    * 📄 [`custom_types.pdf`](./Lecture/Additional%20Concepts/custom_types.pdf)
    * 📄 [`dynamic_memory_allocation.pdf`](./Lecture/Additional%20Concepts/dynamic_memory_allocation.pdf)
    * 📄 [`file_pointers.pdf`](./Lecture/Additional%20Concepts/file_pointers.pdf)
    * 📄 [`hexadecimal.pdf`](./Lecture/Additional%20Concepts/hexadecimal.pdf)
    * 📄 [`pointers.pdf`](./Lecture/Additional%20Concepts/pointers.pdf)
  * 📄 [`Notes.md`](./Lecture/Notes.md)
  * 📂 **Resources**
    * 📄 [`CS50 2025 - Lecture 4 - Memory.pptx`](./Lecture/Resources/CS50%202025%20-%20Lecture%204%20-%20Memory.pptx)
    * 📄 [`lecture4.pdf`](./Lecture/Resources/lecture4.pdf)
  * 📂 **Source Code**
    * 📄 [`addresses0.c`](./Lecture/Source%20Code/addresses0.c)
    * 📄 [`addresses1.c`](./Lecture/Source%20Code/addresses1.c)
    * 📄 [`addresses2.c`](./Lecture/Source%20Code/addresses2.c)
    * 📄 [`addresses3.c`](./Lecture/Source%20Code/addresses3.c)
    * 📄 [`addresses4.c`](./Lecture/Source%20Code/addresses4.c)
    * 📄 [`addresses5.c`](./Lecture/Source%20Code/addresses5.c)
    * 📄 [`addresses6.c`](./Lecture/Source%20Code/addresses6.c)
    * 📄 [`addresses7.c`](./Lecture/Source%20Code/addresses7.c)
    * 📄 [`addresses8.c`](./Lecture/Source%20Code/addresses8.c)
    * 📄 [`addresses9.c`](./Lecture/Source%20Code/addresses9.c)
    * 📄 [`addresses10.c`](./Lecture/Source%20Code/addresses10.c)
    * 📄 [`compare0.c`](./Lecture/Source%20Code/compare0.c)
    * 📄 [`compare1.c`](./Lecture/Source%20Code/compare1.c)
    * 📄 [`compare2.c`](./Lecture/Source%20Code/compare2.c)
    * 📄 [`compare3.c`](./Lecture/Source%20Code/compare3.c)
    * 📄 [`compare4.c`](./Lecture/Source%20Code/compare4.c)
    * 📄 [`copy0.c`](./Lecture/Source%20Code/copy0.c)
    * 📄 [`copy1.c`](./Lecture/Source%20Code/copy1.c)
    * 📄 [`copy2.c`](./Lecture/Source%20Code/copy2.c)
    * 📄 [`copy3.c`](./Lecture/Source%20Code/copy3.c)
    * 📄 [`copy4.c`](./Lecture/Source%20Code/copy4.c)
    * 📄 [`copy5.c`](./Lecture/Source%20Code/copy5.c)
    * 📄 [`cp.c`](./Lecture/Source%20Code/cp.c)
    * 📄 [`garbage.c`](./Lecture/Source%20Code/garbage.c)
    * 📄 [`get0.c`](./Lecture/Source%20Code/get0.c)
    * 📄 [`get1.c`](./Lecture/Source%20Code/get1.c)
    * 📄 [`get2.c`](./Lecture/Source%20Code/get2.c)
    * 📄 [`get3.c`](./Lecture/Source%20Code/get3.c)
    * 📄 [`memory.c`](./Lecture/Source%20Code/memory.c)
    * 📄 [`phonebook.csv`](./Lecture/Source%20Code/phonebook.csv)
    * 📄 [`phonebook0.c`](./Lecture/Source%20Code/phonebook0.c)
    * 📄 [`phonebook1.c`](./Lecture/Source%20Code/phonebook1.c)
    * 📄 [`src4.pdf`](./Lecture/Source%20Code/src4.pdf)
    * 📄 [`swap0.c`](./Lecture/Source%20Code/swap0.c)
    * 📄 [`swap1.c`](./Lecture/Source%20Code/swap1.c)

* **Problem Set 4**
  * 📂 **filter-less**
    * 📄 [`bmp.h`](./Problem%20Set%204/filter-less/bmp.h)
    * 📄 [`filter.c`](./Problem%20Set%204/filter-less/filter.c)
    * 📄 [`helpers.c`](./Problem%20Set%204/filter-less/helpers.c)
    * 📄 [`helpers.h`](./Problem%20Set%204/filter-less/helpers.h)
    * 📄 [`Makefile`](./Problem%20Set%204/filter-less/Makefile)
  * 📂 **filter-more**
    * 📄 [`bmp.h`](./Problem%20Set%204/filter-more/bmp.h)
    * 📄 [`filter.c`](./Problem%20Set%204/filter-more/filter.c)
    * 📄 [`helpers.c`](./Problem%20Set%204/filter-more/helpers.c)
    * 📄 [`helpers.h`](./Problem%20Set%204/filter-more/helpers.h)
    * 📄 [`Makefile`](./Problem%20Set%204/filter-more/Makefile)
  * 📂 **recover**
    * 📄 [`recover.c`](./Problem%20Set%204/recover/recover.c)

## 🎥 Video Resources

### Main Lecture

[![Lecture 4](https://img.youtube.com/vi/db0H0U13YsA/0.jpg)](https://youtu.be/db0H0U13YsA)

### 🧠 Concept Clips

* [Hexadecimal](https://youtu.be/u_atXp-NF6w)
* [Pointers](https://youtu.be/XISnO2YhnsY)
* [Defining Custom Types](https://youtu.be/96M4q0OnMfY)
* [Dynamic Memory Allocation](https://youtu.be/xa4ugmMDhiE)
* [Call Stacks](https://youtu.be/aCPkszeKRa4)
* [File Pointers](https://youtu.be/bOF-SpEAYgk)

## 🛠️ Problem Sets & Labs

### Problem Set 4

* **Filter (Less & More):** A program to apply filters to BMP images, such as grayscale, sepia, reflection, and blur. This involves direct manipulation of pixels and understanding image file formats.
* **Recover:** A forensic image recovery program. It reads a raw memory card image (`card.raw`) and "recovers" lost JPEG files by looking for their signatures (headers) in the byte stream.

---
[← Return to Course Index](../README.md)
