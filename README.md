# FunctionalTreat
# Project: Functional Treat
### Data Analyzer and Transformer Program

A menu-driven Python application designed to analyze, filter, and transform 1D and 2D numerical datasets using fundamental and advanced functional programming concepts.

---

## 🚀 Core Features & Implementation Details

The project satisfies all structural requirements cleanly without using external libraries (like NumPy):

*   **Built-in Functions:** Leverages `len()`, `sum()`, `min()`, and `max()` to dynamically compute base statistics on the current dataset state.
*   **User-Defined Functions (UDF):** Clean separation of concerns with modular functions handling input processing, arithmetic formatting, and menu rendering.
*   **Advanced Arguments & Meta:** Implements `*args` and `**kwargs` for flexible data unpacking alongside structured `__doc__` strings for internal system documentation.
*   **Recursion:** Features a purely recursive mathematical execution model for factorial tracking.
*   **Lambda & High-Order Functions:** Utilizes anonymous `lambda` declarations paired with functional `filter()` and `map()` streams to manipulate matrix elements efficiently based on runtime conditions.
*   **State Management:** Employs the `global` scope mechanics to safely preserve and look up historical runtime data snapshots across different sub-menus.
*   **Matrix Arrays (1D/2D):** Supports raw dimensional scaling from single sequences to uniform multi-layered lists (grids) with native sorting models (`sort()` vs `sorted()`).

---

## 🛠️ Project Structure & Architecture

```text
├── main.py          # Main executable source containing core application logic
└── README.md        # Technical design details and overview
