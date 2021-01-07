



antimony_model1 = """
model MichaelisMenten
    compartment Cell = 1;
    species A, B, C in Cell;
    A = 5; 
    B = 0;
    C = 0;
    k1 = 0.1;
    k2 = 0.1;
    k3 = 0.1;
    R1: A => B; k1*A
    R2: B => A; k2*B
    R3: B => C; k3*B
end
"""


if __name__ == "__main__":
    # checking that the model works
    import tellurium as te

    te.loada(antimony_model1)