if __name__ == "__main__":
    distance = 150
    time = 120

    mph = distance / (time / 60)

    print(
        f"Travelling {distance} miles in {time} minutes is equivalent to {mph:.2f} mph."
    )