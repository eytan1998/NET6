package tcp;
import java.io.*;
import java.net.Socket;



public class Client {
    public static void main(String args[]) {

        try {
            Socket s = new Socket("localhost", 9999);
            InputStream is = s.getInputStream();

            OutputStream output = s.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            writer.println(4);

            ObjectInputStream ois = new ObjectInputStream(is);
            Synagogue to = (Synagogue) ois.readObject();
            if (to != null) {
                System.out.println(to);
            }
            is.close();
            s.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }


}
