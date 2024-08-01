import win32evtlog

server = 'localhost'  # 或者指定远程服务器
logtype = 'System'    # 日志类型，例如 System, Application, Security


hand = win32evtlog.OpenEventLog(server, logtype)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)


