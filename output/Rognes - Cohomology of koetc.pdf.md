# COHOMOLOGY OF $H \mathbb{Z}, k u$ AND $k o$ 

John RogNes

### 23.11 .00

The following material is drawn from Part III of John F. Adams' book "Stable homotopy and generalised homology".

## COHOMOLOGY OF $H \mathbb{Z}$

To determine the cohomology $H^{*}=H^{*}(H \mathbb{Z} ; \mathbb{Z} / 2)$ of $H \mathbb{Z}$ as an $A$-module we consider the cofiber sequence

$$
H \mathbb{Z} \xrightarrow{2} H \mathbb{Z} \xrightarrow{i_{0}} H \mathbb{Z} / 2 \xrightarrow{j_{0}} \Sigma H \mathbb{Z}
$$

and the resulting diagram in cohomology:
![img-0.jpeg](img-0.jpeg)

Here $d$ is induced by the composite $i_{0} j_{0}: H \mathbb{Z} / 2 \rightarrow \Sigma H \mathbb{Z} / 2$ which represents the Bockstein operation $\beta=S q^{1}$, so $d(\Sigma \alpha)=\alpha S q^{1}$ for $\alpha \in A$. The map labelled $2^{*}$ is induced by the multiplication by 2 map on $H \mathbb{Z}$, which is 2 times the identity map and induces the zero map on mod 2 cohomology. So $i_{0}^{*}$ is surjective. Hence $\operatorname{im}\left(j_{0}^{*}\right)=\operatorname{im}(d)=A S q^{1}$ and $H^{*} \cong A / \operatorname{im}\left(j_{0}^{*}\right)=A / A S q^{1}$ as a left $A$-module:

$$
H^{*}(H \mathbb{Z} ; \mathbb{Z} / 2) \cong A / A S q^{1}=A / / E_{0}=A / / A_{0}
$$

## COHOMOLOGY OF $k u$

To determine the cohomology $H^{*}=H^{*}(k u ; \mathbb{Z} / 2)$ of $k u$ as an $A$-module, we consider the cofiber sequence arising from Bott periodicity:

$$
\Sigma^{2} k u \xrightarrow{v_{1}} k u \xrightarrow{i_{1}} H \mathbb{Z} \xrightarrow{j_{1}} \Sigma^{3} k u
$$

Recall that $\pi_{*} K U=\mathbb{Z}\left[u, u^{-1}\right]$ with $u \in \pi_{2} K U$, and $\pi_{*} k u=\mathbb{Z}[u]$, where $k u$ is the connective cover of $K U$ : One model for the spectrum $K U$ has $2 n$-th space $B U$,

while $k u$ has $2 n$-th space $B U[2 n]$, i.e., the $(2 n-1)$-connected cover of $B U$. The class $u \in \pi_{2} k u$ is represented by a map $u: S^{2} \rightarrow k u$, and the map $v_{1}$ is defined as the composite

$$
\Sigma^{2} k u=S^{2} \wedge k u \xrightarrow{u \wedge 1} k u \wedge k u \xrightarrow{\mu} k u
$$

where $\mu$ is the ring spectrum multiplication on $k u$. Then $\pi_{*}\left(v_{1}\right): \Sigma^{2} \mathbb{Z}[u] \rightarrow \mathbb{Z}[u]$ is injective, with cokernel $\mathbb{Z}$ in degree 0 , so the homotopy cofiber of $v_{1}$ has the homotopy type of $H \mathbb{Z}$. This yields the cofiber sequence above.

Consider the map of cofiber sequences of spectra:
![img-1.jpeg](img-1.jpeg)

Here $k u[0,2]$ is the Postnikov section of $k u$ with homotopy concentrated in the interval $[0,2]$, and $k=i_{1} j_{1}$ is the first $k$-invariant of $k u$.

Claim: $k=i_{1} j_{1}: H \mathbb{Z} \rightarrow \Sigma^{3} H \mathbb{Z}$ induces right multiplication by $Q_{1}=S q^{3}+$ $S q^{2} S q^{1}$ in cohomology, hence is represented by this class in $H^{*}(H \mathbb{Z} ; \mathbb{Z}) \subset A$.

There is a similar diagram of third spaces
![img-2.jpeg](img-2.jpeg)
where $B U[6]$ is the 5 -connected cover of $B U$, and $S U[3,5]$ is a Postnikov section of $S U$. The map $i_{1}: S U \rightarrow K(\mathbb{Z}, 3)$ induces an isomorphism on $\pi_{3}$ and thus takes the generator $\iota_{3} \in H^{3}(K(\mathbb{Z}, 3) ; \mathbb{Z} / 2)$ to a generator $e_{3} \in H^{3}(S U ; \mathbb{Z} / 2)$. Thus it maps $Q_{1} \iota_{3} \in H^{6}(K(\mathbb{Z}, 3) ; \mathbb{Z} / 2)$ to $Q_{1} e_{3}=e_{3}^{2}=0 \in H^{6}(S U ; \mathbb{Z} / 2)$, since this group is zero. (To see this, compute $H^{*}(S U(3) ; \mathbb{Z} / 2)=E\left(e_{3}, e_{5}\right)$ with the Serre spectral sequence for $S U(2) \rightarrow S U(3) \rightarrow S^{5}$, and note that $S U(3) \rightarrow S U$ is 6 -connected.) The map $S U \rightarrow S U[3,5]$ is 7 -connected, so also the image of $Q_{1} \iota_{3}$ in $H^{6}(S U[3,5] ; \mathbb{Z} / 2)$ is zero. By the Serre exact sequence for the fibration $S U[3,5] \rightarrow K(\mathbb{Z}, 3) \rightarrow K(\mathbb{Z}, 6)$ the complex

$$
H^{6}(K(\mathbb{Z}, 6) ; \mathbb{Z} / 2) \rightarrow H^{6}(K(\mathbb{Z}, 3) ; \mathbb{Z} / 2) \rightarrow H^{6}(S U[3,5] ; \mathbb{Z} / 2)
$$

