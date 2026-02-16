# 🧠 Smart OCR Reader (Typed & Handwritten)

A **CPU-friendly, free OCR system** that accurately extracts **typed and handwritten text** from images using **separate, specialized OCR pipelines** — designed to work smoothly on laptops **without a GPU**.

This project focuses on **practical OCR engineering**, not just model usage.

---

## ✨ Key Features

- 📄 **Typed Text OCR** using EasyOCR (fast & lightweight)
- ✍️ **Handwritten Text OCR** using TrOCR (handwriting-trained transformer)
- 🔀 **Explicit OCR mode selection** (no unreliable auto-switching)
- 🖼️ **Custom image preprocessing** for better accuracy
- 🧠 Modular, extendable architecture
- 💻 Runs entirely on **CPU**
- 💸 **100% free & open-source**

---

## 🧠 Why This Project Matters

OCR for typed text and handwritten text are **fundamentally different problems**.

Instead of using a single OCR model with heuristics, this system:
- Separates pipelines for **predictability**
- Uses the **right model for the right input**
- Avoids unnecessary compute overhead
- Makes debugging and extension easier

This is **real-world OCR system design**, not a demo.

---

## 🏗️ Architecture Overview

