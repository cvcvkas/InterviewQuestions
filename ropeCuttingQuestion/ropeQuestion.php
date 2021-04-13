<?php
    function cut_rope($rope_length)
    {
        $rope_threes = floor($rope_length / 3);
        $rope_threes_remainder = $rope_length % 3;
        $rope_twos = 0;

        switch($rope_threes_remainder)
        {
            case 1:
                $rope_threes--;
                $rope_twos = 2;
                break;
            case 2:
                $rope_twos = 1;
                break;
        }

        return (3 ** $rope_threes) * (2 ** $rope_twos);
    }

    echo cut_rope(8);
    echo "\n";
    echo cut_rope(9);
    echo "\n";
    echo cut_rope(10);
?>