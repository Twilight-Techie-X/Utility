from datetime import timedelta

def read_lines(source_file):
    """Read all lines from the source file."""
    with open(source_file, 'r') as file:
        return file.readlines()

def add_seconds(time_str, add_sec):
    """Add seconds to a given time string."""
    hours, minutes, seconds = [0] * 3
    time_parts = list(map(int, time_str.split(':')))

    if len(time_parts) == 3:
        hours, minutes, seconds = time_parts
    else:
        minutes, seconds = time_parts

    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds + add_sec)
    total_seconds = int(time_delta.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"

def format_time_part(time_part):
    """Format time part (hours, minutes, seconds) into SRT time format."""
    hours, minutes, seconds = [0] * 3
    time_parts = list(map(int, time_part[:-1].split(':')))
    
    if len(time_parts) == 3:
        hours, minutes, seconds = time_parts
    else:
        minutes, seconds = time_parts
    
    return f"{hours:02}:{minutes:02}:{seconds:02},000"

def format_sub(current, next_sub):
    """Format subtitle with time range and subtitle text."""
    current_time = format_time_part(current[0])
    next_time = format_time_part(next_sub[0])
    return f"{current_time} --> {next_time}\n{current[1]}"

def append_file(source_file, destination_file):
    """Append subtitle information from source file to destination SRT file."""
    lines = read_lines(source_file)

    with open(destination_file, 'w') as dest:
        dest.write("")

    with open(destination_file, 'a') as dest:
        index = 1
        current_line = 0

        while current_line < len(lines) - 1:
            if current_line < len(lines) - 3:
                current = [lines[current_line], lines[current_line + 1]]
                next_sub = [lines[current_line + 2], lines[current_line + 3]]
            else:
                current = [lines[current_line], lines[current_line + 1]]
                next_time = add_seconds(lines[current_line], 10)
                next_sub = [next_time, ""]

            formatted_sub = format_sub(current, next_sub)
            dest.write(f"{index}\n")
            dest.write(formatted_sub + "\n")
            index += 1
            current_line += 2

# File paths
source_file = 'input.txt'
destination_file = 'output.txt'

# Append file
append_file(source_file, destination_file)

print(f"Lines from {source_file} have been appended to {destination_file}.")
