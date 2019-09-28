/******************************************************************************
 *  Compilation:  javac ColoredBall.java
 *  Execution:    java ColoredBall
 *  Dependencies: StdDraw.java
 *
 *  Implementation of a 2-d ball moving in square with coordinates
 *  between -1 and +1. Bounces off the walls upon collision.
 *
 *
 ******************************************************************************/

import java.awt.Color;

public class BasicBall {
    protected double rx, ry;         // position
    protected double vx, vy;         // velocity
    protected double radius;   // radius
    protected final Color color;     // color
    public boolean isOut;


    // constructor
    public BasicBall(double r, Color c) {
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        radius = r;
        color = c;
        isOut = false;
    }


    // move the ball one step
    public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0))
        	isOut = true;
    }

    // draw the ball
    public void draw() {
    	if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
    	} else
    		isOut = true;

    }

    public int reset() {
        rx = 0.0;
        ry = 0.0;
        // Added Random speeds at each reset
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        return 1;
    }

    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
      return true;
		else return false;

    }
    // Only just noticed this exists
    // Not going to use because I already accounted for it
    // but very nifty.
    public int getScore() {
    	return 25;
    }

    public double getRadius() {
    	return radius;
    }


}

// Shrinkball class, inherits from BasicBall
class ShrinkBall extends BasicBall
{
  // Constructor works same as BasicBall
  public ShrinkBall(double r, Color c)
  {
      super(r,c);
  }

  // Override isHit function to shrink the ball when hit
  @Override
  public boolean isHit(double x, double y)
  {
    if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
    {
      // Is hit, shrink radius but 2/3
      radius = radius * .66;
      return true;
    }
    else return false;
  }
}

// SplitBall class
class SplitBall extends BasicBall
{
  // SplitBall functionality handled in main
  // Just needed the class type to exist for type checking
  public SplitBall(double r, Color c)
  {
    super(r,c);
  }
}

// Class for BounceBall
class BounceBall extends BasicBall
{
  // Bouncevar tracks number of times a wall has been hit
  // After 3 it allows for ball to bounce out
  private int bouncevar;
  // Constructor
  public BounceBall(double r, Color c)
  {
    // Same as BasicBall
    super(r,c);
    // Added construction for new bouncevar variable
    bouncevar = 0;
  }

  @Override
  public int reset() {
      rx = 0.0;
      ry = 0.0;
      // Added Random speeds at each reset
      // Allowing bounceball to reset at faster speeds
      // With how slow it was previously it was too easy to just let float
      // This may make it harder?
      vx = StdRandom.uniform(-0.02, 0.02);
      vy = StdRandom.uniform(-0.02, 0.02);
      return 1;
  }

  // Override Move function
  @Override
  public void move() {
      rx = rx + vx;
      ry = ry + vy;
      // If it is past the walls and bounce var has equal to or more than 3 hits
      if (((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) && bouncevar >= 3)
      {
        // Allow it to leave
        isOut = true;
      }
      // Otherwise if it can still bounce and is hitting an x wall
      else if((Math.abs(rx) > (1.0 - radius)) && bouncevar < 3)
      {
        // Make x velocity negative
        vx = -(vx);
        // Increment bouncevar
        bouncevar++;
      }
      // Same as above but for y variables
      else if((Math.abs(ry) > (1.0 - radius)) && bouncevar < 3)
      {
        vy = -(vy);
        bouncevar++;
      }
  }
}
