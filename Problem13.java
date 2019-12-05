class Prb{
    int num,div;

    public Prb(int num){
        this.num = num;
        div = num/2;
    }

    void display_pattern()
    {
        if(num%2!=0){
            for(int i=0;i<num;i++)
            {
                for(int j=0;j<num;j++)
                {
                    if(i==div || j==div)
                    {
                        System.out.print("X ");
                    }
                    else{
                        System.out.print("0 ");
                    }
                }
                System.out.println();
            }
        }
    }
}

public class Problem13{
    public static void main(String st[])
    {
        Prb p = new Prb(10);
        p.display_pattern();
    }
}