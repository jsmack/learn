call_count = 0

# CALL_COUNT = 0 #constant value

def print_count1():
    global call_count
    call_count += 1
    print(f"call_count: {call_count}")

def print_count2():
    global call_count
    call_count += 1
    print(f"call_count: {call_count}")

print_count1()
print_count2()
