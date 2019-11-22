class MyTemp
{
    int n,cnt;
    int[][] arr;
    int[][] arr1;

    MyTemp(int n)
    {
        this.n = n;
        cnt = 1;
        arr = new int[n][n];
        arr1 = new int[n][n];
    }

    void addElements()
    {
        //you can use scanner class to take input from the user
        for(int i=0; i<n;i++)
        {
            for(int j=0; j<n;j++)
            {
                arr[i][j] = cnt++;
            }
        }
    }
    
    void display(int[][] a)
    {
        for(int i=0; i<n;i++)
        {
            for(int j=0; j<n;j++)
            {
                System.out.print(a[i][j]+"\t");
            }
            System.out.println();
        }
    }
    
    void rotate90()
    {
        for(int i=0; i<n;i++)
        {
            for(int j=1; j<=n;j++)
            {
                arr1[i][j-1] = arr[n-j][i];
            }
        }
    }

    void rotate180()
    {
        //find equation for 180deg rotaion clockwise
    }

    void rotate270()
    {
        //find equation for 180deg rotaion clockwise     
    }
}
public class Problem10
{
    public static void main(String st[])
    {
        MyTemp mt = new MyTemp(3);
        mt.addElements();
        mt.display(mt.arr);
        System.out.println("\n");
        mt.rotate90();
        mt.display(mt.arr1);
        System.out.println("\n");
    }
}