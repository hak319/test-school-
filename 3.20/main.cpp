#include<stdio.h>

int main() {
    int i, j, x, y, k,co; 
    
    printf("�Է� ���� �� : ");
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
    printf("===  1. �����ﰢ��                    2. ���������ﰢ��     ===\n");
    printf("===  3. �ݻ������ﰢ��                4. �ݻ翪�������ﰢ�� ===\n");
    printf("===============================================================\n");
    
    printf("���ϴ� ���� ���� : ");
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

