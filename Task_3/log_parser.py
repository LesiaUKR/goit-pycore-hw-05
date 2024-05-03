import re
from prettytable import PrettyTable

LOG_TYPES = {"INFO", "ERROR", "DEBUG", "WARNING"}


def parse_log_line(line: str) -> dict:
    log = {}
    line = line.strip()
    pattern = re.compile(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|DEBUG|ERROR|WARNING) (.+)")
    match = re.match(pattern, line)
    if match:
        log['timestamp'] = match.group(1)
        log['level'] = match.group(2)
        log['message'] = match.group(3)
    return log


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            log = parse_log_line(line)
            if log:
                logs.append(log)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list(filter(lambda log: log['level'] == level, logs))
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    counts_logs_by_level = {}
    for level in LOG_TYPES:
        counts_logs_by_level[level] = len(filter_logs_by_level(logs, level))
    return counts_logs_by_level


def display_log_counts(counts: dict):
    table = PrettyTable(['Level', 'Amount'])
    for level, amount in counts.items():
        table.add_row([level, amount])

    print(table)


def display_filtered_logs(filtered_logs: list):
    print("Details for filtered logs:")
    table = PrettyTable(['Timestamp', 'Message'])
    for log in filtered_logs:
        table.add_row([log['timestamp'], log['message']])
    print(table)  # Виводимо таблицю деталей для вказаного рівня лог
