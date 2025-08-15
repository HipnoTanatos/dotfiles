# - HipnoTanatos Dotfiles -
Repository with my personal config and scripts for my work environment.

## Content
- General user-wide system configuration
- Custom scripts for System/Project management
- A minimal yet powerfull and nice-looking visual configuration

## Components
- Arch Linux
- xorg
- pipewire
- qtile
- picom
- alacritty
- sddm

I chose **Xorg** as the display server for compatibility and the ability to fine-tune configurations. **PipeWire** unifies audio and video, which is especially useful for streaming or virtual cameras over a local network. **Qtile** was chosen as the window manager for its high flexibility and scripting capabilities; exploring tiled windows has been an interesting experience, probably a one-way trip at this point. **Picom** is very lightweight on resources and flexible to configure, without sacrificing compatibility or visually appealing effects. I use **Alacritty** as my terminal emulator is extremely fast and efficient. Tmux is almost indispensable with this terminal, especially for long sessions or complex projects, as it integrates really well. For the **greeter**, I chose SDDM just to test QML for now, but honestly, any greeter would do the job. And of course, I chose Arch Linux ~~for its simplicity, minimalism, and full control over the system.~~ btw.<br>
All components were selected to keep the setup minimal while allowing maximum granular configuration.

## Instalation
Simply clone this repo in your home directory for a complete installation, or manually copy the different modules that compose the repo into your .config/ directory

```bash
git clone git@github.com:HipnoTanatos/dotfiles.git ~/
```

## Updating
Run `sudo pacman -Syu`, or `yay` if using AUR packages, to update, after that `dotfiles pull` to update the configs.

## Usage
### Basic Keybinds:
- `Mod` + `M` - Application Launcher
- `Mod` `Shift` + `M` - Window Switcher
- `Mod` + `#` - Switch to workspace `#`
- `Mod` `Shift` + `#` - Move window to workspace `#`
- `Mod` +`Tab` - Switch monitor focus
- `Mod` + `Enter` - Open terminal
- `Mod` `Shift` + `Enter` - Open Python terminal
- `Mod` + `B` - Open browser
- `Mod` + `E` - Open file browser
- `Mod` `Shift` + `Q` - Log out
- `Mod` `Shift` + `R` - Restart Window Manager

# Installed Software
#### Administration
udisks2 -- disk management daemon<br>
networkmanager -- network connection management daemon<br>
inetutils -- basic networking utilities<br>
zsh -- advanced shell<br>
openssh -- secure shell access (SSH client/server)<br>
openvpn -- vpn client/server daemon<br>
btop -- resource monitor


#### Utilities
paru -- AUR helper<br>
bat -- enhaced cat clone<br>
lsd -- ls replacement<br>
fd -- faster find alternative<br>
fzf -- command-line fuzzy finder<br>
tmux -- terminal multiplexer<br>
xclip -- X11 clipboard access from terminal<br>
rofi -- application launcher and window switcher<br>
keepassxc -- password manager with database encryption<br>
playerctl -- control media players that implement MPRIS<br>
maim -- take screenshots<br>
ueberzug -- image preview in terminal (used with ranger)<br>
rclone -- sync files from/to cloud storage<br>
rsync -- remote file sync tool<br>
syncthing -- p2p file synchronization<br>
dbeaver -- graphical database administration tool<br>
libmypaint -- mypaint brush engine (used in krita)<br>
xdotools -- X11 scripting handler<br>
tesseract-data[spa|eng] -- optical character recognition


#### Analysis
wireshark -- network packet analyzer<br>
ghidra -- reverse engineering tool<br>
virtualbox -- X86 virtualizer for VMs<br>
tinyxxd -- create hexadecimal dump of binaries<br>
ipython -- python command shell for interactive computing


#### Terminal based applications
nvim -- powerful text editor<br>
ranger -- file manager<br>
zathura -- document viewer<br>
zathura-pdf-mupdf -- mupdf backend (PDF/EPUB support)<br>
mpv -- media player with scripting support<br>
feh -- simple fast image viewer<br>
7zip -- file archiver<br>
wget -- retrive files using common network protocols<br>
fastfetch -- system information tool


#### Graphical based applications
obsidian -- markdown-based note-taking/viewer<br>
firefox -- web browser<br>
krita -- digital painting<br>
inkscape -- vector graphics editor<br>
blender-3.6-bin -- 3D creation suite<br>
stremio -- media streaming hub<br>
kotatogram -- telegram fork<br>
gpick


#### Gaming
discord -- VoIP platform<br>
steam -- game store and launcher<br>
wine -- windows compatibility layer<br>
winetricks -- windows libraries on Wine<br>
protonup-qt -- graphical tool for manage compatibility tools (Proton-GE in this case)<br>
proton-GE -- community's custom version of proton<br>
protontricks -- windows libraries on proton (steam)


#### System Components
xorg -- X11 display server<br>
pipewire -- audio and video server<br>
pipewire-pulse -- pulse audio api for pw<br>
wireplumber -- PipeWire session manager<br>
qtile -- tiling window manager<br>
picom -- X11 compositor<br>
alacritty -- GPU-accelerated terminal<br>
sddm -- QML based display manager


#### Dev Tools
base-devel -- general build tools such as compiler, utilities, etc<br>
git -- version control system<br>
nodejs -- js runtime environment<br>
npm -- Node.js package manager<br>
jdk-openjdk -- Open-Source implementation of JDK<br>
drawio-desktop -- diagram/flowchart editor<br>
graphviz -- tool for drawing graph visualization using dot-lang<br>
docker -- container engine for isolated app environments<br>
the_silver_searcher -- code-oriented faster ack/grep alternative<br>
uv -- Python packet manager<br>
python-pynvim -- python provider for nvim<br>
python-pyqt5 -- python bindings for qt5 (i use this for scripting in krita)
cmake<br>
tree -- directory listing display deep indented list of files (i use this for documentation)


#### Database Server
postgresql -- advanced object-relational database system<br>
mariadb -- relational database server<br>
valkey -- in-memory key-value distributed cache and message broker


#### Fonts
noto-fonts -- sans/serif, wide language support<br>
noto-fonts-cjk -- chinese, japanese and korean support<br>
ttf-jetbrains-mono-nerd -- JetBrains Mono with Nerd Fonts glyphs<br>
ttf-hack -- Hack with programming ligatures<br>
ttf-dejavu -- broad Unicode coverage, good for fallback<br>
ttf-liberation -- metric-compatible with microsoft core fonts
