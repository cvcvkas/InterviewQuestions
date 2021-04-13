{
    const cutRope = (ropeLength) => 
    {
        if (typeof ropeLength != typeof 0) throw new Error("Rope's length has to be an Integer (int).");

        let ropeThrees = Math.floor(ropeLength / 3);
        let ropeThreesRem = ropeLength % 3;
        let ropeTwos = 0;

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