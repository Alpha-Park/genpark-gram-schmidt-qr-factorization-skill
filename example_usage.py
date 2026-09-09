"""Example usage for QR Factorization Skill."""
from client import QRDecomposition

def main():
    print("Executing Modified Gram-Schmidt QR Factorization...")
    A = [[12.0, -51.0, 4.0], [6.0, 167.0, -68.0], [-4.0, 24.0, -41.0]]
    Q, R = QRDecomposition.factorize(A)
    print("Matrix Q (Orthogonal):", Q)
    print("Matrix R (Upper Triangular):", R)

    # Verify A = Q * R
    A_rec = [[sum(Q[i][k] * R[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            assert abs(A[i][j] - A_rec[i][j]) < 1e-3
    print("QR Factorization verified successfully!")

if __name__ == "__main__":
    main()
