def calculate_unsafe_reports(data: list[list[int]]) -> int:
    unsafe_count: int = 0

    for report in data:
        level_distance: int = report[1] - report[0]
        if level_distance == 0:
            unsafe_count += 1
            continue

        is_increasing: bool = level_distance > 0

        for i in range(len(report) - 1):
            step: int = report[i + 1] - report[i]
            if abs(step) > 3 or step == 0:
                unsafe_count += 1
                break
            if (step > 0) != is_increasing:
                unsafe_count += 1
                break     
            
    return unsafe_count

def is_safe(report: list[int]) -> bool:
    level_distance: int = report[1] - report[0]
    if level_distance == 0:
        return False
    
    is_increasing: bool = level_distance > 0

    for i in range(len(report) - 1):
        step: int = report[i + 1] - report[i]
        if abs(step) > 3 or step == 0 or (step > 0) != is_increasing:
            return False
        
    return True

def calculate_safe_reports(data):
    safe_count: int = 0

    for report in data:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range (len(report)):
                modified_report: list[int] = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_count +=1 
                    break
                
    return safe_count


def main():
    reports: list[list[int]] = []

    with open('data.txt', 'r') as file:
        for line in file:
            report: list[int] = [int(num) for num in line.strip().split(" ")]
            reports.append(report)

    # sol: int = len(reports) - calculate_unsafe_reports(reports)
    # print(sol)

    print(calculate_safe_reports(reports))

if __name__ == '__main__':
    main()