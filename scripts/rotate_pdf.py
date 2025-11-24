#!/usr/bin/env python3
"""
旋转 PDF 文件的脚本
"""
import sys
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("错误: 需要安装 pypdf 或 PyPDF2 库")
        print("运行: pip install pypdf")
        sys.exit(1)


def rotate_pdf(input_path, output_path=None, rotation=90):
    """
    旋转 PDF 文件
    
    参数:
        input_path: 输入 PDF 文件路径
        output_path: 输出 PDF 文件路径（如果为 None，则覆盖原文件）
        rotation: 旋转角度（90 = 顺时针90度，-90 = 逆时针90度，180 = 180度，270 = 顺时针270度）
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"错误: 文件不存在: {input_path}")
        return False
    
    if output_path is None:
        # 覆盖原文件，先保存到临时文件
        temp_path = input_path.with_suffix('.tmp.pdf')
        output_path = temp_path
    else:
        output_path = Path(output_path)
    
    try:
        # 读取 PDF
        reader = PdfReader(str(input_path))
        writer = PdfWriter()
        
        # 旋转每一页
        for page in reader.pages:
            rotated_page = page.rotate(rotation)
            writer.add_page(rotated_page)
        
        # 写入输出文件
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        # 如果输出到临时文件，则替换原文件
        if output_path.suffix == '.tmp.pdf':
            temp_path.replace(input_path)
            print(f"✓ 成功旋转 PDF: {input_path}")
        else:
            print(f"✓ 成功旋转 PDF: {input_path} -> {output_path}")
        
        return True
        
    except Exception as e:
        print(f"错误: 旋转 PDF 时出错: {e}")
        # 清理临时文件
        if output_path.exists() and output_path.suffix == '.tmp.pdf':
            output_path.unlink()
        return False


def main():
    if len(sys.argv) < 2:
        print("用法: python rotate_pdf.py <pdf_file> [rotation_angle]")
        print("   rotation_angle: 旋转角度（默认90，顺时针）")
        print("                   90 = 顺时针90度")
        print("                   -90 = 逆时针90度")
        print("                   180 = 180度")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    rotation = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    
    success = rotate_pdf(pdf_path, rotation=rotation)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