is exact, and so $Q_{1} \iota_{3}$ lifts to a nonzero class in $H^{6}(K(\mathbb{Z}, 6) ; \mathbb{Z} / 2)$, which must be the generator $\iota_{6}$.

The natural stabilization maps $H^{3}(X ; \mathbb{Z} / 2) \rightarrow H^{6}\left(X_{3} ; \mathbb{Z} / 2\right)$ for a spectrum $X$ with third space $X_{3}$ yield the diagram:
![img-3.jpeg](img-3.jpeg)

Here $Q_{1} \iota_{3}$ lifts uniquely to $Q_{1} \in H^{3}(H \mathbb{Z} ; \mathbb{Z} / 2)$ and $\iota_{6}$ lifts to $\Sigma^{3} 1 \in H^{3}(H \mathbb{Z} ; \mathbb{Z} / 2)$. So $k^{*}\left(\Sigma^{3} 1\right)=Q_{1}$ and $k$ induces right multiplication by $Q_{1}$ in cohomology. This proves the claim.

Returning to the cofiber sequence arising from Bott periodicity, we can now show that $v_{1}$ has positive Adams filtration, i.e., that it induces the zero map on mod 2 cohomology, and use this to determine $H^{*}=H^{*}(k u ; \mathbb{Z} / 2)$.

Consider the cohomology diagram:
![img-4.jpeg](img-4.jpeg)

The Steenrod algebra $A$ is a free module over $E_{1}=E\left(Q_{0}, Q_{1}\right)$, so $A / / E_{0}$ is a free module over $E_{1} / / E_{0} \cong E\left(Q_{1}\right)$, and so $\operatorname{im}(d)=\operatorname{ker}(d) \subset A / / E_{0}$ are both equal to the submodule generated by the class of $Q_{1}$ in $A / / E_{0}$.

Thus $\operatorname{ker}\left(i_{1}^{*}\right) \subseteq \operatorname{ker}(d)=\operatorname{im}(d) \subseteq \operatorname{im}\left(j_{1}^{*}\right)=\operatorname{ker}\left(i_{1}^{*}\right)$ must be a chain of equalities. Thus $\operatorname{im}\left(i_{1}^{*}\right) \cong\left(A / / E_{0}\right) / \operatorname{im}\left(j_{1}^{*}\right)=\left(A / / E_{0}\right) / \operatorname{im}(d)=A / / E_{1}$ is contained in $H^{*}$.

We have a map of exact sequences
![img-5.jpeg](img-5.jpeg)
where the vertical maps are known to be injective. Inductively assume $v_{1}^{*}: H^{*} \rightarrow$ $\Sigma^{2} H^{*}$ is zero in degrees $\leq n$, so that the map $A / / E_{1} \rightarrow H^{*}$ is an isomorphism in these degrees. Then the map $\Sigma^{3} A / / E_{1} \rightarrow \Sigma^{3} H^{*}$ is an isomorphism in degrees $\leq n+3$ and $j_{1}^{*}$ must be injective in the same range of degrees. Hence $v_{1}^{*}: \Sigma H^{*} \rightarrow$ $\Sigma^{3} H^{*}$ is zero in degrees $\leq n+3$, which gives the induction hypothesis in degrees $\leq n+2$. The induction gets started since $k u$ is connective.

We conclude that $v_{1}$ induces the zero map in mod 2 cohomology, and that

$$
H^{*}(k u ; \mathbb{Z} / 2) \cong A / A\left\{S q^{1}, S q^{3}\right\}=A / / E_{1}
$$

(Note that $A\left\{S q^{1}, Q_{1}\right\}=A\left\{S q^{1}, S q^{3}\right\}$.)
This is really a Bockstein spectral sequence argument. The $E_{1}^{*}$-term is $A / / E_{0}$ and the $d_{1}^{*}$-differential is $d$. Since $\operatorname{im}(d)=\operatorname{ker}(d)$ we get $E_{2}^{*}=E_{\infty}^{*}=0$, so all the $v_{1}$-torsion in $H^{*}$ is annihilated by $v_{1}$ itself, and only $v_{1}$-divisible terms remain. But $H^{*}$ is connective and $v_{1}$ has positive degree, so there are no $v_{1}$-divisible terms. Thus $v_{1}^{*}=0, i_{1}^{*}$ is surjective and $H^{*} \cong\left(A / / E_{0}\right) / \operatorname{im}\left(j_{1}^{*}\right)=\left(A / / E_{0}\right) / \operatorname{im}(d)=A / / E_{1}$.

# COHOMOLOGY OF $k o$ 

To proceed to the cohomology of $k o$, we use the cofiber sequence

$$
\Sigma k o \xrightarrow{n} k o \xrightarrow{c} k u \xrightarrow{\partial} \Sigma^{2} k o
$$

which arises from real Bott periodicity. The left hand map arises by smashing the Hopf map $\eta: S^{1} \rightarrow S^{0}$ with ko. The middle map is a ring spectrum map induced by complexification of vector bundles.

Claim: The composite map $d=c \partial: k u \rightarrow \Sigma^{2} k u$ induces right multiplicaton by $S q^{2}$ in cohomology.

To see this, map the cofiber sequence

$$
S^{1} \xrightarrow{\eta} S^{0} \rightarrow C \eta \rightarrow S^{2}
$$

into the cofiber sequence above. The generator $\Sigma^{2} 1 \in H^{2}\left(\Sigma^{2} k u ; \mathbb{Z} / 2\right)$ pulls back to the generator of $H^{2}\left(\Sigma^{2} C \eta ; \mathbb{Z} / 2\right)$, which over $C \eta \rightarrow S^{2} \rightarrow \Sigma^{2} C \eta$ pulls back to the generator of $H^{2}(C \eta ; \mathbb{Z} / 2)$. Hence $d\left(\Sigma^{2} 1\right)$ is the nonzero class in degree 2 of $A / / E_{1}$, i.e., $S q^{2}$.

