# -*- coding: utf-8 -*-
"""
第 1 周 · 第一个脚本：文本文件统计器
------------------------------------------------
用途：读取一个文本文件，统计字数、行数、字符数，并打印结果。
这是 12 周 FDE 学习方案的第一个产出物——不求功能多，只求走完
「写 → 跑 → 改 → 提交 Git」的完整闭环。

用法：
    python week1_text_stats.py <文件路径>
    python week1_text_stats.py samples/sample_sop.txt
"""

import os
import sys


def read_text(path: str) -> str:
    """读取文本文件内容。显式用 utf-8，避免 Windows 下中文乱码。"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_stats(text: str) -> dict:
    """统计字数、行数、字符数。

    注意区分三个口径：
    - 字符数 len(text)：包含空格、换行、标点
    - 非空字符数：去掉所有空白后剩下的字符
    - 行数：按换行符切分后，非空行的数量
    """
    lines = text.splitlines()
    non_empty_lines = [ln for ln in lines if ln.strip()]
    chars_no_space = "".join(text.split())

    return {
        "行数（总）": len(lines),
        "行数（非空）": len(non_empty_lines),
        "字符数（含空白）": len(text),
        "字符数（去空白）": len(chars_no_space),
    }


def print_report(path: str, stats: dict) -> None:
    """把统计结果打印成一份可读的报告。"""
    print("=" * 44)
    print("文本文件统计报告")
    print("=" * 44)
    print(f"文件路径：{path}")
    print("-" * 44)
    for key, value in stats.items():
        print(f"{key:<14}：{value}")
    print("=" * 44)


def main() -> int:
    # 1. 检查参数。没给路径就直接告诉用户怎么用，而不是抛一个看不懂的堆栈。
    if len(sys.argv) < 2:
        print("参数不足。用法：")
        print("    python week1_text_stats.py <文件路径>")
        return 1

    path = sys.argv[1]

    # 2. 检查文件是否存在。异常要给出人能看懂的信息。
    if not os.path.exists(path):
        print(f"找不到文件：{path}")
        print("请确认路径是否正确（Windows 路径含反斜杠时记得加引号）。")
        return 1

    if os.path.isdir(path):
        print(f"这是一个文件夹，不是文件：{path}")
        return 1

    # 3. 真正的逻辑：读 → 算 → 打印
    try:
        text = read_text(path)
    except UnicodeDecodeError:
        print(f"文件编码无法识别（不是 utf-8）：{path}")
        print("试试用编辑器的「另存为」把编码改成 UTF-8。")
        return 1

    stats = count_stats(text)
    print_report(path, stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
