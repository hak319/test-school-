#include<stdio.h>

int main() {
    int i, j, x, y, k; 
    
    printf("�Է� ���� �� : ");
    scanf("%d", &x);
    
    for(i = 1; i <= x; i++) {
        for(j = 1; j <= i; j++) {
            printf("*");
        } 
        printf("\n");
    } 
    return 0;
}
