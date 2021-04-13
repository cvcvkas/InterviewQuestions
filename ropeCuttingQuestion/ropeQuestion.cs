using System;


namespace Interview_Questions
{
    class ropeQuestion
    {

        public static int CutRope(int ropeLength)
        {
            int ropeThrees = 0;
            int ropeThreesRem = 0;
            int ropeTwos = 0;

            ropeThrees = Math.Floor(ropeLength / 3);
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

            return (3 ** ropeThrees) * (2 ** ropeTwos);

        }

        static void Main(string[] args)
        {
            System.Console.WriteLine(this.CutRope(8));
            System.Console.WriteLine(this.CutRope(9));
            System.Console.WriteLine(this.CutRope(10));
        }
    }
}