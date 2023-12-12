#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define NMAX    10000

static bool isNumber(const char ch)
{
    return ((ch >= '0' && ch <= '9') ? true : false);
}

int main()
{
    FILE *fptr;
    unsigned int first, last, indx, acc;
    unsigned int cpt_lines = 0;

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
            unsigned char size = strlen(myString) - 2;

            // Find first number 
            indx = 0;
            while(indx <= size)
            {
                if(isNumber(myString[indx]))
                {
                    char tmp[2] = { myString[indx], '\0'}; 
                    first = atoi(tmp);
                    break;
                }
                indx++;
            }
            // Find last number
            indx = size;
            while(indx >= 0)
            {
                if(isNumber(myString[indx]))
                {
                    char tmp[2] = { myString[indx], '\0'}; 
                    last = atoi(tmp);
                    break;
                }
                indx--;
            }
            acc += (10 * first + last); 
            cpt_lines++;
            printf("acc=%u\n",(10*first+last));
        }
    }
    // If the file does not exist
    else
    {

        printf("Not able to open the file.");
    }

    // Close the file
    fclose(fptr);

    printf("Result: %u\nNb processed lines:%u\n", acc, cpt_lines);

	return 0;
}
