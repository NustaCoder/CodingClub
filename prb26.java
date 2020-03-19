public class prb26 {
    public static void main(String st[]) {
        int[] arr = { 1, 2, 3, 4, 5 };
        int i = 0, c = 0;
        String s = "(";
        // you may take input using scanner class
        if (arr.length % 2 == 0) {
            while (i < arr.length) {
                c = arr[i] + arr[i + 1];
                i += 2;
                s += c + ",";
            }
            s = s.substring(0, s.length() - 1);
            s += ")";
            System.out.println(s);
        } else {
            while (i < arr.length - 1) {
                c = arr[i] + arr[i + 1];
                i += 2;
                s += c + ",";
            }
            s += arr[arr.length - 1] + ")";
            System.out.println(s);
        }
    }
}