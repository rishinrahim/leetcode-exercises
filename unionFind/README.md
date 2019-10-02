Union find Problem :

    Given a set of N objects.
        ・Union command: connect two objects.
        ・Find/connected query: is there a path connecting the two objects?

    Applications:
        ・Percolation.
        ・Games (Go, Hex).
        ・Dynamic connectivity.
        ・Least common ancestor.
        ・Equivalence of finite state automata.
        ・Hoshen-Kopelman algorithm in physics.
        ・Hinley-Milner polymorphic type inference.
        ・Kruskal's minimum spanning tree algorithm.
        ・Compiling equivalence statements in Fortran.
        ・Morphological attribute openings and closings.
        ・Matlab's bwlabel() function in image processing.

    Implementation :
        Find query. Check if two objects are in the same component.
        Union command. Replace components containing two objects with their union.

    Algorithms :

        1. Quick find ( Eigen approach ):
                Find: Check if p and q have the same id.
                Union :  To merge components containing p and q, change all entries whose id equals id[p] to id[q]

        2. Quick Union (Lazy approach ):
         It uses the same data structure or array ID with size M but now it has a different interpretation.
         the array now represents a set of trees that's called a forest

                Find: Check if p and q have the same root.
                Union: To merge components containing p and q,set the id of p's root to the id of q's root.

        3. Weighted quick union

        4. quick union with path compression

        5. Weighted quick union with Path Compression

