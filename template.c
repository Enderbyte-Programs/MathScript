#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isprime(int n) {
    
    for (int i = 2; i < (int)round(sqrt(n))+1; i++) {//Complex math only need to go to sqrt(n)+1
        if (n%i==0) {//Check for a remainder
            return false;//NOT PRIME
        }
    }
    return true;//If it gets through loop, it is prime.
}

long calcprimes(int n) {
    long x = 0;//X may get very large
    int l = 0;//Prime counter, kept as int for comparison with n
    while (1) {//Infinite Loop
        x++;//Increment X
        if (x==1) {
            continue;//If X is one, skip because of error
        }
        if (isprime(x)==0) {//Checking for prime
            continue;//Not prime
        }
        //Prime
        l++;//Increment primt counter
        if (l==n) {//Prime is n:
            return x;
        }
    }

}

bool isnum(char* dat) {

    if(strspn(dat, "0123456789.") == strlen(dat)) {
        size_t big_digit = 0;
        sscanf(dat, "%zu%*c",&big_digit);
        return true;
    }
    return false;
}

double input(char* prompt) {
    while (true){
        printf("%s: ",prompt);
        char l[16];
        char *ptr;
        scanf("%s",&l);
        if (isnum(l)==1) {
            double d;
            d = strtod(l,&ptr);
            return d;
        } else {
            printf("Input is not number. please try again.\n");
        }
        
    }
}

int main() {
    double pi = 3.14;
    //DATAHERE
}