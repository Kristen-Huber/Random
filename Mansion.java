import java.awt.*;

public class Mansion extends Building{

    public Mansion() {
    
    }
    
   public void build(Graphics g) {
		g.setColor(Color.cyan);
		g.fillRect(100,0, 50, 50);
		g.setColor(Color.lightGray);
		g.fillRect(100,25,50,25);	

	}
}