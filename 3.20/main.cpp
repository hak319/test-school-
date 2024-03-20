#include<stdio.h>

int main() {
    int i, j, x, y, k,co; 
    
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
	
	/* for(i = 1; i <= x; i++) {
        for(j = x - i; j >= 1; j--) {
            printf(" ");
        } 
        for(k = 1; k <= i; k++) {
            printf("*");
        }
        printf("\n");
    }*/
    
    printf("===============================================================\n");
    printf("===  1. 직각삼각형                    2. 역직각형삼각형     ===\n");
    printf("===  3. 반사직각삼각형                4. 반사역직각형삼각형 ===\n");
    printf("===============================================================\n");
    
    printf("원하는 형태 고르기 : ");
    scanf(%d, &co);
    
    switch(co){
    	case 1:
    		*for(i = 1; i <= x; i++) {
       			 for(j = 1; j <= i; j++) {
            printf("*");
        	} 
       		 printf("\n");
			}
			break;
		case 2:
			for(i=x;i>=1;i--){
    			for(j=1;j<=i;j++){
    		printf("*");
			}
			printf("\n");
			}
			break;
		case 3:
			
	
    
    return 0;
}

