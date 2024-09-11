def read_lines(source_file):
    with open(source_file, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
        return lines

from datetime import timedelta

def add_seconds(time_str, add_sec):
    temp = list(map(int, time_str.split(':')))
    minutes = temp[-2]
    seconds = temp[-1]
    hours = temp[-3] if len(temp) == 3 else 0
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds + add_sec)
    total_seconds = int(time_delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    return f"{hours:02}:{minutes:02}:{seconds:02}\n"

def format_sub(current, next):
    current_time = current[0]
    temp = list(map(int, current_time[:-1].split(':')))
    current_time = f'0{temp[-3] if len(temp) == 3 else '0'}:{temp[-2] if temp[-2] > 9 else f'0{temp[-2]}'}:{temp[-1] if temp[-1] > 9 else f'0{temp[-1]}'},000'
    current_sub = current[1]
    next_time = next[0]
    temp = list(map(int, next_time[:-1].split(':')))
    next_time = f'0{temp[-3] if len(temp) == 3 else '0'}:{temp[-2] if temp[-2] > 9 else f'0{temp[-2]}'}:{temp[-1] if temp[-1] > 9 else f'0{temp[-1]}'},000'
    formatted_time = f"{current_time} --> {next_time}\n"
    # formatted_time = "00:0"+current_time[:-1]+",000 --> 00:0"+next_time[:-1]+",000"+"\n"
    print(formatted_time + current_sub)
    return formatted_time + current_sub

def append_file(source_file, destination_file):   
    # line_number = 1
    lines = read_lines(source_file)

    with open(destination_file, 'w') as dest:
        dest.write("")

    with open(destination_file, 'a') as dest:
         i = 1
        #  count = 0
         current_line = 0
         while(current_line < len(lines)-1):
            if(0 <= current_line < len(lines)-3):
                current = [lines[current_line], lines[current_line + 1]]
                next = [lines[current_line + 2], lines[current_line + 3]]
            else:
                current = [lines[current_line], lines[current_line + 1]]
                next_time = add_seconds(lines[current_line], 10)
                next = [next_time, ""]

            specific_line = format_sub(current, next)

            dest.writelines([str(i)+"\n"])
            dest.writelines(specific_line+"\n")
            i += 1
            current_line += 2
            # count += 2


source_file = 'input.txt'

destination_file = 'output.srt'

append_file(source_file, destination_file)

print(f"Lines from {source_file} have been appended to {destination_file}.")