import re


def get_total_pause(pause_str):
    values = pause_str.split('+')
    total = 0
    for value in values:
        total = total + float(value)
    return total


def get_cpu_pause(pause_str):
    values = pause_str.split('/')
    result = []
    for value in values:
        pause = get_total_pause(value)
        result.append(pause)
    return result


def get_gc_pause(log_line):
    regex_str = r'gc\s([0-9]+)\s@([0-9]*[.][0-9]+)s.*%:\s([0-9.+]*)\sms\sclock,\s([0-9.+/]*)\sms\scpu'

    match_obj = re.match(regex_str, log_line, re.M | re.I)
    if match_obj:
        gc_pause = get_total_pause(match_obj.group(3))
        return gc_pause
    else:
        return None


def parse_gc_log(file_path):
    f = open(file_path)
    result = []
    for line in f:
        gc_pause = get_gc_pause(line)
        if gc_pause is not None:
            result.append(gc_pause)
    f.close()
    return result


def parse_gc_log_sorted(file_path):
    values = parse_gc_log(file_path)
    values.sort()
    return values
