def to_display_time(time):
    time_seconds = float(time)
    hours = int(time_seconds / 3600000.0)
    str_hours = ""
    if hours > 9:
        str_hours = str(100 + hours)
        str_hours = str_hours[1:3] + ":"
    elif hours > 0:
        str_hours = str(hours) + ":"

    minutes = int((time_seconds - (3600000.0 * hours)) / 60000.0)
    str_minutes = str(100 + minutes)
    seconds = int((time_seconds - (3600000.0 * hours) - (60000.0 * minutes)) / 1000.0)
    str_seconds = str(100 + seconds)
    to_time = str_hours + str_minutes[1:3] + ":" + str_seconds[1:3]
    return to_time


def to_srt_time(time):
    time_seconds = float(time)
    hours = int(time_seconds / 3600000.0)
    str_hours = str(100 + hours)
    minutes = int((time_seconds - (3600000.0 * hours)) / 60000.0)
    str_minutes = str(100 + minutes)
    seconds = int((time_seconds - (3600000.0 * hours) - (60000.0 * minutes)) / 1000.0)
    str_seconds = str(100 + seconds)
    milliseconds = int(time_seconds - (3600000.0 * hours) - (6000 * minutes) - seconds)
    str_milliseconds = str(1000 + milliseconds)
    to_time = (
        str_hours[1:3]
        + ":"
        + str_minutes[1:3]
        + ":"
        + str_seconds[1:3]
        + ","
        + str_milliseconds[1:4]
    )
    return to_time
