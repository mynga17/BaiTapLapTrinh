#include <stdio.h>
#include <math.h>

int laSoChinhPhuong(int num) {
    int can = (int) sqrt(num);
    return can * can == num;
}

void demSoChinhPhuong(int n) {
    printf("Cac so chinh phuong nho hon %d la: ", n);
    int count = 0;
    
    for (int i = 1; i < n; i++) {
        if (laSoChinhPhuong(i)) {
            printf("%d ", i);
            count++;
        }
    }
    
    printf("\nTong so chinh phuong: %d\n", count);
}

int main() {
    int n;
    scanf("%d", &n);
    demSoChinhPhuong(n);
    return 0;
}
