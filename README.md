Flappy Clone
Slam Jones 2022

Practice project for familiarity with Python and game development
in general.

Should function similarly to the game from which is it cloned:
"bird" (player character) moves forward constantly, player hits 
spacebar to move bird upwards; otherwise the bird moves downwards.  
If bird comes into contact with a column or either edge of the 
screen, it is considered a Game Over.  Score (columns passed
successfully) is counted in upper-right corner of the screen.

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

"Demo Mode" is not hooked up yet.  "Demo Mode" pervents user input
during game, instead allowing the pc to control the bird.  Need 
to allow pc to "see" next column and attempt to move upwards or
downwards to pass through column successfully.

-- Move settings to discrete file for better accessability?
