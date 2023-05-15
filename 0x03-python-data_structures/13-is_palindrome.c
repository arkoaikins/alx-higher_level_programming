#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrom
  *         else return 1
  */
int is_palindrome(listint_t **head)
{
	listint_t *begin = NULL, *stop = NULL;
	unsigned int i = 0, len = 0, cycl_len = 0, list_of_len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	begin = *head;
	len = list_f_len(begin);
	cycl_len = len * 2;
	list_of_len = cycl_len - 2;
	stop = *head;
	for (; i < cycl_len; i = i + 2)
	{
		if (begin[i].n != stop[len_list].n)
			return (0);
		list_of_len = list_of_len - 2;
	}
	return (1);
}

/**
  * get_nodeint_at_index - Takes node from list
  * @head:  head of  list
  * @index: index to find in list
  *
  * Return: specific node of list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *working = head;
	unsigned int time_inte = 0;

	if (head)
	{
		while (working != NULL)
		{
			if (time_inte == index)
				return (working);
			working = working->next;
			++time_inte;
		}
	}
	return (NULL);
}

/**
  * slist_f_len - reads the number of elements in list
  * @h: linked list to count
  *
  * Return: Number of elements in list
  */
size_t list_f_len(const listint_t *h)
{
	int leng = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}
	return (lenght);
}
