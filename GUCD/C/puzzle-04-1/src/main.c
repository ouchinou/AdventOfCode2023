#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#define NMAX     1000
#define N          50

typedef struct {
    int num_gagnants[N];
    int num_choisis[N];
} tirage_t;

typedef struct {
    int choisis;
    int gagnants;
} tirage_len_t;

static bool isNumber(char ch)
{
    return ((ch >= '0') && (ch <= '9'));
}

static int size_num(int n)
{
    int res;

    if((n <= 9) && (n >= 0))
    {
        res = 1;
    }
    else if((n <= 99) && (n >= 10))
    {
        res = 2;
    }
    else 
    {
        res = -1;
    }
    return res;
}

int main()
{
    FILE *fptr;

    tirage_t tirage[NMAX];
    tirage_len_t tirage_len[N];

    unsigned int nb_line = 0;
    int num, n = 0;
    int i, j;
    int score = 0;
    double cpt = 0.0;
    double acc = 0.0;

    char * mid_indx;
    bool isPipeGone = false;
    bool isColumnGone = false;

    // Open a file in read mode
    fptr = fopen("../input.txt", "r");

    // Store the content of the file
    char myString[NMAX];

    // If the file exist
    if(fptr != NULL)
    {
        // Read the content and print it
        // "for line in text:" equivalent
        while(fgets(myString, NMAX, fptr))
        {
            // Do the thing
            unsigned int size = strlen(myString) ;

            /*mid_indx = strchr(myString, '|');*/

            for (i = 0; i <= size; i++)
            {
                if(myString[i] == ':')
                {
                    isColumnGone = true;
                }
                if(myString[i] == '|')
                {
                    tirage_len[i].gagnants = n;
                    isPipeGone = true;
                    n = 0;
                }
                if(i == size)
                {
                    tirage_len[i].choisis = n;
                    isPipeGone = false;
                    isColumnGone = false;
                    n = 0;
                }

                if(isPipeGone)
                {
                    if(isNumber(myString[i]) && isColumnGone)
                    {
                        num = atoi(&myString[i]);
                        tirage[nb_line].num_choisis[n] = num;
                        n++;

                        i += size_num(num)-1;
                    }
                }
                else 
                {
                    if(isNumber(myString[i]) && isColumnGone)
                    {
                        num = atoi(&myString[i]);
                        tirage[nb_line].num_gagnants[n] = num;                    
                        n++;

                        i += size_num(num)-1;
                    }
                }              
            }
            nb_line++;
        }

    }
    // If the file does not exist
    else
    {

        printf("Not able to open the file.");
    }

    // Post-processing
    n = 0;
    
    while(nb_line > n)
    {
        for(i = 0; i < 25 ; i++)
        {
            for (j = 0; j < 10 ; j++)
            {
                if(tirage[n].num_choisis[i] == tirage[n].num_gagnants[j])
                {
                    cpt++;   
                }
            }
        }
        if(cpt == 0 || cpt == 1)
        {
            score = cpt;
        }
        else 
        {
            score = pow(2.0, (cpt-1.0));
        }
        acc += score;
        cpt = 0.0;
        n++;
    }
    // Close the file
    fclose(fptr);
    printf("%d %d\n", tirage_len[0].choisis, tirage_len[0].gagnants);
    printf("%lf\n", acc);

	return 0;
}
