def decode_message(in_str):
    if len(in_str) > 100:    # Check the length of the message
        print("Error, message is too long.")
        return False
    
  
    marks = [" ", ",", ";", "."]    # The marks that can include in the message
    all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    str = ""
    for char in in_str:    # Check the marks and characters of the message
        if char not in marks and char.lower() not in all_letters:
            str = str + char
            
    if str != '':
        print(f"Error, incorrect characters: {str}")
        return False
    
    abcd_list = []  # Check "a", "b", "c", "d" in the message
    new_in_str = in_str.lower().replace("buzz" ,"")    # Remove "buzz" in the message in cass "b" of "buzz" presents an arrow
    for char in new_in_str.lower():
        if char == "a":
            abcd_list.append(0) # Present "a" to 0 in the end of message
        elif char == "b":
            abcd_list.append(180)   # Present "b" to 180 in the end of message
        elif char == "c":
            abcd_list.append(270)   # Present "c" to 270 in the end of message
        elif char == "d":
            abcd_list.append(90)    # Present "d" to 90 in the end of message
            
    new_abcd_list = []  # Check "fizz", "buzz" in the message"
    fizz = in_str.lower().find("fizz")
    buzz = in_str.lower().find("buzz")
    if fizz != -1 and buzz != -1:
        for i in abcd_list:
            new_abcd_list.append(i + 270)   # Turn all the arrow to 180 + 90 = 270
    elif buzz != -1:
        for i in abcd_list:
            new_abcd_list.append(i + 90)    # Turn all the arrow to 90
    elif fizz != -1:
        for i in abcd_list:
            new_abcd_list.append(i + 180)   # Turn all the arrow to 180
    else:
        new_abcd_list = abcd_list
        
    str = ""    # Turn new_abcd_list to arrow
    for i in new_abcd_list:
        if i % 360 == 0:
            str = str + "↑" # 0 presents "↑"
        elif i % 360 == 180:
            str = str + "↓" # 180 presents "↓"
        elif i % 360 == 90:
            str = str + "→" # 90 presents "→"
        elif i % 360 == 270:
            str = str + "←" #270 presents "←"
    print(f"Instructions: {str}")
    
    a = new_abcd_list.count(0)
    b = new_abcd_list.count(180)
    c = new_abcd_list.count(270)
    d = new_abcd_list.count(90)
    
    concise = [c-d, a-b]    # Concise the arrow: c-d concises "←" and "→"; a-b concises "↑" and "↓"
    result = ""
    if concise[0] > 0:
        result += "←" * concise[0]
    elif concise[0] < 0 :
        result += "→" * abs(concise[0])
    elif concise[1] > 0:
        result += "↑" * concise[1]
    elif concise[1] < 0:
        result += "↓" * abs(concise[1])
    print(f"Concise instructions: {result}")
    
# For automatic test, DO NOT REMOVE
in_str = input()
decode_message(in_str) 