Briefly write $H^{*}=H^{*}(k o ; \mathbb{Z} / 2)$ and consider the cohomology diagram:
![img-6.jpeg](img-6.jpeg)

Now $A$ is a free $A_{1}$-module, and $d: \Sigma^{2} A / / E_{1} \rightarrow A / / E_{1}$ is induced up from the $A_{1}$-module homomorphism $d^{\prime}: \Sigma^{2} A_{1} / / E_{1} \rightarrow A_{1} / / E_{1}$ given by right multiplication by $S q^{2}$. Then $\operatorname{ker}\left(d^{\prime}\right)=\operatorname{im}\left(d^{\prime}\right) \subset A_{1} / / E_{1}$, and so $\operatorname{ker}(d)=\operatorname{im}(d) \subset A / / E_{1}$.

It follows as before that $\operatorname{im}\left(c^{*}\right) \cong\left(A / / E_{1}\right) / \operatorname{im}(d)=A / / A_{1}$ is contained in $H^{*}$. There is a map of exact sequences
![img-7.jpeg](img-7.jpeg)
where the vertical maps are known to be injective. Inductively assume $\eta^{*}: H^{*} \rightarrow$ $\Sigma H^{*}$ is zero in degrees $\leq n$, so that the map $A / / A_{1} \rightarrow H^{*}$ is an isomorphism in these degrees. Then the map $\Sigma^{2} A / / A_{1} \rightarrow \Sigma^{2} H^{*}$ is an isomorphism in degrees $\leq n+2$ and $\partial^{*}$ must be injective in the same range of degrees. Hence $\eta^{*}: \Sigma H^{*} \rightarrow \Sigma^{2} H^{*}$ is zero in degrees $\leq n+2$, which gives the induction hypothesis in degrees $\leq n+1$. The induction gets started since $k o$ is connective.

We conclude that $\eta$ induces the zero map on mod 2 cohomology, and that

$$
H^{*}(k o ; Z / 2) \cong A / / A_{1}=A / A\left\{S q^{1}, S q^{2}\right\}
$$

# COHOMOLOGY OF bo, bso AND bspin 

John RogNes

### 30.11 .00

## COHOMOLOGY OF bo, bso, bspin

The following material is drawn from John F. Adams and Stewart B. Priddy's paper "Uniqueness of BSO".

We now understand the Postnikov tower of $k u$ cohomologically. The cofiber sequence

$$
\Sigma^{2} k u \xrightarrow{v_{1}} k u \xrightarrow{i_{1}} H \mathbb{Z} \xrightarrow{j_{1}} \Sigma^{3} k u \xrightarrow{\Sigma v_{1}} \Sigma k u
$$

induces an exact sequence of $A$-modules

$$
\Sigma^{2} A / / E_{1} \stackrel{0}{\leftarrow} A / / E_{1} \leftarrow A / / E_{0} \leftarrow \Sigma^{3} A / / E_{1} \stackrel{0}{\leftarrow} \Sigma A / / E_{1}
$$

The middle part of this diagram is the short exact sequence induced from the following short exact sequence of $E_{1}$-modules:

$$
0 \leftarrow E_{1} / / E_{1} \leftarrow E_{1} / / E_{0} \leftarrow \Sigma^{3} E_{1} / / E_{1} \leftarrow 0
$$

by applying the exact functor $A \otimes_{E_{1}}(-)$. ( $A$ is free as a right $E_{1}$-module.) Additively this is the short exact sequence

$$
0 \leftarrow \mathbb{Z} / 2\{1\} \leftarrow \mathbb{Z} / 2\left\{1, Q_{1}\right\} \leftarrow \mathbb{Z} / 2\left\{Q_{1}\right\} \leftarrow 0
$$

The Postnikov tower for $k o$ is more interesting. The cofiber sequence

$$
b o \rightarrow k o \rightarrow H \mathbb{Z} \rightarrow \Sigma b o
$$

induces the exact sequence

$$
H^{*}(b o ; \mathbb{Z} / 2) \leftarrow A / / A_{1} \leftarrow A / / E_{0} \leftarrow \Sigma H^{*}(b o ; \mathbb{Z} / 2)
$$

Here bo is 0 -connected so the middle map is surjective in degree 0 , and therefore surjective in all degrees. Thus $\Sigma H^{*}(b o ; \mathbb{Z} / 2)$ is its kernel. The resulting extension is induced from an extension of $A_{1}$-modules:

$$
0 \leftarrow A_{1} / / A_{1} \leftarrow A_{1} / / E_{0} \leftarrow K \leftarrow 0
$$

by applying $A \otimes_{A_{1}}(-)$. ( $A$ is free as a right $A_{1}$-module.) Additively this is the short exact sequence

$$
0 \leftarrow \mathbb{Z} / 2\{1\} \leftarrow \mathbb{Z} / 2\left\{1, S q^{2}, S q^{3}, S q^{2} S q^{3}\right\} \leftarrow \mathbb{Z} / 2\left\{S q^{2}, S q^{3}, S q^{2} S q^{3}\right\} \leftarrow 0
$$

Note that the kernel $K$ is a cyclic $A_{1}$-module on the generator $S q^{2}$, with annihilator ideal $A_{1}\left\{S q^{2}\right\}$. This can be drawn as below, or vertically as a question-mark (?):
![img-8.jpeg](img-8.jpeg)

So $K \cong \Sigma^{2} A_{1} / A_{1}\left\{S q^{2}\right\}$, the extension above is

$$
0 \leftarrow A_{1} / / A_{1} \leftarrow A_{1} / / E_{0} \leftarrow \Sigma^{2} A_{1} / A_{1}\left\{S q^{2}\right\} \leftarrow 0
$$

