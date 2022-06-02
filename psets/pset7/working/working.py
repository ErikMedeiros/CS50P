# https://cs50.harvard.edu/python/2022/psets/7/working/

from re import fullmatch


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_regex = r"([1-9]|1[0-2])(?::([0-5][0-9]))? ((?:A|P)M)"

    if match := fullmatch(rf"{time_regex} to {time_regex}", s):
        start = convert_time(*match.groups()[0:3])
        end = convert_time(*match.groups()[3:6])

        return f"{start} to {end}"
    else:
        raise ValueError


def convert_time(hours, minutes, period):
    hours = int(hours)

    if minutes:
        minutes = int(minutes)
    else:
        minutes = 0

    factor = period == "PM"
    factor = int(factor) if hours != 12 else int(not factor)

    return f"{(hours + 12 * factor) % 24:02}:{minutes:02}"


if __name__ == "__main__":
    main()
