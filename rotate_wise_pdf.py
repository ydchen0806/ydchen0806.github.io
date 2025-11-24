#!/usr/bin/env python3
"""
旋转 wise研助.pdf 文件
"""
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import os

# 获取脚本所在目录
script_dir = Path(__file__).parent.absolute()
pdf_path = script_dir / "docs" / "wise研助.pdf"

print(f"脚本目录: {script_dir}")
print(f"正在处理: {pdf_path}")
print(f"绝对路径: {pdf_path.absolute()}")
print(f"文件是否存在: {pdf_path.exists()}")

if not pdf_path.exists():
    print(f"错误: 文件不存在")
    exit(1)

try:
    # 读取 PDF
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    
    print(f"PDF 页数: {len(reader.pages)}")
    
    # 旋转每一页（顺时针90度）
    for i, page in enumerate(reader.pages):
        rotated_page = page.rotate(90)
        writer.add_page(rotated_page)
        print(f"已旋转第 {i+1} 页")
    
    # 写入临时文件
    temp_path = pdf_path.with_suffix('.tmp.pdf')
    with open(temp_path, 'wb') as output_file:
        writer.write(output_file)
    
    # 替换原文件
    temp_path.replace(pdf_path)
    print(f"✓ 成功旋转 PDF: {pdf_path}")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
