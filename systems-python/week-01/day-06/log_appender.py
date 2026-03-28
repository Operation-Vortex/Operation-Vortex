import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

log("Application started")
log("User logged in")
log("API call made")
log("Application stopped")

# Read and print the log
with open("app.log", "r") as f:
    print(f.read())