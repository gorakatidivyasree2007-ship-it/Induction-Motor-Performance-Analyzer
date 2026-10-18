frequency = float(input("Supply frequency (Hz): "))
poles = int(input("Number of poles: "))
rotor_speed = float(input("Rotor speed (RPM): "))

if frequency <= 0 or poles <= 0 or poles % 2 != 0:
    print("Enter valid frequency and pole count")
else:
    ns = 120 * frequency / poles
    slip = (ns - rotor_speed) / ns * 100

    print("Synchronous speed:", ns, "RPM")
    print("Rotor speed:", rotor_speed, "RPM")
    print("Slip:", round(slip, 2), "%")
