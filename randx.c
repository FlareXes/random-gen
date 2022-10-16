#include <stdio.h>
#include <stdlib.h>

char *PASSWORD;

char *generatePassword(int length) {
    PASSWORD = (char *)malloc(length * sizeof(char));
    
    for (int i = 0; i < length; i++) {
        PASSWORD[i] = 33 + arc4random() % 94;
    }
    
    PASSWORD[length] = '\0';
    return PASSWORD;
}

int main(int argc, char const *argv[]) {
    if (argc < 2) {
        puts(generatePassword(16));
        return 0;
    }

    int length = atoi(argv[1]);
    puts(generatePassword(length));
    free(PASSWORD);
    return 0;
}