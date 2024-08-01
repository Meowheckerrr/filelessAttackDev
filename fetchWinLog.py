import win32evtlog
import win32evtlogutil

def read_sysmon_logs():
    log_type = 'Microsoft-Windows-Sysmon/Operational'
    server = 'localhost'  # 本地计算机
    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    print(f"Total number of records: {total}")

    events = win32evtlog.ReadEventLog(hand, flags, 0)

    for event in events:
        if event.EventID == 1:  # Sysmon Event ID 1 is process creation
            print(f"Event Category: {event.EventCategory}")
            print(f"Time Generated: {event.TimeGenerated}")
            print(f"Source Name: {event.SourceName}")
            print(f"Event ID: {event.EventID}")
            print(f"Event Type: {event.EventType}")
            print(f"Event Data: {event.StringInserts}")

    win32evtlog.CloseEventLog(hand)

if __name__ == "__main__":
    read_sysmon_logs()