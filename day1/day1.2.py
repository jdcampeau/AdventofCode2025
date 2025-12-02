#solution not found yet. Answer should be less than 7260 and greater than 5999. Unclear what the issue is.

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
                buffer = 0
                while count > 99: 
                    buffer += 1
                    count -= 100
                if count == 0:
                    passcode += (buffer - 1)
                else:
                    passcode += buffer
            else:
                count -= distance
                while count < 0:
                    passcode += 1  
                    count += 100
                if count == 0:
                    passcode += 1

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Passcode: {passcode}")
