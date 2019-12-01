import java.util.*;

public class Problem11
{
    public static void main(String st[])
    {
        Scanner scan = new Scanner(System.in);
        int n;
        System.out.println("enter the no. of elements...!");
        n = scan.nextInt();
        int[] arr = new int[n];
        int[] brr = new int[n];
        int cnt;
        System.out.println("enter the elements...!");
        for(int i=0;i<n;i++)
        {
            arr[i] = scan.nextInt();
        }
        for(int i=0; i<arr.length-1; i++)
        {
            cnt = 0;
            for(int j=i+1; j<arr.length;j++)
            {
                if(arr[i] > arr[j])
                {
                    cnt += 1;
                }
            }
        brr[i] = cnt;
        }
        System.out.println("\n\n");        
        for(int i = 0; i < brr.length;i++)
        {
            System.out.print(brr[i]+"\t");
        }

    }
}