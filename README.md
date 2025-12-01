## ⚠️ **Warning**: This is very much a new work in progress. Many stubs and non-working code.⚠️

#### Built using Python 3.13.5
#### ESP-IDF verion 5.5.1

## What is working?
 - Main cli - currently you can call it from the esp32-starter directory like so:  `python -m esp32_init_tool.esp32_init.cli project_name --board generic`
 - Boards
    - Generic ESP32 - very simple test that should work for almost any ESP32. Creates a FreeRTOS task and outputs a count to the serial console. No other peripherals are initialized. [Generic ESP32](boards/generic/README.md)
    - hackerbox107-128-round [HackerBox 107](boards/hackerbox107-128-round/README.md)

# ESP32 Starter – Project & Board Generator for ESP-IDF

**ESP32 Starter** is a modular project generator for ESP-IDF.  
It helps you quickly bootstrap working ESP32 projects across a large collection of ESP32 + display combo boards, without constantly digging through old repos to find pinouts, display configs, or boilerplate code.

This repo is designed to serve two purposes:

1. **A user-friendly tool** (`esp32-init`) that generates clean ESP-IDF projects for specific boards with optional hardware feature modules (GPS, LVGL UI, WiFi helpers, etc.).  
2. **A knowledge base** of board-specific wiring, reusable feature modules, and a minimal ESP-IDF template that together eliminate repetitive setup work.

---

## 🚀 What This Tool Does

ESP-IDF users often have a *pile* of boards, each slightly different:

- different pins  
- different LCDs  
- different SPI buses  
- different touch controllers  
- different UART wiring  

Setting up each project becomes tedious:

- copy some old project  
- fix board pins  
- rip out old hacks  
- clean up unneeded code  
- add new features manually  
- hope it still builds  

**This tool solves that by letting you do:**

```bash
python -m esp32_init_tool.esp32_init.cli my_project --board generic --gps --lvgl
```

…and you instantly get a *clean*, *minimal*, *correctly-wired*, *feature-enabled* ESP-IDF project.

Every project contains only the files it needs. No bloat. 

---

## 🧠 High-Level Architecture

The system is made of four main pieces:

```
esp32-starter/
├── boards/           # Board pinouts & wiring (per-board C files)
├── features/         # Reusable C modules (GPS, LVGL, WiFi, etc.)
├── idf-templates/    # Minimal ESP-IDF project template
└── esp32_init_tool/  # Python-based project generator
```

---

## 📦 Repository Structure (Explained)

### `boards/` – board-specific wiring implementations

Each board implements functions declared in `board_interface.h` and defines hardware wiring.

### `features/` – reusable feature modules (C code)

Features are optional modules (GPS, LVGL, WiFi, etc.).  
The generator copies only selected features into new projects.

### `idf-templates/` – minimal ESP-IDF base project

Provides `main.c`, board interface, and base CMakeLists.  
Contains no hardware or feature-specific code.

### `esp32_init_tool/` – Python generator

Implements:

- CLI (`esp32-init`)
- project creation logic
- feature plugin system
- board discovery & validation
- template patching + file copying

---

## 🛠️ How a Project Is Generated

Example:

```bash
python -m esp32_init_tool.esp32_init.cli myapp --board generic --gps --lvgl
```

This:

1. Copies the base project
2. Applies board wiring
3. Applies features (GPS, LVGL)
4. Merges Kconfig snippets
5. Updates project names
6. Produces a minimal, fully wired project

---

## 🧩 How to Add a New Board

1. Create a new folder in `boards/<board_id>/`
2. Add `board_impl.c` and optional `idf_component.yml`
3. Implement required functions from `board_interface.h`
4. Generate a test project to verify everything works

---

## 🧩 How to Add a New Feature

1. Create `features/<name>/` with:

```
<name>.c
<name>.h
Kconfig
```

2. Add a Python module under:

```
esp32_init_tool/esp32_init/features/<name>.py
```

3. Register the feature in Python

You can now use `--<name>` in the generator.

---

## 🔧 Installation & Usage

```bash
cd esp32_init_tool
pip install -e .
```

Then:

```bash
python -m esp32_init_tool.esp32_init.cli <project_name> --board <board_id> [--gps] [--lvgl]
```

---

## 🔐 Licensing

All original code in this repository is licensed under Apache License 2.0.  
ESP-IDF and its bundled third-party libraries are licensed separately under permissive licenses (Apache, MIT, BSD, etc.).

---

Enjoy building clean ESP-IDF projects! 🚀




<center> This repository was automatically pushed from my self-hosted Forgejo server. Give it a try <a href="https://forgejo.org/">Forgejo</a>. </center>
