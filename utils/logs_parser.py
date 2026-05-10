def collect_logs():
    logs = {}
    logs["system"] = open("test_logs/system.log")
    logs["workload"] = open("test_logs/workload.log")
    return logs
