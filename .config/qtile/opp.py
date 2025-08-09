import toml
from libqtile.lazy import lazy

@lazy.function
def opacity_up(qtile, n: int):
    n = round(n/100, 3)
    change_opacity(n)

@lazy.function
def opacity_down(qtile, n: int):
    n = round(n/100*-1, 3)
    change_opacity(n)

def change_opacity(n: float):
    with open('/home/HipnoTanatos/.config/alacritty/alacritty.toml', 'r') as file:
        data = toml.load(file)
    data['window']['opacity'] = round((data['window']['opacity']) + n, 3)
    if data['window']['opacity'] < 0:
        data['window']['opacity'] = 0
    elif data['window']['opacity'] > 1:
        data['window']['opacity'] = 1
    with open('/home/HipnoTanatos/.config/alacritty/alacritty.toml', 'w') as file:
        toml.dump(data, file)
    return data

def main():
    opacity_down(n=1)

if __name__ == "__main__":
    main()

