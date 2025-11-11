
# The following lines were added by compinstall

zstyle ':completion:*' completer _complete _ignored
zstyle :compinstall filename '/home/Khaos/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfiles/zsh
HISTSIZE=1000
SAVEHIST=1000
setopt extendedglob
bindkey -v
# End of lines configured by zsh-newuser-install

# pnpm
export PNPM_HOME="/home/Khaos/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

export PAGER='less -R'
export LESS=-S
export REDISCLI_HISTFILE=~/.histfiles/valkey-cli

alias cat='bat'
alias ls='lsd --group-directories-first'
alias grep='grep --color=auto'
alias resource='source ~/.zshrc'
alias vim='nvim'
alias vi='nvim'
alias v='nvim'
alias dotfiles='/usr/bin/git --git-dir="$HOME/Projects/.dotfiles" --work-tree="$HOME"'
alias neofetch=fastfetch
alias btw='neofetch'
alias blender='blender-3.6'
alias feh='feh -Tu'
alias yay='paru'
alias steam='steam_clean_home'
alias protontricks-games='HOME=/home/Games protontricks'
alias btw='fastfetch'
alias pj='projects'
alias fehclip='xclip -selection clipboard -t image/png -o > /tmp/clip.png && feh /tmp/clip.png'
alias wrangler='wrangler2'

alias gestures='fd -t d -i "pole |pole$|daily" -0 | xargs -0 -P0 -n1 -I{} feh -Tu {}'

eval "$(starship init zsh)"

ping () {
if [ $# -eq 0 ]; then
  if ping -c1 -q 1.1.1.1 &>/dev/null; then
    echo pong
  else
    exit 1;
  fi
else
  command ping "$@"
fi
}

