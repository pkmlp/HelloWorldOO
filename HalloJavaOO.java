
public class HalloJavaOO {

    String halloWeltText; 
    
    public HalloJavaOO() {
        halloWeltText = "Hallo Java wirklich Objekt-Orientiert !!!";
    }
 
    public void sagHallo() {
        System.out.println(halloWeltText);
    }
 
 
    public static void main(String[] args) {
    	HalloJavaOO halloJava = new HalloJavaOO();
    	halloJava.sagHallo();
    }

}
