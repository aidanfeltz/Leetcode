//https://leetcode.com/problems/water-bottles-ii/
#import <stdio.h>
int maxBottlesDrunk(int numBottles, int numExchange) {
    bool is = false;
    int drink = numBottles, empties = numBottles;
    numBottles = 0;
    while(numBottles + empties >= numExchange){
        is = false;
        if(empties >= numExchange){
            numBottles++;
            empties = empties - numExchange;
            numExchange++;
             is = true;
            }
        if (is == false){
            drink++, empties++, numBottles--;
            }
        }
    drink = drink + numBottles;
    return drink;
    }
