#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Take input from 2 users
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    // Calculate points for both the users
    int score1 = 0, score2 = 0;

    int points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int i = 0, n = strlen(p1); i < n; i++)
    {
        if (isalpha(p1[i])) // Question! // Answer
        {
            char c = toupper(p1[i]);
            score1 += points[c - 65];
        }
    }

    for (int i = 0, n = strlen(p2); i < n; i++)
    {
        if (isalpha(p2[i])) // Question! // Answer
        {
            char c = toupper(p2[i]);
            score2 += points[c - 65];
        }
    }

    // Winner/Tie
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
