#include<stdio.h>

int main() {
    int i, j, x, y, k; 
    
    printf("입력 라인 수 : ");
    scanf("%d", &x);
    
    /*for(i = 1; i <= x; i++) {
        for(j = 1; j <= i; j++) {
            printf("*");
        } 
        printf("\n");
    } */
    
    /*for(i=x;i>=1;i--){
    	for(j=1;j<=i;j++){
    		printf("*");
		}
		printf("\n");
	}*/
	
	 for(i = 1; i <= x; i++) {
        for(j = x - i; j >= 1; j--) {
            printf(" ");
        } 
        for(k = 1; k <= i; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}

