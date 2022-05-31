#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert node at right space
 * @head: the head opf the list
 * @number: the value of the number
 *
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curt;

	curt = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
		*head = new;
	else
	{
		if (number < curt->n)
		{
			new->next = curt;
			*head = new;
		}
		else
		{
			while (curt->next && number > curt->next->n)
				curt = curt->next;

			new->next = curt->next;
			curt->next = new;
		}
	}
	return (new);
}
