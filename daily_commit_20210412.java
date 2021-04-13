public class Main {

    public static void main(String[] args) {

        int a = howManySeconds(2);
        System.out.println(a);
        int b = howManySeconds(10);
        System.out.println(b);
        int c = howManySeconds(24);
        System.out.println(c);

    }

    private static int howManySeconds(int hours){
        return hours * 60 * 60;
    }
}
