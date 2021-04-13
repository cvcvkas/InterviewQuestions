#include <iostream>
#include <math.h>

int cutRope(int ropeLength)
{
    int ropeThrees = 0;
    int ropeThreesRem = 0;
    int ropeTwos = 0;

    ropeThrees = floor(ropeLength / 3);
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

    return pow(3, ropeThrees) * pow(2, ropeTwos);
}

int main()
{
    std::cout << cutRope(8) << "\n";
    std::cout << cutRope(9) << "\n";
    std::cout << cutRope(10) << "\n";
}