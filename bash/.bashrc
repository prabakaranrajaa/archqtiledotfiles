#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# -------------------- Directory Shortcuts --------------------
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."

# -------------------- Tools & Utilities --------------------
alias v="nvim"
alias cl="clear"

# -------------------- Eza Aliases --------------------
alias l="eza -l --icons --git -a"                    # Detailed list with icons, git, and hidden files
alias lt="eza --tree --level=2 --long --icons --git" # Tree view, level 2, with icons and git
alias ltree="eza --tree --level=2 --icons --git"     # Tree view, level 2, with icons and git
alias ls="eza --icons"                               # Simple list with icons
alias ll="eza --long --icons"                        # Long list with icons
alias tree="eza --tree --icons"                      # Tree view with icons

# -------------------- Bat as Cat --------------------
# Replace `cat` with `bat` for better file preview
alias cat="bat"                            # Use bat as a replacement for cat



# -------------------- Shell Switching --------------------
# switch between shells
#alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"


PS1='[\u@\h \W]\$ '
