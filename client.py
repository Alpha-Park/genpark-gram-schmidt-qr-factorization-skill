"""
Autonomous Agent Modified Gram-Schmidt QR Factorization Skill
Pure Python Standard Library implementation.
"""
import math
from typing import List, Tuple, Dict, Any

class QRDecomposition:
    """
    Modified Gram-Schmidt (MGS) QR Matrix Decomposition.
    """
    @staticmethod
    def factorize(A: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
        m = len(A)
        n = len(A[0])
        Q = [[0.0] * n for _ in range(m)]
        R = [[0.0] * n for _ in range(n)]

        v = [[A[i][j] for i in range(m)] for j in range(n)]

        for j in range(n):
            for i in range(j):
                R[i][j] = sum(Q[k][i] * v[j][k] for k in range(m))
                for k in range(m):
                    v[j][k] -= R[i][j] * Q[k][i]

            norm = math.sqrt(sum(v[j][k] ** 2 for k in range(m)))
            R[j][j] = norm
            for k in range(m):
                Q[k][j] = v[j][k] / norm if norm > 1e-12 else 0.0

        return [[round(x, 6) for x in row] for row in Q], [[round(x, 6) for x in row] for row in R]
