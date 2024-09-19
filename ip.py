def IP(string, i, count, sofar, n):
    if i == n and count == 4:
        print(sofar[:-1])  # Remove the trailing dot
        return
    if i >= n or count >= 4:
        return
    for j in range(i, min(i+3, n)):
        part = string[i:j+1]
        if (len(part) > 1 and part[0] == '0') or int(part) > 255:
            break
        IP(string, j+1, count+1, sofar + part + ".", n)

# IP("25525511135", 0, 0, "", len("25525511135"))
# IP("0000", 0, 0, "", len("0000"))

# Test cases
def run_test_cases():
    test_cases = [
        "25525511135",  
        "0000",         
        "1111",         
        "010010",       
        "101023",       
        "0279245587303", 
        "000000000000",  
        "111111111111",  
        "255255255255",  
        "123456789",     
        "1",             
        "12345",         
    ]

    for case in test_cases:
        print(f"Testing: {case}")
        IP(case, 0, 0, "", len(case))
        print("---")

if __name__ == "__main__":
    run_test_cases()