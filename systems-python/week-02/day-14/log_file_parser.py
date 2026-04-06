from collections import Counter


def analyze_log_file(filename):
    ip_counts = Counter()
    error_by_hour = Counter()

    slowest_time = 0.0
    slowest_endpoint = ""

    with open(filename, "r") as file:
        for current_line_under_iteration in file:
            parts = current_line_under_iteration.strip().split()

            if len(parts) != 7:
                print("Skipping malformed line:", current_line_under_iteration)
                continue

            date = parts[0]
            time = parts[1]
            ip_address = parts[2]
            method = parts[3]
            endpoint = parts[4]
            status_code = parts[5]
            response_time = float(parts[6])

            # count IP
            ip_counts[ip_address] += 1

            # error by hour (4xx + 5xx)
            if status_code.startswith("4") or status_code.startswith("5"):
                hour = time.split(":")[0]
                error_by_hour[hour] += 1

            # slowest endpoint
            if response_time > slowest_time:
                slowest_time = response_time
                slowest_endpoint = endpoint

    return ip_counts, error_by_hour, slowest_endpoint, slowest_time


def print_results(ip_counts, error_by_hour, slowest_endpoint, slowest_time):
    print("\nTOP 10 IP ADDRESSES")
    for ip, count in ip_counts.most_common(10):
        print(ip, "->", count)

    print("\nERRORS BY HOUR")
    for hour in sorted(error_by_hour):
        print(hour + ":00", "->", error_by_hour[hour])

    print("\nSLOWEST ENDPOINT")
    print("Endpoint:", slowest_endpoint)
    print("Time:", slowest_time)


def run():
    ip_counts, error_by_hour, slowest_endpoint, slowest_time = analyze_log_file("server.log")
    print_results(ip_counts, error_by_hour, slowest_endpoint, slowest_time)


run()