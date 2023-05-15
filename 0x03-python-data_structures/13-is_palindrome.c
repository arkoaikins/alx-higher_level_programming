#include "lists.h"

/**
 * is_palindrome - checks if a singly-linked list is a palindrome
 *
 * @head: points to address of first node on the list
 * Return: 0 it it is not a palindrome
 *         else return 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len_list = 0;

	if (!*head)
		return (1);

	temp = *head;
	while (temp)
	{
		len_list++;
		temp = temp->next;
	}
	if (len_list % 2 != 0)
		return (0);

	return (1);
}
