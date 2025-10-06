if __name__ == "__main__":
    name = input("Good Evening, what is your full name? ")

    current_year = int(input("What year is it in 10 years "))
    birth_year = int(input("What year was you born in? "))

    age = current_year - birth_year

    print(f"Hello, {name}! In 10 years you will be {age} years old!")