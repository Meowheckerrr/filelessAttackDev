import wmi

# 創建 WMI 客戶端
c = wmi.WMI()

# 查詢所有進程並獲取 CommandLine 屬性
processes = c.Win32_Process()

# 過濾並顯示包含 'cmd.exe' 的行
for process in processes:
    if process.CommandLine and 'cmd.exe' in process.CommandLine.lower():
        print(process.CommandLine)