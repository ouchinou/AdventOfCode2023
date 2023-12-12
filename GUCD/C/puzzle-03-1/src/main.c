#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE_LENGTH 500
#define MAX_LINE       1000

char point[MAX_LINE][MAX_LINE_LENGTH];
unsigned int nb_line = 0;

static int nb_digit(int a)
{
    int res ;

    if((a <= 9) && (a >= 0))
    {
        res = 1;
    }
    else if((a <= 99) && (a >= 10))
    {
        res = 2;
    }
    else if((a <= 999) && (a >= 100))
    {
        res = 3;
    }
    else 
    {
        perror("Error...");
    }
    return res;
}

static bool isNumber(char ch)
{
    return ((ch <= '9') && (ch >= '0'));
}

static bool seek_n_destroy(int nb_digit, int indx_line, int indx_col)
{
    bool isPartEngine;

    for(int i = indx_line-1 ; i <= indx_line+1 ; i++)
    {
        for(int j = indx_col-1 ; j <= indx_col+nb_digit ; j++)
        {
            // Is the point in the plan sheet ?
            if((i >= 0) && (i <= nb_line) && (j >= 0) && (j <= strlen(point[i])))
            {
                // Is a symbol adjacent ?
                if(('.' != point[i][j]) && !isNumber(point[i][j]) && ('\n' != point[i][j]))
                {
                    isPartEngine = true;
                }
            }
        }
    }
    return isPartEngine;
}

void parse_and_process(FILE *file) 
{
    int i = 0;
    int j;
    int n_digit, nb = 0;
    unsigned int acc = 0;
    unsigned int size ;

    // Parsing
    while (fgets(point[i], MAX_LINE_LENGTH, file) != NULL) 
    {
        i++; 
    }

    nb_line = i;
    i = 0;
    size = strlen(point[i]);

    // Processing
    // for line in text (index: i)
    while(i < nb_line) 
    {
        // for char in line (index: j)
        for(j = 0; j < strlen(point[i]); j++)
        {
             if(isNumber(point[i][j]))
            {
                nb = atoi(&point[i][j]);
                n_digit = nb_digit(nb);

                // Track an adjacent symbol
                if(seek_n_destroy(n_digit, i, j))
                {
                    acc += nb; 
                }
                j += (n_digit-1);
            }
        }
        i++;
    }
    printf("%d %u\n", nb_line ,  acc);
}

int main() 
{
    // Open the file
    FILE *file = fopen("../input.txt", "r");

    if (file == NULL) 
    {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Parse and print the first 3 lines
    parse_and_process(file);

    // Close the file
    fclose(file);

    return 0;
}
