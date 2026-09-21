from seven_segment import segment_map

digit = int(input("Enter a digit (0-9): "))

if digit in segment_map:
    segments = segment_map[digit]

    print()
    print("  " + ("---" if segments[0] else "   "))
    print(" " + ("|" if segments[5] else " ") + "   " + ("|" if segments[1] else " "))
    print("  " + ("---" if segments[6] else "   "))
    print(" " + ("|" if segments[4] else " ") + "   " + ("|" if segments[2] else " "))
    print("  " + ("---" if segments[3] else "   "))

else:
    print("Invalid input. Please enter a digit from 0 to 9.")