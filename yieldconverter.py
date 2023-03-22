# Conversion rates
ACRE_TO_HECTARE = 0.404686
BUSHELS_PER_BAG = 3
KILOGRAMS_PER_BUSHEL = 27.2155
KILOGRAMS_PER_TONNE = 1000

# Weight kg per bushel THIS ISN'T IN THE CODE YET
WHEAT = 27.22
BARLEY = 21.77
CORN = 25.40
CANOLA = 22.68
LENTILS = 27.22

# Crop type
crop_type = input("What is the crop type you want to convert? wheat, barley, corn, canola or lentils: ").lower()
# Original unit
original_unit = input("What unit are you converting from? (Ba)gs (Bu)shels (T)onnes: ").lower()
original_area = input("What unit of area are you converting from? (Ac)res (H)ectares: ").lower()

# Converted unit
desired_unit = input("What unit are you converting to? (Ba)gs (Bu)shels (T)onnes: ").lower()
desired_area = input("What unit of are are you converting to? (Ac)res (H)ectares: ").lower()

# Input number
original_value = float(input("Enter the number of {0} per {1}: "))

# Convert to T ha
if original_unit == "ba" or "bags":
    kilograms_per_bag = BUSHELS_PER_BAG * KILOGRAMS_PER_BUSHEL
    kilograms_per_hectare = (original_value * kilograms_per_bag) / (ACRE_TO_HECTARE)
    original_value = kilograms_per_hectare / KILOGRAMS_PER_TONNE
elif original_unit == "bu" or "bushels":
    kilograms_per_bushel = KILOGRAMS_PER_BUSHEL
    kilograms_per_hectare = (original_value * kilograms_per_bushel) / (ACRE_TO_HECTARE)
    original_value = kilograms_per_hectare / KILOGRAMS_PER_TONNE
elif original_unit == "t" or "tonnes":
    original_value = original_value

# Convert SOMETHING IS WRONG HERE
if desired_unit == "ba" or "bags":
    kilograms_per_bag = BUSHELS_PER_BAG * KILOGRAMS_PER_BUSHEL
    kilograms_per_hectare = original_value * KILOGRAMS_PER_TONNE * ACRE_TO_HECTARE
    desired_value = kilograms_per_hectare / kilograms_per_bag
elif desired_unit == "bu" or "bushels":
    kilograms_per_bushel = KILOGRAMS_PER_BUSHEL
    kilograms_per_hectare = original_value * KILOGRAMS_PER_TONNE * ACRE_TO_HECTARE
    desired_value = kilograms_per_hectare / kilograms_per_bushel
elif desired_unit == "t" or "tonnes":
    desired_value = original_value

# Convert area
if original_area != desired_area:
    if original_area == "acres":
        desired_value *= ACRE_TO_HECTARE
    else:
        desired_value /= ACRE_TO_HECTARE

# Print
print("{0:.2f} {1} per {2} is equivalent to {3:.2f} {4} per {5}.".format(original_value, original_unit, original_area, desired_value, desired_unit, desired_area))
