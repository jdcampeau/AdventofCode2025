input_file = "day1.1input.txt"

count = 50
passcode = 0

try:
    with open(input_file, 'r') as file:
        for line in file:
            clean_line = line.strip()
            direction = clean_line[0]
            distance_str = clean_line[1:]
            distance = int(distance_str)
            if direction == "R":
                count += distance
                while count > 99:
                    count -= 100
                if count == 0:
                    passcode += 1
            else:
                count -= distance
                while count < 0:
                    count += 100
                if count == 0:
                    passcode += 1

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Passcode: {passcode}")
