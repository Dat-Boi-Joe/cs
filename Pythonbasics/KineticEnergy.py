# In physics, an object that is in motion is said to have kinetic energy. The following formula can
# be used to determine a moving object’s kinetic energy:
# KE=12mv2
# The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass in
# kilograms, and v is the object’s velocity in meters per second.
# Write a function named kinetic_energy that accepts an object’s mass (in kilograms) and
# velocity (in meters per second) as arguments. The function should return the amount of kinetic
# energy that the object has. Write a program that asks the user to enter values for mass and
# velocity, then calls the kinetic_energy function to get the object’s kinetic energy.

def main():
    print('This program will help you calculate KE or kinetic energy!')
    mass = float(input('Enter mass in kilograms: '))
    velocity = float(input('Enter velocity in meters per second: '))
    answer = kinetic_energy(mass, velocity)
    print('KE =', answer, 'Joules')


def kinetic_energy(m, v):
    answer = (1 / 2) * m * (v ** 2)
    return answer


main()
