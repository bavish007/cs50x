# Week 5 Data Structures

## 🎯 Overview

This week, the focus shifts from fixed-size arrays to dynamic memory organization. We explore **Data Structures**—forms of organizing data in memory to solve problems efficiently.

Top 3 Learning Outcomes:

1. **Abstract Data Types (ADTs):** Understanding conceptual structures like **Queues** (FIFO) and **Stacks** (LIFO) and their implementations.
2. **Dynamic Structures:** Mastering **Linked Lists** to allow data to grow and shrink dynamically, and **Trees** (specifically Binary Search Trees) for efficient $O(\log n)$ searching.
3. **Hash Tables & Tries:** Implementing **Hash Tables** for constant-time $O(1)$ access and **Tries** for rapid prefix-based data retrieval.

## 📚 Documentation & Resources

| Document | Type | Location |
| :--- | :---: | :--- |
| **Notes** | Markdown | [Notes.md](./Lecture/Notes.md) |
| **Data Structures** | PDF | [Lecture/Additional Concepts/data_structures.pdf](./Lecture/Additional%20Concepts/data_structures.pdf) |
| **Doubly Linked Lists** | PDF | [Lecture/Additional Concepts/doubly_linked_lists.pdf](./Lecture/Additional%20Concepts/doubly_linked_lists.pdf) |
| **Hash Tables** | PDF | [Lecture/Additional Concepts/hash_tables.pdf](./Lecture/Additional%20Concepts/hash_tables.pdf) |
| **Queues** | PDF | [Lecture/Additional Concepts/queues.pdf](./Lecture/Additional%20Concepts/queues.pdf) |
| **Singly Linked Lists** | PDF | [Lecture/Additional Concepts/singly_linked_lists.pdf](./Lecture/Additional%20Concepts/singly_linked_lists.pdf) |
| **Stacks** | PDF | [Lecture/Additional Concepts/stacks.pdf](./Lecture/Additional%20Concepts/stacks.pdf) |
| **Structures** | PDF | [Lecture/Additional Concepts/structures.pdf](./Lecture/Additional%20Concepts/structures.pdf) |
| **Tries** | PDF | [Lecture/Additional Concepts/tries.pdf](./Lecture/Additional%20Concepts/tries.pdf) |
| **Lecture 5 Slides** | PPTX | [Lecture/Resources/CS50 2025 - Lecture 5 - Data Structures.pptx](./Lecture/Resources/CS50%202025%20-%20Lecture%205%20-%20Data%20Structures.pptx) |
| **Lecture 5 PDF** | PDF | [Lecture/Resources/lecture5.pdf](./Lecture/Resources/lecture5.pdf) |
| **Lecture Source PDF** | PDF | [Lecture/Source Code/src5.pdf](./Lecture/Source Code/src5.pdf) |
| **Section 5 PDF** | PDF | [Section/Resources/section5.pdf](./Section/Resources/section5.pdf) |
| **Section Source PDF** | PDF | [Section/Source Code/src5.pdf](./Section/Source Code/src5.pdf) |

## 🗂️ Complete File Index

<details><summary><b>📂 View Source Files</b></summary>