and $\Sigma H^{*}(b o ; \mathbb{Z} / 2) \cong A \otimes_{A_{1}} \Sigma^{2} A_{1} / A_{1}\left\{S q^{2}\right\} \cong \Sigma^{2} A / A\left\{S q^{2}\right\}$. Thus

$$
H^{*}(b o ; \mathbb{Z} / 2) \cong \Sigma A / A\left\{S q^{2}\right\}
$$

Next, the cofiber sequence

$$
b s o \rightarrow b o \rightarrow \Sigma H \mathbb{Z} / 2 \rightarrow \Sigma b s o
$$

induces the exact sequence

$$
H^{*}(b s o ; \mathbb{Z} / 2) \leftarrow \Sigma A / A\left\{S q^{2}\right\} \leftarrow \Sigma A \leftarrow \Sigma H^{*}(b s o ; \mathbb{Z} / 2)
$$

Here $b s o$ is 1-connected, so the middle map is surjective in degree 1, and therefore surjective in all degrees. Thus $\Sigma H^{*}(b s o ; \mathbb{Z} / 2)$ is its kernel. The resulting extension is induced from an extension of $A_{1}$-modules

$$
0 \leftarrow A_{1} / A_{1}\left\{\underline{S} q^{2}\right\} \leftarrow A_{1} \leftarrow K^{\prime} \leftarrow 0
$$

by applying $\Sigma A \otimes_{A_{1}}(-)$. Additively this is the short exact sequence

$$
\begin{aligned}
0 \leftarrow \mathbb{Z} / 2\left\{1, S q^{1}, S q^{2} S q^{1}\right\} \leftarrow & A_{1} \leftarrow \\
& \mathbb{Z} / 2\left\{S q^{2}, S q^{3}, S q^{2} S q^{2}, S q^{2} S q^{3}, S q^{2} S q^{2} S q^{2}\right\} \leftarrow 0
\end{aligned}
$$

The kernel $K^{\prime}$ is a cyclic $A_{1}$-module on the generator $S q^{2}$, with annihilator ideal $A_{1}\left\{S q^{3}\right\}$. This can be drawn as below:
![img-9.jpeg](img-9.jpeg)

or more symmetrically as a joker's hat and face:
![img-10.jpeg](img-10.jpeg)

So $K^{\prime} \cong \Sigma^{2} A_{1} / A_{1}\left\{S q^{3}\right\}$, the extension above is

$$
0 \leftarrow A_{1} / A_{1}\left\{S q^{2}\right\} \leftarrow A_{1} \leftarrow \Sigma^{2} A_{1} / A_{1}\left\{S q^{3}\right\} \leftarrow 0
$$

and $\Sigma H^{*}(b s o ; \mathbb{Z} / 2) \cong \Sigma A \otimes_{A_{1}} \Sigma^{2} A_{1} / A_{1}\left\{S q^{3}\right\}$. Thus

$$
H^{*}(b s o ; \mathbb{Z} / 2) \cong \Sigma^{2} A / A\left\{S q^{3}\right\}
$$

Continuing, the cofiber sequence

$$
b \operatorname{spin} \rightarrow b s o \rightarrow \Sigma^{2} H \mathbb{Z} / 2 \rightarrow \Sigma b s p i n
$$

induces an exact sequence

$$
H^{*}(b \operatorname{spin} ; \mathbb{Z} / 2) \leftarrow \Sigma^{2} A / A\left\{S q^{3}\right\} \leftarrow \Sigma^{2} A \leftarrow \Sigma H^{*}(b \operatorname{spin} ; \mathbb{Z} / 2)
$$

Here bspin is 2 -connected, so the middle map is surjective in degree 2, and therefore surjective in all degrees. Thus $\Sigma H^{*}(b s p i n ; \mathbb{Z} / 2)$ is its kernel. The resulting extension is induced from an extension of $A_{1}$-modules

$$
0 \leftarrow A_{1} / A_{1}\left\{S q^{3}\right\} \leftarrow A_{1} \leftarrow K^{\prime \prime} \leftarrow 0
$$

by applying $\Sigma^{2} A \otimes_{A_{1}}(-)$. Additively this is the short exact sequence

$$
\begin{aligned}
& 0 \leftarrow \mathbb{Z} / 2\left\{1, S q^{1}, S q^{2}, S q^{2} S q^{1}, S q^{2} S q^{2}\right\} \leftarrow A_{1} \leftarrow \\
& \mathbb{Z} / 2\left\{S q^{3}, S q^{2} S q^{3}, S q^{1} S q^{2} S q^{3}\right\} \leftarrow 0 .
\end{aligned}
$$

The kernel $K^{\prime \prime}$ is a cyclic $A_{1}$-module on the generator $S q^{3}$, with annihilator ideal $A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\}$. This can be drawn as below, or vertically as an inverted question$\operatorname{mark}(\dot{\iota}):$
![img-11.jpeg](img-11.jpeg)

So $K^{\prime \prime} \cong \Sigma^{3} A_{1} / A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\}$, the extension above is

$$
0 \leftarrow A_{1} / A_{1}\left\{S q^{3}\right\} \leftarrow A_{1} \leftarrow \Sigma^{3} A_{1} / A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\} \leftarrow 0
$$

and $\Sigma H^{*}(b s p i n ; \mathbb{Z} / 2) \cong \Sigma^{2} A \otimes_{A_{1}} \Sigma^{3} A_{1} / A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\}$. Thus

$$
H^{*}(b s p i n ; \mathbb{Z} / 2) \cong \Sigma^{4} A / A\left\{S q^{1}, S q^{2} S q^{3}\right\}
$$

The final cofiber sequence

$$
\Sigma^{8} k o \rightarrow b \text { spin } \rightarrow \Sigma^{4} H \mathbb{Z} \rightarrow \Sigma^{9} k o
$$

induces the exact sequence

$$
0 \leftarrow \Sigma^{4} A / A\left\{S q^{1}, S q^{2} S q^{3}\right\} \leftarrow \Sigma^{4} A / / E_{0} \leftarrow \Sigma^{9} A / / A_{1} \leftarrow 0
$$

