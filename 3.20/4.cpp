#include<stdio.h>

int main() {
    int i, j, x, y, k; 
    
    printf("�Է� ���� �� : ");
    scanf("%d", &x);
    
  for(i = x; i >= 1; i--) {
        for(j = i-1; j >= 1; j--) {
            printf(" ");
        }
        for(k = 1; k <= (x-i+1); k++) {
            printf("*");
        }
        printf("\n");
    }
    
    
    
    return 0;
}

