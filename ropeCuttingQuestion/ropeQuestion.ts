{
    const cutRope = (ropeLength: number) => 
    {
        if (typeof ropeLength != typeof 0) throw new Error("Rope's length has to be an Integer (int).");

        let ropeThrees: number = 0;
        let ropeThreesRem: number = 0;
        let ropeTwos: number = 0;

        ropeThrees = Math.floor(ropeLength / 3);
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
    };


    console.log(cutRope(8));
    console.log(cutRope(9));
    console.log(cutRope(10));
};