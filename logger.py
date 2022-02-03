from datetime import datetime


def _log_datetime():
    ts = datetime.now()
    timestamp = ts.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp


def log_response(response):
    timestamp = _log_datetime()
    response = str(response)
    log = f"Profile update initiated at: {timestamp} with a response of {response}"
    print(log)
    return log


def log_file(data: str):
    if type(data) == str:
        with open("log.txt", "a") as log:
            log.write(data)
        return
    else:
        print("log_file failed")
