# 🧨 Extreme PDF Compressor

This Python tool applies **brutally aggressive compression** to any PDF file — perfect for reducing the size to the **absolute minimum**, even at the cost of quality, structure, and editability.

> ⚠️ The resulting PDF is **low-resolution**, **grayscale**, fully **rasterized** (text becomes images), with **all metadata removed**. Ideal for archiving, emailing, or storage purposes where quality is not a priority.

---

## ✅ Features

- Converts each PDF page to a low-resolution JPEG image.
- Grayscale image conversion for better compression.
- Reassembles all pages into a new compressed PDF.
- Applies Ghostscript for final extreme compression.
- Automatically cleans up temporary files.

---

## 📦 Requirements

- **Python 3.7+**
- **Ghostscript**

---

## 📥 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/extreme-pdf-compressor.git
cd extreme-pdf-compressor
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install Ghostscript

**macOS (using Homebrew):**

```bash
brew install ghostscript
```

**Ubuntu/Debian:**

```bash
sudo apt install ghostscript
```

**Windows:**

Download and install from: https://www.ghostscript.com/download.html

---

## 🚀 Usage

```bash
python comprimir_pdf_ultra.py your_file.pdf
```

The output will be a file called:

```
comprimido_ultra.pdf
```

in the same folder — **highly compressed**.

---

## 🛠 Customization

If you want to adjust the compression strength, edit the following variables inside the script:

```python
dpi = 35             # Controls rasterized image resolution (lower = smaller file)
jpeg_quality = 15    # JPEG quality (1 = worst, 100 = best)
```

---

## 💡 Tip

This tool is **destructive** by design — don't use it on files you intend to preserve in high quality.

---

## 📄 License

MIT License — free to use, modify, and distribute.
