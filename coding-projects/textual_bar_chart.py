from rich import print

class_size = {
    "Period 1": 25,
    "Period 2": 37,
    "Period 3": 20,
    "Period 4": 30,
    "Period 5": 26,
    "Period 6": 15,
}

marker = "#"
largest_class = max(class_size.values())
total_width = len("Period x: ") + largest_class
title = "Class Size by Period".center(total_width)

print()
print(f"[b][#c678dd]{title}[/#c678dd][/b]")
print("=" * total_width, end="\n\n")

for label, data in class_size.items():
    print(f"[#98be65]{label}[/#98be65]: [#51afef]{marker*(data)}[/#51afef]")
