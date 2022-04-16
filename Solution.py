output_buf = []

def main():
    Test_cases = int(input()) # Insert test cases
    test_case(Test_cases)
    print_output(Test_cases)

def test_case(n):
    if n == 0:
        return 0
    num = int(input()) # Total Number
    value_str = input() # Numbers to be squared
    values = value_str.split()
    
    output_buf.insert(0, square(num, values))
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