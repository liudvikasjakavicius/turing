# Enter/define the value of speed of light in meters per second that is around 300000000
speed_of_light = 300000000
# Create a function to calculate energy from mass
def calculate_energy(mass):
    energy = mass * speed_of_light**2
    return energy
# The main function
def main():
    print("Enter the mass in kilograms:")
    mass = int(input())
    energy = calculate_energy(mass)
    print(f"Equivalent energy in Joules: {energy}")
if __name__ == "__main__":
    main()