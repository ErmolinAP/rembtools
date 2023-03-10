import datetime


def dt_convert(string):
    local_time_from_iso = datetime.datetime.fromisoformat(string)

    return str(local_time_from_iso.date())+ " "+ str(local_time_from_iso.time())

print(dt_convert("2023-01-17T08:30:00.000+10:00"))


