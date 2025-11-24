#!/usr/bin/env python3
"""在 docs 目录中旋转 PDF"""
from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_name = "wise研助.pdf"
pdf_path = Path(__file__).parent / pdf_name

print(f"处理文件: {pdf_path}")
print(f"文件存在: {pdf_path.exists()}")

if not pdf_path.exists():
    print("错误: 文件不存在")
    exit(1)

reader = PdfReader(str(pdf_path))
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    writer.add_page(page.rotate(90))
    print(f"已旋转第 {i+1} 页")

temp_path = pdf_path.with_suffix('.tmp.pdf')
with open(temp_path, 'wb') as f:
    writer.write(f)

temp_path.replace(pdf_path)
print("✓ 成功旋转 PDF")
