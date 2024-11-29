def statistika(*args, operacija="suma"):
    if operacija == "suma":
        rezultatas = sum(args)
    elif operacija == "min":
        rezultatas = min(args)
    elif operacija == "max":
        rezultatas = max(args)
    elif operacija == "average":
        rezultatas = sum(args) / len(args)
    return rezultatas
