
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


export PAGER=less
export LESS=-S
export REDISCLI_HISTFILE=~/.histfiles/valkey-cli

alias cat='bat'
alias ls='lsd --group-directories-first'
alias grep='grep --color=auto'
alias resource='source ~/.zshrc'
alias vim='nvim'
alias vi='nvim'
alias dotfiles='/usr/bin/git --git-dir="$HOME/Projects/.dotfiles" --work-tree="$HOME"'
alias btw='neofetch'
alias blender='blender-3.6'
alias feh='feh -Tu'
alias yay='paru'
alias steam='steam_clean_home'
alias protontricks-games='HOME=/home/Games protontricks'
alias pj='projects'
alias btw='fastfetch'
