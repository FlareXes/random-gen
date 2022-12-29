#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generatePassword(char *password, int length) {
    uint randomIdx;
    int charactersLength = 94;
    const char *characters;
    characters = "1234567890`-=~!@#$%^&*()_+[]{}\\|;'/.,<>?:\"qwertyuioplkjhgfdsazxcvbnmPOIUYTREWQASDFGHJKLMNBVCXZ";

    for (int i = 0; i < length; i++) {
        randomIdx = arc4random() % charactersLength;
        password[i] = characters[randomIdx];
    }
    password[length] = '\0';
}

int main(int argc, char const *argv[]) {
    if (argc < 2) {
        char password[16];
        generatePassword(password, 16);
        printf("%s", password);
        return 0;
    }

    if (strcmp(argv[1], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
        printf("Usage: %s password_length\n", argv[0]);
        printf("Generates a secure password of the specified length.\n");
        return 0;
    }

    int length = atoi(argv[1]);
    char password[length];
    generatePassword(password, length);
    printf("%s", password);
}
