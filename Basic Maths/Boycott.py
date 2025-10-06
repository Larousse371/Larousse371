if __name__ == "__main__":
    matches = 400
    times_batted = 360
    times_not_out = 80
    runs_scored =500

    batting_average = runs_scored / (times_batted - times_not_out)

    print(f"Sir Geoffrey Boycott's Batting Average is {batting_average:.2f}.")