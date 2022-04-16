output_buf = []

def main():
    Test_cases = int(input()) # Get Number of test cases
    test_case(Test_cases)
    print_output(Test_cases) # print values if done

def test_case(n):
    if n == 0:
        return 0
    num = int(input()) # Get Total Numbers to be entered 
    value_str = input() # Get the actual Numbers to be squared
    values = value_str.split()
    
    output_buf.insert(0, square(num, values)) # insert the answer at index zero.
    test_case(n-1)

def square(n, values):
    if n == 0:
        return 0
    value = int(values[n-1])
    if value < 0:
        return square(n-1, values)
    return value**2 + square(n-1, values)

def print_output(n):
    if n == 0:
        return
    print(output_buf[n-1])
    print_output(n-1)

if __name__ == "__main__":
    main()
