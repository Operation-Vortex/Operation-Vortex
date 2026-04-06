import random
from datetime import datetime, timedelta


def generate_fake_log_lines(total_lines):
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    endpoints = [
        "/api/users",
        "/api/orders",
        "/api/products",
        "/api/login",
        "/api/logout",
        "/api/payments",
        "/api/reports",
        "/api/profile",
    ]
    status_codes = [200, 201, 400, 401, 403, 404, 500]
    start_time = datetime(2025, 3, 30, 0, 0, 0)

    for _ in range(total_lines):
        current_time = start_time + timedelta(
            seconds = random.randint(0, 86399)
        )
        ip_address = f"192.168.131.{random.randint(0, 50)}"
        method = random.choice(methods)
        endpoint = random.choice(endpoints)
        status_code = random.choice(status_codes)
        response_time = f"{random.uniform(0.001, 2.000):.3f}"

        log_line = (
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"{ip_address} "
            f"{method} "
            f"{endpoint} "
            f"{status_code} "
            f"{response_time}"
        )

        yield log_line


def write_fake_log_file(filename, total_lines):
    with open(filename, "w") as file:
        for log_line in generate_fake_log_lines(total_lines):
            file.write(log_line + "\n")


write_fake_log_file("server.log", 100_000)
print("Done. 100,000 log lines written.")