import java.awt.*;

public class Road extends Pavement implements BuildableItems {

    public Road() {
    
    }
    
    public void buildPavement(Graphics g){
        g.setColor(Color.black);
        g.drawRect(0, 100, 50, 5);
        g.setColor(Color.gray);
        g.fillRect(0, 100, 50, 5);
        }
        
    public void construct(Graphics g){
        buildPavement(g);
        
        }
   }
    
    