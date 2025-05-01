# Python Fundamentals Practice Code

This repository contains a series of Python practice exercises designed to teach and reinforce fundamental programming concepts. The exercises progressively introduce new topics, building upon previous ones.

## Overview of Concepts Covered

These practices cover a range of essential Python fundamentals, including:

*   **Basic Syntax:** Variables, data types (integers, floats, strings), operators.
*   **Input/Output:** Getting user input (`input()`) and displaying output (`print()`), formatted strings (f-strings).
*   **Control Flow:**
    *   Conditional statements (`if`, `elif`, `else`).
    *   Loops (`while`).
*   **Data Structures:**
    *   Lists (creation, appending, accessing elements, iterating).
*   **Functions:** Defining and calling functions, passing arguments, returning values.
*   **Modules:** Creating and importing custom modules to organize code.
*   **File I/O:** Reading from and writing to text files (`.txt`, `.csv`).
*   **Error Handling:** Using `try...except` blocks to handle potential errors (e.g., `ValueError`).
*   **Input Validation:** Writing functions to ensure user input meets specific criteria (ranges, types, lengths).
*   **Code Organization:** Using configuration files (`_config.py`) for constants.

## Practice Breakdown

Here's a summary of what each practice directory covers:

*   **Practice_1 & Practice_0B:**
    *   **Task:** Basic calculations (gross pay, discounts).
    *   **Concepts:** Variables, basic data types, `input()`, `print()`, arithmetic operations.
*   **Practice_02:**
    *   **Task:** Calculate costs with tiered discounts and sales tax.
    *   **Concepts:** Constants, `if`/`elif`/`else` statements for decision making, formatted output.
*   **Practice_03:**
    *   **Task:** Process multiple sales transactions, accumulating totals until a sentinel value is entered.
    *   **Concepts:** `while` loops for repetition, accumulators (summing totals), basic `try...except` for numeric input validation, nested loops/conditionals.
*   **Practice_04:**
    *   **Task:** Refactor Practice_03 using functions and modules.
    *   **Concepts:** Defining functions, creating and importing modules (`_module.py`), using configuration files (`_config.py`), global variables for accumulators, modular code design.
*   **Practice_05:**
    *   **Task:** Create and read a sequential data file (one piece of data per line).
    *   **Concepts:** File I/O (`open()`, `with open()`, `'w'`, `'r'`), writing (`write()`) and reading (`readline()`) files line by line, string manipulation (`rstrip()`), sequential file processing logic.
*   **Practice_06:**
    *   **Task:** Process sales data for multiple salespeople using lists. Calculate statistics (min, max, average) and sort sales data without using built-in functions.
    *   **Concepts:** Lists (creation, appending), list iteration, implementing custom logic for finding min/max values and sorting (e.g., bubble sort).
*   **Practice_07:**
    *   **Task:** Create and read data from a CSV (Comma Separated Values) file.
    *   **Concepts:** File I/O with CSV format, string splitting (`split(',')`), data type conversions after reading from file, combining file handling with modular code.

## How to Use for Learning

1.  **Study the Code:** Read through the Python files (`.py`) in each practice folder, starting from `Practice_0`. Pay attention to the comments and structure.
2.  **Run the Code:** Execute the main script (e.g., `Practice_07.py`) to see how it works. Provide input as prompted.
3.  **Understand the Logic:** Trace the execution flow. How do the loops, conditionals, and functions work together? How is data validated and processed?
4.  **Examine Supporting Files:** Look at the `_module.py` and `_config.py` files in later practices to understand how code is organized. Review the OIP/Pseudo Code files (`.txt`, `.docx`) for the planning steps.
5.  **Modify and Experiment:** Change parts of the code to see what happens. Try different inputs. Add new features or validation rules.
6.  **Replicate:** Try to solve the problem described in the comments or OIP/Pseudo Code yourself before looking at the provided solution.

These exercises provide a practical way to grasp core Python concepts through building small, focused applications.
