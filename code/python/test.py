def compare_files(file1_path, file2_path):
    # 读取两个文件的内容
    with open(file1_path, 'r') as file1:
        lines1 = set(line.strip() for line in file1.readlines())
    with open(file2_path, 'r') as file2:
        lines2 = set(line.strip() for line in file2.readlines())
    
    # 找出文件之间的差异
    only_in_file1 = lines1 - lines2  # 只在 file1 中的行
    only_in_file2 = lines2 - lines1  # 只在 file2 中的行
    
    return only_in_file1, only_in_file2

# 示例调用
file1 = r'D:\work\data lake\test\2024\11\11-25\235.21\export_jilian_tags.txt'
file2 = r'D:\work\data lake\test\2024\11\11-25\235.21\vxbasetags.txt'
differences = compare_files(file1, file2)
print("Only in file1 size[{0}]: {1}".format(len(differences[0]), differences[0]))
print("Only in file2 size[{0}]: {1}".format(len(differences[1]), differences[1]))
# print("Only in file2:", differences[1])
