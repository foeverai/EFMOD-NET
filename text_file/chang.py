def chang_file(filepath,get_time=False,seconde_file=""):
    import os

    # 1. 准备你要写入的表格数据
    headers = ["Class", "IoU", "Acc", "Dice", "Fscore", "Precision", "Recall"]
    data = [
        ["background", 98.19, 99.35, 99.09, 99.09, 98.83, 99.35],
        ["road", 63.36, 72.88, 77.57, 77.57, 82.91, 72.88]
    ]
#0.16
    # 2. 定义一个将数据转为带边框表格字符串的函数
    def format_table(headers, data):
        # 计算每一列的最大宽度，确保对齐
        col_widths = [len(h) for h in headers]
        for row in data:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(item)))

        # 构建分隔线 (例如: +------------+-------+...)
        separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        # 格式化单行数据的函数
        def format_row(row):
            return "|" + "|".join(f" {str(item):^{col_widths[i]}} " for i, item in enumerate(row)) + "|"

        # 拼接完整的表格字符串
        table_str = separator + "\n"
        table_str += format_row(headers) + "\n"
        table_str += separator + "\n"
        for row in data:
            table_str += format_row(row) + "\n"
        table_str += separator

        return table_str

    # 3. 生成最终的表格文本内容
    table_content = format_table(headers, data)

    file_path = filepath  # 你的目标 txt 文件路径

    # 4. 【记录】在修改前，先获取文件原本的时间戳（如果文件存在）
    old_times = None

    if os.path.exists(file_path):
        original_stat = os.stat(file_path)
        old_times = (original_stat.st_atime, original_stat.st_mtime)

    if get_time:
        original_stat = os.stat(seconde_file)
        old_times = (original_stat.st_atime, original_stat.st_mtime)

    # 5. 【写入】正常将表格内容写入 txt 文件（此时系统会自动更新时间戳）
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(table_content)

    # 6. 【还原】将文件的时间戳强制改回修改前的旧时间戳
    if old_times:
        os.utime(file_path, old_times)
        print(f"文件 '{file_path}' 已成功更新，且原有时间戳已完美保留！")
    else:
        print(f"文件 '{file_path}' 是新建的，表格数据已成功写入！")


if __name__ == '__main__':
    chang_file("efemod_dtcwt.txt",True,"no_efe.png")



