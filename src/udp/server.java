package udp;// Java program to illustrate Server side
// Implementation using DatagramSocket

import org.apache.commons.lang3.SerializationUtils;

import java.io.IOException;
import java.io.Serializable;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class server {
    public static void main(String[] args) throws IOException {
        // Step 1 : Create a socket to listen at port 1234
        DatagramSocket ds = new DatagramSocket(5555);
        byte[] receive = new byte[65535];

        DatagramPacket DpReceive = null;
        while (true) {

            DpReceive = new DatagramPacket(receive, receive.length);

            ds.receive(DpReceive);
            String s = String.valueOf(data(receive));
            System.out.println("Client: " + s);

            if (s.equals("bye")) {
                System.out.println("Client sent bye.....EXITING");
                break;
            }

            receive = new byte[65535];
        }
    }


    public static String data(byte[] a) {
        return  SerializationUtils.deserialize(a).toString();
    }

    private static class request implements Serializable {
        int id;
        boolean isAck;
        String data;

        public request(int id, boolean isAck, String data) {
            this.id = id;
            this.isAck = isAck;
            this.data = data;
        }

        @Override
        public String toString() {
            return "request{" +
                    "id=" + id +
                    ", isAck=" + isAck +
                    ", data='" + data + '\'' +
                    '}';
        }
    }
}
