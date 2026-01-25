# Ethical Nmap Recon Tool

A Python-based ethical reconnaissance tool that wraps Nmap with proper authorization checks, input validation, scan customization, and controlled execution.

This project focuses on **responsible security automation**, not blind scanning.

---

## 🚀 Features

- Explicit **authorization check** before scanning
- Clear **ethical disclaimer**
- Target input validation (empty input blocked)
- DNS resolution check (invalid targets blocked)
- Dependency check for Nmap
- **Scan type selection**
  - Fast scan (`-F`)
  - Service version detection (`-sV`)
  - TCP connect scan (`-sT`)
- **Output format selection**
  - Normal (`-oN`)
  - XML (`-oX`)
  - All formats (`-oA`)
- Optional **host discovery bypass (`-Pn`)**
- Automatic report generation
- Clean exit and user-friendly messages

---

## 🧠 Why this tool exists

While Nmap already provides powerful scanning capabilities, this tool adds:

- Ethical enforcement
- User intent validation
- Safer defaults
- Workflow automation
- SOC-style operational thinking

The goal is to demonstrate **how security tools should be used responsibly in real environments**.

---

## 🛠️ Requirements

- Python 3.x
- Nmap installed and available in PATH

Check Nmap installation:
```bash
nmap --version
