class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit
        self.to_inches_factor = {
            "inches": 1, "feet": 12, "yards": 36, "miles": 63360,
            "millimeters": 0.0393701, "centimeters": 0.393701,
            "meters": 39.3701, "kilometers": 39370.1
        }
        if unit not in self.to_inches_factor:
            raise ValueError(f"Unsupported unit: {unit}")
        self.length_in_inches = length * self.to_inches_factor[unit]

    def to_feet(self):
        return self.length_in_inches / 12

    def to_meters(self):
        return self.length_in_inches / 39.3701

    def convert_to_all(self):
        return {unit: self.length_in_inches / factor for unit, factor in self.to_inches_factor.items()}

    def __str__(self):
        return f"{self.length} {self.unit} is equivalent to {self.length_in_inches} inches"

# Get user input
try:
    length = float(input("Enter the length: "))
    unit = input("Enter the unit (inches, feet, yards, miles, millimeters, centimeters, meters, kilometers): ").lower()
    c = Converter(length, unit)
    print(c.to_feet())  # Output in feet
    print(c.to_meters())  # Output in meters
    print(c.convert_to_all())  # Output conversion to all units
    print(c)  # Output original length in inches
except ValueError as e:
    print(e)