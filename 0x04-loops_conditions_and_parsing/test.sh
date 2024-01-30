#!/usr/bin/env bash
#testing the shell looping techniques displaying numbers from 1 to 20
#and adding some flavour with the case command
counter=1
while [ $counter -le 20 ]; do
    echo "$counter"
    case $counter in
        4)
            echo "bad luck from China"
            ;;
        9)
            echo "bad luck from Japan"
            ;;
        17)
            echo "bad luck from Italy"
            ;;
        esac
    ((counter++))
done
