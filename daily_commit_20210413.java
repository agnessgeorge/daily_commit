public class Main {

    public static void main(String[] args) {

        int a = triArea(3, 2);
        System.out.println(a);
        int b = triArea(7, 4);
        System.out.println(b);
        int c = triArea(10, 10);
        System.out.println(c);

    }

    private static int triArea(int base, int height){
        return (base * height) / 2;
    }
}
