def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    prev_val = None
    
    while True:
        cur_val = int(input("Enter Value Here: "))
        
        if prev_val is None or cur_val <= prev_val:
            numbers.append(cur_val)
            prev_val = cur_val
        else:
            break
        
        
    
    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
