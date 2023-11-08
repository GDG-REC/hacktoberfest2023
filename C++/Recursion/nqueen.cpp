#include <iostream>
#include <cmath>
using namespace std;

const int maxN = 20; // Maximum board size

int board[maxN];  // board[i] represents the column where the queen in row i is placed

int N; // Size of the chessboard (N x N)

bool isSafe(int row, int col) {
    // Check for queens in the same column
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(i - row) == abs(board[i] - col)) {
            return false;
        }
    }
    return true;
}

void printSolution() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i] == j) {
                std::cout << "Q ";
            } else {
                std::cout << ". ";
            }
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

void solveNQueens(int row) {
    if (row == N) {
        // All queens are placed, print the solution
        printSolution();
        return;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row] = col;
            solveNQueens(row + 1);
        }
    }
}

int main() {
    std::cout << "Enter the size of the chessboard (N x N): ";
    std::cin >> N;

    if (N <= 0 || N > maxN) {
        std::cout << "Invalid board size." << std::endl;
        return 1;
    }

    solveNQueens(0);

    return 0;
}
