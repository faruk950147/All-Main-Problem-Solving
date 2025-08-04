class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def discriminant(self):
        return self.b**2 - 4*self.a*self.c
    
    def roots(self):
        disc = self.discriminant()
        if disc < 0:
            return None
        elif disc == 0:
            return -self.b/(2*self.a)
        else:
            return (-self.b + disc**0.5)/(2*self.a), (-self.b - disc**0.5)/(2*self.a)

# Example usage:
if __name__ == "__main__":
    eq = QuadraticEquation(1, -3, 2)
    print(eq.roots())  # Output: (2.0, 1.0)