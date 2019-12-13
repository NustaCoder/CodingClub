//use scanner class for taking input from user
//n is number of rows that can be made, make logic to find n
public class Problem15
{
    public static void main(String st[]){
        int n = 3, flag = 1;
        int[] arr = {1,2,3,1,5,1};
        int pos = arr[0], p = 0, s = arr.length/2;        
        int[] temp = new int[s];
        for(int i=1;i<n;i++)
        {
            int a = 0;
            while(a<=i)
            {
                temp[a] = arr[flag];
                flag++;
                a++;
            }
            if(temp[p] > temp[p+1])
            {
                pos += temp[p];
            }
            else{
                pos += temp[p+1];
                p = p + 1;
            }
        }
        System.out.println(pos);
    }
}