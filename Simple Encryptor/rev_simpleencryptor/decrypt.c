#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <string.h>

int main() {
    FILE *flag = fopen("flag.enc", "rb");
    if (!flag) {
        perror("Error al abrir el archivo");
        return 1;
    }

    uint32_t seed;
    fread(&seed, sizeof(seed), 1, flag);
    printf("%u\n", seed); 
    printf("%s\n", ctime((time_t *)&seed)); 
    srand(seed);
    
    uint8_t byte;
    uint8_t decrypted_flag[1024];
    size_t decrypted_length = 0;

    while (fread(&byte, sizeof(byte), 1, flag) == 1) {
        // Aqui se pone el decryptors
        
    }
    
    fclose(flag);

    decrypted_flag[decrypted_length] = '\0';

    if (decrypted_length > 0 && decrypted_flag[0] != '\0') {
        printf("%s\n", decrypted_flag);
    } else {
        for (size_t i = 0; i < decrypted_length; i++) {
            printf("%c", decrypted_flag[i]);
        }
        printf("\n");
    }

    return 0;
}
