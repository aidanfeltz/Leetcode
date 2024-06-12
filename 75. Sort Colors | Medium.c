#include <stdio.h>
void sortColors(int* nums, int numsSize) {
    int red = 0, white = 0, blue = 0;
    for (int i = 0;i < numsSize; i ++) {
        int num = *(nums + i);
        printf("%d",num);
        switch(num){
            case 0:
                red ++;
                break;
            case 1:
                blue ++;
                break;
            case 2:
                white ++;
                break;
        }
    }
    for(int i = 0; i < red; i ++){nums[i] = 0;}
    for(int i = red; i < (red+blue); i++){nums[i] = 1;}
    for(int i = (red+blue); i <(red+blue+white);i++){nums[i]=2;}
}
