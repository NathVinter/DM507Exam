# Script for visualizing extractMin on a minHeap, step-by-step.
# The initial heap is stored in the myHeap variable (in the bottom of the script)
# Created by Brian Pedersen

def min_heapify(heap, i):
	left = i * 2 + 1
	right = i * 2 + 2

	if left < len(heap) and heap[left] < heap[i]:
		smallest = left
	else:
		smallest = i

	if right < len(heap) and heap[right] < heap[smallest]:
		smallest = right

	if smallest != i:
		heap[i], heap[smallest] = heap[smallest], heap[i]
		print(str(heap) + " exchanged " + str(heap[i]) + " with " + str(heap[smallest]))
		min_heapify(heap, smallest)

def heap_extract_min(heap):
	if len(heap) < 0:
		print("Heap underflow")
	print(str(heap) + " original heap")
	min_node = heap[0]
	heap[0] = heap[len(heap) - 1]
	heap.pop(len(heap)-1)
	print(str(heap) + " extracted root: " + str(min_node))
	min_heapify(heap, 0)

def heap_insert(hp, i):
    print(str(hp) + " original heap")
    hp.append(i)
    min_heapify(hp, 0)
    print(str(hp) + " inserted element: " + str(i))

# Edit here
myheap = [2, 4, 5, 8, 7, 6, 6, 9]
heap_insert(myheap, 1)