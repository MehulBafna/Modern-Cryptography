# Modern-Cryptography

## **Primitive root**

In modular arithmetic, a  primitive root is described as a number d modulo n such that for every integer y coprime to n, there exist some integer x for which d<sup>x</sup>  ≡ y (mod n). 
The value x is termed as the index or discrete logarithm of y to the base d modulo n. 

## **Baby step giant step algorithm**

It is an efficient algorithm for computing discrete logarithm in the following manner.

1. Compute m = int(√n)+1
2. Write x in terms of m, q and r as x=qm+r with 0≤q, r≤m−1. 
3. We need to find q and r such that (α<sup>m</sup>)<sup>q</sup> = n(α<sup>-1</sup>)<sup>r</sup>(mod p).
4. Compute value of f(r) = n(α<sup>-r</sup>)(mod  p) for r ∈ {0,···,m−1} and create the baby-step list.
5. Compute value of h(q) = (α<sup>m</sup>)<sup>q</sup>(mod p) for q ∈ {0,···,m−1} and create the giant-step list.
6. Look for q,r such that f(r) = h(q) and that gives discrete logarithm value as x=qm+r.

## **Edwards Curve**
An Edwards curve over a field K such that characteristic of K is an odd prime is given by
x<sup>2</sup>+y<sup>2</sup>=1+dx<sup>2</sup>y<sup>2</sup>
where d ∈ K/{0,1}

## **Twisted Edwards Curve**
A twisted Edwards curve over a field K such that characteristic of K is an odd prime is given by
ax<sup>2</sup>+y<sup>2</sup>=1+dx<sup>2</sup>y<sup>2</sup>
where a,d ∈ K/{0} and a is not equal to d.

## **Byzantine Agreement**
Given a set of k independent components with each component having
a secret information Ij for all j ∈ {1, · · · , k} with the below assumptions:

• Point-to-point fail-free communication among all the components

• At most i components are faulty (malicious) such that k ≥ 3i + 1

is termed as tolerant towards Byzantine faults, if for a component X after communicating
its secret information IX with all other components it follows that:
1. If X is non-faulty (reliable) component, then all non-faulty components agree on
the value IX .
2. In any scenario, all reliable components agree on a common value.
