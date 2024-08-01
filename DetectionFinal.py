import os
import time

duplicateRecords = set()

# 初始化一个空列表用于存储包含可疑调用方式的行
suspicious_lines = []
suspicious_invokes = [
    # Regsvr32.exe 调用方式
    "regsvr32",
    "C:\\Windows\\System32\\regsvr32.exe",
    ".\\regsvr32.exe",

    # Powershell.exe 调用方式
    "powershell",
    "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
    ".\\powershell.exe",

    # Cmd.exe 调用方式
    "cmd",
    "C:\\Windows\\System32\\cmd.exe",
    ".\\cmd.exe",

    # Mshta.exe 调用方式
    "mshta",
    "C:\\Windows\\System32\\mshta.exe",
    ".\\mshta.exe",

    # Winword.exe 调用方式
    "winword",
    "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    ".\\WINWORD.EXE",

    # Rundll32.exe 调用方式
    "rundll32",
    "C:\\Windows\\System32\\rundll32.exe",
    ".\\rundll32.exe"
]

while True: 
    # 执行 wmic 命令并获取输出
    output = os.popen('wmic process get commandline').read()

    # 将输出按行分割成列表
    lines = output.splitlines()

  
    # 遍历每一行
    for line in lines:
        # 初始化一个标志，表示是否发现可疑调用
        is_suspicious = False
        
        # 检查当前行是否包含任何一个可疑调用方式
        for invoke in suspicious_invokes:
            if invoke in line:
                is_suspicious = True
                break
        
        # 如果包含，将该行添加到 suspicious_lines 列表中
        if is_suspicious:
            processLine = line.replace('\n', ' ').replace('\r', ' ').strip()
            suspicious_lines.append(processLine)

            if processLine not in duplicateRecords:
                suspicious_lines.append(processLine)
                duplicateRecords.add(processLine)

    # 打印包含可疑调用方式的行
    for suspicious_line in suspicious_lines:
        print(suspicious_line)

    time.sleep(1)



# AI CHECK


