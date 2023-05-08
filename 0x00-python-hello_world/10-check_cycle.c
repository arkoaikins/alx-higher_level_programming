#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: points to the list
 * Return: 0 if there is no cycle
 *         else return 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *end;

	if (!list || !list->next)
		return (0);
	head = list;
	end = list;
	while (end != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		end = end->next;

		if (head == end)
			return (1);
	}
	return (0);
}
