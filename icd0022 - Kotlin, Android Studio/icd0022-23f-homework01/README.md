$$
\Large Karl \: Müllerbeck
$$
$$
Student \: code: \: 223231IADB
$$
$$
School \: email: \: kmulle@taltech.ee
$$
$$
UNI-ID: \: kmulle
$$
- https://en.wikipedia.org/wiki/15_Puzzle

Support rotation (landscape/portrait) correctly (shifting around UI components, not just scaling) 
and state save/restore.

Run timer in background sevice, 
use broadcasts for communication.

Divide screen into 2 sections, gameboard and statistics. 
Show move count, 
time spent (suspend timer when ui is not visible).  
Support at least 2 steps of undo.

UI made out of buttons, movement solved with changing text/images on buttons (but you are welcomed to use animations, etc).

Support native color schema (dark/light).

Support both full random shuffeling of board (sometimes not solvable) 
and solvable shuffeling (ie starting from solved board make x random legal moves).

Use ConstraintLayout for everything, use includes for shared components.

Test UI layout (and make it nice) on all possible screen sizes/densities and positions.

No warnings in Android Studio layout editor!