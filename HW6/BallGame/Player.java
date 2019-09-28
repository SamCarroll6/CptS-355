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
 import java.awt.Font;

 public class Player
 {
   // Private variables
   private int Hits;
   private int Score;
   private int HitType[];
   private int Highhold;
   private String HighHit[];
   // Constructor
   public Player()
   {
     Hits = 0;
     Score = 0;
     Highhold = 0;
     HitType = new int[4];
     HighHit = new String[]{"Basic", "Split", "Bounce", "Shrink"};
   }
   // Mainly used function
   public void ScoreP(BasicBall check)
   {
     // Check instances of ball type
     if(check instanceof SplitBall)
     {
       // Account for score update
       Score = Score + 10;
       // Number of hits to this ball type goes up one
       HitType[1]++;
       // Check if number of hits on this ball type is highest
       // If it is set the value to it's specified spot in the array
       if(HitType[1] > HitType[Highhold])
       Highhold = 1;
     }
     else if(check instanceof BounceBall)
     {
       Score = Score + 15;
       HitType[2]++;
       if(HitType[2] > HitType[Highhold])
       Highhold = 2;
     }
     else if(check instanceof ShrinkBall)
     {
       Score = Score + 20;
       HitType[3]++;
       if(HitType[3] > HitType[Highhold])
       Highhold = 3;
     }
     else if(check instanceof BasicBall)
     {
       Score = Score + 25;
       HitType[0]++;
       if(HitType[0] > HitType[Highhold])
       Highhold = 0;
     }
     // Increment Hit count
     Hits++;
   }

   // Displays your score in upper left of screen
   public void DisplayScore()
   {
     // Taken from display in main
     StdDraw.setPenColor(StdDraw.YELLOW);
     Font font = new Font("Arial", Font.BOLD, 15);
     StdDraw.setFont(font);
     // Print various scores
     StdDraw.text(-0.65, 0.85, "Hits: "+ Hits);
     StdDraw.text(-0.65, 0.80, "Score: "+ Score);
      StdDraw.text(-0.65, 0.75, "Most Hit Type: "+ HighHit[Highhold]);
   }
 }
