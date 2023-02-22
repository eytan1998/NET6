package tcp;// Java program to illustrate Server side
// Implementation using DatagramSocket

import java.io.*;
import java.net.*;
import java.util.HashMap;

public class App {
    static HashMap<Integer, Synagogue> hashMap = new HashMap<>();

    public static void main(String[] args) throws IOException, InterruptedException {

        hashMap.put(1, new Synagogue("בית כנסת 1"));
        hashMap.put(123, new Synagogue("בית כנסת 41"));
        hashMap.put(54, new Synagogue("בית כנסת 4121"));

        ServerSocket serverSocket = null;
        Socket socket = null;

        try {
            serverSocket = new ServerSocket(9999);
        } catch (IOException e) {
            e.printStackTrace();
        }
        while (true) {

            try {
                if (serverSocket != null) {
                    socket = serverSocket.accept();
                }
            } catch (IOException e) {
                System.out.println("I/O error: " + e);
            }
            new mThread(socket).start();
        }



    }
    private static class mThread extends Thread {
        Socket socket;

        public mThread(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try {

                InputStream input = socket.getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(input));

                int key = Integer.parseInt(reader.readLine());


                OutputStream os = socket.getOutputStream();
                ObjectOutputStream oos = new ObjectOutputStream(os);
                oos.writeObject(hashMap.get(key));
                oos.close();
                os.close();
                socket.close();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}
