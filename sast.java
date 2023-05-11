import javax.xml.parsers.DocumentBuilderFactory;

public class XMLParser {
    public static void main(String[] args) {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setFeature("http://xml.org/sax/features/external-parameter-entities", true);
    }
}
