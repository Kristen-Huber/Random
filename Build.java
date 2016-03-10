import java.applet.*;
import java.awt.*;

public class Waitress extends Applet   {

    public Food[] myMeal = new Food[3];
    
    public void paint(Graphics g)  {
    
        myBuilding[0] = new House(0, 0, Color.yellow);
        myBuilding[1] = new Mansion(0, 100, Color.blue);
        myBuilding[2] = new Art Museum(100, 0, Color.grey);
       
       
        for (int x = 0; x < myBuilding.length; x++) {
           myBuilding[x].build(g);
        }
        
    }
}