import fitz  # PyMuPDF
from PIL import Image
import os
import subprocess

def convertir_paginas_a_imagenes(pdf_path, dpi=40, calidad_jpeg=20):
    doc = fitz.open(pdf_path)
    img_paths = []

    os.makedirs("paginas", exist_ok=True)

    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csGRAY)  # Escala de grises
        img_path = f"paginas/pagina_{i+1}.jpg"
        img = Image.frombytes("L", [pix.width, pix.height], pix.samples)  # L = grayscale
        img.save(img_path, "JPEG", quality=calidad_jpeg, optimize=True)
        img_paths.append(img_path)

    doc.close()
    return img_paths

def ensamblar_imagenes_a_pdf(imagenes, salida_pdf):
    imagenes_pil = [Image.open(img).convert("RGB") for img in imagenes]
    imagenes_pil[0].save(salida_pdf, save_all=True, append_images=imagenes_pil[1:])
    print(f"📄 PDF ensamblado desde imágenes: {salida_pdf}")

def comprimir_con_ghostscript(entrada, salida):
    comando = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dColorImageDownsampleType=/Bicubic",
        "-dColorImageResolution=72",
        "-dGrayImageDownsampleType=/Bicubic",
        "-dGrayImageResolution=72",
        "-dMonoImageDownsampleType=/Subsample",
        "-dMonoImageResolution=72",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={salida}",
        entrada
    ]
    subprocess.run(comando, check=True)
    print(f"✅ PDF final comprimido con Ghostscript: {salida}")

def compresion_extrema_ultra(pdf_entrada):
    print("🧨 Convirtiendo PDF a imágenes JPEG escala de grises...")
    imagenes = convertir_paginas_a_imagenes(pdf_entrada)

    ensamblado = "pdf_imagenes.pdf"
    comp_final = "comprimido_ultra.pdf"

    print("🧩 Ensamblando imágenes a PDF...")
    ensamblar_imagenes_a_pdf(imagenes, ensamblado)

    print("📦 Aplicando compresión final con Ghostscript...")
    comprimir_con_ghostscript(ensamblado, comp_final)

    print("🧹 Limpiando archivos temporales...")
    os.remove(ensamblado)
    for img in imagenes:
        os.remove(img)
    os.rmdir("paginas")

    print(f"🎯 PDF final ultra-comprimido: {comp_final}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python comprimir_pdf_ultra.py archivo.pdf")
    else:
        compresion_extrema_ultra(sys.argv[1])
