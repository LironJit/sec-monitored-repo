// hi

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.owasp.encoder.Encode;
import java.io.IOException;

public class XSSServlet extends javax.servlet.http.HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userContent = request.getParameter("userContent");
        response.getWriter().write(Encode.forHtml(userContent));
    }
}
