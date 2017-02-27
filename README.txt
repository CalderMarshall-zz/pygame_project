CONTROLS:
UP: FORWARD
DOWN: BACKWARD
LEFT: ROTATE LEFT 90dg
RIGHT: ROTATE RIGHT 90dg
S: SWITCH CONTROLLED CAR


My fist software project ever.  The idea was a parking game, where points were scored, and cars could move around.  This game was written after two weeks of intense python instruction at DigitalCrafts.  My vision for this game turned out to be a little ambitious considering how proficient I was in object oriented programming after two weeks on Python.  Nevertheless, the game does, work.  However, it is not really a game.  There is no way to win, and no points system was ever introduced.  I will go into further detail of the challenges I faced as a new programmer while trying to write my carpark game.

My original idea was to attempt to mimic the style of a few similar online games I remembered playing in the first decade of the millennium.  My idea was born, I would create a parking game, where a car was given to the player, a spot was designated, and based on how well they parked, they were given a score.  It would take a certain score to get to the next level.  I had not really decided if leaving the lot and heading towards the exit would be part of the game or not.

My grand vision of having the parking lines determine amount of points scored actually was never attempted to be put into practice at all, as I will describe.  The issue was the physics of the movement of the car.  I was not interested in a car parking game where the vehicle could travel perpendicular to the direction which the rear bumper(boot) or hood(bonnet) was facing.  The original plan was to have the current car being controlled's x and y direction incremented accordingly while (up, down) or (left, right) were being pressed in conjunction, so it would be akin to how an real car is able to travel around.  This proved increasingly difficult.

What made it so difficult to write code for a vehicle that could travel like a real one was the rotate function built into Pygame.  The rotate function was super helpful for this, but only at a very basic level.  If you run my game now, the vehicle will only rotate 90 degrees at a time.  What proved to be so difficult for me to attempt to write was the keybindings.  Mostly in how they relate to the current angle of the car, which was stored as a variable.  The amount by which x versus y direction would be incremented would have been different for every angle form 0-360.  Even if I was able to determine all of the values, writing them and bindings them to the keys in relation to the current angle of the car seemed like spending too much time on just movement of the car.  I submitted to the fact that if I wanted my project to be somewhat presentable for class on Monday, I had better move on.

I now focused on rendering more cars in the game, having to re-write many lines in my code to do so.  I had to re-write even more lines to implement a function to switch between the new cars I had rendered.
I presented this project to my class with a huge feeling of dissatisfaction for actual amount of working game that I had.  We were instructed to create the simplest bare bones version of our idea that would actually work.  My parking game did work, the application never crashes, but the functionality is not there.  As I set this project aside and moved on to CSS and HTML, I felt a sense of accomplishment, for what I did do, but was unhappy that I had not done more.

Lastly, to improve my project without spending too much time on it, I hope to add some pedestrians with random movement, and collision detection between the people and the cars, and of course, the cars themselves.  An exit would be designated, and the bumper of the car would have to be past that point to reach the end of the level.  Once again, the physics of my game are incomplete and left me feeling as such.  Consider rotating the car by 90 degrees and hitting a pedestrian in the process and losing.  This would be extremely frustrating, and not a game that I would want to play personally.



#Thanks for the read!

Calder Marshall
Web Developer at DigitalCrafts
