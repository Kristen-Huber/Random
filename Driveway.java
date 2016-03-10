import java.awt.*;

public class Driveway extends Pavement implements BuildableItems {

    public Driveway() {
    
    }
    
      public void buildPavement(Graphics g){
        g.setColor(Color.black);
        g.drawRect(100, 100, 5, 25);
        g.setColor(Color.gray);
        g.fillRect(100, 100, 5, 25);
        }
        
    public void construct(Graphics g){
        buildPavement(g);
        
        }
   }