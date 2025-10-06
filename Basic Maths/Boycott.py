if __name__ == "__main__":
    matches = 300
    times_started = 280
    times_not_out = 25
    goals_scored =168

    batting_average = goals_scored / (times_started - times_not_out)

    print(f"Mr Larousse Isaac's average goal per game {batting_average:.2f}.")