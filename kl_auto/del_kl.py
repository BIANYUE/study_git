with open('xh.txt', 'r') as file:
    # 逐行读取文件内容
    for line in file.readlines():
        # 处理每一行数据
        print(line.strip())
        with open('啊哈加速器.txt', 'a', encoding='utf-8') as f:
            f.write(
                "啊哈加速器" + "\t" + "3" + "\t" + "OTHER" + "\t" + "TLS" + "\t" + line.strip() + "\t" +
                "TCP" + "\t" + "443" + "\t" + "443" + "\n")