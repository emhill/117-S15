---
title: "Customize your Terminal"
published: true
morea_id: unix-custom
morea_summary: "Setup so we can all use the same command to open our python programs"
morea_type: experience
morea_sort_order: 3
morea_labels:
 - due 2/2
---
# Terminal Customization
<!--*Customize your terminal so we can all open our editors from the command line with the same command.*-->

The following tutorial will setup an alias, ped, that you can type on the command line to open your editor of choice directly from the terminal.

## Mac

1. Open your terminal and type `ls -a`
1. If there is no file named .bash_profile, type `touch .bash_profile`
1. Open this .bash_profile file in your editor: `open -a textwrangler .bash_profile`
1. Add the following line to your .bash_profile: `alias ped='open -a textwrangler`
1. Save the file, close the terminal, & reopen the terminal
1. Try it out by typing `ped`

## Windows

1. Open your terminal and type `ls -a`
1. Open .bashrc file in your editor: `gedit .bash_profile &`
1. Add the following line to your .bashrc if it's not there already: `alias ped='gedit &'`
1. Save the file, close the terminal, & reopen the terminal
1. Try it out by typing `ped`