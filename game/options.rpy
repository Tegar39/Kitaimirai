## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' are comments, and you shouldn't delete them.
## Lines with a single '#' are commented-out code, which you can uncomment if needed.


## Basics ######################################################################

## The human-readable name of the game. This is used to set the window title,
## and is also displayed in the interface and error reports.
##
## The _() around the string marks it as translatable.

define config.name = _("Kitaimirai: The Future We Hope For")
define build.itch_project = "tgsoft/kitaimirai-the-future-we-hope-for"


## Determines whether the title given above is shown on the main menu.
## Set this to False to hide the title.

define gui.show_name = False


## Game version.

define config.version = "demo"


## Text that is placed on the about screen. Place the text between the triple
## quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
A visual novel about promises, lost memories, and the future we hope for.

Developed by TG'Soft.
""")


## A short name for the game used for executables and directories in the
## built distributions. This must only contain ASCII characters, and must not
## contain spaces, commas, or quotes.

define build.name = "Kitaimirai"


## Sound and music #############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or music channel,
## uncomment the line below and set it to a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set the audio file that will be played on the
## main menu. This file will continue playing until the game starts, is stopped,
## or another file is played.

define config.main_menu_music = "audio/bgm/kitaimirai instrument.mp3"
define main_menu_voice = "audio/sfx/kitaimirai.mp3"


## Transitions #################################################################

## These variables set the transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## Transition that is used after the game is loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game ends.

define config.end_game_transition = None


## Variables to set transitions used when starting the game are not available.
## Instead, use the with statement after showing certain screens.


## Window management ###########################################################

## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is available. If
## "auto", the window is hidden before scene statements and shown again when
## dialogue is displayed.
##
## After the game starts, this can be changed with the "window show", "window
## hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window.

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Default preferences #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to display.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to a longer wait, with
## 0 to 30 being the valid range.

default preferences.afm_time = 15


## Save directory #############################################################

## Controls where the save files for this game are placed on each platform.
## The files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Kitaimirai-1767095818"


## Icon ########################################################################

## The icon shown on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build settings #############################################################

## This section controls how Ren'Py transforms your project into distribution
## files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and are matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ## In a pattern:
    ##
    ## / Is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the build distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.jpeg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.mp4', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')

    ## Documentation files matching patterns are duplicated in the Mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## Google Play license key required for in-app purchases.
## This key can be found in the Google Play Developer Console, under
## "Monetization" > "Monetization Setup" > "License".

# define build.google_play_key = "..."


## The username and project name associated with the itch.io project,
## separated by a slash.

# define build.itch_project = "tgsoft/kitaimirai"