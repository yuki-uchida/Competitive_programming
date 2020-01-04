#include<iostream>
using namespace std;

struct Card {char suit, value;};

void bubble(struct Card A[], int N ){
    for (int i = 0; i < N; i++){
        for (int j = N - 1; j >= i+1; j--){
            if ( A[j].value < A[j - 1].value) {
                Card t = A[j]; A[j] = A[j - 1]; A[j - 1] = t;
            }
        }
    }
}

void selection(struct Card A[], int N){
    for (int i = 0; i < N; i++){
        int minj = i;
        for (int j = i; j < N; i++){
            if (A[j].value < A[minj].value) minj = j;
        }
        Card t = A[i]; A[i] = A[minj]; A[minj] = t;
    }
}

void print(struct Card A[], int N ){
    for (int i = 0; i < N; i++){
        if (i>0) cout << " ";
        cout << A[i].suit << A[i].value;
    }
    cout << endl;
}

