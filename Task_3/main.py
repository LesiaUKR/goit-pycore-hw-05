import sys
from log_parser import *


def main():
    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) < 2:
        print(
            "Usage: python main.py /path/to/logfile.log [optional: log_level]")
        sys.exit(1)

    log_file = sys.argv[1]
    log_level = None
    if len(sys.argv) == 3:
        # Перетворюємо рівень логу в верхній регістр
        log_level = sys.argv[2].upper()

        # Перевірка чи вказаний рівень логу належить до переліку допустимих значень
        if log_level not in LOG_TYPES:
            print(
                "Error: log_level should be one of 'INFO', 'ERROR', 'DEBUG', 'WARNING'.")
            sys.exit(1)

    logs = load_logs(log_file)
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        display_log_counts(count_logs_by_level(logs))
        print("\nDetails for log level '{}':".format(log_level.upper()))
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
    else:
        display_log_counts(count_logs_by_level(logs))


if __name__ == "__main__":
    main()
