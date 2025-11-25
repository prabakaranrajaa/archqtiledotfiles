# --- First add /etc/zsh/zprofile
# add this line --> export ZDOTDIR="$HOME/.config/zsh"   

# enable command-not-found (Arch uses pkgfile)
if [ -f /usr/share/doc/pkgfile/command-not-found.zsh ]; then
    source /usr/share/doc/pkgfile/command-not-found.zsh
fi



# main zsh settings. env in ~/.zprofile
# read second
export PATH="$HOME/.local/bin:$PATH"

#setopt autocd

# ~/.bashrc
export TERM="xterm-256color"

setopt autocd              # change directory just by typing its name
#setopt correct            # auto correct mistakes
setopt interactivecomments # allow comments in interactive mode
setopt magicequalsubst     # enable filename expansion for arguments of the form ‘anything=expression’
setopt nonomatch           # hide error message if there is no match for the pattern
setopt notify              # report the status of background jobs immediately
setopt numericglobsort     # sort filenames numerically when it makes sense
setopt promptsubst         # enable command substitution in prompt

# -------------------- Shell Behavior --------------------
# Command behavior and convenience
setopt autocd                     # Automatically change directories when typing a path
setopt autopushd                  # Push directory onto the stack with cd
setopt no_clobber                 # Prevent overwriting files with >
setopt complete_in_word           # Autocomplete within a word
setopt extended_glob              # Enable advanced globbing features
setopt correct                    # Attempt to auto-correct commands

# Prompt and other tweaks
setopt no_beep                    # Disable terminal beep on error
setopt prompt_subst               # Enable dynamic prompt evaluation
setopt interactive_comments       # Allow comments (#) in interactive shells
setopt no_flow_control            # Disable Ctrl+S and Ctrl+Q flow control

