import java.applet.*;
import java.awt.*;

public class Cities extends Applet {

    public String[] cities = new String[5];
    
    public void init()    {
    }
    
    public void paint(Graphics g) {
         cities[0] = "New York";
         cities[1] = "Los Angeles";
         cities[2] = "Dallas";
         cities[3] = "San Francisco";
         cities[4] = "Boston";
         
         for (int x = 0; x < 7; x++)  {
             g.drawString(cities[x],10, 20 * x + 10);
         }
     }
 }