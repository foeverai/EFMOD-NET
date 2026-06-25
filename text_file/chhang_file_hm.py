def function(file_path):
    import os
    from datetime import datetime, timedelta

    # 1. 准备表格数据
    headers = ["Class", "IoU", "Acc", "Dice", "Fscore", "Precision", "Recall"]
    data = [
        ["background", 97.24, 98.67,  98.6,  98.6, 98.53, 98.67],
        ["road", 63.58, 76.57, 77.74, 77.74, 77.61, 77.87]
    ]

    # 2. 格式化表格字符串的函数
    def format_table(headers, data):
        col_widths = [len(h) for h in headers]
        for row in data:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(item)))
        separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

        def format_row(row):
            return "|" + "|".join(f" {str(item):^{col_widths[i]}} " for i, item in enumerate(row)) + "|"

        table_str = separator + "\n" + format_row(headers) + "\n" + separator + "\n"
        for row in data:
            table_str += format_row(row) + "\n"
        table_str += separator
        return table_str

    table_content = format_table(headers, data)
    file_path = file_path

    # 3. 获取文件原本的时间戳
    if not os.path.exists(file_path):
        print(f"错误：文件 '{file_path}' 不存在，请先创建该文件。")
    else:
        original_stat = os.stat(file_path)
        old_atime = original_stat.st_atime
        old_mtime = original_stat.st_mtime

        # 4. 【核心步骤】在原修改时间的基础上增加指定的小时和分钟
        # 比如：增加 2 个小时 和 30 分钟
        add_hours = 0
        add_minutes = 1
        add_seconds = 15  # 新增的秒数

        # 将原来的时间戳转换为 datetime 对象
        original_datetime = datetime.fromtimestamp(old_mtime)
        # 使用 timedelta 进行时间加法运算
        new_datetime = original_datetime + timedelta(hours=add_hours, minutes=add_minutes, seconds=add_seconds)        # 将计算后的新时间转换回时间戳
        new_mtime = new_datetime.timestamp()

        print(f"原修改时间: {original_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"新修改时间: {new_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

        # 5. 写入文件内容（此时系统会生成一个当前时间的临时时间戳）
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(table_content)

        # 6. 【还原】将计算好的新时间戳（原时间+2小时30分）设置给文件
        # 这里我们保持访问时间(old_atime)不变，只更新修改时间(new_mtime)
        os.utime(file_path, (old_atime, new_mtime))
        print(f"文件 '{file_path}' 内容已更新，且修改时间已成功在原基础上增加了 {add_hours}小时{add_minutes}分{add_seconds}秒！")

if __name__ == '__main__':
    function("chn6.txt")