obtained by applying $\Sigma^{4} A \otimes_{A_{1}}(-)$ to the short exact sequence

$$
0 \leftarrow A_{1} / A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\} \leftarrow A_{1} / / E_{0} \leftarrow \Sigma^{5} A_{1} / / A_{1} \leftarrow 0
$$

of $A_{1}$-modules. Here the right hand map takes the generator to the class of $S q^{2} S q^{2}=S q^{5}+S q^{4} S q^{1}$ in $A_{1} / / E_{0}$.

Later we can consider the Postnikov towers for $k u$ and $k o$ and form the associated cohomology spectral sequences. The extensions above completely determine the differential structure.

Department of Mathematics, University of Oslo
E-mail address: rognes@math.uio.no

# CONJUGATION 

John Rognes

### 07.12 .00

## Hopf algebras

Let $k$ be a commutative ring. Write $M \otimes N=M \otimes_{k} N$ for the tensor product of two graded $k$-modules $M$ and $N$. Let $T: M \otimes N \rightarrow N \otimes M$ be the twist isomorphism given by $T(a \otimes b)=(-1)^{|a||b|}(b \otimes a)$. Consider $k$ as a graded $k$-module concentrated in degree 0 . All modules will hereafter be graded $k$-modules without further mention.

An algebra $(A, \phi, \eta)$ is a module $A$ equipped with a product map $\phi: A \otimes A \rightarrow A$ and a unit map $\eta: k \rightarrow A$ such that the following diagrams commute:
![img-12.jpeg](img-12.jpeg)
(associativity),
![img-13.jpeg](img-13.jpeg)
(unitality). If $\phi \circ T=\phi: A \otimes A \rightarrow A$ we say that $A$ is a commutative algebra.
A coalgebra $(C, \psi, \epsilon)$ is a module $C$ equipped with a coproduct map $\psi: C \rightarrow$ $C \otimes C$ and a counit map $\epsilon: C \rightarrow k$ such that the following diagrams commute:
![img-14.jpeg](img-14.jpeg)
(coassociativity),
![img-15.jpeg](img-15.jpeg)

(counitality). If $T \circ \psi=\psi: C \rightarrow C \otimes C$ we say that $C$ is a cocommutative coalgebra.
Sometimes the product $\phi$ is called a multiplication, the coproduct $\psi$ is called a diagonal, the counit $\epsilon$ is called an augmentation and the unit $\eta$ is called a supplementation, as a later example will make clear.

Let $A$ be an algebra. The tensor product $A \otimes A$ is again an algebra with product

$$
(A \otimes A) \otimes(A \otimes A) \xrightarrow{(23)} A \otimes A \otimes A \otimes A \xrightarrow{\phi \otimes \phi} A \otimes A
$$

where $(23)=1 \otimes T \otimes 1$ transposes the second and third tensor factors. The unit map is

$$
k \cong k \otimes k \xrightarrow{\eta \otimes \eta} A \otimes A
$$

Suppose $B$ is both an algebra and a coalgebra, i.e., comes equipped with a product $\phi$, coproduct $\psi$, unit $\eta$ and counit $\epsilon$, making the four diagrams above commute. We say that $B$ is a bialgebra if the coproduct $\psi: B \rightarrow B \otimes B$ and counit $\epsilon: B \rightarrow k$ are algebra maps, where $B \otimes B$ has the algebra structure just introduced.

This is to say that the diagram
![img-16.jpeg](img-16.jpeg)
commutes, together with the unitality conditions $\psi \eta=\eta \otimes \eta, \epsilon \phi=\epsilon \otimes \epsilon$ and $\epsilon \eta=1_{k}$.
Dually one might define a coalgebra structure on $B \otimes B$ and demand that the product $\phi: B \otimes B \rightarrow B$ and unit $\eta: k \rightarrow B$ be coalgebra maps, but this turns out to be equivalent to the conditions just given. A bialgebra may be commutative or cocommutative, meaning that the underlying algebra is commutative, or that the underlying coalgebra is cocommutative, respectively.

A Hopf algebra $H$ is a bialgebra equipped with a conjugation map $\chi: H \rightarrow H$ making the following diagram commute:
![img-17.jpeg](img-17.jpeg)

In symbols, $\phi(1 \otimes \chi) \psi=\eta \epsilon=\phi(\chi \otimes 1) \psi$.
Topological GROUPS
Let $G$ be a topological group. Then $H_{*}(G ; k)$ is a graded $k$-module. Suppose that $H_{*}(G ; k)$ is flat as a graded $k$-module, meaning that the functor $H_{*}(G ; k) \otimes(-)$ is exact. Then there is a Künneth isomorphism

$$
H_{*}(G ; k) \otimes H_{*}(G ; k) \stackrel{\times}{\cong} H_{*}(G \times G ; k)
$$

For example, if $H_{*}(G ; k)$ is a free $k$-module in each degree, then it is flat. This always holds if $k$ is a field, such as $\mathbb{F}_{p}$ or $\mathbb{Q}$.

Lemma. Let $H=H_{*}(G ; k)$. Then $H$ is a cocommutative Hopf algebra.
The group product $\mu: G \times G \rightarrow G$ induces the product map

$$
\phi: H_{*}(G ; k) \otimes H_{*}(G ; k) \cong H_{*}(G \times G ; k) \xrightarrow{\mu_{*}} H_{*}(G ; k)
$$

while the inclusion of the unit element $e \in G$ induces the unit map

$$
\eta: k \cong H_{*}(\{e\} ; k) \rightarrow H_{*}(G ; k)
$$

The resulting algebra structure on $H_{*}(G ; k)$ is called the Pontryagin algebra of $G$. It will be commutative if e.g. $G$ is homotopy commutative.

The diagonal map $\Delta: G \rightarrow G \times G$ induces the coproduct map

