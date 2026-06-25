def chang_file(filepath,get_time=False,seconde_file=""):
    import os

    file_path = filepath  # 你的目标 txt 文件路径
    time_file = seconde_file

    # 4. 【记录】在修改前，先获取文件原本的时间戳（如果文件存在）
    old_times = None

    if os.path.exists(time_file):
        original_stat = os.stat(time_file)
        old_times = (original_stat.st_atime, original_stat.st_mtime)

    # 【还原】将文件的时间戳强制改回修改前的旧时间戳
    if old_times:
        os.utime(file_path, old_times)
        print(f"文件 '{file_path}' 已成功更新")



if __name__ == '__main__':
    chang_file("with_dtc.png",True,"20251119_112454.log")



