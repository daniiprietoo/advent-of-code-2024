def main():
    data: list[list[str]] = []

    with open('data.txt', 'r') as file:
        for line in file:
            report: list[int] = line.strip().split(" ")
            reports.append(report)

    # sol: int = len(reports) - calculate_unsafe_reports(reports)
    # print(sol)