$$
\psi: H_{*}(G ; k) \xrightarrow{\Delta_{*}} H_{*}(G \times G ; k) \cong H_{*}(G ; k) \otimes H_{*}(G ; k)
$$

while the unique map $G \rightarrow\{e\}$ induces the counit map

$$
\epsilon: H_{*}(G ; k) \rightarrow H_{*}(\{e\} ; k) \cong k
$$

There results a coalgebra structure on $H_{*}(G ; k)$. It is cocommutative since $t \Delta=\Delta$ where $t: G \times G \rightarrow G \times G$ is the transposition inducing $T$ on homology. More generally $H_{*}(X ; k)$ is a cocommutative coalgebra for any space $X$ such that the homology $H_{*}(X ; k)$ is flat over $k$.

The algebra and coalgebra structures on $H_{*}(G ; k)$ are compatible, and thus define a cocommutative bialgebra structure.

The group inverse $\iota: G \rightarrow G$ induces the conjugation map $\chi: H_{*}(G ; k) \rightarrow$ $H_{*}(G ; k)$. The right and left inverse conditions $g \cdot g^{-1}=e=g^{-1} \cdot g$ assert that $\mu(1 \times \iota) \Delta(g)=e=\mu(\iota \times 1) \Delta(g)$ for all $g \in G$. Hence the induced maps on homology satisfy the conjugation conditions, making the hexagonal diagram commute.

Thus $H_{*}(G ; k)$ is a cocommutative Hopf algebra.
Hopf algebras are sometimes called quantum groups, when the category of groups is viewed as embedded into the category of Hopf algebras in this fashion.

When $G$ is a discrete group, $H_{*}(G ; k)=k[G]$ is the group ring of $G$ over $k$ concentrated in degree $k$. The coproduct $\psi: k[G] \rightarrow k[G] \otimes k[G]$ takes $g$ to $g \otimes g$ and the counit $\epsilon: k[G] \rightarrow k$ takes $g$ to 1 , for every $g \in G$.

# Connected Hopf Algebras 

A graded $k$-module $M=M_{*}$ with an augmentation $\epsilon: M \rightarrow k$ is said to be connected if it $M_{n}=0$ for $n<0$ and the map $\epsilon: M_{0} \rightarrow k$ in degree 0 is an isomorphism.

If $B=B_{*}$ is a connected bialgebra, the unit $1=\eta(1)$ generates $B_{0}$ as a free $k$-module, since $\epsilon \eta=1_{k}$.

Let $B$ be a connected bialgebra. The coproduct $\psi(a) \in B \otimes B$ of a class $a \in B$ in a positive degree can be written

$$
\psi(a)=a \otimes 1+1 \otimes a+\sum_{i} a_{i}^{\prime} \otimes a_{i}^{\prime \prime}
$$

where $a_{i}^{\prime}, a_{i}^{\prime \prime} \in B$ are in positive degrees, of degree less than that of $a$. This follows from counitality.

In this case there exists a unique conjugation $\chi$. Let $\chi(1)=1$. For $a$ in positive degrees we must have $\phi(1 \otimes \chi) \psi(a)=\eta \epsilon(a)=0$, which in the notation above yields

$$
a \cdot 1+1 \cdot \chi(a)+\sum_{i} a_{i}^{\prime} \cdot \chi\left(a_{i}^{\prime \prime}\right)=0
$$

This gives the recursive definition

$$
\chi(a)=-a-\sum_{i} a_{i}^{\prime} \cdot \chi\left(a_{i}^{\prime \prime}\right)
$$

Note that this works because each $a_{i}^{\prime \prime}$ has lower degree than $a$.
Proposition (Milnor-Moore). Let $B$ be a connected bialgebra. Then $B$ is a Hopf algebra, with:conjugation $\chi$ defined as above.

The only thing that requires proof is that $\phi(\chi \otimes 1) \psi(a)=\eta \epsilon(a)$, which goes by a lengthy multiple induction on the degree of $a$.
Lemma. The mod $p$ Steenrod algebra $A=\mathcal{A}(p)$ is a cocommutative Hopf algebra, with conjugation $\chi: A \rightarrow A$ satisfying

$$
\sum_{i+j=k} S q^{i} \cdot \chi\left(S q^{j}\right)=0
$$

for $p=2$ and $k>0$, and

$$
\sum_{i+j=k} P^{i} \cdot \chi\left(P^{j}\right)=0
$$

for $p$ odd and $k>0$. In the odd case $\chi(\beta)=-\beta$.
This follows from the coproduct formulas:

$$
\begin{aligned}
\psi\left(S q^{k}\right) & =\sum_{i+j=k} S q^{i} \otimes S q^{j} \\
\psi\left(P^{k}\right) & =\sum_{i+j=k} P^{i} \otimes P^{j} \\
\psi(\beta) & \equiv \beta \otimes 1+1 \otimes \beta
\end{aligned}
$$

For example we have $\chi\left(S q^{1}\right)=S q^{1}, \chi\left(S q^{2}\right)=S q^{2}, \chi\left(S q^{3}\right)=S q^{2} S q^{1}$ and $\chi\left(S q^{4}\right)=S q^{4}+S q^{3} S q^{1}$.
((Show that $\chi$ an anti-homomorphism, satisfying $\chi(a b)=\chi(b) \chi(a)$. Why is $\chi \chi=1$ ?))
The dual Steenrod algebra is also connected.
Lemma. The dual mod $p$ Steenrod algebra $A_{*}=\mathcal{A}(p)_{*}$ is a commutative Hopf algebra, with conjugation $\chi: A_{*} \rightarrow A_{*}$ satisfying

$$
\sum_{i+j=k} \xi_{i}^{2^{j}} \cdot \chi\left(\xi_{j}\right)=0
$$

for $p=2$ and $k>0$,

$$
\sum_{i+j=k} \xi_{i}^{p^{j}} \cdot \chi\left(\xi_{j}\right)=0
$$

for $p$ odd and $k>0$, and

