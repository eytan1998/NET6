package tcp;

import java.io.Serializable;

public class Synagogue implements Serializable {
    String name;
    int id;
    String nosahe;

    public Synagogue(String name, int id, String nosahe) {
        this.name = name;
        this.id = id;
        this.nosahe = nosahe;
    }

    public Synagogue(String name) {
        this.name = name;
    }

    public Synagogue() {
    }

    @Override
    public String toString() {
        return "Synagogue{" +
                "name='" + name + '\'' +
                ", id=" + id +
                ", nosahe='" + nosahe + '\'' +
                '}';
    }
}


