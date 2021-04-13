class ropeQuestion
{
    public static Integer CutRope(int ropeLength)
    {
        int ropeThrees = 0;
        int ropeThreesRem = 0;
        int ropeTwos = 0;

        ropeThrees = ropeLength / 3;
        ropeThreesRem = ropeLength % 3;


        switch(ropeThreesRem)
        {
            case 1:
                ropeThrees--;
                ropeTwos = 2;
                break;
            case 2:
                ropeTwos = 1;
                break;
        }

        return (int) (Math.pow(3, ropeThrees) * Math.pow(2, ropeTwos));
    }


    public static void main(String[] args)
    {
        System.out.println(CutRope(8));
        System.out.println(CutRope(9));
        System.out.println(CutRope(10));
    }
}