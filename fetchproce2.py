import wmi

# 創建 WMI 客戶端
c = wmi.WMI()

# 查詢所有進程並獲取 CommandLine 和 CreationDate 屬性
processes = c.Win32_Process()

# 根據 CreationDate 排序並顯示最近一筆資料
if processes:
    sorted_processes = sorted(processes, key=lambda p: p.CreationDate, reverse=True)
    latest_process = sorted_processes[0]
    print(f"CommandLine: {latest_process.CommandLine}")
    print(f"CreationDate: {latest_process.CreationDate}")
else:
    print("No processes found.")