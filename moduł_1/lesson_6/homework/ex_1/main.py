import speed_calc

distance = float(input("Jaką odległość pokonałeś w km? "))
time = float(input("Ile czasu Ci to zajęło w h? "))

speed = speed_calc.speed(distance, time)
print(f"Twoja średnia prędkość to {speed}km/h.")

