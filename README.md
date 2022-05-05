Flappy Clone
Slam Jones 2022

Practice project for familiarity with Python and game development
in general.

Main loop updates as per settings["frame_rate"], which can be 
modified by user in-game using the Settings option from the
main menu.  Many other settings can be changed as well.

Columns are spawned every X frames, as determined by settings.
Columns consist of two parts: the full line that spans the height
of the screen, and a second, smaller line which is drawn on top
of the full line, which allows passage through by the user.

Every X columns, as defined in settings, several parameters are
increased, making the game progressively more difficult the longer
it is played.  Crashing or returning to the menu will reset the
parameters to their original values, as defined in Settings.

-- Move settings to discrete file for better accessability?
