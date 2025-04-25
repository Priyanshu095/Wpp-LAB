def convert_length(feet, choice):
    # Conversion factors
    conversions = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
    units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

    if 1 <= choice <= 7:
        result = feet * conversions[choice - 1]
        print(f"{feet} feet is equal to {result:.4f} {units[choice - 1]}.")
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

# Get user input
feet = float(input("Enter length in feet: "))
print("Choose a conversion:")
print("1. Inches\n2. Yards\n3. Miles\n4. Millimeters\n5. Centimeters\n6. Meters\n7. Kilometers")
choice = int(input("Enter your choice (1-7): "))

convert_length(feet, choice)