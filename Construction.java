import java.applet.*;
import java.awt.*;

public class Construction extends Applet   {

    public BuildableItems[] myBlock = new BuildableItems [4];
    
    public void paint(Graphics g){
    
        myBlock[0] = new House();
        myBlock[1] = new Mansion();
        myBlock[2] = new Road();
        myBlock[3] = new Driveway();
        
        for(int x =0; x < myBlock.length; x++) {
            myBlock[x].construct(g);
            }
    }
}