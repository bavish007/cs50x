#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Validate the Command-Line Argument
    // Length of Command-Line Arguments == 2

    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // Length of key == 26

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Valid key (Only Alphabets)
    // No duplicates

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        // YTNSHKVEFXRBAUQZCLWDMIPGJO
        // i & j
        if (isalpha(argv[1][i]) == 0)
        {
            printf("Key should be all alphabets.\n");
            return 1;
        }

        for (int j = i + 1; j < n; j++)
        {
            if (toupper(argv[1][i]) == toupper(argv[1][j]))
            {
                printf("No duplicate values allowed.\n");
                return 1;
            }
        }
    }

    string key = argv[1];

    // Input from the user (Plaintext)

    string plain = get_string("plaintext: ");

    // Print the Ciphertext

    printf("ciphertext: ");
    for (int i = 0, n = strlen(plain); i < n; i++)
    {
        if (isalpha(plain[i]))
        {
            if (isupper(plain[i]))
            {
                // Encrypt & fix case
                printf("%c", toupper(key[plain[i] - 65]));
            }
            else
            {
                // Encrypt & fix case
                printf("%c", tolower(key[plain[i] - 97]));
            }
        }
        else
        {
            printf("%c", plain[i]);
        }
    }
    printf("\n");
}
