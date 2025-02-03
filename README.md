Protontricks
============

[![image](https://img.shields.io/pypi/v/protontricks.svg)](https://pypi.org/project/protontricks/)
[![Coverage Status](https://coveralls.io/repos/github/nullorigin/protontricks/badge.svg?branch=main)](https://coveralls.io/github/nullorigin/protontricks?branch=main)
[![Test Status](https://github.com/nullorigin/protontricks/actions/workflows/tests.yml/badge.svg)](https://github.com/nullorigin/protontricks/actions/workflows/tests.yml)

[<img width="240" src="https://flathub.org/assets/badges/flathub-badge-en.png">](https://flathub.org/apps/details/com.github.nullorigin.protontricks)

Run Winetricks commands for Steam Play/Proton games among other common Wine features, such as launching external Windows executables.

# What is it?

This is a wrapper script that allows you to easily run Winetricks commands for Steam Play/Proton games among other common Wine features, such as launching external Windows executables. This is often useful when a game requires closed-source runtime libraries or applications that are not included with Proton.

# Requirements

* Python 3.6 or newer
* Winetricks
* Steam
* YAD (recommended) **or** Zenity. Required for GUI.

# Usage

**Protontricks can be launched from desktop or using the `protontricks` command.**

## Command-line

The basic command-line usage is as follows:

```
# Find your game's App ID by searching for it
protontricks -s <GAME NAME>

# or by listing all games
protontricks -l

# Run winetricks for the game.
# Any parameters in <ACTIONS> are passed directly to Winetricks.
# Parameters specific to Protontricks need to be placed *before* <APPID>.
protontricks <APPID> <ACTIONS>

# Run a custom command for selected game
protontricks -c <COMMAND> <APPID>

# Run the Protontricks GUI
protontricks --gui

# Launch a Windows executable using Protontricks
protontricks-launch <EXE>

# Launch a Windows executable for a specific Steam app using Protontricks
protontricks-launch --appid <APPID> <EXE>

# Print the Protontricks help message
protontricks --help
```

Since this is a wrapper, all commands that work for Winetricks will likely work for Protontricks as well.

If you have a different Steam directory, you can export ``$STEAM_DIR`` to the directory where Steam is.

If you'd like to use a local version of Winetricks, you can set ``$WINETRICKS`` to the location of your local winetricks installation.

You can also set ``$PROTON_VERSION`` to a specific Proton version manually. This is usually the name of the Proton installation without the revision version number. For example, if Steam displays the name as `Proton 5.0-3`, use `Proton 5.0` as the value for `$PROTON_VERSION`.

[Wanna see Protontricks in action?](https://asciinema.org/a/229323)

## Desktop

Protontricks comes with desktop integration, adding the Protontricks app shortcut and the ability to launch external Windows executables for Proton apps. To run an executable for a Proton app, select **Protontricks Launcher** when opening a Windows executable (eg. **EXE**) in a file manager.

The **Protontricks** app shortcut should be available automatically after installation. If not, you may need to run `protontricks-desktop-install` in a terminal to enable this functionality.

# Troubleshooting

For common issues and solutions, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

# Installation

You can install Protontricks with the included Makefile by running 'make install' from this README file's current directory. More options comming soon!
