import java.applet.*;
import java.awt.*;

public class DataTypeConverter extends Applet {

        private int xPosition = 125;
        private String somethingToAdd = "5.12345";

        public void paint(Graphics g) {
                double xPositionDoubleValue = new Integer(xPosition).doubleValue();
                double somethingToAddDoubleValue = new Double(somethingToAdd).doubleValue();
                double answerDoubleValue = somethingToAddDoubleValue + xPositionDoubleValue;
                
                g.drawString("Before Conversion: " + Integer.toString(xPosition) + " + "
                + somethingToAdd + " = " + Integer.toString(xPosition) + somethingToAdd, 10, 10);
                
                g.drawString("After Data Conversion:" + new Double(xPositionDoubleValue).toString() + " + "
                + new Double(somethingToAddDoubleValue).toString() + " ="
                + new Double(answerDoubleValue).toString(),
                10,50);
                
            }
        
}