| File | Type | Link |
| :--- | :---: | :--- |
| 📄 `Readme.md` | .md | [View](./Readme.md) |
| 📂 **Lecture** | Folder | [View](./Lecture) |
| 📄 `Notes.md` | .md | [View](./Lecture/Notes.md) |
| 📂 **Lecture / Additional Concepts** | Folder | [View](./Lecture/Additional%20Concepts) |
| 📄 `data_structures.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/data_structures.pdf) |
| 📄 `doubly_linked_lists.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/doubly_linked_lists.pdf) |
| 📄 `hash_tables.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/hash_tables.pdf) |
| 📄 `queues.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/queues.pdf) |
| 📄 `singly_linked_lists.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/singly_linked_lists.pdf) |
| 📄 `stacks.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/stacks.pdf) |
| 📄 `structures.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/structures.pdf) |
| 📄 `tries.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/tries.pdf) |
| 📂 **Lecture / Resources** | Folder | [View](./Lecture/Resources) |
| 📄 `CS50 2025 - Lecture 5 - Data Structures.pptx` | .pptx | [Download](./Lecture/Resources/CS50%202025%20-%20Lecture%205%20-%20Data%20Structures.pptx) |
| 📄 `lecture5.pdf` | .pdf | [Download](./Lecture/Resources/lecture5.pdf) |
| 📂 **Lecture / Source Code** | Folder | [View](./Lecture/Source%20Code) |
| 📄 `list0.c` | .c | [View](./Lecture/Source%20Code/list0.c) |
| 📄 `list1.c` | .c | [View](./Lecture/Source%20Code/list1.c) |
| 📄 `list2.c` | .c | [View](./Lecture/Source%20Code/list2.c) |
| 📄 `list3.c` | .c | [View](./Lecture/Source%20Code/list3.c) |
| 📄 `list4.c` | .c | [View](./Lecture/Source%20Code/list4.c) |
| 📄 `list5.c` | .c | [View](./Lecture/Source%20Code/list5.c) |
| 📄 `list6.c` | .c | [View](./Lecture/Source%20Code/list6.c) |
| 📄 `list7.c` | .c | [View](./Lecture/Source%20Code/list7.c) |
| 📄 `list8.c` | .c | [View](./Lecture/Source%20Code/list8.c) |
| 📄 `list9.c` | .c | [View](./Lecture/Source%20Code/list9.c) |
| 📄 `src5.pdf` | .pdf | [Download](./Lecture/Source%20Code/src5.pdf) |
| 📂 **Problem Set 5 / inheritance** | Folder | [View](./Problem%20Set%205/inheritance) |
| 📄 `inheritance.c` | .c | [View](./Problem%20Set%205/inheritance/inheritance.c) |
| 📂 **Problem Set 5 / speller** | Folder | [View](./Problem%20Set%205/speller) |
| 📄 `Makefile` | Makefile | [View](./Problem%20Set%205/speller/Makefile) |
| 📄 `dictionary.c` | .c | [View](./Problem%20Set%205/speller/dictionary.c) |
| 📄 `dictionary.h` | .h | [View](./Problem%20Set%205/speller/dictionary.h) |
| 📄 `speller.c` | .c | [View](./Problem%20Set%205/speller/speller.c) |
| 📂 **Problem Set 5 / speller / dictionaries** | Folder | [View](./Problem%20Set%205/speller/dictionaries) |
| 📄 `large` | dict | [View](./Problem%20Set%205/speller/dictionaries/large) |
| 📄 `small` | dict | [View](./Problem%20Set%205/speller/dictionaries/small) |
| 📂 **Problem Set 5 / speller / keys** | Folder | [View](./Problem%20Set%205/speller/keys) |
| 📄 `aca.txt` | .txt | [View](./Problem%20Set%205/speller/keys/aca.txt) |
| 📄 *(Contains 39+ text files for testing)* | .txt | — |
| 📂 **Problem Set 5 / speller / texts** | Folder | [View](./Problem%20Set%205/speller/texts) |
| 📄 `aca.txt` | .txt | [View](./Problem%20Set%205/speller/texts/aca.txt) |
| 📄 *(Contains 30+ text sources)* | .txt | — |
| 📂 **Section / Resources** | Folder | [View](./Section/Resources) |
| 📄 `section5.pdf` | .pdf | [Download](./Section/Resources/section5.pdf) |
| 📂 **Section / Source Code** | Folder | [View](./Section/Source%20Code) |
| 📄 `hash.c` | .c | [View](./Section/Source%20Code/hash.c) |
| 📄 `list.c` | .c | [View](./Section/Source%20Code/list.c) |
| 📄 `src5.pdf` | .pdf | [Download](./Section/Source%20Code/src5.pdf) |

</details>

## 🎥 Video Resources

### Main Lecture

<div align="center">

[![Lecture 5](https://img.youtube.com/vi/PmAI76OGE_E/0.jpg)](https://youtu.be/PmAI76OGE_E)

</div>

### 🧠 Concept Clips

* [Structures](https://youtu.be/E4lb2gkyXr8)
* [Singly Linked Lists](https://youtu.be/zQI3FyWm144)
* [Doubly Linked Lists](https://youtu.be/FHMPswJDCvU)
* [Stacks](https://youtu.be/hVsNqhEthOk)
* [Queues](https://youtu.be/3TmUv1uS92s)
* [Hash Tables](https://youtu.be/nvzVHwrrub0)
* [Tries](https://youtu.be/MC-iQHFdEDI)
* [Data Structures](https://youtu.be/3uGchQbk7g8)

## 🛠️ Problem Sets & Labs

### 🧬 Inheritance

Simulate the inheritance of blood types for each member of a family tree.

* **Location:** [`Problem Set 5/inheritance`](./Problem%20Set%205/inheritance)
* **Key Concepts:** Recursive data structures, memory allocation, struct pointers.

### 📖 Speller

Implement a program that spell-checks a file using a hash table.

* **Location:** [`Problem Set 5/speller`](./Problem%20Set%205/speller)
* **Key Concepts:** Hash functions, hash tables, linked lists (for chaining), memory management (malloc/free).
* **Objective:** Optimize check time and memory usage while correctly identifying misspelled words.

---

<div align="center">
  <br />
  <a href="../README.md">
    <img src="https://img.shields.io/badge/Return_to_Master_Index-181717?style=for-the-badge&logo=github&logoColor=white" alt="Back to Master Index" />
  </a>
</div>
