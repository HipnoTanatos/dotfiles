from libqtile.config import Group

icon = ""
groups = []
total_groups = 5
names_groups = [
    "", "", "", "", "", "", "", "", ""
]
names_groups2 = [
    "", "", "󰈷", "󰺱", "a"
]

for i in range(total_groups):
    groups.append(Group(name=str(i+1), label=icon)) # label=names_groups[i]
