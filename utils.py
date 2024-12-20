# utils.py
import time

def time_and_print(func, func_name):
    start_time = time.time()
    result = func()
    end_time = time.time()
    print(f"{func_name}:", result)
    print(f"⏰ Time taken for {func_name}:", round(end_time - start_time, 5), "seconds")

def read_input_file(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()