fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange"
}
fruits["kiwi"] = "green"
color_banana = fruits["banana"]
fruits["apple"] = "green"
del fruits["banana"]
print(f"{fruits}")