$$
\tau_{k}+\sum_{i+j=k} \xi_{j}^{p^{j}} \cdot \chi\left(\tau_{j}\right)=0
$$

for $p$ odd and $k \geq 0$.
This follows from the coproduct formulas:

$$
\begin{aligned}
& \psi\left(\xi_{k}\right)=\sum_{i+j=k} \xi_{i}^{2^{j}} \otimes \xi_{j} \\
& \psi\left(\xi_{k}\right)=\sum_{i+j=k} \xi_{i}^{p^{j}} \otimes \xi_{j} \\
& \psi\left(\tau_{k}\right)=\tau_{k} \otimes 1+\sum_{i+j=k} \xi_{i}^{p^{j}} \otimes \tau_{j}
\end{aligned}
$$

For example we have $\chi\left(\xi_{1}\right)=\xi_{1}, \chi\left(\xi_{2}\right)=\xi_{2}+\xi_{1}^{3}$ and $\chi\left(\xi_{3}\right)=\xi_{3}+\xi_{1} \xi_{2}^{2}+\xi_{1}^{4} \xi_{2}+\xi_{1}^{7}$. For brevity we often write $\tilde{\xi}_{k}=\chi\left(\xi_{k}\right)$.

# SKEW MAPS 

Let $G$ be a topological group and $H \subset G$ a closed subgroup. Suppose that $X$ is a left $G$-space. We can form the orbit space $G / H$ of cosets $g H$ with $g \in G$, and the balanced product $G \times_{H} X$ of pairs $(g, x)$ with $g \in G, x \in X$, subject to the relation $(g h, x) \simeq(g, h x)$ for $h \in H$. Write $[g, x] \in G \times_{H} X$ for the resulting equivalence class of $(g, x)$.

The product $G / H \times X$ is a left $G$-space, with $G$ acting diagonally by left multiplication on both factors $G / H$ and $X$. Likewise the left $G$-action on the left factor of $G \times X$ (only) descends to a left $G$-action on $G \times_{H} X$.
Lemma. There are inverse homeomorphisms of left $G$-spaces

$$
G / H \times X \cong G \times_{H} X
$$

taking $(g H, x)$ to $\left[g, g^{-1} x\right]$ and $[g, x]$ to $(g H, g x)$, respectively.
Note that while the definition of $G \times_{H} X$ only uses the (restricted) $H$-action on $X$, the existence of the above homeomorphism uses that it extends to a $G$-action. We view this homeomorphism as untwisting the diagonal $H$-action on $G \times X$ to an action on the left factor $G$ only.

Similarly, let $A$ be an algebra, let $B \subset A$ be a subalgebra with an augmentation ( $=$ counit) $\epsilon: B \rightarrow k$, and let $M$ be a left $A$-module, i.e., a module over the underlying algebra of $A$. Then we can form the quotient left $A$-module $A / / B=$ $A \otimes_{B} k$. Here $A$ is a right $B$-module via the inclusion and $k$ is a left $B$-module via the augmentation. Alternatively

$$
A / / B=A / A \cdot I B
$$

where $I B=\operatorname{ker}(\epsilon: B \rightarrow k)$ is the augmentation ideal of $B$. Applying $A \otimes_{B}(-)$ to the short exact sequence of left $B$-modules

$$
0 \rightarrow I B \rightarrow B \xrightarrow{\epsilon} k \rightarrow 0
$$

yields the half-exact sequence of left $A$-modules

$$
A \otimes_{B} I B \rightarrow A \xrightarrow{\pi} A / / B \rightarrow 0
$$

which explains the displayed formula.

Lemma. Let $A$ be a Hopf algebra, let $B \subset A$ be a Hopf subalgebra and let $M$ be a left A-module. There are inverse isomorphisms of left A-modules

$$
A / / B \otimes M \cong A \otimes_{B} M
$$

taking $[a] \otimes m$ to $\sum_{i} a_{i}^{\prime} \otimes_{B} \chi\left(a_{i}^{\prime \prime}\right) \cdot m$ and $a \otimes_{B} m$ to $\sum_{i}\left[a_{i}^{\prime}\right] \otimes a_{i}^{\prime \prime} \cdot m$ Here $\psi(a)=$ $\sum_{i} a_{i}^{\prime} \otimes a_{i}^{\prime \prime}$ and $\chi$ are the coproduct and conjugation in $A$, while $[a]=\pi(a)$ is the image of $A$ in $A / / B$.

Here $A / / B \otimes M$ is a left $A$-module by the diagonal action, which factors through the coproduct $\psi: A \rightarrow A \otimes A$, while $A \otimes_{B} M$ has the left $A$-module structure induced up from the (restricted) left $B$-module structure on $M$.

The proof is by straight-forward calculation in both cases. Note that the coproduct and conjugation on $A$ are used in an essential way.

# What is SEEN by a homology theory? 

The subalgebras $E_{n}, A_{n} \subset A$ are Hopf subalgebras of the Steenrod algebra. Here $A_{n}$ is generated by $S q^{i}$ for $i \leq 2^{n}$, so $A_{n}$ is clearly closed under coproducts and conjugation. The case of $E_{n}$ is perhaps better studied in the dual situation, but for $E_{1}=E\left(Q_{0}, Q_{1}\right)$ we can see directly that $\chi\left(Q_{1}\right)=\chi\left(S q^{3}+S q^{2} S q^{1}\right)=$ $S q^{2} S q^{1}+S q^{3}=Q_{1}$, so $\chi$ acts trivially on $E_{1}$.
(We have $E_{n *}=A_{*} / I E_{n *}$ with $I E_{n *}=\left(\xi_{1}^{2}, \ldots, \xi_{n+1}^{2}, \xi_{n+2}, \ldots\right)$ a Hopf ideal. From

$$
\chi\left(\xi_{k}\right)=\sum_{i=1}^{k-1} \xi_{i}^{2^{k-i}} \cdot \chi\left(\xi_{k-i}\right)+\xi_{k}
$$

it follows that $\chi\left(\xi_{k}\right) \equiv \xi_{k} \bmod I E_{n *}$, so $\chi=1$ on $E_{n *}$ and thus, dually, also on $\left.E_{n}.\right)$ )

