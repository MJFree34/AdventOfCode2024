def parse_input(file_path):
    reports = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(' ')
            reports.append([int(x) for x in parts])
    
    return reports

def is_monotonic_within_range(report):
    increasing = all(-3 <= report[i] - report[i + 1] < 0 for i in range(len(report) - 1))
    decreasing = all(0 < report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def check_report(report):
    if is_monotonic_within_range(report):
        return True

    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1:]
        if is_monotonic_within_range(temp_report):
            return True

    return False

if __name__ == "__main__":
    file_path = 'day2/input.txt'
    reports = parse_input(file_path)

    safe_reports_count = 0
    for report in reports:
        if check_report(report):
            safe_reports_count += 1

    print(safe_reports_count)