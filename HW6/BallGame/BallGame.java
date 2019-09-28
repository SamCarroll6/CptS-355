/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

public class BallGame {

    public static void main(String[] args) {

    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
      //Variable for player statistics
      Player Results = new Player();
    	//ArrayList of Ball
      ArrayList<BasicBall> ballList = new ArrayList<BasicBall>();
      ArrayList<SplitBall> holdList = new ArrayList<SplitBall>();
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
        // Make sure array contains proper input
        try
        {
    		  ballTypes[i] = args[index];
    		  index = index+2;
        }
        catch(ArrayIndexOutOfBoundsException exception)
        {
          // If no arguments passed simply make basic
          ballTypes[i] = "basic";
        }
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
        // Check for right number of elements in arguments
        try
        {
          // Check if the value parses to a double
          try
          {
    		    ballSizes[i] = Double.parseDouble(args[index]);
          }
          // If not set size to .08
          catch(NumberFormatException e)
          {
            ballSizes[i] = 0.08;
          }
    		  index = index+2;
        }
        // If out of bounds set size to .08
        catch(ArrayIndexOutOfBoundsException exception)
        {
          ballSizes[i] = 0.08;
        }
    	}

    	//TO DO: create a Player object and initialize the player game stats.


    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls
      // Based on given BallType set new Balls
      for (int i = 0; i < ballSizes.length; i++)
      {
        // Various cases for different balls
        if(ballTypes[i].equalsIgnoreCase("shrink"))
        {
          ballList.add(new ShrinkBall(ballSizes[i],Color.BLUE));
        }
        else if(ballTypes[i].equalsIgnoreCase("bounce"))
        {
          ballList.add(new BounceBall(ballSizes[i],Color.green));
        }
        else if(ballTypes[i].equalsIgnoreCase("split"))
        {
          ballList.add(new SplitBall(ballSizes[i],Color.YELLOW));
        }
        else if(ballTypes[i].equalsIgnoreCase("basic"))
        {
          ballList.add(new BasicBall(ballSizes[i],Color.RED));
        }
        // If random name given just default to basic with .08 size
        // and default color black
        else
        {
          ballList.add(new BasicBall(.08,Color.BLACK));
        }
   	    // Add 1 to number of balls in the game
   		  numBallsinGame++;
      }

        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
          // Instances of ball placed in for loop
          // Where ball is a variable in the ball list arraylist
          for(BasicBall ball : ballList)
          {
            ball.move();
          }
            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                // Check if ball is hit for each ball in list
                for(BasicBall ball : ballList)
                {
                  if (ball.isHit(x,y))
                  {
                      ball.reset();
                      // Update score, pass in ball for ball type
                      Results.ScoreP(ball);
                      // If ball is split ball add new splitball of same size
                      // to holdList (adding to balllist was causing issues)
                      if(ball instanceof SplitBall)
                      {
                        holdList.add(new SplitBall(ball.getRadius(), Color.YELLOW));
                      }
                    	//TO DO: Update player statistics
                  }
                }
                // Take holdlist of splitballs and add to balllist
                for(SplitBall ball : holdList)
                {
                  ballList.add(ball);
                }
                // Clear hold list so you dont add doubles later
                holdList.clear();
            }

            numBallsinGame = 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);

          // Check if each ball is out.
          for(BasicBall ball : ballList)
          {
            if (ball.isOut == false) {
                ball.draw();
                numBallsinGame++;
            }
          }
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            //TO DO: print the rest of the player statistics
            Results.DisplayScore();
            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            //TO DO: print the rest of the player statistics
            StdDraw.show();
            StdDraw.pause(10);
        }


    }
}