WORDCHARS=${WORDCHARS//\/} # Don't consider certain characters part of the word

# hide EOL sign ('%')
PROMPT_EOL_MARK=""

# configure key keybindings
bindkey -e                                        # emacs key bindings
bindkey ' ' magic-space                           # do history expansion on space
bindkey '^U' backward-kill-line                   # ctrl + U
bindkey '^[[3;5~' kill-word                       # ctrl + Supr
bindkey '^[[3~' delete-char                       # delete
bindkey '^[[1;5C' forward-word                    # ctrl + ->
bindkey '^[[1;5D' backward-word                   # ctrl + <-
bindkey '^[[5~' beginning-of-buffer-or-history    # page up
bindkey '^[[6~' end-of-buffer-or-history          # page down
bindkey '^[[H' beginning-of-line                  # home
bindkey '^[[F' end-of-line                        # end
bindkey '^[[Z' undo                               # shift + tab undo last action


# -------------------- History Settings --------------------
HISTFILE="${XDG_CACHE_HOME:-$HOME/.cache}/zsh_history" # move histfile to cache
HISTSIZE=100000                   # Number of commands to keep in memory
SAVEHIST=100000                   # Number of commands to save in the history file

setopt append_history             # Append new history to the file, rather than overwriting
setopt inc_append_history         # Save each command to the history file as it's entered
setopt share_history              # Share history across all Zsh sessions
setopt hist_ignore_all_dups       # Remove all duplicate commands from the history
setopt hist_ignore_dups           # Ignore consecutive duplicates
setopt hist_ignore_space          # Ignore commands that start with a space
setopt hist_verify                # Verify history commands before executing


# enable completion features
autoload -Uz compinit
compinit -d ~/.cache/zcompdump
zstyle ':completion:*:*:*:*:*' menu select
zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' rehash true
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# -------------------- FZF Setup --------------------
# fzf setup
source <(fzf --zsh) # allow for fzf history widget
bindkey '^R' fzf-history-widget

# Syntax highlighting
if [ -f /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]; then
    source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
fi

# Autosuggestions
if [ -f /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
    ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#999'
    ZSH_AUTOSUGGEST_STRATEGY=(history completion)
fi

# Bind autosuggestions only in vi insert mode
bindkey -M viins '^e' autosuggest-accept
bindkey -M viins '^w' autosuggest-execute
bindkey -M viins '^t' autosuggest-toggle

# zsh-vi-mode configuration
#ZVM_LINE_INIT_MODE=insert        # start in insert mode
ZVM_VI_INSERT_ESCAPE_BINDKEY=jj  # use 'jj' to leave insert mode
ZVM_INIT_MODE=sourcing           # faster startup
ZVM_PROMPT_SYMBOLS=(INSERT:NORMAL)

# Load zsh-vi-mode
if [ -f /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh ]; then
    source /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh
fi


# You may need to manually set your language environment
# -------------------- Environment --------------------
export LANG=en_US.UTF-8

# -------------------- History Filter --------------------
# Only save successful commands
function zshaddhistory() {
# Remove line continuations for cleaner history
LASTHIST=${1//\\\\$\'\\n\'/}
# Return 2 to save to internal history but not write to file
return 2
}

    function precmd() {
        # Write the last command if successful
        if [[ $? == 0 && -n ${LASTHIST//[[:space:]\\n]/} && -n $HISTFILE ]] ; then
            print -sr -- ${=${LASTHIST%%\'\\n\'}}
        fi
    }

# -------------------- Git Aliases --------------------
# Core Git Aliases
alias gi="git init"                  # Initialize a new Git repository
alias gib="git init --bare"          # Create a bare Git repository
alias ga="git add ."                 # Stage all changes
alias gadd="git add"                 # Add specific files to the staging area
alias gc="git commit -m"             # Commit changes with a message
alias gca="git commit -a -m"         # Commit all changes with a message
alias gst="git status"               # Show the status of the repository
alias gsr="git status -s"            # Show a summarized status of the repository
alias gl="git log"                   # Display commit logs
alias glog="git log --graph --topo-order --pretty='%w(100,0,6)%C(yellow)%h%C(bold)%C(black)%d %C(cyan)%ar %C(green)%an%n%C(bold)%C(white)%s %N' --abbrev-commit" # Graphical log
alias glpr="git log --pretty=format:\"%C(yellow)%h%Creset - %Cred%d%Creset %s %C(bold green)(%cr)%Creset %C(blue)<%an>\"" # Pretty log format
alias gdiff="git diff"               # Show changes between commits, branches, or working trees

# Branch Management
alias gb="git branch"                # List local branches
alias gba="git branch -a"            # List all branches, including remote ones
alias gcb="git checkout -b"          # Create and switch to a new branch
alias gch="git checkout"             # Switch to another branch
alias gcoall="git checkout -- ."     # Discard changes to all tracked files
alias grb="git branch -d"            # Delete a local branch

# Remote and Merging
alias gr="git remote"                # Manage set of tracked repositories
alias grmt="git remote -v"           # List remote repositories with URLs
alias grso="git remote show origin"  # Show detailed info about the remote 'origin'
alias gm="git merge"                 # Merge the specified branch
alias gpoa="git push -u origin --all" # Push all local branches to remote 'origin'
alias gp="git push origin HEAD"      # Push the current branch to remote 'origin'
alias gpu="git pull origin"          # Pull the latest changes from remote 'origin'

# Reset and Checkout
alias gre="git reset"                # Reset the current HEAD to a specific state
alias gco="git checkout"             # Checkout a branch or paths to the working tree


# -------------------- Docker Aliases --------------------
# Docker Compose Aliases
alias dco="docker compose"     # Simplified 'docker compose' command

# General Docker Aliases
alias dk="docker"                     # Shortcut for Docker command
alias dr="docker run"                 # Run a Docker container
alias drit="docker run -it"           # Run a container interactively
alias dritrm="docker run -it --rm"    # Run and auto-remove a container after exit

# Container Management Aliases
alias dps="docker ps"                 # List running containers
alias dpa="docker ps -a"              # List all containers, including stopped ones
alias dl="docker ps -l -q"            # Get the last used container's ID
alias dpss="docker ps -s"             # Show container sizes
alias dx="docker exec -it"            # Execute commands inside a running container

# Image Management Aliases
alias dimg="docker images"            # List all Docker images
alias drmi="docker rmi"               # Remove a specific image
alias drmiall="docker rmi -f \$(docker images -q)" # Force remove all images

# Container Start/Stop Aliases
alias dstart="docker start"           # Start a stopped container
alias dstop="docker stop"             # Stop a running container
alias drm="docker rm"                 # Remove a specific container
alias drmall="docker rm -f \$(docker ps -a -q)" # Force remove all containers

# Volume Management Aliases
alias dvc="docker volume create"      # Create a new Docker volume
alias dvls="docker volume ls"         # List all Docker volumes
alias dvrm="docker volume rm"         # Remove a specific Docker volume


# -------------------- Tools & Utilities --------------------
alias cl="clear"
alias http="xh"
alias mat='tmux neww "cmatrix"'
#alias mat='osascript -e "tell application \"System Events\" to key code 126 using {command down}" && tmux neww "cmatrix"'


# -------------------- Eza Aliases --------------------
# File system
if command -v eza &> /dev/null; then
  alias ls='eza -lh --group-directories-first --icons=auto'
  alias lsa='ls -a'
  alias lt='eza --tree --level=2 --long --icons --git'
  alias lta='lt -a'
fi

alias ff="fzf --preview 'bat --style=numbers --color=always {}'"

# -------------------- Bat as Cat --------------------
# Replace `cat` with `bat` for better file preview
alias cat="bat"                            # Use bat as a replacement for cat

# -------------------- Yazi Integration --------------------
#yazi command
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

# ---- Zoxide (better cd) ----
eval "$(zoxide init zsh)"
alias cd="z"

n() { if [ "$#" -eq 0 ]; then nvim .; else nvim "$@"; fi; }

# -------------------- Directory Shortcuts --------------------
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."

alias yt='qutebrowser --set tabs.show never --set window.hide_decoration true --target window https://www.youtube.com'
alias fb='qutebrowser --set tabs.show never --set window.hide_decoration true --target window https://www.facebook.com'
alias ins='qutebrowser --set tabs.show never --set window.hide_decoration true --target window https://www.instagram.com'
alias wa='qutebrowser --set tabs.show never --set window.hide_decoration true --target window https://web.whatsapp.com'

# -------------------- Fastfetch Banner --------------------
#fastfetch | lolcat

# -------------------- Fastfetch Banner --------------------
if [[ -z "$FASTFETCH_SHOWN" ]]; then
    FASTFETCH_SHOWN=1
    fastfetch
fi


# -------------------- Shell Switching --------------------
# switch between shells
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
#alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"

# -------------------- Powerlevel10k --------------------
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.config/zsh/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.config/zsh/.p10k.zsh.
[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh

