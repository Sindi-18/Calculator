Absolutely — here is the improved version formatted fully in Markdown, ready for your README.md ✅


---

# 🧮 Project Setup & Usage Guide

Welcome! Follow the steps below to set up, run, and test this project successfully.

---

## ✅ Requirements

Ensure you have the following installed:

- **UV** (Python package/environment manager)
- **Python 3.12+**
- **Tkinter**
- A **code editor** of your choice

---

## 📦 Install Dependencies

1️⃣ Navigate into the project directory:

```bash
cd <project-directory>

2️⃣ Install dependencies using:

uv sync

3️⃣ Run the project:

uv run main.py --help


---

🧪 Running Tests

This project uses pytest for automated testing.

Running an example test suite:

uv run pytest utils/test_operators.py

Example output:

=================== test session starts ===================
platform linux -- Python 3.12.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /data/data/com.termux/files/home/Calculator
configfile: pyproject.toml
collected 6 items

utils/test_operators.py FF...F                      [100%]

======================== FAILURES =========================
_____________________ test_add_valid ______________________

    def test_add_valid():
>       assert op.add(5, 7) == 12
               ^^^^^^
E       AttributeError: module 'operators' has no attribute 'add'
...
=============== 3 failed, 3 passed in 0.31s ===============

This output indicates 3 tests passed and 3 tests failed, meaning further improvements are required 🔧✅


---

🧰 Available Commands (Alpha Version)

Check version:

uv run main.py version

Perform division:

uv run main.py divide 5 6

Perform multiplication:

uv run main.py multiply 5 6


---

📌 Notes

This is the alpha version — expect changes, improvements, and bug fixes as development continues 🚧


---

⭐ Contributions

Feel free to open issues or suggest improvements!


---

