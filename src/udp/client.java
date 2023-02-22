package udp;// Java program to illustrate Client side
// Implementation using DatagramSocket

import org.apache.commons.lang3.SerializationUtils;

import java.io.IOException;
import java.io.Serializable;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.Scanner;

public class client {
    //TODO חבילת בקשה
//???? flow control ?????????
// ??? congestion control - //תחזיר ack
//אם לא הגיע ack  - נוריד תחלון ל בית כנסת אחד
//כל אחד שמגיע נשלח אחד ועוד אחד

//checksum
// id 2^8\ -1
//nosah -1;2^2
//queury ""


//TODO חבילת תגובה
//???? flow control ?????????
// ??? congestion control - //תחזיר ack
//אם לא הגיע ack  - נוריד תחלון ל בית כנסת אחד
//כל אחד שמגיע נשלח אחד ועוד אחד

//checksum
// flag
//בית כנסת

    /*******************חבילת בקשה*******
     * d
     *
     *
     *
     */
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);


        DatagramSocket ds = new DatagramSocket();

        InetAddress ip = InetAddress.getLocalHost();
        byte buf[] = constractPacket(true, -12512412, "sdfghjkl");

        while (true) {

            DatagramPacket DpSend =
                    new DatagramPacket(buf, buf.length, ip, 5555);


            ds.send(DpSend);

            break;
        }
    }

    private static byte[] constractPacket(boolean isAck, int id, String data) {
        // |________  ________ ________ ________| id
        // |________  ________ ________ ________|
        // |________  ________ ________ ________|
        // |________  ________ ________ ________|
 /*       ByteBuffer buffer = ByteBuffer.allocate(100);
        buffer.rewind();

        buffer.put(IntToByteArray(id));
        buffer.put((byte) (isAck? 1:0));
        buffer.put(data.getBytes());
        */

        return SerializationUtils.serialize(new request(id,isAck,data));


    }
    private static byte[] IntToByteArray(int data) {
        byte[] result = new byte[4];
        result[0] = (byte) ((data & 0xFF000000) >> 24);
        result[1] = (byte) ((data & 0x00FF0000) >> 16);
        result[2] = (byte) ((data & 0x0000FF00) >> 8);
        result[3] = (byte) ((data & 0x000000FF) >> 0);
        return result;
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
