#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	// Node *next;
	// Node *prev;
	int index;
	int value;
	// both is the xor of both next and prev &
	// current address as well as information to next and prev
	struct Node *both;
} Node;

typedef struct XorLinkedList {
	Node *start;
	Node *end;
	int size;

} XorLinkedList;

Node *add(XorLinkedList *list, int value) {
	Node *temp = (Node *)malloc(sizeof(Node));

	//printf("%d\n", value);
	if (list->size == 0) {
		temp->index = 0;
		temp->both = 0;
		list->start = temp;
	}
	else {
		Node *prev = list->end;
		prev->both = (Node *)((uintptr_t)prev->both ^ (uintptr_t)temp);
		temp->both = (Node *)((uintptr_t)prev);
	}
	
	temp->value = value;
	list->end = temp;
	list->size +=1;
	temp->index = list->size - 1;
	return temp;
}

Node *get(XorLinkedList *list, int index) {
	
	int i = 0;
	if(index >= list->size || index < 0) {
		return NULL;
	}
	if(index == 0) {
		return list->start;
	}
	if(index == list->size - 1) {
		return list->end;
	}

	Node *cur = list->start;
	Node *next = (Node *)((uintptr_t)cur->both);
	Node *temp;

	while(i < index) {
		temp = cur;
		cur = next;
		next = (Node *)((uintptr_t)cur->both ^ (uintptr_t)temp);
		i++;
	}
	return cur;

}

XorLinkedList *createList() {
	XorLinkedList *temp = (XorLinkedList *)malloc(sizeof(XorLinkedList));
	temp->start = NULL;
	temp->end = NULL;
	temp->size = 0;

	return temp;
}

int main() {
	XorLinkedList *list = createList();
	for(int i = 0; i < 5; i++) {
		add(list, i);
	}

	//get(list,4);
	// printf("%d",get(list, 1)->index);

	for(int i = 0; i < 5; i++) {
		printf("i: %d, index: %d, value: %d\n", i, get(list,i)->index, get(list,i)->value);
	} 
	return 0;
}