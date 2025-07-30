# 🧨 Extreme PDF Compressor

This Python tool applies **brutally aggressive compression** to any PDF file — perfect for reducing size to the **absolute minimum**, even at the cost of quality, structure, and editability.

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

1. **Python 3.7+**
2. **Ghostscript**

### 📥 Installation

#### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/extreme-pdf-compressor.git
cd extreme-pdf-compressor
