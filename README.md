# Behave_JSON_Integration

**Python Behave BDD project using JSON data-driven testing** for [https://www.saucedemo.com](https://www.saucedemo.com):

```markdown
# 🧪 Python BDD JSON DDTF - SauceDemo Login Automation

This project showcases a **Data-Driven Testing Framework (DDTF)** using **Python Behave (BDD)** and **JSON** to manage test data. It automates login tests for [SauceDemo](https://www.saucedemo.com/), runs multiple credentials from a JSON file, and updates test results back into the same file.

---

## 🚀 Features

- 📁 Test data stored and updated in JSON
- ✅ BDD with **Behave**
- 🧪 Automated testing with **Selenium WebDriver**
- 🔁 Clean, reusable **Page Object Model**
- 🧼 Lightweight and readable test configuration

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/behave-json-saucedemo.git
cd behave-json-saucedemo
````

2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Ensure your Chrome version matches the ChromeDriver version.

---

## 🧪 Run the Tests

```bash
behave
```

---

## 📁 Sample JSON Structure

```json
[
  {
    "username": "standard_user",
    "password": "secret_sauce",
    "expected": "success",
    "result": ""
  },
  {
    "username": "locked_out_user",
    "password": "secret_sauce",
    "expected": "failure",
    "result": ""
  }
]
```

> 🟢 `result` is updated post-test execution.

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

* [Behave](https://github.com/behave/behave)
* [Selenium](https://selenium.dev/)
* [SauceDemo](https://www.saucedemo.com/)

---



