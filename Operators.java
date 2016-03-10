import java.applet.*;
import java.awt.*;

public class Operators extends Applet {
     float a;
     
     
    public void paint(Graphics g){
           int leftLocation=10;
           int topLocation=10;
           float c=2;
           float b=10;
    
           a=15;
        
           b+= a;
           --a;
           a *= c;
           
           g.drawString("the value is " + a, leftLocation, topLocation);
        
        }
}
       
  
        
                

    

    
