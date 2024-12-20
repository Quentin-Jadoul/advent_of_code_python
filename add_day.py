import os
import sys

def add_day(year, day):
    year_dir = str(year)
    src_dir = os.path.join(year_dir, "src")
    data_dir = os.path.join(year_dir, "data")

    # Create year directory structure if it does not exist
    if not os.path.exists(year_dir):
        os.makedirs(src_dir)
        os.makedirs(data_dir)
        print(f"Created structure for year {year}")

    day_src_file = os.path.join(src_dir, f"day_{day:02d}.py")
    day_data_file = os.path.join(data_dir, f"day_{day:02d}.txt")

    if not os.path.exists(day_src_file) and not os.path.exists(day_data_file):
        with open(day_data_file, "w") as f:
            f.write("# Add your puzzle input here\n")
        with open(day_src_file, "w") as f:
            f.write(
                f'"""Solution for Day {day} of {year}"""\n\n'
                f"import sys\n"
                f"import os\n\n"
                f"sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))\n"
                f"from utils import time_and_print, read_input_file\n\n"
                f"def parse_input():\n"
                f'    content = read_input_file("{year}/data/day_{day:02d}.txt")\n'
                f'    return content\n\n'
                f"def part1():\n    pass\n\n"
                f"def part2():\n    pass\n\n"
                f'if __name__ == "__main__":\n'
                f'    time_and_print(part1, "Part 1")\n'
                f'    time_and_print(part2, "Part 2")\n'
            )
        print(f"Created structure for Day {day:02d} in year {year}")
    else:
        print(f"Day {day:02d} in year {year} already exists.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_day.py <year> <day>")
    else:
        try:
            year = int(sys.argv[1])
            day = int(sys.argv[2])
            if 1 <= day <= 25:
                add_day(year, day)
            else:
                print("Day number must be between 1 and 25.")
        except ValueError:
            print("Please provide valid numeric arguments for year and day.")