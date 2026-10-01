# Password Security Assessment and Secure Password Generator Using Python

## 1. Project Title

**Password Security Assessment and Secure Password Generator Using Python**

---

## 2. Problem Statement

Weak passwords are one of the common security risks in computer systems. Passwords that are short or contain only simple characters can be easier to guess.

This project provides a Python/Tkinter-based tool that checks the strength of a password according to different password-policy conditions and generates a secure 16-character random password.

The project is developed as a mini-project for **Cryptography and Network Security (CNS)**.

---

## 3. Objectives

The main objectives of this project are:

* To assess the strength of a user-provided password.
* To check the minimum password length.
* To check the presence of uppercase and lowercase characters.
* To check the presence of digits.
* To check the presence of special characters.
* To classify passwords as WEAK, MEDIUM, STRONG, or VERY STRONG.
* To provide suggestions for improving weak passwords.
* To generate a secure 16-character random password.
* To understand basic password security concepts.
* To demonstrate secure random password generation using Python.

---

## 4. Technologies Used

The following technologies are used in this project:

* **Python 3.10+**
* **Tkinter** – for graphical user interface development
* **VS Code** – development environment

---

## 5. Python Libraries Used

### 5.1 `secrets`

The `secrets` module is used for generating secure random passwords.

### 5.2 `string`

The `string` module is used for accessing predefined character sets such as:

* Uppercase letters
* Lowercase letters
* Digits
* Special characters

### 5.3 `tkinter`

Tkinter is used to create the graphical user interface of the application.

---

## 6. Cryptography / Network Security Concepts Used

The project demonstrates the following Cryptography and Network Security concepts:

### 6.1 Authentication

Passwords are commonly used as an authentication mechanism to verify a user's identity.

### 6.2 Password Policies

The application checks password requirements such as length, uppercase/lowercase characters, digits, and special characters.

### 6.3 Input Validation

The entered password is checked against predefined security conditions.

### 6.4 Secure Random Generation

The Python `secrets` module is used to generate a 16-character secure random password.

### 6.5 Resistance to Simple Guessing

Using longer passwords containing different types of characters can make simple password guessing more difficult.

---

## 7. Key Features

The main features of the project are:

* Hidden password input
* Minimum length check
* Uppercase character check
* Lowercase character check
* Digit check
* Special-character check
* WEAK password classification
* MEDIUM password classification
* STRONG password classification
* VERY STRONG password classification
* Password improvement suggestions
* 16-character secure random password generation
* Clear/Reset button
* Simple graphical user interface

---

## 8. System Requirements

### Hardware Requirements

* Processor: Intel i3 or equivalent
* RAM: 4 GB or above
* Available storage for the project files

### Software Requirements

* Windows/Linux/macOS
* Python 3.10 or above
* Visual Studio Code
* Tkinter
* Git and GitHub, if required for repository submission

---

## 9. Project Structure

```text
CNS_Password_Security_Tool/
│
├── password_security_tool.py
├── README.md
├── PROJECT_REPORT.pdf
├── PRESENTATION.pptx
│
└── screenshots/
    ├── 01_home.png
    ├── 02_weak_password.png
    ├── 03_strong_password.png
    ├── 04_generated_password.png
    └── 05_vscode.png
```

---

## 10. How to Install and Run

### Step 1: Install Python

Install **Python 3.10 or above** on your computer.

### Step 2: Download or Clone the Project

Clone the GitHub repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Or download the project ZIP file and extract it.

### Step 3: Open the Project

Open the project folder in **Visual Studio Code**.

### Step 4: Run the Program

Open the VS Code terminal and execute:

```bash
python password_security_tool.py
```

### Step 5: Use the Application

1. Enter a password.
2. Check the password strength.
3. View the strength classification.
4. Read improvement suggestions if required.
5. Use the password generator to generate a secure 16-character password.
6. Use the Clear/Reset button to start again.

---

## 11. Test Cases

The following test cases are included in the project:

| Test Case | Input        | Expected Result |
| --------- | ------------ | --------------- |
| TC01      | `abc`        | WEAK            |
| TC02      | `abcdefgh`   | MEDIUM          |
| TC03      | `Tanvi123`   | STRONG          |
| TC04      | `Tanvi@2026` | VERY STRONG     |
| TC05      | Empty input  | Warning         |

---

## 12. Screenshots

The project screenshots are stored in the `screenshots/` folder.

### Screenshot 1 – Home Screen

![Homepage](../Pictures/Screenshots/Homepage.png)

Shows the main interface of the password security tool.

### Screenshot 2 – Weak Password

![weakpw](../Pictures/Screenshots/weakpw.png)

Shows the result when a weak password is entered.

### Screenshot 3 – Strong Password

![strongpw](../Pictures/Screenshots/strongpw.png)

Shows the password strength assessment for a stronger password.

### Screenshot 4 – Generated Password

![generatedpw](../Pictures/Screenshots/generatedpw.png)

Shows the secure 16-character password generated by the application.

### Screenshot 5 – VS Code

![vscode](../Pictures/Screenshots/vscode.png)

Shows the project being executed/developed in Visual Studio Code.

---

## 13. Project Demonstration

The working of the project can be demonstrated using the following steps:

```text
        Start Application
               ↓
       Enter Password
               ↓
       Validate Password
               ↓
    Check Security Conditions
               ↓
     ┌─────────┴─────────┐
     ↓                   ↓
Password Assessment   Password Generator
     ↓                   ↓
Strength Result       Secure Password
     ↓
Suggestions
```

### Password Assessment

The application checks:

* Password length
* Uppercase characters
* Lowercase characters
* Digits
* Special characters

Based on these conditions, the password is classified as:

* **WEAK**
* **MEDIUM**
* **STRONG**
* **VERY STRONG**

### Password Generation

The application can generate a **16-character secure random password** using Python's `secrets` module.

---

## 14. Advantages

* Simple and easy-to-use interface.
* Helps users understand password security requirements.
* Provides password-strength classification.
* Provides suggestions for improving passwords.
* Generates secure random passwords.
* Does not require a database.
* Suitable for demonstrating basic CNS concepts.

---

## 15. Limitations

This is an educational password-policy checker.

The application:

* Does not store passwords.
* Does not perform account authentication.
* Does not estimate real password-cracking time.
* Does not check passwords against breach databases.

---

## 16. Future Scope

The project can be enhanced in the future by adding:

* Password entropy estimation
* Common-password checking
* Configurable password policies
* Breached-password checking
* Multi-factor authentication (MFA) demonstration
* Password manager integration
* Web-based version

---

## 17. GitHub Repository Link

**GitHub Repository:**

YOUR_GITHUB_REPOSITORY_LINK

---





The complete project report is included in the repository as:



## 18. Academic Context

**Subject:** Cryptography and Network Security (CNS)

**Project:** Password Security Assessment and Secure Password Generator Using Python

**Student:** Tanvi Sapate

**Course:** B.Tech (IT)

**Roll No.:** 144
