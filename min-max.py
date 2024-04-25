"""
Implement Min-Max Algorithm

Experiment: 6

@Learner: TE-CO
Name: Arman Aslam Khan
Roll No: 22DCO03
Batch: 3
Academic Year: 2024
Sem - 6
"""

# Program:

import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

def get_user_input():
    scores = []
    n = int(input("Enter the number of elements in the scores array: "))
    for i in range(n):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)
    return scores

def main():
    scores = get_user_input()
    treeDepth = math.log2(len(scores))

    print("The optimal value is:", end=" ")
    print(minimax(0, 0, True, scores, treeDepth))

if __name__ == "__main__":
    main()


'''
Output:
Enter the number of elements in the scores array: 8
Enter score 1: 3
Enter score 2: 5
Enter score 3: 2
Enter score 4: 9
Enter score 5: 12
Enter score 6: 5
Enter score 7: 23
Enter score 8: 23
The optimal value is: 12
'''