Let $E$ be a spectrum. The $E$-homology of a spectrum $X$ is defined as the homotopy of the smash product $E \wedge X$ :

$$
E_{*}(X)=\pi_{*}(E \wedge X)
$$

One approach to understanding these homotopy groups is by the Adams spectral sequence, which takes as input the corresponding $\bmod p$ cohomology groups $H^{*}(E \wedge$ $\left.X ; \mathbb{F}_{p}\right)$ as a left $A$-module, where $A$ is the $\bmod p$ Steenrod algebra. There is a Künneth isomorphism

$$
H^{*}\left(E \wedge X ; \mathbb{F}_{p}\right) \cong H^{*}\left(E ; \mathbb{F}_{p}\right) \otimes H^{*}\left(X ; \mathbb{F}_{p}\right)
$$

of left $A$-modules, where $a \in A$ acts on the right hand side via $\psi(a) \in A \otimes A$.
Now suppose $H^{*}\left(E ; \mathbb{F}_{p}\right) \cong A / / B$ as a left $A$-module. By the lemma above, with $M=H^{*}\left(X ; \mathbb{F}_{p}\right)$, we get an isomorphism

$$
A / / B \otimes H^{*}\left(X ; \mathbb{F}_{p}\right) \cong A \otimes_{B} H^{*}\left(X ; \mathbb{F}_{p}\right)
$$

of left $A$-modules. To evaluate the right hand side we only need to know the restricted $B$-module structure on $H^{*}\left(X ; \mathbb{F}_{p}\right)$.

For example, with $E=k o$ and $p=2$ we have $H^{*}\left(k o ; \mathbb{F}_{2}\right)=A / / A_{1}$, and to understand the ko-homology of a spectrum $X$ it usually suffices to understand

$$
H^{*}\left(k o \wedge X ; \mathbb{F}_{2}\right) \cong A \otimes_{A_{1}} H^{*}\left(X ; \mathbb{F}_{2}\right)
$$

Thus principally the $A_{1}$-module structure on $H^{*}\left(X ; \mathbb{F}_{2}\right)$ is seen by ko-homology, i.e., the action by $S q^{1}$ and $S q^{2}$.

Similarly, with $E=k u$ and $p=2$ we have $H^{*}\left(k u ; \mathbb{F}_{2}\right)=A / / E_{1}$, so

$$
H^{*}\left(k u \wedge X ; \mathbb{F}_{2}\right) \cong A \otimes_{E_{1}} H^{*}\left(X ; \mathbb{F}_{2}\right)
$$

only involves the $E_{1}$-module structure on $H^{*}\left(X ; \mathbb{F}_{2}\right)$, i.e., the action by $Q_{0}=S q^{1}$ and $Q_{1}$.

The Hopkins-Miller spectrum $e o_{2}$ has $H^{*}\left(e o_{2} ; \mathbb{F}_{2}\right)=A / / A_{2}$, so

$$
H^{*}\left(e o_{2} \wedge X ; \mathbb{F}_{2}\right) \cong A \otimes_{A_{2}} H^{*}\left(X ; \mathbb{F}_{2}\right)
$$

and the $e o_{2}$-homology of a spectrum $X$ sees what is determined by the the $A_{2^{-}}$ module structure on $H^{*}\left(X ; \mathbb{F}_{2}\right)$, i.e., the actions of $S q^{1}, S q^{2}$ and $S q^{4}$.

The connective $n$th Morava K-theory $k(n)$ has $H^{*}\left(k(n) ; \mathbb{F}_{p}\right)=A / / E\left(Q_{n}\right)$, where $E\left(Q_{n}\right) \subset A$ is a Hopf subalgebra for every $n \geq 0$. Thus $k(n)$-homology $k(n)_{*}(X)=$ $\pi_{*}(k(n) \wedge X)$ is tied only to the $Q_{n}$-action on $H^{*}\left(X ; \mathbb{F}_{p}\right)$ (modulo differentials in the Adams spectral sequence). Similar considerations appear in the context of motivic stable homotopy theory in the work of V. Voevodsky.
((Get equivalences bo $\simeq k o \wedge K$ where $H^{*}\left(K ; \mathbb{F}_{2}\right)=\Sigma A_{1} / A_{1}\left\{S q^{2}\right\}$, bso $\simeq k o \wedge K^{\prime}$ where $H^{*}\left(K^{\prime} ; \mathbb{F}_{2}\right)=\Sigma^{2} A_{1} / A_{1}\left\{S q^{3}\right\}$ and bspin $\simeq k o \wedge K^{\prime \prime}$ where $H^{*}\left(K^{\prime \prime} ; \mathbb{F}_{2}\right)=$ $\Sigma^{4} A_{1} / A_{1}\left\{S q^{1}, S q^{2} S q^{3}\right\}$.))
((Dualize to describe conjugation on $A_{*}$. Deduce $H_{*}\left(H \mathbb{Z} ; \mathbb{F}_{2}\right)=P\left(\bar{\xi}_{1}^{2}, \bar{\xi}_{k} \mid k \geq\right.$ 2), $H_{*}\left(k u ; \mathbb{F}_{2}\right)=P\left(\bar{\xi}_{1}^{2}, \bar{\xi}_{2}^{2}, \xi_{k} \mid k \geq 3\right)$ and $H_{*}\left(k o ; \mathbb{F}_{2}\right)=P\left(\bar{\xi}_{1}^{4}, \bar{\xi}_{2}^{2}, \xi_{k} \mid k \geq 3\right)$ as subalgebras of $A_{*}$.))

Department of Mathematics, University of Oslo
E-mail address: rognes@math.ulo.no

.