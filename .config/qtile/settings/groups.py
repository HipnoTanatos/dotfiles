from libqtile.config import Group

class Icons:
    lambda_ = "󰘧"
    haskell = ""
    atom = "" 
    fingerprint = ""
    a1 = ""
    a2 = ""
    toxic = ""
    insomnia = ""

icon = Icons.haskell
groups = []
total_groups = 5

for i in range(total_groups):
    groups.append(Group(name=str(i+1), label=icon)) # label=names_groups[i]
