# Spectral sequences, décalage, and the Beilinson $t$-structure 

Benjamin Antieau

November 15, 2024


#### Abstract

This paper explains the theory of spectral sequences via décalage and the Beilinson $t$-structure.


| $\pi_{s} \mathrm{~F}^{*} M$ | $\mathrm{E}_{n, t}^{1}=\pi_{s+t} \mathrm{gr}^{-s} M \Rightarrow \pi_{s+t} M$ | $(-r, r-1)$ | $\mathrm{F}^{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{\pi_{s, s+n}}^{\infty}$ |
| :-- | :-- | :-- | :-- | :-- |
| $\pi_{s} \mathrm{~F}_{*} M$ | $\mathrm{E}_{n, t}^{1}=\pi_{s+t} \mathrm{gr}_{s} M \Rightarrow \pi_{s+t} M$ | $(-r, r-1)$ | $\mathrm{F}_{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}_{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{\pi_{s-s+n}}^{\infty}$ |
| $\mathrm{H}^{s} \mathrm{~F}^{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s+t} \mathrm{gr}^{s} M \Rightarrow \mathrm{H}^{s+t} M$ | $(r,-r+1)$ | $\mathrm{F}^{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}^{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{s-s+n}$ |
| $\mathrm{H}^{s} \mathrm{~F}_{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s+t} \mathrm{gr}_{-s} M \Rightarrow \mathrm{H}^{s+t} M$ | $(r,-r+1)$ | $\mathrm{F}_{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}_{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{-s, s+n}$ |

Figure 1: Spectral sequence conventions for decreasing filtrations $\mathrm{F}^{*}$ and increasing filtrations $\mathrm{F}_{*}$. We use $\Rightarrow$ even when no convergence is implied.

| $\pi_{s} \mathrm{~F}^{*} M$ | ${ }^{t} \mathrm{E}_{s, t}^{2}=\mathrm{E}_{-t, s+2 t}^{1}=\pi_{s+t} \mathrm{gr}^{t} M \Rightarrow \pi_{s+t} M$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{\pi_{s+n, s}}^{\infty}$ |
| :-- | :-- | :-- |
| $\pi_{s} \mathrm{~F}_{*} M$ | ${ }^{t} \mathrm{E}_{s, t}^{2}=\mathrm{E}_{-t, s+2 t}^{1}=\pi_{s+t} \mathrm{gr}_{-t} M \Rightarrow \pi_{s+t} M$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{\pi+n,-s}^{\infty}$ |
| $\mathrm{H}^{s} \mathrm{~F}^{*} M$ | ${ }^{t} \mathrm{E}_{2}^{s, t}=\mathrm{E}_{1}^{-t, s+2 t}=\mathrm{H}^{s+t} \mathrm{gr}^{-t} M \Rightarrow \mathrm{H}^{s+t} M$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{s+n,-s}$ |
| $\mathrm{H}^{s} \mathrm{~F}_{*} M$ | ${ }^{t} \mathrm{E}_{2}^{s, t}=\mathrm{E}_{1}^{-t, s+2 t}=\mathrm{H}^{s+t} \mathrm{gr}_{t} M \Rightarrow \mathrm{H}^{s+t} M$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{-s+n, s}$ |

Figure 2: Reindexing to ${ }^{t} \mathrm{E}^{2}$. The differentials have the same bidegree as in the $\mathrm{E}^{1}$-spectral sequences from Figure 1. The filtrations on the abutment are also defined in the same way as in the $\mathrm{E}^{1}$ spectral sequences.

| $\pi_{s} \mathrm{~F}^{*} M$ | $\mathrm{E}_{n, t}^{1}=\pi_{s} \mathrm{gr}^{t} M \Rightarrow \pi_{s} M$ | $(-1, r)$ | $\mathrm{F}^{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{\pi, s}^{\infty}$ |
| :-- | :-- | :-- | :-- | :-- |
| $\pi_{s} \mathrm{~F}_{*} M$ | $\mathrm{E}_{n, t}^{1}=\pi_{s} \mathrm{gr}_{-t} M \Rightarrow \pi_{s} M$ | $(-1, r)$ | $\mathrm{F}_{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}_{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{\pi,-s}^{\infty}$ |
| $\mathrm{H}^{s} \mathrm{~F}^{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s} \mathrm{gr}^{-t} M \Rightarrow \mathrm{H}^{s} M$ | $(1,-r)$ | $\mathrm{F}^{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}^{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{n,-s}$ |
| $\mathrm{H}^{s} \mathrm{~F}_{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s} \mathrm{gr}_{t} M \Rightarrow \mathrm{H}^{s} M$ | $(1,-r)$ | $\mathrm{F}_{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}_{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{n, s}$ |

Figure 3: Adams indexing spectral sequence conventions.

# 1 Introduction 

There has been a recent cultural movement best portrayed as:
"there is a spectral sequence" $\Rightarrow$ "there is a filtration".
This move is due to the fact that filtrations admit better functorial properties than spectral sequences. For example, Bhatt, Morrow, and Scholze use quasisyntomic descent in [7] to define new filtrations on topological Hochschild homology and related invariants of $p$-adic rings by reducing to particularly simple cases. This requires descending a filtration, where descending a spectral sequence would not classically be meaningful.

The Beilinson $t$-structure plays an important role in [7] and one can also use the Beilinson $t$-structure to construct related filtrations on integral periodic cyclic homology, as in [1], or on TP of schemes in characteristic $p$, as in [3]. Given a stable $\infty$-category $\mathcal{C}$ which admits sequential limits and equipped with a $t$-structure, the Beilinson $t$-structure is a $t$-structure on $\mathrm{F} \mathcal{C}$, the $\infty$-category of filtered objects in $\mathcal{C}$, whose heart is the abelian category $\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right)$ of cochain complexes. Given a filtration $\mathrm{F}^{\star} \in \mathrm{F} \mathcal{C}$, the cochain complexes appearing as the homotopy objects with respect to the Beilinson $t$-structure are precisely the cochain complexes occurring on the $\mathrm{E}^{1}$-page of the associated spectral sequence. This $t$-structure was first defined and studied by Beilinson in $[6]$; see $[7,4,30]$ for recent treatments.

The goal of this paper is to explain the theory of spectral sequences as seen through the lens of the Beilinson $t$-structure. The main construction is the décalage $\operatorname{Dec}(\mathrm{F})^{\star}$ of a filtration $\mathrm{F}^{\star}$. If $\mathcal{C}$ additionally admits sequential colimits, then every filtered object $\mathrm{F}^{\star}$ of $\mathcal{C}$ admits an underlying object $\left|\mathrm{F}^{\star}\right|$ obtained by forgetting the filtration, or taking the colimit. Each connective cover $\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{F}^{\star}\right)$ in the Beilinson $t$-structure is, by definition, itself a filtered object in $\mathcal{C}$. Thus, given a filtered object $\mathrm{F}^{\star}$ one can obtain a new filtered object $\operatorname{Dec}(\mathrm{F})^{\star}$ by taking the underlying objects of the Whitehead tower

$$
\cdots \rightarrow\left|\tau_{\geqslant n+1}^{\mathrm{B}}\left(\mathrm{~F}^{\star}\right)\right| \rightarrow\left|\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{~F}^{\star}\right)\right| \rightarrow\left|\tau_{\geqslant n-1}^{\mathrm{B}}\left(\mathrm{~F}^{\star}\right)\right| \rightarrow \cdots
$$

This construction defines an endomorphism Dec: $\mathrm{F} \mathcal{C} \rightarrow \mathrm{F} \mathcal{C}$, the décalage functor. The main result of the paper is that décalage turns the page. Specifically, if $\mathcal{C}$ is a stable $\infty$-category equipped with a $t$-structure and $\mathrm{F}^{\star} \in \mathrm{F} \mathcal{C}$, there is an associated spectral sequence defined, for example, in [24, Sec. 1.2.2]. Below, an isomorphism of pages between two spectral sequences includes compatibility of the isomorphism the differentials.

Theorem 1.1 (See Theorem 4.13). Let $\mathcal{C}$ be a stable $\infty$-category which admits sequential limits and colimits and fix a $t$-structure on $\mathcal{C}$. For $r \geqslant 1$, the $\mathrm{E}^{r}$-page of the spectral sequence for $\operatorname{Dec}\left(\mathrm{F}^{\star}\right)$ is naturally isomorphic to the $\mathrm{E}^{r+1}$-page of the spectral sequence for $\mathrm{F}^{\star}$.

Let $\operatorname{Dec}^{(r-1)}\left(\mathrm{F}^{\star}\right)$ denote the $(r-1)$-fold composition of the décalage construction.
Corollary 1.2. The $\mathrm{E}^{r}$-page of the spectral sequence for $\mathrm{F}^{\star}$ is naturally isomorphic to the $\mathrm{E}^{1}$-page of the spectral sequence for $\operatorname{Dec}^{(r-1)}\left(\mathrm{F}^{\star}\right)$.

The corollary leads to a quick definition of the spectral sequence associated to a filtered object $\mathrm{F}^{\star} \in \mathrm{F} \mathcal{C}$.
Definition 1.3. Let $\mathrm{F}^{\star}$ be a filtered object in a stable $\infty$-category $\mathcal{C}$ with a $t$-structure and suppose that $\mathcal{C}$ admits sequential limits and colimits. Write the associated coherent cochain complex

$$
\cdots \rightarrow \mathrm{gr}^{-1}[-1] \rightarrow \mathrm{gr}^{0} \rightarrow \mathrm{gr}^{1}[1] \rightarrow \cdots
$$

obtained by pasting together the boundary maps

$$
\mathrm{F}^{n} / \mathrm{F}^{n+2} \rightarrow \mathrm{gr}^{n} \rightarrow \mathrm{gr}^{n+1}[1]
$$

and take homotopy objects with respect to the $t$-structure on $\mathcal{C}$ to obtain cochain complexes

$$
\cdots \rightarrow \pi_{t+1} \mathrm{gr}^{-1} M \rightarrow \pi_{t} \mathrm{gr}^{0} M \rightarrow \pi_{t-1} \mathrm{gr}^{1} M \rightarrow \cdots
$$

These form the $\mathrm{E}^{1}$-page of the spectral sequence associated to $\mathrm{F}^{*}$, where $\mathrm{E}_{s, t}^{1}=\pi_{s+t} \mathrm{gr}^{-s}$. To define the $\mathrm{E}^{r+1}$-page, for some $r \geqslant 0$, apply the décalage construction above $(r-1)$ times and take the $\mathrm{E}^{1}$-page of the resulting filtration, applying the transformation

$$
\left(\begin{array}{cc}
-r+1 & -r \\
r & r+1
\end{array}\right)
$$

to the indices.
Definition 1.3 gives a sequence of pages for which it is not hard to prove that the cohomology groups of one page agree with the terms on the next page. (See Remark 4.7.) In other words, Definition 1.3 produces a spectral sequence in the sense of any standard textbook, such as [27]. The homotopy coherent nature of the décalage functor makes it possible to make $\infty$-categorical arguments about the nature of the spectral sequence attached to a filtered object via Definition 1.3. For example, the multiplicative properties of these spectral sequences follow immediately from the fact that the décalage functor admits a lax symmetric monoidal structure. See Hedenlund's thesis [18] and also Section 8.

The content of Theorem 1.1 is that Definition 1.3 yields $\mathrm{E}^{r+1}$-pages and $d^{r+1}$-differentials which agree naturally for $r \geqslant 0$ with the usual definition of the spectral sequence of a filtration, for which our reference is [24, Const. 1.2.2.6].

The Beilinson $t$-structure implements in a homotopy coherent way Deligne's décalage functor, which was used to construct canonical mixed Hodge structures on the singular cohomology of complex algebraic varieties in [12, 13]. Suppose that $\mathrm{F}^{*} M^{\bullet}$ is a strictly filtered cochain complex and let $\operatorname{Dec}(\mathrm{F})^{*} M^{\bullet}$ be Deligne's décalage construction (see Definition 5.1), which is a new strict filtration on $M^{\bullet}$. One can put on each $\operatorname{Dec}(\mathrm{F})^{*} M^{\bullet}$ a secondary filtration $\mathrm{G}^{\circ} \operatorname{Dec}(\mathrm{F})^{*} M$ in such a way that $\mathrm{G}^{\circ} \operatorname{Dec}(\mathrm{F})^{*} M$ becomes a strictly bifiltered cochain complex.

Theorem 1.4 (See Theorem 5.4). There is a natural map $\mathrm{G}^{\circ} \operatorname{Dec}(\mathrm{F})^{*} M^{\bullet} \rightarrow \mathrm{F}^{*} M$ inducing an equivalence

$$
\mathrm{G}^{\circ} \operatorname{Dec}(\mathrm{F})^{*} M^{\bullet} \simeq \tau_{\geqslant*}^{\mathrm{B}}(\mathrm{~F}) M
$$

In particular, Delgine's strict décalage functor is equivalent to the $\infty$-categorical décalage functor.
An $\infty$-categorical form of décalage was constructed by Levine in [21] in the context of cosimplicial spectra. Levine does not use the language of the Beilinson $t$-structure, but does prove analogues of Theorems 1.1 and 1.4; see [21, Prop. 6.3] and [21, Rem. 6.4]. Theorem 1.4 was discovered independently by the author around 2019 and by Bhatt, Morrow, and Scholze [7]. The author discovered Theorem 1.1 as stated shortly thereafter and communicated it to several people. See for example [4, 14, 18, 28], which contain expositions of some of the ideas of this paper. In particular, the paper [14] of Gheorghe-Isaksen-Krause-Ricka shows that if $\operatorname{Tot}^{*}\left(\mathrm{MU}^{\bullet}\right)$ denotes the Adams tower associated to the Čech complex of $\mathbf{S} \rightarrow \mathrm{MU}$, then $\operatorname{Dec}\left(\operatorname{Tot}^{*}\left(\mathrm{MU}^{\bullet}\right)\right)$ is what is now called the even filtration $\mathbf{S}_{\mathrm{ev}}$ on the sphere spectrum in the language of [17]. Recently, Tyler Lawson [20] has given a generalized version of a décalage construction which applies more generally to filtrations in a broad class of $\infty$-categories, not just stable ones. Lawson gives a sketch of the agreement of $\mathrm{E}^{r}(\operatorname{Dec}(\mathrm{F}))$ and $\mathrm{E}^{r+1}(\mathrm{~F})$ in [20, Prop. 9.17].

Besides the theoretical results mentioned above, this paper is intended as a brief manual on spectral sequences, so more is included than strictly necessary for the proofs of the main theorems. For example, we include discussions of indexing conventions and convergence, which do not in fact require the methods

developed here. The convergence discussion is especially simplistic as we are awaiting forthcoming work of Hedenlund, Krause, and Nikolaus on a new approach to conditional convergence.

Two applications of the décalage approach to spectral sequences are given, namely to multiplicativity of spectral sequences and to the proof that the two standard constructions of the Atiyah-Hirzebruch spectral sequence agree from the $\mathrm{E}_{2}$-page on.

Additional related work. Our perspective places filtered objects at the heart of the study of spectral sequences, including the higher pages. By contrast, refer to work of Livernet-Whitehouse [22] or Cirici-Egas-Santander-Livernet [9] who study homotopy theories of extended spectral sequences and define décalage functors for these theories. In another direction, Cirici-Guillén [10] use Deligne's décalage to denote certain localizations of the homotopy theory of filtered complexes with applications to mixed Hodge theory.

Acknowledgments. Peter Scholze suggested to me the problem of constructing a "BMS" filtration on periodic cyclic homology and related invariants without $p$-completeness assumptions. This led to [1] and to an appreciation of the Beilinson $t$-structure. Akhil Mathew asked how the décalage used there relates to that defined by Deligne in [12], leading to this paper. I thank both for their motivating questions. Additionally, I thank Achim Krause and Thomas Nikolaus for explaining parts of their work on convergence.

This paper would never have been completed without the interest of Julie Creemers, Lennart Meier, and Itamar Mor. Additionally, Julie Creemers and Alice Hedenlund provided very helpful comments on a draft, for which I am very grateful.

I was supported by NSF grants DMS-2120005, DMS-2102010, and DMS-2152235, by Simons Fellowships 666565 and 00005925, and by the Simons Collaboration on Perfection. This paper was completed while I was a guest at the MPIM.

# $2 \quad t$-structures 

Stable $\infty$-categories are the natural higher categorical models of triangulated categories. We include a brief overview of the theory. For proofs and more details, see [24, Chap. 1] or [25, App. C].

Definition 2.1. (a) An $\infty$-category is pointed if it admits an object 0 which is both initial and terminal.
(b) If $\mathcal{C}$ is pointed and admits finite colimits, then there is a suspension functor $\Sigma: \mathcal{C} \rightarrow \mathcal{C}$ obtained by taking the pushout of the functors $0 \leftarrow \mathrm{id} \rightarrow 0$. The Spanier-Whitehead $\infty$-category of $\mathcal{C}$ is $\operatorname{SW}(\mathcal{C}) \simeq \operatorname{colim}\left(\mathcal{C} \xrightarrow{\Sigma} \mathcal{C} \xrightarrow{\Sigma} \cdots\right)$. An $\infty$-category is prestable if it is pointed, admits finite colimits, the suspension functor $\Sigma$ is fully faithful, and the essential image of the fully faithful functor $\mathcal{C} \rightarrow \mathrm{SW}(\mathcal{C})$ is closed under extensions.
(c) An $\infty$-category $\mathcal{C}$ is stable if it is pointed, admits finite colimits, and the suspension functor $\Sigma$ is an equivalence. If $\mathcal{C}$ is prestable, then $\operatorname{SW}(\mathcal{C})$ is prestable.

Definition 2.2. A functor $\mathcal{C} \rightarrow \mathcal{D}$ between stable $\infty$-categories is exact if it preserves finite colimits.
Fact 2.3. If $\mathcal{C}$ is a stable $\infty$-category, then its homotopy category $\operatorname{Ho}(\mathcal{C})$ admits a natural triangulated structure. If $f: \mathcal{C} \rightarrow \mathcal{D}$ is an exact functor between stable $\infty$-categories, then $\operatorname{Ho}(f): \operatorname{Ho}(\mathcal{C}) \rightarrow \operatorname{Ho}(\mathcal{D})$ is a triangulated functor.

No non-trivial pointed 1-category is stable or prestable. Indeed, in a pointed 1-category the suspension functor is the constant functor on 0 . In particular, triangulated categories are neither prestable nor stable.

Example 2.4. (a) The $\infty$-category $\mathcal{S p}$ is the stabilization (in $\operatorname{Pr}^{\mathrm{L}}$ ) of the $\infty$-category $\mathcal{S}$ of anima. This is a symmetric monoidal stable $\infty$-category which is compactly generated by its unit, the sphere spectrum $\mathbf{S}$. Thus, we will also write $\mathrm{D}(\mathbf{S})$ for $\mathcal{S p}$ as $\operatorname{Mod}_{\mathbf{S}}(\mathcal{S p}) \simeq \mathcal{S p}$.
(b) If $A$ is an $\mathbf{A}_{\infty}$-ring spectrum, then $\operatorname{LMod}_{A}(\mathrm{D}(\mathbf{S}))=\mathrm{D}(A)$ is the $\infty$-category of left $A$-module spectra. If $A$ is a dg algebra, then the homotopy category of $\mathrm{D}(A)$ is equivalent to the usual triangulated category of left dg modules over $A$ up to quasi-isomorphism. In particular, this holds when $A$ is a discrete commutative ring.
(c) If $X$ is a quasicompact and quasiseparated scheme, then $\mathrm{D}_{\mathrm{qc}}(X)=\lim _{\operatorname{Spec} R \rightarrow X} \mathrm{D}(R)$ defines a stable $\infty$-category whose homotopy category is the familiar triangulated category of complexes of sheaves of $\mathcal{O}_{X}$-modules with quasicoherent cohomology.

The theory of $t$-structures plays a fundamental role in this paper.
Definition 2.5. A $t$-structure on a stable $\infty$-category $\mathcal{C}$ consists of a pair $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ of full subcategories of $\mathcal{C}$ satisfying the following conditions:
(a) $\mathcal{C}_{\geqslant 0}[1] \subseteq \mathcal{C}_{\geqslant 0}$ and $\mathcal{C}_{\leqslant 0} \subseteq \mathcal{C}_{\leqslant 0}[1]$;
(b) if $X \in \mathcal{C}_{\geqslant 0}$ and $Y \in \mathcal{C}_{\leqslant 0}$, then the mapping space $\operatorname{Map}_{\mathcal{C}}(X, Y[-1])$ is contractible;
(c) every object $X$ in $\mathcal{C}$ fits into a fiber sequence $W \rightarrow X \rightarrow Z$ where $W \in \mathcal{C}_{\geqslant 0}$ and $Z[1] \in \mathcal{C}_{\leqslant 0}$.

It is not hard to see that to give a $t$-structure on $\mathcal{C}$ is equivalent to give one on its triangulated homotopy category $\operatorname{Ho}(\mathcal{C})$.

Remark 2.6. If $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ is a $t$-structure, then the inclusions of $\mathcal{C}_{\geqslant 0}$ and $\mathcal{C}_{\leqslant 0}$ into $\mathcal{C}$ admit right and left adjoints, respectively. This follows from a Bousfield localization argument using the orthogonality relation in (b) to show that given $X \in \mathcal{C}$ the sequence $W \rightarrow X \rightarrow Z$ is unique up to homotopy. The functor $\mathcal{C} \rightarrow \mathcal{C}_{\geqslant 0}$ is $\tau_{\geqslant 0}$, while $\mathcal{C} \rightarrow \mathcal{C}_{\leqslant 0}$ is $\tau_{\leqslant 0}$. No care will be taken to distinguish between these functors and the corresponding colocalization and localization functors $\mathcal{C} \rightarrow \mathcal{C}_{\geqslant 0} \hookrightarrow \mathcal{C}$ and $\mathcal{C} \rightarrow \mathcal{C}_{\leqslant 0} \hookrightarrow \mathcal{C}$.

More generally, one defines subcategories $\mathcal{C}_{\geqslant n} \simeq \mathcal{C}_{\geqslant 0}[n]$ and $\mathcal{C}_{\leqslant n} \simeq \mathcal{C}_{\leqslant 0}[n]$ for any integer $n$. There are corresponding truncation functors $\tau_{\geqslant n}: \mathcal{C} \rightarrow \mathcal{C}_{\geqslant n}$ and $\tau_{\leqslant n}: \mathcal{C} \rightarrow \mathcal{C}_{\leqslant n}$ for any $n$.

Definition 2.7. The objects of $\mathcal{C}_{\geqslant 0}$ are called connective while those of $\mathcal{C}_{\leqslant 0}$ are coconnective or 0-truncated. More generally, objects of $\mathcal{C}_{\geqslant n}$ are $n$-connective and those of $\mathcal{C}_{\leqslant n}$ are called $n$-truncated, or at times $n$ coconnective. Note: these notions depend on the chosen $t$-structure on $\mathcal{C}$. Often, as is the case in spectra or $\mathrm{D}(\mathbf{Z})$, this $t$-structure is not specified, in which case the standard $t$-structure is always implicit.

The following lemma guarantees that the order of application of truncation and connective cover functors is irrelevant.

Lemma 2.8. For any $m \leqslant n$, define $\mathcal{C}_{[m, n]}=\mathcal{C}_{\geqslant m} \cap \mathcal{C}_{\leqslant n}$. There is a natural equivalence $\tau_{\geqslant m} \circ \tau_{\leqslant n} \simeq \tau_{\leqslant n} \circ \tau_{\geqslant m}$ of functors $\mathcal{C} \rightarrow \mathcal{C}_{[m, n]}$.

Remark 2.9. Additionally, there are natural equivalences $\Sigma \circ \tau_{\geqslant n} \simeq \tau_{\geqslant n+1} \circ \Sigma$ and $\Sigma \circ \tau_{\leqslant n} \simeq \tau_{\leqslant n+1} \circ \Sigma$ and similarly for higher powers of $\Sigma$.

Definition 2.10. Given a $t$-structure on $\mathcal{C}$, the heart of the $t$-structure is the intersection $\mathcal{C}^{\odot}=\mathcal{C}_{\geqslant 0} \cap \mathcal{C}_{\leqslant 0}$. This turns out to be an abelian category, although it might be trivial. Given any integer $n$, one takes $\pi_{n}: \mathcal{C} \rightarrow \mathcal{C}^{\odot}$ to be the functor $\Sigma^{-n} \circ \tau_{\geqslant n} \circ \tau_{\leqslant n} \simeq \Sigma^{-n} \circ \tau_{\leqslant n} \circ \tau_{\geqslant n} \simeq \tau_{\leqslant 0} \circ \tau_{\geqslant 0} \circ \Sigma^{-n} \simeq \tau_{\geqslant 0} \circ \tau_{\leqslant 0} \circ \Sigma^{-n}$.

Remark 2.11. Given a fiber sequence $X \rightarrow Y \rightarrow Z$ in $\mathcal{C}$, there is an induced long exact sequence

$$
\cdots \rightarrow \pi_{n} X \rightarrow \pi_{n} Y \rightarrow \pi_{n} Z \rightarrow \pi_{n-1} X \rightarrow \cdots
$$

in $\mathcal{C}^{\odot}$. These sequences give a hands-on way for understanding stable $\infty$-categories using more familiar abelian categories.

Remark 2.12. If $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ is a $t$-structure on a stable $\infty$-category $\mathcal{C}$, then $\mathcal{C}_{\geqslant 0}$ is a prestable $\infty$-category which is closed under extensions in $\mathcal{C}$. The converse is true under the presence of enough colimits using a Bousfield localization argument. See [24, Prop. 1.4.4.11].

Example 2.13. (a) The $\infty$-category $\mathcal{S p} \simeq \mathrm{D}(\mathbf{S})$ of spectra admits a $t$-structure where $\mathcal{S}_{\mathrm{p}_{\geqslant 0}}$ is the full subcategory of spectra $X$ such that $\pi_{n} X=0$ for $n<0$ while $\mathcal{S}_{\mathrm{p} \leqslant 0}$ is the full subcategory of $X$ where $\pi_{n} X=0$ for $n>0$. The heart $\mathcal{S p}^{\odot}$ is the abelian category $\operatorname{Mod}_{\mathbf{Z}}$ of abelian groups.
(b) More generally, if $A$ is any connective $\mathbf{E}_{1}$-ring spectrum, then $\mathrm{D}(A)$ inherits a $t$-structure where $\mathrm{D}(A)_{\geqslant 0}$ consists of the $A$-module spectra $X$ where $\pi_{n} X=0$ for $n<0$ and $\mathrm{D}(A)_{\leqslant 0}$ consists of those where $\pi_{n} X=0$ for $n>0$. The connectivity assumption on $A$ guarantees that if $X$ is an $A$-module spectrum, then $\tau_{\geqslant 0} X$, where the truncation is taken in spectra, inherits a canonical $A$-module spectrum structure. The heart of this $t$-structure is naturally equivalent to the abelian category $\operatorname{Mod}_{\pi_{0} A}$ of left $\pi_{0} A$-modules. If $A$ is discrete, then this $t$-structure on $\mathrm{D}(A)$ recovers the usual $t$-structure on the derived $\infty$-category of $A$, which encodes the "good truncations" of complexes.
(c) If $\mathcal{C}$ is a stable $\infty$-category equipped with a $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ and if $I$ is an $\infty$-category, then the pair $\left(\operatorname{Fun}\left(I, \mathcal{C}_{\geqslant 0}\right), \operatorname{Fun}\left(I, \mathcal{C}_{\leqslant 0}\right)\right)$ forms a $t$-structure on $\operatorname{Fun}(I, \mathcal{C})$ with heart $\operatorname{Fun}(I, \mathcal{C})^{\odot} \simeq \operatorname{Fun}\left(I, \mathcal{C}^{\odot}\right) \simeq$ $\operatorname{Fun}\left(\operatorname{Ho}(I), \mathcal{C}^{\odot}\right)$, where $\operatorname{Ho}(I)$ denotes the homotopy category of $I$.

# 3 Beilinson's $t$-structure 

Filtered objects in a stable $\infty$-category have been studied in several places. See [4, 16, 23, 24, 29, 30].
Let $\mathbf{Z}$ denote the ordered set of integers viewed as a category so that there is a (unique) morphism $m \rightarrow n$ if and only if $m \leqslant n$, in which case the morphism is unique. Let $\mathbf{Z}^{\text {op }}$ be the opposite of $\mathbf{Z}$.
Definition 3.1. Let $\mathcal{C}$ be an $\infty$-category. The $\infty$-category of decreasing filtrations in $\mathcal{C}$ is

$$
\mathrm{FC}=\operatorname{Fun}\left(\mathbf{Z}^{\mathrm{op}}, \mathcal{C}\right)
$$

The $\infty$-category of increasing filtrations in $\mathcal{C}$ is $\operatorname{Fun}(\mathbf{Z}, \mathcal{C})$.
Remark 3.2. There is an equivalence $\mathbf{Z} \simeq \mathbf{Z}^{\text {op }}$ obtained by sending $m$ to $-m$. The theory of increasing filtrations and decreasing filtrations are thus equivalent, so we focus below on decreasing filtrations.

A decreasing filtration in $\mathcal{C}$ is represented as an infinite sequence

$$
\mathrm{F}^{*}: \cdots \rightarrow \mathrm{F}^{s+1} \rightarrow \mathrm{~F}^{s} \rightarrow \mathrm{~F}^{s-1} \rightarrow \cdots
$$

Included in the data of a functor $\mathbf{Z}^{\text {op }} \rightarrow \mathcal{C}$ is homotopy coherence data expressing for example a specific homotopy between $\mathrm{F}^{s+1} \rightarrow \mathrm{~F}^{s-1}$ and the composition of $\mathrm{F}^{s+1} \rightarrow \mathrm{~F}^{s}$ with $\mathrm{F}^{s} \rightarrow \mathrm{~F}^{s-1}$.

Example 3.3. If $\mathcal{C} \simeq \mathrm{D}(\mathbf{Z})$ is the $\infty$-category of $\mathbf{Z}$-module spectra, then $\mathrm{FD}(\mathbf{Z})$ is the $\infty$-category of filtered Z-module spectra. The homotopy category of $\mathrm{FD}(\mathbf{Z})$ is what is often called the derived category of filtered complexes. In fact, if $\mathrm{FMod}_{\mathbf{Z}}$ is the Grothendieck abelian category of filtered abelian groups, then $\mathrm{FD}(\mathbf{Z}) \simeq \mathrm{D}\left(\mathrm{FMod}_{\mathbf{Z}}\right)$ is its derived $\infty$-category. This follows for example from Proposition 3.31 below.

Warning 3.4. By Definition 3.1, a filtered object of $\mathrm{FMod}_{\mathbf{Z}}$ is an arbitrary $\mathbf{Z}^{\text {op }}$-indexed sequence of maps of abelian groups. There is no requirement that the transition maps in the sequence be injective. When they are, the filtration is called strict. The category of strict filtrations on $\operatorname{Mod}_{\mathbf{Z}}$ has kernels and cokernels, but is not abelian.

Often, one considers filtrations of specific objects.
Definition 3.5. A decreasing filtration on an object $X$ of $\mathcal{C}$ is a filtration $\mathrm{F}^{*}$ together with a map $\mathrm{F}^{*} \rightarrow X$ of filtrations, where $X$ denotes the constant decreasing filtration on $X$. A filtration $\mathrm{F}^{*}$ on $X$ is exhaustive if $X$ is a colimit of the diagram $\mathrm{F}^{*}$. In analogy with the ordinal $\omega+1$, one can consider the $\infty$-category of pairs $\left(\mathrm{F}^{*} \rightarrow X\right)$ of filtrations on objects of $\mathcal{C}$ as the functor category $\operatorname{Fun}\left(\mathbf{Z}^{\mathrm{op}}+1, \mathcal{C}\right)$, where $\mathbf{Z}^{\mathrm{op}}+1$ is the union of $\mathbf{Z}^{\mathrm{op}}$ and a new, terminal element $-\infty$. Of course, we have $\mathbf{Z}^{\mathrm{op}}+1 \simeq\left(\mathbf{Z}^{\mathrm{op}}\right)^{\triangleright} \simeq\left(\mathbf{Z}^{\triangleleft}\right)^{\mathrm{op}}$.

The picture to have in mind here is a large commutative diagram
![img-0.jpeg](img-0.jpeg)

Example 3.6. If $\mathcal{C}$ admits sequential colimits, then any filtration $\mathrm{F}^{*}$ can be viewed as giving a filtration on $\mathrm{F}^{-\infty}=\operatorname{colim}_{s} \mathrm{~F}^{s}$. This construction will appear frequently, so we denote it by $\left|\mathrm{F}^{*}\right|=\mathrm{F}^{-\infty}$. If $\mathrm{F}^{*}$ is a filtration on $X$, then there is a canonical map $\left|\mathrm{F}^{*}\right| \rightarrow X$, which is an equivalence if the filtration is exhaustive. If $\mathcal{C}$ has sequential colimits, the functor $|-|: \mathrm{FC} \rightarrow \mathcal{C}$ is left adjoint to the constant filtration functor $\mathcal{C} \rightarrow \mathrm{FC}$.

Notation 3.7. We use the notation $\mathrm{F}^{*}$ for a generic filtration to emphasize the primacy of the filtration as opposed to a possible object being filtered. Sometimes, we will write $\mathrm{F}^{*} X$ for a generic filtration as well, in which case, unless specified otherwise, $X=\left|\mathrm{F}^{*}\right|$.

Definition 3.8. If $\mathcal{C}$ has a final object $*$ and admits cofibers and if $\mathrm{F}^{*}$ is a decreasing filtration in $\mathcal{C}$, the associated graded pieces are

$$
\operatorname{gr}_{\mathrm{F}}^{*}=\operatorname{cofiber}\left(\mathrm{F}^{s+1} \rightarrow \mathrm{~F}^{s}\right)=\frac{\mathrm{F}^{s+1}}{\mathrm{~F}^{s}}
$$

for $s \in \mathbf{Z}$. The collection of associated graded pieces forms a graded object $\operatorname{gr}_{\mathrm{F}}^{*}$ of $\mathcal{C}$, i.e., an object of $\operatorname{Fun}\left(\mathbf{Z}^{\delta}, \mathcal{C}\right)$, where $\mathbf{Z}^{\delta}$ denotes the set $\mathbf{Z}$ viewed as a 1-category with only identity morphisms. If $\mathrm{F}^{*}$ is a filtration then its weights are the integers $s$ for which $\operatorname{gr}_{\mathrm{F}}^{*} \simeq \mathrm{~F}^{s} / \mathrm{F}^{s+1}$ is non-zero.

The underlying goal of spectral sequences, and this paper, is to explain how to understand $X$ from information about the graded pieces $\operatorname{gr}_{\mathrm{F}}^{*} X$ of some filtration $\mathrm{F}^{*} X$ on $X$. This understanding is what spectral sequences 'do'. For the remainder of this paper, filtrations are studied in the context of stable $\infty$-categories.

Definition 3.9. A filtration $\mathrm{F}^{*}$ in $\mathcal{C}$ is complete if $\mathrm{F}^{\infty}=\lim _{s} \mathrm{~F}^{s} \simeq 0$, the initial object of $\mathcal{C}$. In particular, the limit exists. Let $\widehat{\mathrm{F}} \mathcal{C} \subseteq \mathrm{FC}$ be the full subcategory of complete filtrations. If $\mathcal{C}$ admits sequential limits, then the inclusion $\widehat{\mathrm{F}} \mathcal{C} \subseteq \mathrm{FC}$ admits a left adjoint, called completion, given by $\widehat{\mathrm{F}}^{*}=\mathrm{F}^{*} / \mathrm{F}^{\infty}$. Let $\mathrm{F}^{*}$ be a decreasing filtration on an object $X$ of $\mathcal{C}$. The completion of $X$ with respect to the filtration is $\widehat{X}=\lim _{s}\left(X / \mathrm{F}^{s} X\right) \simeq X /\left(\lim _{s} \mathrm{~F}^{s} X\right) \simeq X /\left(\mathrm{F}^{\infty} X\right)$. The completion $\widehat{\mathrm{F}}^{*}$ is a complete filtration on $\widehat{X}$.

Example 3.10. Let $p^{*} \mathbf{Z}$ denote the $p$-adic filtration of $\mathbf{Z}$. Specifically, $p^{s} \mathbf{Z}$ is the ideal $\left(p^{s}\right) \subseteq \mathbf{Z}$ for $s \geqslant 0$ and $p^{s} \mathbf{Z}=\mathbf{Z}$ for $s \leqslant 0$. The graded pieces are $\operatorname{gr}^{s} \mathbf{Z} \simeq\left(p^{s}\right) /\left(p^{s+1}\right) \cong \mathbf{Z} / p$ for $s \geqslant 0$ and 0 for $s<0$. This filtration is exhaustive, but not complete: $\mathrm{F}^{\infty}=\lim _{s}\left(p^{s}\right) \simeq\left(\mathbf{Z}_{p} / \mathbf{Z}\right)[-1]$. The completion is the $p$-adic filtration $p^{*} \mathbf{Z}_{p}$ of $\mathbf{Z}_{p}$.

Remark 3.11. There is a duality between complete exhaustive filtrations $\mathrm{F}^{*} X$ on $X$ and non-complete filtrations on 0 with limit $X$. Indeed, if $\mathrm{F}^{*} X$ is complete and exhaustive, consider the cone of $\mathrm{F}^{*} X \rightarrow X$, which is the filtration $\frac{X}{\mathrm{~F}^{*} X}$. The limit of this filtration is $\lim _{s} X / F^{s} X \simeq X$ and the colimit is $\operatorname{colim}_{s} X / F^{s} X \simeq 0$. Conversely, if $\mathrm{F}^{*}$ is an exhaustive filtration on 0 with with limit $Z$, then taking the fiber of $Z \rightarrow \mathrm{~F}^{*}$ gives a complete exhaustive filtration on $Z$. As example, consider the two perspectives on the completeness of the $p$-adic filtration: $\lim _{s} p^{s} \mathbf{Z}_{p}=0$ versus $\mathbf{Z}_{p} \cong \lim _{s} \mathbf{Z}_{p} / p^{s}$.

Example 3.12. Let $M^{\bullet} \in \operatorname{Ch}^{\bullet}(\mathbf{Z})$ be a cochain complex. The stupid filtration $\sigma^{*} M^{\bullet}$ on $M$ is the filtered cochain complex with $\sigma^{s} M^{\bullet}=M^{\bullet \geqslant s}$. The graded pieces are $\mathrm{gr}^{s} M^{\bullet} \cong M^{s}$ placed in cohomological degree $s$. The stupid filtration is a complete exhaustive filtration on $M^{\bullet}$ in $\mathrm{Ch}^{\bullet}(\mathbf{Z})$. Looking at underlying homotopy types produces a complete exhaustive filtration $\sigma^{*} M$ on the image $M$ of $M^{\bullet}$ in the derived $\infty$-category $\mathrm{D}(\mathbf{Z})$. The graded pieces are $\mathrm{gr}^{s} M \simeq M^{s}[-s]$. We return to this example below in Construction 3.28.

Example 3.13. Let $X \in \mathrm{D}(\mathbf{S})$ be a spectrum and let $\mathrm{F}^{*} X=\tau_{\geqslant *} X$ be its Whitehead tower:

$$
\cdots \rightarrow \tau_{\geqslant s+1} X \rightarrow \tau_{\geqslant s} X \rightarrow \tau_{\geqslant s-1} X \rightarrow \cdots
$$

This is a complete and exhaustive filtration on $X$; the graded pieces are $\mathrm{gr}^{s} X \simeq \pi_{s} X[s] \in \mathrm{D}(\mathbf{S})$.
Warning 3.14. Whitehead towers are neither complete nor exhaustive in a general stable $\infty$-category with a $t$-structure. In the case of spectra, the usual, Postnikov $t$-structure is compatible with filtered colimits, so that the homotopy groups of a filtered colimit are the filtered colimit of the homotopy groups, and is left-complete, so that Postnikov towers converge. These properties are shared by many other $t$-structures which occur in algebra, geometry, and topology, but not all. For an extensive discussion, see [11, Sec. 2].

Example 3.15. Let $X$ be a CW complex, which we view as a space with a certain increasing filtration $\mathrm{F}_{*} X$ by cells. The filtration is complete and exhaustive by definition. Taking Z-cochains yields a filtered complex with

$$
\mathrm{F}_{\mathrm{CW}}^{s} \mathrm{R} \Gamma(X, \mathbf{Z})=\operatorname{fib}\left(\mathrm{R} \Gamma(X, \mathbf{Z}) \rightarrow \mathrm{R} \Gamma\left(X_{s-1}, \mathbf{Z}\right)\right)
$$

where $\mathrm{R} \Gamma(-, \mathbf{Z})$ denotes the singular cohomology functor (which is equivalent to sheaf cohomology for CW complexes). The choice of indexing here implies that $\mathrm{F}_{\mathrm{CW}}^{0} \mathrm{R} \Gamma(X, \mathbf{Z}) \simeq \mathrm{R} \Gamma(X, \mathbf{Z})$ since the cohomology of the empty set vanishes. The CW filtration is complete and exhaustive on $\mathrm{R} \Gamma(X, \mathbf{Z})$ with associated graded pieces $\operatorname{gr}^{s} \mathrm{R} \Gamma(X, \mathbf{Z}) \simeq\left(\mathrm{R} \Gamma\left(X_{s-1}, \mathbf{Z}\right) / \mathrm{R} \Gamma\left(X_{s}, \mathbf{Z}\right)\right)[-1] \simeq \prod_{s \text { cells }} \mathbf{Z}[-s]$. This filtration is used below in Section 9.

Notation 3.16. Let $\mathrm{F}^{*}$ be a filtered object in a stable $\infty$-category. For $j \geqslant i$ finite, let $\operatorname{gr}_{\mathrm{F}}^{[i, j)}=\operatorname{cofib}\left(\mathrm{F}^{j} \rightarrow\right.$ $\left.\mathrm{F}^{i}\right)=\frac{\mathrm{F}^{i}}{\mathrm{~F}^{j}}$. For example, $\operatorname{gr}_{\mathrm{F}}^{[i, i)} \simeq 0$ and $\operatorname{gr}_{\mathrm{F}}^{[i, i+1)} \simeq \operatorname{gr}_{\mathrm{F}}^{i}$. Additionally, let $\operatorname{gr}_{\mathrm{F}}^{(i, \infty)}=\operatorname{cofib}\left(\mathrm{F}^{\infty} \rightarrow \mathrm{F}^{i}\right)=$ $\lim _{j \rightarrow \infty} \operatorname{gr}_{\mathrm{F}}^{[i, j)}$ and let $\operatorname{gr}^{(-\infty, j)}=\operatorname{colim}_{i \rightarrow-\infty} \operatorname{gr}_{\mathrm{F}}^{[i, j)}$. The graded pieces for other intervals are defined analogously. When unambiguous, $\mathrm{gr}^{i}$ is used for $\mathrm{gr}_{\mathrm{F}}^{i}$.

Construction 3.17 (Filtration on gradeds). It often convenient to view $\operatorname{gr}_{\mathrm{F}}^{[i, j)}$ as admitting a residual filtration

$$
\cdots \rightarrow 0 \rightarrow \frac{\mathrm{~F}^{j-1}}{\mathrm{~F}^{j}} \rightarrow \frac{\mathrm{~F}^{j-2}}{\mathrm{~F}^{j}} \rightarrow \cdots \rightarrow \frac{\mathrm{~F}^{i}}{\mathrm{~F}^{j}} \rightarrow \frac{\mathrm{~F}^{i}}{\mathrm{~F}^{j}} \rightarrow \cdots
$$

where the term $\frac{\mathrm{F}^{j-1}}{\mathrm{~F}^{j}}$ is in filtration weight $j-1$. This is a complete exhaustive filtration on $\operatorname{gr}_{\mathrm{F}}^{[i, j)}$ with natural identifications

$$
\operatorname{gr}^{a}\left(\operatorname{gr}_{\mathrm{F}}^{[i, j)}\right) \simeq \begin{cases}\operatorname{gr}_{\mathrm{F}}^{a} & \text { if } i \leqslant a<j, \text { and } \\ 0 & \text { otherwise }\end{cases}
$$

Lurie observed in [24, Rem. 1.2.2.3] that if $\mathrm{F}^{*}$ is a filtration, then the graded objects form a kind of cochain complex. Specifically, each fiber sequence

$$
\operatorname{gr}^{s+1} \rightarrow \frac{\mathrm{~F}^{s}}{\mathrm{~F}^{s+2}} \rightarrow \mathrm{gr}^{s}
$$

gives rise to a 'differential' $\delta: \mathrm{gr}^{s} \rightarrow \mathrm{gr}^{s+1}[1]$.
Lemma 3.18. If $\mathrm{F}^{*}$ is a filtration, then there is a canonical nullhomotopy $\delta \circ \delta \simeq 0$ of maps from $\mathrm{gr}^{s}$ to $\mathrm{gr}^{s+2}[2]$.

Proof. The upper left $3 \times 3$ part of the diagram below is commutative with exact rows and columns:
![img-1.jpeg](img-1.jpeg)

The rest of the diagram is obtained by taking horizontal and vertical cofibers. The bottom right square expresses the nullhomotopy $\delta \circ \delta \simeq 0$.

It follows that the sequence of morphisms

$$
\cdots \rightarrow \operatorname{gr}^{-2}[-2] \xrightarrow{\delta} \operatorname{gr}^{-1}[-1] \xrightarrow{\delta} \operatorname{gr}^{0} \xrightarrow{\delta} \operatorname{gr}^{1}[1] \xrightarrow{\delta} \operatorname{gr}^{2}[2] \rightarrow \cdots
$$

is a kind of cochain complex object in $\mathcal{C}$.
The filtration $\mathrm{F}^{*}$ contains much more information than just the graded pieces, the differentials $\delta$, and the nullhomotopies. In order to reconstruct more of it, Nikolaus suggested using the pointed 1-category $\Xi$ of Joyal $[19,35.1]$. The set of objects is $\mathbf{Z}_{*}$, the set of integers with an extra base point which is both an initial and final object. The sets of morphisms between integers are

$$
\operatorname{Hom}_{\Xi}(m, n)= \begin{cases}* & \text { if } n \neq m, m-1 \\ \text { id, } * & \text { if } n=m \\ \delta, * & \text { if } n=m-1\end{cases}
$$

In particular, in $\Xi$, one has $\delta \circ \delta \simeq *$ whenever the left-hand side makes sense.
Definition 3.19. Let $\mathcal{C}$ be a pointed $\infty$-category. A coherent chain complex in $\mathcal{C}$ is a pointed functor $\Xi \rightarrow \mathcal{C}$. The $\infty$-category of coherent chain complexes in $\mathcal{C}$ is the functor category $\mathrm{Ch}_{\bullet}(\mathcal{C}) \simeq \operatorname{Fun}_{*}(\Xi, \mathcal{C})$. Similarly, a coherent cochain complex in $\mathcal{C}$ is a pointed functor $\Xi^{\text {op }} \rightarrow \mathcal{C}$ and the $\infty$-category of coherent chain complexes in $\mathcal{C}$ is $\mathrm{Ch}^{\bullet}(\mathcal{C})=\operatorname{Fun}_{*}\left(\Xi^{\text {op }}, \mathcal{C}\right)$.
Example 3.20. If $\mathcal{A}$ is an abelian category, then $\operatorname{Ch}^{\bullet}(\mathcal{A}) \simeq \operatorname{Fun}_{*}\left(\Xi^{\text {op }}, \mathcal{A}\right)$ recovers the usual abelian category of cochain complexes in $\mathcal{A}$.

The following theorem is due to Ariotta [4] and can also be extracted from Raksit [30] or [5, Ex. 1.10.6]. There is a connection to quasicoherent sheaves on $\mathbf{A}^{1} / \mathbf{G}_{m}$; see $[23,29]$.
Theorem 3.21 (Ariotta's $\mathrm{E}^{1}$-page theorem). Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits. The associated graded functor $\mathrm{gr}^{\star}: \mathrm{FC} \rightarrow \mathrm{GrC}$ factors through the forgetful functor $\mathrm{Ch}^{\bullet}(\mathcal{C}) \rightarrow \mathrm{GrC}$ and induces an equivalence $\widetilde{\mathrm{F}} \mathcal{C} \simeq \mathrm{Ch}^{\bullet}(\mathcal{C})$ between the $\infty$-category of complete decreasing filtrations in $\mathcal{C}$ and the $\infty$-category of coherent cochain complexes in $\mathcal{C}$.

The theorem says that giving a filtered object is equivalent to giving the $\mathrm{E}^{1}$-page of the spectral sequence associated to the filtration, at least if this $\mathrm{E}^{1}$-page is viewed as an appropriately homotopy coherent object.
Notation 3.22. If $\mathrm{F}^{\star} \in \mathrm{FC}$ is a filtered object, let $\operatorname{gr}_{\mathrm{F}}^{\bullet}[\bullet]$ denote the associated coherent cochain complex as displayed in (1). If $C^{\bullet}$ is a coherent cochain complex in $\mathcal{C}$, let $\sigma^{\star} C$ be the associated decreasing filtration in $\mathcal{C}$, obtained via the inverse to the equivalence in Theorem 3.21.

Example 3.23. If $C^{\bullet}$ is a cochain complex in $\operatorname{Mod}_{\mathbf{Z}}$, then $\sigma^{\star} C$ is the usual stupid filtration on the underlying homotopy type $\left|C^{\bullet}\right|$ of $C$ in $\mathrm{D}(\mathbf{Z})$ as in Example 3.12.

The functor $\widetilde{\mathrm{F}} \mathcal{C} \rightarrow \mathrm{Ch}^{\bullet}(\mathcal{C})$ is a souped-up version of Lurie's construction (1) and indeed the restriction to the 2 -skeleton of (the nerve of) $\Xi$ recovers the sequence (1) together with the nullhomotopies $\delta \circ \delta \simeq 0$.

The theorem is blind to any preferred $t$-structure on $\mathcal{C}$. When one is fixed, the induced $t$-structure on $\widetilde{\mathrm{F}} \mathcal{C}$ is called the Beilinson $t$-structure.

Definition 3.24 (Complete Beilinson $t$-structures). If $\mathcal{C}$ admits sequential limits and is equipped with a $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$, then $\mathrm{Ch}^{\bullet}(\mathcal{C})$ inherits the pointwise $t$-structure, where a coherent cochain complex $X^{\bullet}$ is connective if and only if each $X^{n} \in \mathcal{C}_{\geqslant 0}$. The associated $t$-structure obtained through transport via Theorem 3.21 on the equivalent $\infty$-category $\widetilde{\mathrm{F}} \mathcal{C}$ is called the Beilinson $t$-structure associated to $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. Unwinding the equivalence, the connective objects in the Beilinson $t$-structure are those complete filtrations $\mathrm{F}^{\star}$ such that $\operatorname{gr}_{\mathrm{F}}^{n} \in \mathcal{C}_{\geqslant-n}$ and the coconnective objects are those complete filtrations $\mathrm{F}^{\star}$ with $\operatorname{gr}_{\mathrm{F}}^{n} \in \mathcal{C}_{\leqslant-n}$ for all $n$. The heart of the Beilinson $t$-structure is equivalent to $\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right)$, the abelian category of cochain complexes in the heart of $\mathcal{C}$.

Definition 3.25 (Incomplete Beilinson $t$-structures). When $\mathcal{C}$ admits sequential limits, there is a localization sequence $\mathcal{C} \rightarrow \mathrm{FC} \rightarrow \widetilde{\mathrm{F}} \mathcal{C}$ where the right adjoints are given by taking the limit of a filtration and by including complete filtrations into all filtrations, respectively. If a $t$-structure on $\mathcal{C}$ is fixed, the induced Beilinson $t$-structure on $\widetilde{\mathrm{F}} \mathcal{C}$ defines a $t$-structure on $\mathrm{FC}$, also called the Beilinson $t$-structure, by declaring that $(\mathrm{FC})_{\geqslant 0}^{\mathrm{B}}$ is the full subcategory of filtrations $\mathrm{F}^{\star}$ such that $\operatorname{gr}_{\mathrm{F}}^{n} \in \mathcal{C}_{\geqslant-n}$ for all $n \in \mathbf{Z}$. Equivalently, $(\mathrm{FC})_{\geqslant 0}^{\mathrm{B}}$ consists of those filtrations whose completion is connective in the Beilinson $t$-structure on $\widetilde{\mathrm{F}} \mathcal{C}$. In particular, the full subcategory $\mathcal{C} \subseteq \mathrm{FC}$ of constant filtrations is $\infty$-connective in the (or any) Beilinson $t$-structure on $\mathrm{FC}$. With this definition, $(\mathrm{FC})_{\leqslant 0}^{\mathrm{B}} \simeq(\widetilde{\mathrm{F}} \mathcal{C})_{\leqslant 0}^{\mathrm{B}}$. In particular, any bounded above object is complete and the inclusion functor $\widetilde{\mathrm{F}} \mathcal{C} \rightarrow \mathrm{FC}$ is $t$-exact.

Remark 3.26 (Bounded above objects). If $\mathcal{C}$ is a stable $\infty$-category which admits sequential limits and a $t$-structure on $\mathcal{C}$ is fixed, then the objects $\mathrm{F}^{\star}$ of $(\mathrm{FC})_{\leqslant 0}^{\mathrm{B}} \simeq(\widetilde{\mathrm{F}} \mathcal{C})_{\leqslant 0}^{\mathrm{B}}$ have the property that the filtration is complete and $\operatorname{gr}_{\mathrm{F}}^{n} \in \mathcal{C}_{\leqslant-n}$. It follows inductively that each $\operatorname{gr}_{\mathrm{F}}^{[n, m]} \in \mathcal{C}_{\leqslant-n}$ for $m \geqslant n$ and hence that the limit $\lim _{m} \operatorname{gr}_{\mathrm{F}}^{(n, m)}$ is in $\mathcal{C}_{\leqslant-n}$ since the $(-n)$-coconnectives are closed under limits. By completeness, $\lim _{m} \operatorname{gr}_{\mathrm{F}}^{(n, m)} \simeq \mathrm{F}^{n}$, so $\mathrm{F}^{n} \in \mathcal{C}_{\leqslant-n}$ for all $n$. If the $t$-structure on $\mathcal{C}$ is right separated, then the converse is true: if $\mathrm{F}^{\star}$ is a filtration in $\mathrm{FC}$ with the property that $\mathrm{F}^{n} \in \mathcal{C}_{\leqslant-n}$, then it is in $(\mathrm{FC})_{\leqslant 0}$ and, in particular, complete. Indeed, the condition implies that each $\operatorname{gr}_{\mathrm{F}}^{n} \in \mathcal{C}_{\leqslant-n}$ by taking cofibers, so it is enough to check completeness. But, $\lim _{m} \mathrm{~F}^{m}$ is in $\mathcal{C}_{\leqslant-n}$ for all $n$, so it vanishes by right separatedness.

Remark 3.27 (Bounded Beilinson $t$-structures). If $\mathcal{C}$ is a small stable $\infty$-category with a bounded $t$-structure, then it can be embedded into $\operatorname{Ind}(\mathcal{C})$ and $\operatorname{Ind}(\mathcal{C})$ admits a $t$-structure which is compatible with filtered colimits and right complete. The induced Yoneda embedding $\mathcal{C} \rightarrow \operatorname{Ind}(\mathcal{C})$ is $t$-exact. See for example [2, Prop. 2.13]. Of course, $\operatorname{Ind}(\mathcal{C})$ admits sequential limits, so the formalism above can be applied to discuss the Beilinson $t$-structure on $\operatorname{FInd}(\mathcal{C})$. However, it may be desirable to consider only a certain class of filtrations, $\mathrm{F}^{b} \mathcal{C} \subseteq \operatorname{FInd}(\mathcal{C})$ consisting of the filtrations $\mathrm{F}^{+} M$ in $\mathrm{F} \mathcal{C}$ such that $\mathrm{F}^{i} M \simeq 0$ for $i$ sufficiently large and $\operatorname{gr}^{i} M \simeq 0$ for $i$ sufficiently small. (These are the eventually zero, eventually constant filtrations.) The Beilinson $t$-structure on $\operatorname{FInd}(\mathcal{C})$ restricts to a $t$-structure on $\mathrm{F}^{b} \mathcal{C}$ whose heart is the abelian category $\mathrm{Ch}^{\bullet, b}\left(\mathcal{C}^{\ominus}\right)$ of bounded cochain complexes of objects of $\mathcal{C}^{\ominus}$. To see this, note that the truncation functors $\tau_{\geqslant 0}^{\mathrm{B}}$ and $\tau_{\leqslant 0}^{\mathrm{B}}$ on $\operatorname{FInd}(\mathcal{C})$ preserve $\mathrm{F}^{b} \mathcal{C}$.

The following construction will place an important role in the analysis of the décalage functor.
Construction 3.28 (Realization of cochain complexes). Let $\mathcal{C}$ be a stable $\infty$-category admitting sequential limits and colimits with a fixed $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. There is an induced functor $\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right) \rightarrow \mathcal{C}$ defined by the composition

$$
\operatorname{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right) \hookrightarrow(\widehat{\mathrm{F}} \mathcal{C})_{\geqslant 0} \hookrightarrow \widehat{\mathrm{~F}} \mathcal{C} \hookrightarrow \mathrm{~F} \mathcal{C} \xrightarrow{|-|} \mathcal{C}
$$

In other words, this functor takes a cochain complex $C^{\bullet}$ to $\left|\sigma^{*} C\right|$, the object underlying the stupid filtration $\sigma^{*} C$ associated to $C^{\bullet}$. Write $\left|C^{\bullet}\right|$ for this underlying object.

Lemma 3.29. Let $\mathcal{C}$ be a stable $\infty$-category admitting sequential limits and colimits with a fixed $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. If $C^{\bullet}$ is a cochain complex, then there is a natural isomorphism $\pi_{n}\left(\left|C^{\bullet}\right|\right) \cong \mathrm{H}^{-n}\left(C^{\bullet}\right)$.

Proof. We prove the case $n=0$. There is a natural isomorphism $\pi_{0} \operatorname{gr}_{\sigma}^{[-1,2]} C \cong \mathrm{H}^{0}\left(C^{\bullet}\right)$. Indeed, $\pi_{0} \operatorname{gr}_{\sigma}^{[0,2]} C$ fits into a short exact sequence

$$
0 \rightarrow \pi_{0} \operatorname{gr}_{\sigma}^{[0,2]} C \rightarrow C^{0} \xrightarrow{\mathrm{~d}} C^{1} \rightarrow \pi_{-1} \operatorname{gr}_{\sigma}^{(0,2)} C \rightarrow 0
$$

so $\pi_{0} \operatorname{gr}_{\sigma}^{(0,2)} C$ is identified with $Z^{0}$, the object of cycles in degree 0 . Now, the fiber sequence $\operatorname{gr}_{\sigma}^{(0,2)} C \rightarrow$ $\operatorname{gr}_{\sigma}^{[-1,2]} C \rightarrow \operatorname{gr}_{\sigma}^{-1} C$ induces an exact sequence

$$
C^{-1} \xrightarrow{\mathrm{~d}} Z^{0} \rightarrow \pi_{0} \operatorname{gr}_{\sigma}^{[-1,2)} C \rightarrow 0
$$

which proves the claim. We also have that $\tau_{\geqslant 0} \operatorname{gr}_{\sigma}^{[-1, \infty)} C \simeq \lim _{n} \tau_{\geqslant 0} \operatorname{gr}_{\sigma}^{[-1, n)} C$ as $\tau_{\geqslant 0}$ preserves limits and since the filtration $\sigma^{*} C$ is complete. However, $\tau_{\geqslant 0} \operatorname{gr}_{\sigma}^{[-1, n+1)} C \rightarrow \tau_{\geqslant 0} \operatorname{gr}_{\sigma}^{[-1, n)} C$ is an equivalence for $n \geqslant 2$ since it is the fiber of a map $\operatorname{gr}_{\sigma}^{[-1, n)} C \rightarrow\left(\operatorname{gr}_{\sigma}^{n} C\right)[1], \tau_{\geqslant 0}\left(\operatorname{gr}_{\sigma}^{n} C\right)[1] \simeq \tau_{\geqslant 0}\left(C^{n}[-n+1]\right) \simeq 0$ for $n \geqslant 2$, and $\tau_{\geqslant 0}$ preserves fibers. It follows that $\pi_{0} \operatorname{gr}_{\sigma}^{[-1, \infty)} C \cong \mathrm{H}^{0}\left(C^{\bullet}\right)$. For $m \geqslant 1$, the map $\tau_{\leqslant 0} \sigma_{\sigma}^{[-m, \infty)} C \rightarrow \tau_{\leqslant 0} \sigma_{\sigma}^{[-m-1, \infty)} C$ is an equivalence since $\tau_{\leqslant 0}$ preserves cofibers and this map is a cofiber of a map $\operatorname{gr}_{\sigma}^{-m-1} C[-1] \rightarrow \sigma_{\sigma}^{[-m-1, \infty)} C$, where $\operatorname{gr}_{\sigma}^{-m-1} C[-1] \simeq C^{-m-1}[m]$ is connective for $m \geqslant 1$. As $\tau_{\leqslant 0}$ commutes with colimits, it follows that $\tau_{\leqslant 0} C \simeq \operatorname{colim} \tau_{\leqslant 0} \operatorname{gr}_{\sigma}^{[-m, \infty)} C \simeq \tau_{\leqslant 0} \operatorname{gr}_{\sigma}^{[-1, \infty)} C$. This completes the proof.

Corollary 3.30. Suppose that $\mathcal{C}$ is a stable $\infty$-category with sequential limits and colimits. If $\mathcal{C}$ is equipped with a t-structure which is separated, then the functor

$$
\operatorname{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right) \xrightarrow{C^{\bullet} \mapsto\left|C^{\bullet}\right|} \mathcal{C}
$$

factors through $\mathrm{D}\left(\mathcal{C}^{\ominus}\right)$, the $\infty$-categorical localization of $\mathrm{Ch}^{\bullet}(\mathcal{C})$ at the quasi-isomorphisms.

We conclude this section with some generalities on the properties of Beilinson $t$-structures on $\widetilde{\mathrm{F}} \mathcal{C}$ as inherited from a $t$-structure on $\mathcal{C}$. This material will not be used below. For background on prestable $\infty$-categories and the terminology used below, see [25, App. C].

Proposition 3.31. Let $I$ be a 1-category and let $\mathcal{C}$ be a stable $\infty$-category equipped with a $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. The following properties of $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ are inherited by $\operatorname{Fun}(I, \mathcal{C})$ and, if $I$ is pointed, they are inherited by $\operatorname{Fun}_{*}(I, \mathcal{C})$ :
(a) right or left separatedness;
(b) right or left completeness;
(c) compatibility with filtered colimits;
(d) Grothendieck;
(e) compactly generation.

If, moreover, $I$ has the property that $\operatorname{Hom}_{I}(i, i)=\left\{\mathrm{id}_{i}\right\}$ for all $i \in I$, then the following property is inherited by $\operatorname{Fun}(I, \mathcal{C})$ and $\operatorname{Fun}_{*}(I, \mathcal{C})$ :
(f) compatibility with filtered colimits and either weakly n-complicial or n-complicial.

Proof. For part (a), if $X: I \rightarrow \mathcal{C}$ is an object of $\operatorname{Fun}(I, \mathcal{C})$ which is in $\cap_{n} \operatorname{Fun}(I, \mathcal{C})_{\leqslant n} \simeq \cap_{n} \operatorname{Fun}\left(I, \mathcal{C}_{\leqslant n}\right)$, then it must vanish if $\mathcal{C}$ is right separated. Similarly for left separatedness.

If $\mathcal{C} \simeq \lim _{n} \mathcal{C}_{\leqslant n}$, then $\operatorname{Fun}(I, \mathcal{C}) \simeq \lim _{n} \operatorname{Fun}\left(I, \mathcal{C}_{\leqslant n}\right) \simeq \lim _{n} \operatorname{Fun}(I, \mathcal{C})_{\leqslant n}$, so $\mathcal{C}$ is left complete. Similarly for right completeness. This gives (b).

If $\mathcal{C}_{\leqslant 0}$ is closed under filtered colimits in $\mathcal{C}$, then the same is true for $\operatorname{Fun}(I, \mathcal{C})_{\leqslant 0} \simeq \operatorname{Fun}\left(I, \mathcal{C}_{\leqslant 0}\right)$ in $\operatorname{Fun}(I, \mathcal{C})$ as colimits in a functor category are computed pointwise. This proves (c).

Since the $t$-structure on $\mathcal{C}$ is Grothendieck, it is right complete and compatible with filtered colimits. Moreover, $\mathcal{C}$ and $\mathcal{C}_{\geqslant 0}$ are presentable. These are inherited by $\operatorname{Fun}(I, \mathcal{C})$, which shows part (d).

For part (e), if $X \in \mathcal{C}$ is compact, then $i_{!} X$ is compact in $\operatorname{Fun}(I, \mathcal{C})$ for any $i \in I$ since $i^{*}$ preserves filtered colimits. The collection of $i_{!} X$ as $i$ ranges over $I$ and $X$ ranges over a set of compact generators of $\mathcal{C}$ provides a set of compact generators for $\operatorname{Fun}(I, \mathcal{C})$.

Let $X: I \rightarrow \mathcal{C}_{\geqslant 0}$ be an object of $\operatorname{Fun}(I, \mathcal{C})_{\geqslant 0}$ and assume that $\mathcal{C}$ is $n$-complicial. For each object $X(i) \simeq i^{*} X \in \mathcal{C}_{\geqslant 0}$, this means that there is a morphism $y_{i} \rightarrow X(i)$ inducing a surjection on $\pi_{0}$ in $\mathcal{C}^{\bigcirc}$ and such that $y_{i} \in \mathcal{C}_{[0, n]}$. By adjunction, there is a map $i_{!} Y_{i} \rightarrow X$ in $\operatorname{Fun}(I, \mathcal{C})$. Computing the value of $i_{!} Y_{i}$ at $j \in I$ yields

$$
\bigoplus_{f \in \operatorname{Hom}_{I}(i, j)} Y_{i}
$$

in $\mathcal{C}$ by the assumption on $I$, which is in $\mathcal{C}_{[0, n]}$ since the $t$-structure is compatible with filtered colimits. In particular, $i_{!} Y_{i}$ is in $\left.\operatorname{Fun}(I, \mathcal{C})_{[0, n]}\right]$ and $i_{!} Y_{i} \rightarrow X(i)$ is surjective on $i^{*} \pi_{0}$. Taking a sum over $i \in I$ of the $i_{!} Y_{i} \rightarrow X$ yields

$$
\bigoplus_{i \in I} i_{!} Y_{i} \rightarrow X
$$

The map is surjective on $\pi_{0}$ and the sum is in $\operatorname{Fun}(I, \mathcal{C})_{[0, n]}$ by compatibility of the $t$-structure on $\mathcal{C}$ with filtered colimits. This proves $n$-complicialness. The proof for weak $n$-compliciality is the same, so (f) is proved.

Corollary 3.32. Let $\mathcal{A}$ be a Grothendieck abelian category. The $\infty$-category $\widetilde{\mathrm{FD}}(\mathcal{A}) \simeq \operatorname{Ch}^{\bullet}(\mathrm{D}(\mathcal{A}))$ is Grothendieck and 0 -complicial: the natural map $\mathrm{D}\left(\mathrm{Ch}^{\bullet}(\mathcal{A})\right) \rightarrow \widetilde{\mathrm{FD}}(\mathcal{A}) \simeq \mathrm{Ch}^{\bullet}(\mathrm{D}(\mathcal{A}))$ is an equivalence.

Example 3.33. $\widehat{\mathrm{PD}}(\mathbf{Z}) \simeq \operatorname{Ch}^{\bullet}(\mathrm{D}(\mathbf{Z})) \simeq \mathrm{D}\left(\mathrm{Ch}^{\bullet}(\mathbf{Z})\right)$.
Remark 3.34. Let $\mathcal{A}$ be a Grothendieck abelian $n$-category. There is a canonical separated $n$-complicial Grothendieck prestable $\infty$-category $\mathrm{D}(\mathcal{A})_{\geqslant 0}$ associated to $\mathcal{A}$ by [25, Prop. C.5.4.5] with presentable stabilization $\mathrm{D}(\mathcal{A})$. By construction, $\mathrm{D}(\mathcal{A})_{] 0, n-1]} \simeq \mathcal{A}$. By Proposition 3.31, the $\infty$-category $\widehat{\mathrm{PD}}(\mathrm{D}(\mathcal{A})) \simeq \operatorname{Ch}^{\bullet}(\mathrm{D}(\mathcal{A}))$ is equivalent to $\mathrm{D}\left(\mathrm{Ch}^{\bullet}(\mathcal{A})\right)$, the derived $\infty$-category of the Grothendieck abelian $n$-category $\mathrm{Ch}^{\bullet}(\mathcal{A})$.

# 4 Décalage 

This section contains the definition of a spectral sequence in an abelian category as well as two constructions of the spectral sequence associated to a filtered object in a stable $\infty$-category equipped with a $t$-structure, one via décalage and one following Lurie [24, Prop. 1.2.2.7]. The main theorem is that the definitions agree.

Definition 4.1 (Spectral sequences). Let $\mathcal{A}$ be an abelian category. A spectral sequence in $\mathcal{A}$ starting at the $a$ th page consists of
(i) objects $\mathrm{E}_{s, t}^{r}$ of $\mathcal{A}$ for $r \geqslant a$ and $s, t \in \mathbf{Z}$,
(ii) differentials $\mathrm{d}_{s, t}^{r}: \mathrm{E}_{s, t}^{r} \rightarrow \mathrm{E}_{s-r, t+r-1}^{r}$ for $r \geqslant a$ and $s, t \in \mathbf{Z}$, and
(iii) isomorphisms between the cohomology at $\mathrm{E}_{s, t}^{r}$ with respect to $\mathrm{d}^{r}$ and $\mathrm{E}_{s, t}^{r+1}$ for $r \geqslant a$ and $s, t \in \mathbf{Z} .{ }^{1}$

For fixed $r \geqslant a$, the collection $\left\{\mathrm{E}_{s, t}^{r}\right\}$ together with the differentials $\left\{\mathrm{d}_{s, t}^{r}\right\}$ form the $r$ th page of the spectral sequence.

Remark 4.2. In this paper, most spectral sequences will start at the 1st page. See Section 7 for comments about alternative indexing conventions.

The primary sources of spectral sequences are strictly filtered complexes (see for example [27, 31]), exact couples (see for example [31, Sec. 5.9]), and filtrations in stable $\infty$-categories with fixed $t$-structures. Note that while part (iii) of Definition 4.1 implies that the $\mathrm{E}^{r}$-page of a spectral sequence determines the objects on the $\mathrm{E}^{r+1}$-page, it does not generally determine the $\mathrm{d}^{r+1}$-differential. This must be constructed in some way.

Fix a stable $\infty$-category $\mathcal{C}$ with sequential limits and colimits and let $\mathrm{F}^{*}$ be a decreasing filtration in $\mathcal{C}$. Assume also that $\mathcal{C}$ is equipped with a $t$-structure. As mentioned above, the basic problem is to go from presumably accessible information about the graded pieces, specifically the homotopy objects

$$
\pi_{*} \operatorname{gr}_{\mathrm{F}}^{*}
$$

and to learn something about $\pi_{*} \mathrm{~F}^{-\infty}$. There are two fundamental obstructions to a class $x \in \pi_{i} \operatorname{gr}_{\mathrm{F}}^{i}$ contributing to $\pi_{i} \mathrm{~F}^{-\infty}$ : the obstructions to lifting $x$ to $\pi_{i} \mathrm{~F}^{j}$ and then the possibility that a lift $\tilde{x} \in \pi_{i} \mathrm{~F}^{j}$ is in the kernel of the map

$$
\pi_{i} \mathrm{~F}^{j} \rightarrow \pi_{i} \mathrm{~F}^{-\infty}
$$

A spectral sequence is a way of packaging these wrinkles together in a reasonable format.
Construction 4.3. Associated to $\mathrm{F}^{*}$ is the coherent cochain complex

$$
\cdots \rightarrow \operatorname{gr}_{\mathrm{F}}^{-s-1}[-s-1] \rightarrow \operatorname{gr}_{\mathrm{F}}^{-s}[-s] \rightarrow \operatorname{gr}_{\mathrm{F}}^{-s+1}[-s+1] \rightarrow \cdots
$$

[^0]
[^0]:    ${ }^{1}$ Some sources, such as [27], require only that the $\mathrm{E}^{r+1}$-page be isomorphic to the cohomology of the $\mathrm{E}^{r}$-page, without fixing the isomorphism.

discussed in the previous section. Applying $\pi_{t}$ with respect to the fixed $t$-structure on $\mathcal{C}$ to the coherent cochain complex produces a cochain complex in $\mathcal{C}^{\odot}$ of the form

$$
\cdots \rightarrow \pi_{t} \operatorname{gr}_{\mathrm{F}}^{-s-1}[-s-1] \rightarrow \pi_{t} \operatorname{gr}_{\mathrm{F}}^{-s}[-s] \rightarrow \pi_{t} \operatorname{gr}_{\mathrm{F}}^{-s+1}[-s+1] \rightarrow \cdots
$$

which can be rewritten as

$$
\cdots \rightarrow \pi_{s+t+1} \operatorname{gr}_{\mathrm{F}}^{-s-1} \rightarrow \pi_{s+t} \operatorname{gr}_{\mathrm{F}}^{-s} \rightarrow \pi_{s+t-1} \operatorname{gr}_{\mathrm{F}}^{-s+1} \rightarrow \cdots
$$

Definition 4.4 ( $\mathrm{E}^{1}$-page). The $\mathrm{E}^{1}$-page of the spectral sequence associated to $\mathrm{F}^{\star}$ is the graded chain complex

$$
\mathrm{E}_{s, t}^{1}=\pi_{s+t} \operatorname{gr}^{-s} M
$$

with differentials

$$
\mathrm{d}_{s, t}^{1}: \mathrm{E}_{s, t}^{1} \rightarrow \mathrm{E}_{s-1, t}^{1}
$$

In other words,

$$
\mathrm{E}_{\bullet, t}^{1}=\pi_{t}^{\mathrm{B}}(\mathrm{~F})^{-\bullet}
$$

the chain complex associated to cochain complex $\pi_{t}^{\mathrm{B}}(\mathrm{F})$. In particular, $\mathrm{d}^{1} \circ \mathrm{~d}^{1}=0$, so objects $\mathrm{E}_{s, t}^{2}(\mathrm{~F}) \in \mathcal{C}^{\odot}$ are defined as the homology of the $\mathrm{E}^{1}$-page with respect to $\mathrm{d}^{1}$.

Construction 4.5 (Décalage). Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits and colimits which admits a $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. Let $\mathrm{F}^{\star}$ be a filtered object of $\mathcal{C}$. Let $\tau_{\geqslant s}^{\mathrm{B}}(\mathrm{F})$ denote the Whitehead tower of $\mathrm{F}^{\star}$ with respect to the Beilinson $t$-structure on $\mathrm{FC}$ (associated to the fixed $t$-structure on $\mathcal{C}$ ). Note that each $\tau_{\geqslant n}^{\mathrm{B}}(\mathrm{F})$ is itself a filtered object of $\mathcal{C}$. By applying realization to the Whitehead tower

$$
\cdots \rightarrow \tau_{\geqslant n+1}^{\mathrm{B}}(\mathrm{~F}) \rightarrow \tau_{\geqslant n}^{\mathrm{B}}(\mathrm{~F}) \rightarrow \tau_{\geqslant n-1}^{\mathrm{B}}(\mathrm{~F}) \rightarrow \cdots
$$

one obtains a new filtered object

$$
\cdots \rightarrow\left|\tau_{\geqslant n+1}^{\mathrm{B}}(\mathrm{~F})\right| \rightarrow\left|\tau_{\geqslant n}^{\mathrm{B}}(\mathrm{~F})\right| \rightarrow\left|\tau_{\geqslant n-1}^{\mathrm{B}}(\mathrm{~F})\right| \rightarrow \cdots
$$

of $\mathcal{C}$, called the décalage of $\mathrm{F}^{\star}$ and denoted $\operatorname{Dec}(\mathrm{F})^{\star}$. Since there are natural maps $\tau_{\geqslant n}^{\mathrm{B}}(\mathrm{F}) \rightarrow \mathrm{F}^{\star}$, taking colimits gives natural maps

$$
\left|\tau_{\geqslant n}^{\mathrm{B}}(\mathrm{~F})\right| \rightarrow\left|\mathrm{F}^{\star}\right|
$$

Thus, if $\mathrm{F}^{\star}$ is a filtration on $M$, then $\operatorname{Dec}(\mathrm{F})^{\star}$ can be equipped with the structure of a filtration on $M$ as well.
Remark 4.6. Décalage gives an endofunctor of $\mathrm{FC}$ when $\mathcal{C}$ admits sequential limits and colimits and is equipped with a $t$-structure. There is an analogue of décalage for any sequence of full subcategories $\cdots \rightarrow(\mathrm{FC})_{n} \rightarrow(\mathrm{FC})_{n-1} \rightarrow \cdots$ for which the inclusions admits right adjoints. The case here is where $(\mathrm{FC})_{n}=(\mathrm{FC})_{\geqslant n}^{\mathrm{B}}$, the full subcategory of $n$-connective objects with respect to the Beilinson $t$-structure.

Remark 4.7 (Graded pieces of décalage). As $\tau_{\geqslant n+1}^{\mathrm{B}}(\mathrm{F}) \rightarrow \tau_{\geqslant n}^{\mathrm{B}}(\mathrm{F}) \rightarrow \pi_{n}^{\mathrm{B}}(\mathrm{F})[n]$ forms a cofiber sequence in filtered complexes, one finds that the associated graded pieces of $\operatorname{Dec}(\mathrm{F})^{\star}$ are given by

$$
\operatorname{gr}_{\mathrm{Dec}(\mathrm{~F})}^{\mathrm{n}} \simeq\left|\pi_{n}^{\mathrm{B}}(\mathrm{~F})\right| n]|\simeq| \pi_{n}^{\mathrm{B}}(\mathrm{~F})|[n]
$$

Under the identification of the heart of the Beilinson $t$-structure with cochain complexes, $\pi_{n}^{\mathrm{B}}(\mathrm{F})$ is the cochain complex

$$
\pi_{n}^{\mathrm{B}}(\mathrm{~F})^{\bullet}: \cdots \rightarrow \pi_{n+1} \operatorname{gr}^{-1} \rightarrow \pi_{n} \operatorname{gr}^{0} \rightarrow \pi_{n-1} \operatorname{gr}^{1} \rightarrow \pi_{n-2} \operatorname{gr}^{2} \rightarrow \cdots
$$

where $\pi_{n} \mathrm{gr}^{0}$ is placed in cohomological degree 0 . Thus, $\operatorname{gr}_{\mathrm{Dec}(\mathrm{F})}^{\mathrm{n}}$ is the $n$-fold suspension of the realization of this cochain complex in the sense of Construction 3.28. After reindexing to a chain complex, this complex is precisely the $n$th horizontal line on the $\mathrm{E}^{1}$-page of the spectral sequence of $\mathrm{F}^{\star}$.

Definition 4.8 (Décalage definition of the spectral sequence). Let $\mathcal{C}$ be a stable $\infty$-category which admits sequential limits and colimits and suppose $\mathcal{C}$ is equipped with a fixed $t$-structure. If $\mathrm{F}^{\star} \in \mathrm{FC}$ is a filtered object, then let $\operatorname{Dec}^{(r)}(\mathrm{F})^{\star}$ denote the $r$-fold composition of the décalage functor for $r \geqslant 0$. Let

$$
\mathrm{E}_{s, t}^{r+1}(\mathrm{~F})=\mathrm{E}_{-(r-1) s-r t, r s+(r+1) t}^{1}\left(\operatorname{Dec}^{(r)}(\mathrm{F})\right)
$$

with the corresponding differentials.
Lemma 4.9. Suppose that $\mathcal{C}$ is a stable $\infty$-category with sequential limits and colimits and equipped with a $t$-structure. If $\mathrm{F}^{\star} \in \mathrm{FC}$, then the pages of Definition 4.8 admit the structure of a spectral sequence starting at the 1 st page.

Proof. The bidegree of the differential on $\mathrm{E}^{1}\left(\operatorname{Dec}^{(r)}(\mathrm{F})\right)$ is $(-1,0)$. To transform these coordinates to those of $\mathrm{E}^{r+1}(\mathrm{~F})$ one uses the inverse to the matrix

$$
\left(\begin{array}{cc}
-r+1 & -r \\
r & r+1
\end{array}\right)
$$

which is

$$
\left(\begin{array}{cc}
r+1 & r \\
-r & -r+1
\end{array}\right)
$$

Thus, the reindexed differential on $\mathrm{E}_{s, t}^{r+1}$ has bidegree $(-r-1, r)$, which is the bidegree of the differential on the $\mathrm{E}^{r+1}$-page of a spectral sequence. Thus, it suffices to construct an isomorphism between the cohomology on the $\mathrm{E}^{r}$-page and the $\mathrm{E}^{r+1}$-page. Inductively, it is enough to do this for $r=1$. By Remark 4.7,

$$
\mathrm{E}_{s, t}^{2}(\mathrm{~F}) \cong \mathrm{H}^{-s}\left(\pi_{t}^{\mathrm{B}}(\mathrm{~F})^{\bullet}\right) \cong \pi_{s}\left(\left|\pi_{t}^{\mathrm{B}}(\mathrm{~F})^{\bullet}\right|\right) \cong \pi_{s+t}\left(\left|\pi_{t}^{\mathrm{B}}(\mathrm{~F})\right|[t]\right) \cong \mathrm{E}_{-t, s+2 t}^{1}(\operatorname{Dec}(\mathrm{~F}))
$$

where the second isomorphism follows from Lemma 3.29 .
It follows that Definition 4.8 gives one definition of the spectral sequence of a filtered object in $\mathcal{C}$, at least if $\mathcal{C}$ admits sequential limits and colimits. In the remainder of this section, Lurie's definition of a spectral sequence of a filtered object in $\mathcal{C}$ is given and the two definitions are compared.

Construction 4.10. Let $\mathcal{C}$ be a stable $\infty$-category with a $t$-structure and let $\mathrm{F}^{\star} \in \mathrm{FC}$ be a filtration in $\mathcal{C}$. All graded pieces below are constructed with respect to $\mathrm{F}^{\star}$. For $r \geqslant 1$, and $s \in \mathbf{Z}$, there is a map

$$
\operatorname{gr}^{(-s,-s+r)} \rightarrow \operatorname{gr}^{(-s-r+1,-s+1)}
$$

induced by the commutative square
![img-2.jpeg](img-2.jpeg)
by taking horizontal cofibers. These fit into a natural commutative diagram
![img-3.jpeg](img-3.jpeg)

of cofiber sequences. For $r \geqslant 1$ and $s, t \in \mathbf{Z}$, let

$$
\mathrm{E}_{s, t}^{r}=\operatorname{im}\left(\pi_{s+t} \mathrm{gr}^{[-s,-s+r)} \rightarrow \pi_{s+t} \mathrm{gr}^{[-s-r+1,-s+1)}\right)
$$

and consider the commutative diagram
![img-4.jpeg](img-4.jpeg)
where the rows are epi-mono factorizations and the left and right vertical maps come from the boundary maps in homotopy associated to the fiber sequences in (2). The claim is that the outer square above commutes. This follows immediately from the fact that there is a canonical map from the top fiber sequence above to the bottom fiber sequence. By functoriality of epi-mono factorization, the dotted arrow exists. Denote it by $\mathrm{d}_{s, t}^{r}$.

Definition 4.11 (Lurie's definition of the spectral sequence). The bigraded collection $\mathrm{E}_{s, t}^{r}$ of objects of $\mathcal{C}^{\bigcirc}$ together with the differentials $\mathrm{d}_{s, t}^{r}: \mathrm{E}_{s, t}^{r} \rightarrow \mathrm{E}_{s-r, t+r-1}^{r}$ is the $\mathrm{E}^{r}$-page of the spectral sequence associated to $\mathrm{F}^{*}$.

Parts (ii) and (iii) of the following proposition appears as [24, Prop. 1.2.2.7].
Proposition 4.12. Let $\mathrm{F}^{*} M$ be a filtered object in a stable $\infty$-category equipped with a $t$-structure.
(i) The definitions of the $\mathrm{E}^{1}$-page given in Definitions 4.4 and 4.11 agree.
(ii) The composition $\mathrm{d}^{r} \circ \mathrm{~d}^{r}$ vanishes for $r \geqslant 1$.
(iii) The homology of the chain complexes on the $\mathrm{E}^{r}$-page is naturally isomorphic to the terms of the $\mathrm{E}^{r+1}$-page for $r \geqslant 1$.

In particular, the sequence of pages of Definition 4.11 defines a spectral sequence in the sense of Definition 4.1.
Proof of (i). Part (i) follows by observing that in the second definition $\mathrm{E}_{s, t}^{1}=\pi_{s+t} \mathrm{gr}^{-s}$, just as in the first definition. The check that the differentials agree follows from examining the boundary maps associated to the fiber sequences in (2).

The proof of part (iii) of Proposition 4.12 is nontrivial. It will follow from Theorem 4.13 that Lurie's definition of the $\mathrm{E}^{r}$-pages agrees with the décalage definition of the $\mathrm{E}^{r}$-page given here. Inductively, this implies parts (ii) and (iii) of Proposition 4.12. In particular, the proof of Theorem 4.13 does not use parts (ii) or (iii) of Proposition 4.12 .

Until the end of the section, unless specified otherwise, $\mathrm{E}_{s, t}^{r}(\mathrm{~F})$ refers to Lurie's definition.
Theorem 4.13 (Comparison theorem). Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits and colimits and a $t$-structure. For $r \geqslant 1$, there are natural isomorphisms $\mathrm{E}_{-t, s+2 t}^{r}(\operatorname{Dec}(\mathrm{~F})) \cong \mathrm{E}_{s, t}^{r+1}(\mathrm{~F})$ compatible with the differentials on the $\mathrm{E}^{r}(\operatorname{Dec}(\mathrm{~F}))$ and $\mathrm{E}^{r+1}(\mathrm{~F})$-pages.

Corollary 4.14. Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits and colimits and a $t$-structure. For $r \geqslant 0$, there are natural isomorphisms $\mathrm{E}_{-(r-1) s-r t, r s+(r+1) t}^{1}\left(\operatorname{Dec}^{(r)}(\mathrm{F})\right) \cong \mathrm{E}_{s, t}^{r+1}(\mathrm{~F})$ compatible with the differentials on the $\mathrm{E}^{1}\left(\operatorname{Dec}^{(r)}(\mathrm{F})\right)$ and $\mathrm{E}^{r+1}(\mathrm{~F})$-pages.

Remark 4.15. In particular, the décalage definition of the spectral sequence of a filtration agrees with Lurie's.

Remark 4.16 (Bounded décalage). The main situation we foresee where the hypotheses of Theorem 4.13 are not met is when $\mathcal{C}$ is a small abelian category admitting a bounded $t$-structure, such as $\mathrm{D}^{b}(X)$ for a regular noetherian scheme. However, as in Remark 3.26, we can embed $\mathcal{C}$ inside $\operatorname{Ind}(\mathcal{C})$ and apply the theory of the Beilinson $t$-structure and décalage to $\operatorname{FInd}(\mathcal{C})$. As the Dec endofunctor preserves $\mathrm{F}^{b} \mathcal{C} \subseteq \operatorname{FInd}(\mathcal{C})$, we see that Theorem 4.13 also applies to $\mathrm{F}^{b} \mathcal{C}$.

The proof is given at the end of the section after some preliminaries.
Example 4.17. If $\mathrm{F}^{\star} M$ is the constant filtration on $M$, then each $\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{F}^{\star} M\right)$ is the constant filtration on $M$ and $\operatorname{Dec}\left(\mathrm{F}\right)^{\star} M$ is the constant filtration on $M$.

Lemma 4.18. If $\mathrm{F}^{\star} M$ is a complete filtration, then each $\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{F}^{\star} M\right)$ is complete.
Proof. There is a cofiber sequence

$$
\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M\right) \rightarrow \mathrm{F}^{\star} M \rightarrow \tau_{\leqslant n-1}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M\right)
$$

of filtered objects of $\mathcal{C}$. As $\tau_{\leqslant n-1}^{\mathrm{B}}\left(\mathrm{F}^{\star} M\right)$ is necessarily complete (see Definition 3.25), it follows that $\tau_{\geqslant n}^{\mathrm{B}}\left(\mathrm{F}^{\star} M\right)$ is complete.

Remark 4.19. If $\mathrm{F}^{\star} M^{\prime} \rightarrow \mathrm{F}^{\star} M \rightarrow \mathrm{~F}^{\star} M^{\prime \prime}$ is a fiber sequence of fibrations, so that each $\mathrm{F}^{s} M^{\prime} \rightarrow \mathrm{F}^{s} M \rightarrow$ $\mathrm{F}^{s} M^{\prime \prime}$ is a fiber sequence, there is a long-exact sequence

$$
\cdots \rightarrow \pi_{n+1}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M^{\prime \prime}\right) \rightarrow \pi_{n}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M^{\prime}\right) \rightarrow \pi_{n}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M\right) \rightarrow \pi_{n}^{\mathrm{B}}\left(\mathrm{~F}^{\star} M^{\prime \prime}\right) \rightarrow \cdots
$$

of cochain complexes. It does not typically break up into short exact sequences, which explains why one does not often find "short exact sequences of spectral sequences" in nature.

There is an important class of examples which run counter to the general situation of Remark 4.19 and which will be important in the proof of Theorem 4.13. First, we need a standard lemma.

Lemma 4.20. Let $\mathcal{C}$ be a stable $\infty$-category with a t-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. Suppose that $x \rightarrow y \rightarrow z$ is a cofiber sequence in $\mathcal{C}$.
(i) If $\pi_{0} y \rightarrow \pi_{0} z$ is an epimorphism in $\mathcal{C}^{\odot}$, then $\tau_{\geqslant 0} x \rightarrow \tau_{\geqslant 0} y \rightarrow \tau_{\geqslant 0} z$ is a cofiber sequence in $\mathcal{C}$.
(ii) If $\pi_{0} x \rightarrow \pi_{0} y$ is a monomorphism in $\mathcal{C}^{\odot}$, then $\tau_{\leqslant 0} x \rightarrow \tau_{\leqslant 0} y \rightarrow \tau_{\leqslant 0} z$ is a cofiber sequence in $\mathcal{C}$.

Proof. It suffices to prove part (i). Consider the induced map $z \rightarrow x[1]$ and note that the composition $\tau_{\geqslant 0} z \rightarrow \tau_{\geqslant 0} x[1] \rightarrow \pi_{-1} x$ factors through the boundary map $\pi_{0} z \rightarrow \pi_{-1} x$, which is assumed to be zero. Thus, there is a lift $\tau_{\geqslant 0} z \rightarrow\left(\tau_{\geqslant 0} x\right)[1]$. As $\mathcal{C}_{\geqslant 0}$ is prestable, there is by definition a fiber $w$ of this map in $\mathcal{C}_{\geqslant 0}$ such that the square
![img-5.jpeg](img-5.jpeg)
is a fiber square and a cofiber square in $\mathcal{C}_{\geqslant 0}$. As $\tau_{\geqslant 0}$ preserves fiber squares, we see that there is a map $w \rightarrow \tau_{\geqslant 0} y$ in $\mathcal{C}_{\geqslant 0}$ with trivial fiber and which induces an isomorphism on $\pi_{0}$. If this map is an equivalence, then $\tau_{\geqslant 0} y \rightarrow \tau_{\geqslant 0} z \rightarrow\left(\tau_{\geqslant 0} x\right)[1]$ is a cofiber sequence in $\mathcal{C}$, proving (i). Now, suppose that $a \rightarrow b$ is a map in $\mathcal{C}_{\geqslant 0}$ which has trivial fiber and induces a surjection on $\pi_{0}$. Let $f$ be the fiber of $a \rightarrow b$ in $\mathcal{C}$, so that $\tau_{\geqslant 0} f \simeq 0$ is the fiber computed in $\mathcal{C}_{\geqslant 0}$. We have a fiber sequence $a \rightarrow b \rightarrow f[1]$ and hence a fiber sequence $a \rightarrow b \rightarrow \tau_{\geqslant 0}(f[1])$ in $\mathcal{C}_{\geqslant 0}$. As $\tau_{\geqslant 0}(f[1]) \cong \pi_{-1} f$ and as $\pi_{0} a \rightarrow \pi_{0} b$ is surjective, with have that $b \rightarrow \tau_{\geqslant 0}(f[1])$ is zero, so that $a \simeq b \oplus \Omega\left(\pi_{-1} f\right) \simeq b$, as desired.

Example 4.21. Suppose that $\mathrm{F}^{\star}$ is a filtered object in $\mathcal{C}$ and consider the fiber sequence $\operatorname{gr}^{[b, c)} \rightarrow \operatorname{gr}^{[a, c)} \rightarrow$ $\operatorname{gr}^{[a, b)}$ of filtered objects using the filtrations of Construction 3.17 for $a \leqslant b \leqslant c$ (including infinite values). Then,

$$
0 \rightarrow \pi_{0}^{\mathrm{B}}\left(\operatorname{gr}^{[b, c)}\right) \rightarrow \pi_{0}^{\mathrm{B}}\left(\operatorname{gr}^{[a, c)}\right) \rightarrow \pi_{0}^{\mathrm{B}}\left(\operatorname{gr}^{[a, b)}\right) \rightarrow 0
$$

is short exact. Indeed, the middle term is the cochain complex

$$
\cdots \rightarrow 0 \rightarrow \pi_{-a} \operatorname{gr}^{a} \rightarrow \pi_{-a-1} \operatorname{gr}^{a+1} \rightarrow \cdots \pi_{-c+1} \operatorname{gr}^{c-1} \rightarrow 0 \rightarrow \cdots
$$

and the left-hand term is the inclusion of the stupid truncation $\sigma^{\geqslant b}$ with quotient the right-hand term the stupid truncation $\sigma^{\leqslant b-1}$. It follows by Lemma 4.20 that $\operatorname{Dec}\left(\operatorname{gr}^{[b, c)}\right) \rightarrow \operatorname{Dec}\left(\operatorname{gr}^{[a, c)}\right) \rightarrow \operatorname{Dec}\left(\operatorname{gr}^{[a, b)}\right)$ is in fact a fiber sequence of filtered spectra.

Recall that $\operatorname{ins}^{s} M$ denotes the filtration on $M$ obtained by left Kan extension of the constant functor on $M$ along the inclusion $\{s\} \hookrightarrow \mathbf{Z}^{c p}$. Concretely, $\mathrm{F}^{i} \operatorname{ins}^{s} M \simeq 0$ for $i>s$ and $\mathrm{F}^{i} \operatorname{ins}^{s} M \simeq M$ for $i \leqslant s$, with all transition maps the identity. The filtration on $\operatorname{gr}^{a}$ of Construction 3.17 is naturally equivalent to $\operatorname{ins}^{a} \operatorname{gr}^{a}$.
Lemma 4.22. Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits and with a t-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. The functor ins ${ }^{s}: \mathcal{C} \rightarrow \mathrm{F} \mathcal{C}$ is $t$-exact with respect to the $t$-structure $\left(\mathcal{C}_{\geqslant-s}, \mathcal{C}_{\leqslant-s}\right)$ on $\mathcal{C}$ and the Beilinson $t$-structure associated to $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ on $\mathrm{F} \mathcal{C}$.

Proof. The functor ins ${ }^{s}$ lands in $\widetilde{\mathrm{F}} \mathcal{C}$, so it is enough to see it is $t$-exact as a functor to $\widetilde{\mathrm{F}} \mathcal{C}$ by Definition 3.25. As a coherent cochain complex, ins ${ }^{s} M$ is simply $M[s]$ in degree $s$ and 0 elsewhere. This is a $t$-exact assignment with the given $t$-structures.

Example 4.23. The functor ins ${ }^{0}: \mathcal{C} \rightarrow \mathrm{F} \mathcal{C}$ is $t$-exact.
Lemma 4.24. The filtration $\operatorname{Dec}^{\star}\left(\operatorname{gr}^{s} M\right)$ is equivalent to $\tau_{\geqslant-s+\star} \operatorname{gr}^{s} M$.
Proof. It is enough to consider the case $s=0$, in which case we have that $\tau_{\geqslant \star}^{\mathrm{B}}\left(\operatorname{gr}^{0} M\right)=\tau_{\geqslant \star}^{\mathrm{B}}\left(\operatorname{ins}^{0} M\right) \simeq$ $\operatorname{ins}^{0}\left(\tau_{\geqslant \star} M\right)$ by Lemma 4.22. Taking colimits gives the result.

Proof of Theorem 4.13. Consider the following commutative diagram
![img-6.jpeg](img-6.jpeg)
referred to below as the $2 \times 5$-diagram. To make precise what is meant here, for example $\operatorname{gr}_{\mathrm{Dec}}^{[0, \infty)} \operatorname{gr}_{\mathrm{F}}^{[0, r+1]}=$ $\operatorname{Dec}^{0}\left(\operatorname{gr}_{\mathrm{F}}^{[0, r+1)}\right)$, where $\operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ is viewed as a filtration via Construction 3.17. Similarly, $\operatorname{gr}_{\mathrm{Dec}}^{[0, r)}$ is the $[0, r)$ associated graded of the décalage filtration associated to the original filtration $\mathrm{F}^{\star}$. The maps arise from functoriality of the décalage construction.

Note that $\mathrm{E}_{0,0}^{r+1}(\mathrm{~F})$ is the epi-mono factorization of the left-hand map, while $\mathrm{E}_{0,0}^{r}(\operatorname{Dec}(\mathrm{F}))$ is the epi-mono factorization of the right-hand map. Justification of the displayed properties of maps $\mathbf{1}, \ldots, \mathbf{8}$ will show that there is a canonical isomorphism of these objects of $\mathcal{C}^{\heartsuit}$.
(1) There is a fiber sequence of filtered objects $\tau_{\geqslant 0}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)} \rightarrow \operatorname{gr}_{\mathrm{F}}^{[0, r+1)} \rightarrow \tau_{\leqslant-1}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ whose colimit is $\operatorname{gr}_{\mathrm{Dec}}^{[0, \infty]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)} \rightarrow \operatorname{gr}_{\mathrm{F}}^{[0, r+1)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{\left(-\infty,-1\right]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$. By Example $4.21, \operatorname{gr}_{\mathrm{Dec}}^{\left(-\infty,-1\right]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ has a finite filtration (induced by F ) with associated graded pieces $\operatorname{gr}_{\mathrm{Dec}}^{\left(-\infty,-1\right]} \operatorname{gr}_{\mathrm{F}}^{a}$. By Lemma 4.24, $\operatorname{gr}_{\mathrm{Dec}}^{\left(-\infty,-1\right]} \operatorname{gr}_{\mathrm{F}}^{a} \simeq$ $\tau_{\leqslant-a-1} \operatorname{gr}_{\mathrm{F}}^{a}$ for $0 \leqslant a \leqslant r$. Thus, $\operatorname{gr}_{\mathrm{Dec}}^{\left(-\infty,-1\right]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ is an iterated extension of objects in $\mathcal{C}_{\leqslant-1}$, so it is in $\mathcal{C}_{\leqslant-1}$, which shows that $\mathbf{1}$ is an isomorphism.

(2) By Lemma 4.21, $\mathrm{gr}_{\mathrm{Dec}}^{[0, \infty]} \mathrm{gr}_{\mathrm{F}}^{[0, r+1)}$ has a finite filtration with graded pieces $\mathrm{gr}_{\mathrm{Dec}}^{[0, \infty]} \operatorname{gr}_{\mathrm{F}}^{a} \simeq \tau_{\geqslant-a} \operatorname{gr}_{\mathrm{F}}^{a}$ for $0 \leqslant a \leqslant r$ and similarly $\operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \mathrm{gr}_{\mathrm{F}}^{[0, r+1)}$ has a finite filtration with graded pieces $\operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \operatorname{gr}_{\mathrm{F}}^{a} \simeq \tau_{[-a,-a+r)} \operatorname{gr}_{\mathrm{F}}^{a}$. The natural map is compatible with these filtrations, so on its fiber there is a finite filtration with graded pieces $\tau_{\geqslant-a+r} \operatorname{gr}_{\mathrm{F}}^{a}$ for $0 \leqslant a \leqslant r$. It follows that the fiber is connective and hence the displayed map 2 on $\pi_{0}$ is surjective.
(3) The fiber of the morphism which induces $\mathbf{3}$ is $\mathrm{gr}_{\mathrm{Dec}}^{[0, r]} \mathrm{gr}_{\mathrm{F}}^{[r+1, \infty)}$, which has a finite filtration (now using Dec) whose associated graded pieces are given by $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1, \infty)}[a]\right|$ for $0 \leqslant a<r$. The question of whether $\mathbf{3}$ is an isomorphism depends only on the homotopy objects of $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1, \infty)}[a]\right|$ for $0 \leqslant a<r$ and hence the cohomology groups of the corresponding cochain complexes thanks to Lemma 3.29. The cochain complex representing $\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1, \infty)}$ is of the form

$$
\cdots \rightarrow 0 \rightarrow \pi_{-r-1+a} \operatorname{gr}_{\mathrm{F}}^{r+1} \rightarrow \pi_{-r-a+a-1} \operatorname{gr}_{\mathrm{F}}^{r+2} \rightarrow \cdots
$$

where $\pi_{-r-1+a} \operatorname{gr}^{r+1}$ has cohomological degree $r+1$. This cochain complex has $\mathrm{H}^{a}=0$ for $a<r+1$ and hence the object $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1, \infty)}[a]\right|$ has $\pi_{b}=0$ for $b>-r-1+a$. In particular, as $a<r, \pi_{b}=0$ for $b>-2$. Hence, $\mathbf{3}$ is an isomorphism.
(4) The map 4 is induced by a map $\operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \operatorname{gr}_{\mathrm{F}}^{[0, \infty)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{[0, r]}$, whose cofiber is $\operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}$, where $\operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}$ denotes the filtered object

$$
\cdots \rightarrow 0 \rightarrow \frac{\mathrm{~F}^{-1}}{\mathrm{~F}^{0}} \rightarrow \frac{\mathrm{~F}^{-2}}{\mathrm{~F}^{0}} \rightarrow \cdots
$$

It is enough to show that $\pi_{0}$ of this cofiber vanishes. For this, one can again filter using the Beilinson Whitehead tower and reduce to considering $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}[a]\right|$ for $0 \leqslant a<r$. The cochain complex representing $\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}$ is of the form

$$
\cdots \pi_{a+3} \operatorname{gr}_{\mathrm{F}}^{-3} \rightarrow \pi_{a+2} \operatorname{gr}_{\mathrm{F}}^{-2} \rightarrow \pi_{a+1} \operatorname{gr}_{\mathrm{F}}^{-1} \rightarrow 0 \rightarrow \cdots
$$

where $\pi_{a+1} \operatorname{gr}_{\mathrm{F}}^{-1}$ is in cohomological degree -1 . It follows that $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}[a]\right|$ has homotopy concentrated in degrees $\geqslant 1+a$. Thus, $\operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \operatorname{gr}_{\mathrm{F}}^{[-\infty,-1]}$ has vanishing $\pi_{0}$ since $0 \leqslant a<r$. In particular, 4 is an epimorphism.
(5) Arguing as in the case of $\mathbf{1}$, one reduces to studying the cofiber $\operatorname{gr}_{\mathrm{Dec}}^{[-\infty,-r]} \operatorname{gr}_{\mathrm{F}}^{[-r, 1)}$ which reduces via a finite filtration to $\operatorname{gr}_{\mathrm{Dec}}^{[-\infty,-r]} \operatorname{gr}_{\mathrm{F}}^{a} \simeq \tau_{\leqslant-a-r} \operatorname{gr}_{\mathrm{F}}^{a}$ for $-r \leqslant a<1$. For these $a$, the truncation $\tau_{\leqslant-a-r} \operatorname{gr}_{\mathrm{F}}^{a}$ is in $\mathcal{C}_{\leqslant 0}$, so the cofiber is coconnective. It follows that $\mathbf{5}$ is a monomorphism.
(6) The fiber of the map inducing $\mathbf{6}$ has a finite filtration with associated graded pieces $\operatorname{gr}_{\mathrm{Dec}}^{[1, \infty]} \operatorname{gr}_{\mathrm{F}}^{a} \simeq$ $\tau_{\geqslant-a+1} \operatorname{gr}_{\mathrm{F}}^{a}$ for $-r \leqslant a<1$. It follows that the fiber is 1 -connective and hence $\mathbf{6}$ is an isomorphism.
(7) The fiber of the map in question is $\operatorname{gr}_{\mathrm{Dec}}^{[-r+1,1]} \operatorname{gr}_{\mathrm{F}}^{[1, \infty]}$, which has a finite filtration with associated graded pieces $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[1, \infty)}[a]\right|$ for $-r+1 \leqslant a<1$. The homotopy objects $\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[1, \infty)}$ are represented by cochain complexes

$$
\cdots \rightarrow 0 \rightarrow \pi_{a-1} \operatorname{gr}_{\mathrm{F}}^{1} \rightarrow \pi_{a-2} \operatorname{gr}_{\mathrm{F}}^{2} \rightarrow \cdots
$$

where $\pi_{a-1} \operatorname{gr}_{\mathrm{F}}^{1}$ is in cohomological degree 1. Thus, the objects $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[1, \infty)}[a]\right|$ are in homological degree $\leqslant-1+a$. As $a \leqslant 0$, these have no $\pi_{0}$. Thus, the given map $\mathbf{7}$ is injective.

(8) Finally, the cofiber of $\operatorname{gr}_{\mathrm{F}}^{(-r, \infty)} \rightarrow \mathrm{F}$ is $\operatorname{gr}_{\mathrm{F}}^{(-\infty,-r)}$. Thus, the cofiber of $\operatorname{gr}_{\mathrm{Dec}}^{(-r+1,1)} \operatorname{gr}_{\mathrm{F}}^{(-r, \infty)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{(-r+1,1)}$ admits a finite filtration with graded pieces given by $\left[\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{(-\infty,-r)}[a]\right]$ for $-r+1 \leqslant a<1$. The homotopy objects themselves are represented by objects

$$
\cdots \rightarrow \pi_{r+2+a} \operatorname{gr}_{\mathrm{F}}^{-r-2} \rightarrow \pi_{r+1+a} \mathrm{gr}^{-r-1} \rightarrow 0 \rightarrow \cdots
$$

where the $\mathrm{gr}^{-r-1}$ term is in cohomological degree $-r-1$. Thus, the suspension has homotopy concentrated in degrees $\geqslant r+1+a$. As $-r+1 \leqslant a$, this is in degrees at least 2 . Thus, the cofiber does not contribute to $\pi_{0}$ and 8 is an isomorphism.

This completes the justification of the decorations in the commutative diagram above.
By functoriality of epi-mono factorizations in an abelian category, each commutative square in the commutative diagram above induces an isomorphism of epi-mono factorizations of the vertical morphisms. In particular, there is a canonical zigzag

$$
\mathrm{E}_{0,0}^{r+1}(\mathrm{~F}) \leftarrow A \rightarrow B \leftarrow C \rightarrow \mathrm{E}_{0,0}^{r}(\operatorname{Dec}(F))
$$

where each map is an isomorphism. This proves that the homotopy objects on the $\mathrm{E}^{r+1}(\mathrm{~F})$ and $\mathrm{E}^{r}(\operatorname{Dec}(\mathrm{F}))$ pages agree naturally for all filtrations and all $r \geqslant 1$.

To finish the proof, it is enough to show that the identifications constructed above are compatible with the differentials. It is enough to check this for the differentials emanating from $(0,0)$. For this, consider the general form of the $2 \times 5$-diagram above, which computes the isomorphism between the $\mathrm{E}_{s, t}^{r+1}(\mathrm{~F})$-term and the $\mathrm{E}_{-t, s+2 t}^{r}(\operatorname{Dec}(\mathrm{F}))$-term:
![img-7.jpeg](img-7.jpeg)

We will use the following commutative diagram
![img-8.jpeg](img-8.jpeg)

Here, the bottom $3 \times 5$-diagram has exact columns, which defines $P$. The map $\operatorname{gr}_{\mathrm{Dec}}^{[r, 2 r]} \operatorname{gr}_{\mathrm{F}}^{(r+1,2 r+2)} \rightarrow P$ exists, and fits into such a commutative diagram, because the composition

$$
\operatorname{gr}_{\mathrm{Dec}}^{[r, 2 r]} \operatorname{gr}_{\mathrm{F}}^{(r+1,2 r+2)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{[0,2 r]} \operatorname{gr}_{\mathrm{F}}^{(0,2 r+2)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{[0, r]} \operatorname{gr}_{\mathrm{F}}^{(0, r+1)}
$$

is nullhomotopic. By taking vertical boundaries from $\pi_{0}$ to $\pi_{-1}$ in the $3 \times 5$-diagram and then precomposing with the map on $\pi_{-1}$ from the top $2 \times 5$-diagram one obtains the following diagram:
![img-9.jpeg](img-9.jpeg)

The middle $3 \times 5$-diagram is commutative by commutativity of the $4 \times 5$-diagram above. The outer trapezoids are commutative by definition of the the $\mathrm{d}_{\mathrm{F}}^{r+1}$ and $\mathrm{d}_{\mathrm{Dec}}^{r}$-differentials. Now, we claim that the arrow marked $\mathbf{A}$ is an isomorphism and that the arrow marked $\mathbf{B}$ is injective.

To check the claim for $\mathbf{A}$, we can argue as in the case of $\mathbf{2}$ above to observe that the cofiber of $\operatorname{gr}_{\mathrm{Dec}}^{[r, \infty]} \mathrm{gr}_{\mathrm{F}}^{[r+1,2 r+2)} \rightarrow \mathrm{gr}_{\mathrm{Dec}}^{[0, \infty]} \mathrm{gr}_{\mathrm{F}}^{[r+1,2 r+2)}$ admits a finite filtration with graded pieces given by $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1,2 r+2)}\right| a] \mid$ for $0 \leqslant a<r$. The cochain complex $\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1,2 r+2)}$ takes the form

$$
\cdots \rightarrow 0 \rightarrow \pi_{-r-1+a} \operatorname{gr}_{\mathrm{F}}^{r+1} \rightarrow \pi_{-r-2+a} \operatorname{gr}_{\mathrm{F}}^{r+2} \rightarrow \cdots \rightarrow \pi_{-2 r-1+a} \operatorname{gr}_{\mathrm{F}}^{2 r+1} \rightarrow 0 \rightarrow \cdots
$$

where $\pi_{-r-1+a} \operatorname{gr}_{\mathrm{F}}^{r+1}$ is in cohomological degree $r+1$. This complex has cohomology concentrated in $[r+1,2 r+1]$ and hence the $a$-fold suspension of its realization $\left|\pi_{a}^{\mathrm{B}} \operatorname{gr}_{\mathrm{F}}^{[r+1,2 r+2)}\right| a] \mid$ has nonzero homotopy objects in $[-2 r-1+a,-r-1+a]$. As $r \geqslant 1$ and $0 \leqslant a<r$, each graded piece is $(-2)$-coconnective.

For $\mathbf{B}$, consider the induced map on long exact sequences in homotopy from the fourth column to the third column in the $4 \times 5$-diagram above. It yields a commutative diagram
![img-10.jpeg](img-10.jpeg)

The two left vertical arrows and the rightmost vertical arrow are isomorphisms by now-standard arguments, which we omit (but one of them is $\mathbf{3}$ ). This proves that $\mathbf{B}$ is injective.

We can now check that the two maps from $\pi_{0} \operatorname{gr}_{\mathrm{Dec}}^{[0, \infty]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ to $\mathrm{E}_{-r, r-1}^{r}(\operatorname{Dec}(\mathrm{F}))$ are equal, one given by composition along the top to $\mathrm{E}_{0,0}^{r}(\operatorname{Dec}(\mathrm{F}))$ followed by $\mathrm{d}_{\mathrm{Dec}}^{r}$ and the other given by the composition of the boundary to $\pi_{-1} \operatorname{gr}_{\mathrm{Dec}}^{[0, \infty)} \operatorname{gr}_{\mathrm{F}}^{[r+1,2 r+2)}$, the inverse of $A$, and the composition along the bottom row to $\mathrm{E}_{-r, r-1}^{r}(\mathrm{Dec})$. Indeed, the bottom row and top row paths from $\pi_{0} \operatorname{gr}_{\mathrm{Dec}}^{[0, \infty]} \operatorname{gr}_{\mathrm{F}}^{[0, r+1)}$ to $\pi_{-1} P$ agree and then the bottom row and top row paths to $\pi_{-1} \operatorname{gr}_{\mathrm{Dec}}^{[r, 2 r]} \operatorname{gr}_{\mathrm{F}}^{[0, \infty)}$ agree by injectivity of $\mathbf{B}$. The rest follows by commutativity and this completes the proof.

Remark 4.25. The arguments in $\mathbf{1}, \ldots, \mathbf{8}$ can be deduced pictorially as follows. We show the case of $\mathbf{2}$ for $r=7$. Figure 4 shows the spectral sequence for $\operatorname{gr}_{\mathrm{Dec}}^{[0,7]} \operatorname{gr}_{\mathrm{F}}^{[7,8)}$ sitting inside the spectral sequence for $\mathrm{F}^{*}$ as the filled symbols. The map $\operatorname{gr}_{\mathrm{Dec}}^{[0, \infty)} \operatorname{gr}_{\mathrm{F}}^{[0,8)} \rightarrow \operatorname{gr}_{\mathrm{Dec}}^{[0,7]} \operatorname{gr}_{\mathrm{F}}^{[0,8)}$ cuts away the $*$ s and we see that it induces a surjection on $\pi_{0}$, which the green symbols contribute to.

![img-11.jpeg](img-11.jpeg)

Figure 4: The spectral sequence for $\mathrm{F}^{*}$ in the proof of Theorem 4.13 in the special case of $r=7$. The solid symbols contribute the spectral sequence for $\operatorname{gr}_{\mathrm{Dec}}^{(0,7)} \operatorname{gr}_{\mathrm{F}}^{(0,8)} M$, while only the solid circles contribute to the spectral squence for $\operatorname{gr}_{\mathrm{Dec}(\mathrm{F})}^{(0,7)} \operatorname{gr}_{\mathrm{F}}^{(0,8)}$. A $\mathrm{d}^{7}$-differential is shown and the green symbols contribute to $\pi_{0}$.

# 5 Deligne's décalage 

To compare the décalage functor constructed via the Beilinson $t$-structure to Deligne's décalage functor from $[12,1.3 .3]$, suppose that $\mathrm{F}^{*} M_{\bullet}$ is a filtered chain complex of objects in an abelian category $\mathcal{A}$ and that the filtration is strict in the sense that $\mathrm{F}^{s+1} M_{n} \rightarrow \mathrm{~F}^{*} M_{n}$ is injective for each $s$ and $n$ in $\mathbf{Z}$.

Definition 5.1. Define $\operatorname{Dec}(\mathrm{F})^{*} M_{\bullet}$ by the formula

$$
\operatorname{Dec}(\mathrm{F})^{s} M_{n}=\operatorname{ker}\left(\mathrm{~d}: \mathrm{F}^{s-n} M_{n} \rightarrow \frac{M_{n-1}}{\mathrm{~F}^{s-n+1} M_{n-1}}\right)
$$

By construction, the differential on $M_{\bullet}$ restricts to a differential on each $\operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}$ so that $\operatorname{Dec}(\mathrm{F})^{*} M_{\bullet}$ defines a filtered complex.

Remark 5.2 (Cohomological version). If $\mathrm{F}^{*} M^{\bullet}$ is a strictly filtered cochain complex, $\operatorname{Dec}(\mathrm{F})^{*} M^{\bullet}$ is defined analogously as

$$
\operatorname{Dec}(\mathrm{F})^{s} M^{n}=\operatorname{ker}\left(\mathrm{d}: \mathrm{F}^{s+n} M^{n} \rightarrow \frac{M^{n+1}}{\mathrm{~F}^{s+n+1} M^{n}}\right)
$$

Construction 5.3. Each $\operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}$ admits its own filtration by subcomplexes $\mathrm{G}^{*} \operatorname{Dec}(\mathrm{~F})^{s} M$ defined by

$$
\mathrm{G}^{w} \operatorname{Dec}(\mathrm{~F})^{s} M_{n}=\operatorname{ker}\left(\mathrm{d}: \mathrm{F}^{\max (w, s-n)} M_{n} \rightarrow \frac{M_{n-1}}{\mathrm{~F}^{\max (w, s-n+1)} M_{n-1}}\right)
$$

For $w \geqslant s-n+1, \mathrm{G}^{w} \operatorname{Dec}(\mathrm{~F})^{s} M_{n}=\mathrm{F}^{w} M_{n}$ and for $w \leqslant s-n, \mathrm{G}^{w} \operatorname{Dec}(\mathrm{~F})^{s} M_{n}=\operatorname{Dec}(\mathrm{F})^{s} M_{n}$. Thus, $\mathrm{G}^{*} \operatorname{Dec}(\mathrm{~F})^{s} M_{\bullet}$ is an exhaustive filtration on $\operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}$, which is complete if and only if the original filtration

$\mathrm{F}^{\star} M$ is. The natural inclusions induce maps

$$
\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s+1} M_{\bullet} \rightarrow \mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}
$$

which make $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{\star} M_{\bullet}$ into a (strict) bifiltration in chain complexes. For $s$ fixed, $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}$ is a filtered subcomplex of $\mathrm{F}^{\star} M_{\bullet}$.

The following theorem was one of the starting points for this paper.
Theorem 5.4. The natural inclusion $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet} \rightarrow \mathrm{F}^{\star} M_{\bullet}$ induces an equivalence $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s} M \rightarrow$ $\tau_{\geqslant s}^{\mathrm{B}}(\mathrm{F}) M$ of towers of filtered objects.

Proof. It is enough to prove that $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet} \rightarrow \mathrm{F}^{\star} M_{\bullet}$ is equivalent to the $s$-connective cover in the Beilinson $t$-structure on $\mathrm{FD}(\mathbf{Z})$. For this, it is enough to check that $\operatorname{gr}_{\mathrm{G}}^{\mathrm{w}} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet} \simeq \tau_{\geqslant s-w} \operatorname{gr}_{\mathrm{F}}^{w} M$ for all $w, s \in \mathbf{Z}$. By construction, $\operatorname{gr}_{\mathrm{G}}^{\mathrm{w}} \operatorname{Dec}(\mathrm{F})^{s} M_{\bullet}$ is given by a complex

$$
\cdots \rightarrow \operatorname{gr}_{\mathrm{F}}^{\mathrm{w}} M_{s-w+2} \rightarrow \operatorname{gr}_{\mathrm{F}}^{\mathrm{w}} M_{s-w+1} \rightarrow \frac{\operatorname{ker}\left(\mathrm{~d}: \mathrm{F}^{w} M_{s-w} \rightarrow \frac{M_{s-w-1}}{\mathrm{~F}^{w+1} M_{s-w-1}}\right)}{\mathrm{F}^{w+1} M_{s-w}} \rightarrow 0 \rightarrow \cdots
$$

The natural map to $\operatorname{gr}_{\mathrm{F}}^{\mathrm{w}} M_{\bullet}$ is a quasi-isomorphism to $\tau_{\geqslant s-w} \operatorname{gr}_{\mathrm{F}}^{\mathrm{w}} M_{\bullet}$ since every cycle of $\operatorname{gr}_{\mathrm{F}}^{\mathrm{w}} M_{\bullet}$ in homological degree $s-w$ is represented by an element of $\operatorname{ker}\left(\mathrm{d}: \mathrm{F}^{w} M_{s-w} \rightarrow \frac{M_{s-w-1}}{\mathrm{~F}^{w+1} M_{s-w-1}}\right)$.

Corollary 5.5. The décalage construction of Construction 4.5 agrees with Deligne's for strictly filtered chain complexes and there is a natural equivalence $\mathrm{G}^{\star} \operatorname{Dec}(\mathrm{F})^{\star} M \simeq \tau_{\geqslant \star}^{\mathrm{B}}(\mathrm{F}) M$ of bifiltered objects of $\mathrm{D}(\mathbf{Z})$.

# 6 Convergence 

As mentioned in the introduction, only a limited convergence result is given. Hedenlund-Krause-Nikolaus have announced stronger results along the lines of Boardman's [8] using an $\infty$-categorical approach.

Definition 6.1. Let $\mathrm{F}^{\star} M$ be a filtered object of a stable $\infty$-category $\mathcal{C}$ which is equipped with a fixed $t$-structure. The induced filtration on $\pi_{m} M$ is

$$
\mathrm{F}^{\star} \pi_{n} M=\operatorname{im}\left(\pi_{m} \mathrm{~F}^{\star} M \rightarrow \pi_{m} M\right)
$$

This is a strict filtration.
The goal is to compute the associated graded pieces of $\mathrm{F}^{\star} \pi_{n} M$ via the spectral sequence associated to $\mathrm{F}^{\star} M$.

Definition 6.2. (1) An upper half-plane spectral sequence is one for which $\mathrm{E}_{s, t}^{1}=0$ for $t<N$ for some fixed $N$. An upper half-plane filtration $\mathrm{F}^{\star} M$ is one which is bounded below in the Beilinson $t$-structure. A left half-plane spectral sequence is one for which $\mathrm{E}_{s, t}^{1}=0$ for $s>N$ for some fixed $N$. A left half-plane filtration is a filtration $\mathrm{F}^{\star} M$ such that $\mathrm{gr}^{-s} M \simeq 0$ for $s>N$. Lower and right half-plane filtrations are defined similarly.
(2) By intersecting regions in the plane, one finds the notion of first, second, third, and fourth quadrant spectral sequences and filtrations. For example, a first quadrant filtration is one which is bounded below in the Beilinson $t$-structure and where $\mathrm{gr}^{-s} M \simeq 0$ for $-s$ sufficiently large.

(3) Finally, a spectral sequence is column-bounded if it is left and right half-plane, so it is concentrated in a bounded vertical strip in the $(s, t)$-plane. A filtration $\mathrm{F}^{\star} M$ is bounded if $\operatorname{gr}^{s} M \simeq 0$ for $s \notin[-N, N]$ for some integer $N$. A filtration is row-bounded if it is bounded in the Beilinson $t$-structure. A spectral sequence is row-bounded if $\mathrm{E}_{s, t}^{1}$ vanishes for $t \notin[-N, N]$, so the $\mathrm{E}^{1}$-page is concentrated in a bounded horizontal strip in the $(s, t)$-plane.

Lemma 6.3. If $\mathrm{F}^{\star} M$ is a filtration which is upper half-plane, then the associated spectral sequence is upper half-plane. Similarly for left half-plane, column-bounded, row-bounded, etc.

Proof. Left to the reader.
Notation 6.4 (Boundaries and cycles). Each term $\mathrm{E}_{s, t}^{r}$ is a subquotient of $\pi_{s+t} \mathrm{gr}^{-s} M$, defining subobjects $\tilde{\mathrm{B}}_{s, t}^{r} \subseteq \tilde{\mathrm{Z}}_{s, t}^{r}$ of $\pi_{s+t} \mathrm{gr}^{-s} M$ consisting of boundaries and cycles with the properties that

$$
\cdots \subseteq \tilde{\mathrm{B}}_{s, t}^{r} \subseteq \tilde{\mathrm{~B}}_{s, t}^{r+1} \subseteq \cdots \cdots \subseteq \tilde{\mathrm{Z}}_{s, t}^{r+1} \subseteq \tilde{\mathrm{Z}}_{s, t}^{r} \subseteq \cdots
$$

and

$$
\frac{\tilde{\mathrm{Z}}_{s, t}^{r}}{\tilde{\mathrm{~B}}_{s, t}^{r}} \cong \mathrm{E}_{s, t}^{r+1}
$$

Alternatively, the cycles may be defined as the terms $\mathrm{E}_{s, t}^{r+1}\left(\operatorname{gr}_{\mathrm{F}}^{[-s, \infty)}\right)$ (so there are no nonzero differentials hitting the $(s, t)$-term); the boundaries may be defined as the terms $\mathrm{E}_{s, t}^{r+1}\left(\operatorname{gr}_{\mathrm{F}}^{[-\infty,-s]} M\right)$ (so there are no nonzero differentials out of the $(s, t)$-term).

Definition 6.5 (The $\mathrm{E}^{\infty}$-page). Assume that $\mathcal{C}$ admits sequential limits and colimits (which implies that $\mathcal{C}^{\odot}$ admits countable unions and intersections). Let $\tilde{\mathrm{B}}_{s, t}^{\infty}=\operatorname{colim}_{r} \tilde{\mathrm{~B}}_{s, t}^{r}$ and let $\tilde{\mathrm{Z}}_{s, t}^{\infty}=\lim _{r} \tilde{\mathrm{Z}}_{s, t}^{r}$, where the limits and colimits are computed in $\mathcal{C}^{\odot} .{ }^{2}$ The sequential limits and colimits can be obtained by computing them in $\mathcal{C}$ and then applying $\pi_{0}$. The $\mathrm{E}^{\infty}$-page of the spectral sequence is the lattice of objects with

$$
\mathrm{E}_{s, t}^{\infty}=\operatorname{coker}\left(\tilde{\mathrm{B}}_{s, t}^{\infty} \rightarrow \tilde{\mathrm{Z}}_{s, t}^{\infty}\right)
$$

Remark 6.6. If $\mathrm{F}^{\star} M$ is upper half-plane or left half-plane, then the $\mathrm{E}^{\infty}$-page can be accessed in a slightly different way. For example, if $\mathrm{F}^{\star} M$ is $(-N)$-connective in the Beilinson $t$-structure (so it is upper half-plane), then for $n \geqslant N+t+1$, no differential can hit $\mathrm{E}_{s, t}^{n}$ so one obtains a decreasing sequence

$$
\cdots \subseteq \mathrm{E}_{s, t}^{N+t+3} \subseteq \mathrm{E}_{s, t}^{N+t+2} \subseteq \mathrm{E}_{s, t}^{N+t+1}
$$

of objects of $\mathcal{C}^{\odot}$. Since $\mathrm{F}^{\star} M$ is upper half-plane or left half-plane, for any pair $(s, t)$, the boundary sequence $\tilde{\mathrm{B}}_{s, t}^{r}$ stabilizes, which implies that the two definitions of the $\mathrm{E}^{\infty}$-page agree. It follows that $\mathrm{E}_{s, t}^{\infty}$ is the intersection of these objects.

Recall that a decreasing system $\mathrm{G}^{\star} N$ of objects of $\mathcal{C}$ (and in particular $\mathcal{C}^{\odot}$ ) is pro-zero if for each $n \in \mathbf{Z}$ there is an $m \geqslant n$ such that $\mathrm{G}^{m} N \rightarrow \mathrm{G}^{n} N$ is nullhomotopic (zero if in $\mathcal{C}^{\odot}$ ).

Lemma 6.7. Let $\mathcal{C}$ be a stable $\infty$-category with sequential limits. If $\mathrm{G}^{\star} N$ is a pro-zero filtered object of $\mathcal{C}$, then it is a complete filtration, i.e., $\lim _{s} \mathrm{G}^{s} N \simeq 0$.

[^0]
[^0]:    ${ }^{2}$ Note that $\widetilde{\mathrm{Z}}_{s, t}^{\infty}$ is necessarily a subobject of $\mathrm{E}_{s, t}^{1} \cong \pi_{s+t} \mathrm{gr}^{-s}$ since limits are left exact, but that the natural map $\tilde{\mathrm{B}}_{s, t}^{\infty} \rightarrow \mathrm{E}_{s, t}^{1}$ need not be injective in general. However, it will be injective as long as the $t$-structure on $\mathcal{C}$ is compatible with sequential colimits.

Proof. Let $M \in \mathcal{C}$. Then, $\mathrm{F}^{*} X=\operatorname{Map}_{\mathcal{C}}\left(M, \mathrm{F}^{*} N\right)$ is a pro-zero filtered spectrum and $\lim _{s} \mathrm{~F}^{s} X=$ $\operatorname{Map}_{\mathcal{C}}\left(M, \lim _{s} \mathrm{~F}^{s} N\right)$. Since $M$ was arbitrary, it follows that it is enough to show that $\lim _{s} \mathrm{~F}^{s} X \simeq 0$ if $\mathrm{F}^{*} X$ is a pro-zero filtered spectrum. However, for each $n \in \mathbf{Z}, \pi_{n} \mathrm{~F}^{*} X$ is a pro-zero filtered abelian group, so that $\lim _{s}{ }^{1} \pi_{n} \mathrm{~F}^{s} X=0=\lim _{s} \pi_{n} \mathrm{~F}^{s} X$ by the Mittag-Leffler condition. By the Milnor sequence

$$
0 \rightarrow \lim _{s}^{1} \pi_{n+1} \mathrm{~F}^{s} X \rightarrow \pi_{n} \lim _{s} \mathrm{~F}^{s} X \rightarrow \lim _{s} \pi_{n} \mathrm{~F}^{s} X \rightarrow 0
$$

which follows from the fact that the $t$-structure on spectra is compatible with countable products, it follows that $\pi_{n} \lim _{s} \mathrm{~F}^{s} X \simeq 0$ for all $n$. In other words, $\lim _{s} \mathrm{~F}^{s} X \simeq 0$.

If $\mathcal{C}$ is a stable $\infty$-category with sequential limits, derived limits of objects of $\mathcal{C}^{\circ}$ are always computed in $\mathcal{C}$. This notion depends on the ambient $\infty$-category $\mathcal{C}$ and not just on the abelian category $\mathcal{C}^{\circ}$.

Theorem 6.8 (Convergence theorem). Suppose that $\mathcal{C}$ admits sequential limits and colimits and that the fixed $t$-structure on $\mathcal{C}$ is compatible with sequential colimits. Let $\mathrm{F}^{*} M$ be a filtration on an object $M$ of $\mathcal{C}$.
(i) If $\mathrm{F}^{*} M$ is an exhaustive filtration of $M$, then for each $n$ the induced filtration $\mathrm{F}^{*} \pi_{n} M$ is exhaustive.
(ii) If for some integer $n$ the pro-object $\left\{\pi_{n} \mathrm{~F}^{s} M\right\}_{s}$ is pro-zero, then the filtration $\mathrm{F}^{*} \pi_{n} M$ is pro-zero and derived complete.
(iii) There are natural inclusions

$$
\operatorname{gr}^{s} \pi_{n} M \subseteq \mathrm{E}_{-s, n+s}^{\infty}
$$

for each $s$ and $n$. The inclusions are equalities if $\mathrm{F}^{*} M$ is column-bounded, row-bounded, first quadrant, or third quadrant.

Proof. The fact that $\mathrm{F}^{*} \pi_{n} M$ is exhaustive follows from the compatibility of the $t$-structure on $\mathcal{C}$ with sequential colimits and the fact that $\mathrm{F}^{*} M$ is exhaustive, so colim $_{\mathrm{s}} \mathrm{F}^{s} M \simeq M$. This proves (i).

For (ii), since $\pi_{n} \mathrm{~F}^{*} M \rightarrow \mathrm{~F}^{*} \pi_{n} M$ is a surjection of pro-objects of $\mathcal{C}^{\circ}$ and since $\pi_{n} \mathrm{~F}^{*} M$ is pro-zero, it follows that $\mathrm{F}^{*} \pi_{n} M$ is pro-zero and in particular derived complete by Lemma 6.7.

Now, consider the commutative diagram
![img-12.jpeg](img-12.jpeg)
of exact sequences, where $B$ and $Z$ are defined to be the vertical cokernels of the upper left square. This implies that $B$ and $Z$ are subobjects of $\pi_{n} \operatorname{gr}^{s} M$ and in fact they are subobjects of $\widetilde{\mathrm{Z}}_{-s, s+n}^{\infty}$. Indeed, $Z \subseteq \widetilde{\mathrm{Z}}_{-s, s+n}^{\infty}$ is the subobject of permanent cycles that actually lift to $\pi_{n} \mathrm{~F}^{s} M$.

The kernel $\operatorname{ker}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ is the union of the kernels of $\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} \mathrm{~F}^{s-N} M$ since the $t$-structure is compatible with sequential colimits. The commutative diagram
![img-13.jpeg](img-13.jpeg)
in which the columns are exact, implies that $\operatorname{ker}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ maps to $\operatorname{ker}\left(\pi_{n} \operatorname{gr}^{s} M \rightarrow \pi_{n} \operatorname{gr}^{(s-N, s+1)} M\right)$, which is $\tilde{\mathrm{B}}_{-s, s+n}^{n}$. It follows there is a commutative diagram of exact sequences
![img-14.jpeg](img-14.jpeg)

This diagram presents $B$ as a pullback. To prove this, write $B^{N}=\operatorname{ker}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} \mathrm{~F}^{s-N} M\right)$. Consider the intersection $\mathrm{B}_{-s, s+n}^{N} \cap Z \subseteq \pi_{n} \operatorname{gr}^{s} M$ and let $C$ be the inverse image of the intersection in $\pi_{n} \mathrm{~F}^{s} M$. By construction, the map $C \hookrightarrow \pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} \mathrm{~F}^{s-N} M \rightarrow \operatorname{gr}^{(s-N, s+1)} M$ maps to zero, so $C$ maps to $\operatorname{im}\left(\pi_{n} \mathrm{~F}^{s+1} M \rightarrow \pi_{n} \mathrm{~F}^{s-N} M\right)$ in $\pi_{n} \mathrm{~F}^{s-N} M$. Let $\tilde{C}$ be the pullback in
![img-15.jpeg](img-15.jpeg)

Since the bottom map is an epimorphism, so is $\tilde{C} \rightarrow C$. Let $f$ be the composition $\tilde{C} \rightarrow C \hookrightarrow \pi_{n} \mathrm{~F}^{s} M$ and let $g$ be the composition $\tilde{C} \rightarrow \pi_{n} \mathrm{~F}^{s+1} M \rightarrow \pi_{n} \mathrm{~F}^{s} M$. Consider the map $\tilde{C} \xrightarrow{g-f} \pi_{n} \mathrm{~F}^{s} M$. By construction, $g-f$ maps $\tilde{C}$ into $B^{N}$. The kernel of $\tilde{C} \rightarrow C$ is isomorphic to $\operatorname{ker}\left(\pi_{n} \mathrm{~F}^{s+1} M \rightarrow \pi_{n} \mathrm{~F}^{s-N} M\right)$, which maps to zero in $\pi_{n} \operatorname{gr}^{s} M$ (using any of the maps $f, g$, or $g-f$ ). Thus, there is a commutative square
![img-16.jpeg](img-16.jpeg)

The top and right arrows are surjective and hence the bottom arrow is surjective as well. Since the $t$-structure is compatible with sequential colimits, $B \cong \cup \mathrm{~B}^{N} \rightarrow \cup\left(\mathrm{~B}_{-s, s+n}^{N} \cap Z\right) \cong\left(\cup \mathrm{B}_{-s, s+n}^{n}\right) \cap Z$ is a surjection.

It follows that the induced map $Z / B \rightarrow \dot{\mathrm{Z}}_{-s, s+n}^{\infty} / \tilde{\mathrm{B}}_{-s, s+n}^{\infty} \cong \mathrm{E}_{-s, s+n}^{\infty}$ is injective. It is an isomorphism if $Z \rightarrow \dot{\mathrm{Z}}_{-s, s+n}^{\infty}$ is surjective. This is the case if $\mathrm{F}^{s} M$ is column-bounded, row-bounded, first quadrant, or third quadrant since in those cases $\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} \mathrm{~F}^{(s, s+N+1)} M$ is an isomorphism for large $N$. This proves (iii).

# 7 Indexing conventions 

It should be understood that the choice of $\mathrm{E}_{s, t}^{1}=\pi_{s+t} \mathrm{gr}^{-s} M$ is entirely a convention. One could make many other choices. This one is the Serre grading convention.

Sometimes it is useful to reindex a spectral sequence to start at the second page instead of the first, in which case we write the resulting spectral sequence as ${ }^{\prime} \mathrm{E}^{2}$. This is a purely psychological move, but it leads to some useful comparisons as one can see in Section 9. The matrices to go back and forth between the $\mathrm{E}^{1}$ and $\mathrm{E}^{2}$-conventions are

$$
\left(\begin{array}{cc}
0 & -1 \\
1 & 2
\end{array}\right): \text { from } \mathrm{E}^{2} \text { to } \mathrm{E}^{1} \quad \text { and }\left(\begin{array}{cc}
2 & 1 \\
-1 & 0
\end{array}\right): \text { from } \mathrm{E}^{1} \text { to } \mathrm{E}^{2}
$$

There is also a common reindexing in homotopy theory called the Adams grading convention. The beautiful charts one sees of the Adams spectral sequence are all given in this convention. The matrices to go back and forth between the Serre and Adams grading conventions are

$$
\left(\begin{array}{cc}
0 & -1 \\
1 & 1
\end{array}\right): \text { from Adams to Serre and }\left(\begin{array}{cc}
1 & 1 \\
-1 & 0
\end{array}\right): \text { from Serre to Adams. }
$$

Note that Adams spectral sequences are not spectral sequences if one defines a spectral sequence to have differentials of a certain bidegree.

The main advantage of Adams indexing is that all contributions to $\pi_{n}$ of the abuttment are in the $n$th column and all differentials leaving or entering this column relate to the $(n+1)$ st or $(n-1)$ st column. This makes displaying spectral sequences more compact in some situations.

| $\pi_{*} \mathrm{~F}^{*} M$ | $\mathrm{E}_{s, t}^{1}=\pi_{s+t} \mathrm{gr}^{-s} M \Rightarrow \pi_{s+t} M$ | $(-r, r-1)$ | $\mathrm{F}^{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{\pi, s+n}^{\infty}$ |
| :-- | :-- | :-- | :-- | :-- |
| $\pi_{*} \mathrm{~F}_{*} M$ | $\mathrm{E}_{s, t}^{1}=\pi_{s+t} \mathrm{gr}_{s} M \Rightarrow \pi_{s+t} M$ | $(-r, r-1)$ | $\mathrm{F}_{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}_{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{\pi,-s+n}^{\infty}$ |
| $\mathrm{H}^{*} \mathrm{~F}^{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s+t} \mathrm{gr}^{s} M \Rightarrow \mathrm{H}^{s+t} M$ | $(r,-r+1)$ | $\mathrm{F}^{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}^{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{s,-s+n}$ |
| $\mathrm{H}^{*} \mathrm{~F}_{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s+t} \mathrm{gr}_{-s} M \Rightarrow \mathrm{H}^{s+t} M$ | $(r,-r+1)$ | $\mathrm{F}_{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}_{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{-s, s+n}$ |

Figure 5: Spectral sequence conventions for decreasing filtrations $\mathrm{F}^{*}$ and increasing filtrations $\mathrm{F}_{*}$. We use $\Rightarrow$ even when no convergence is implied.

| $\pi_{*} \mathrm{~F}^{*} M$ | ${ }^{\prime} \mathrm{E}_{s, t}^{2}=\mathrm{E}_{-t, s+2 t}^{1}=\pi_{s+t} \mathrm{gr}^{t} M \Rightarrow \pi_{s+t} M$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{\pi, s+n, s}^{\infty}$ |
| :-- | :-- | :-- |
| $\pi_{*} \mathrm{~F}_{*} M$ | ${ }^{\prime} \mathrm{E}_{s, t}^{2}=\mathrm{E}_{-t, s+2 t}^{1}=\pi_{s+t} \mathrm{gr}_{-t} M \Rightarrow \pi_{s+t} M$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{\pi, s+n,-s}^{\infty}$ |
| $\mathrm{H}^{*} \mathrm{~F}^{*} M$ | ${ }^{\prime} \mathrm{E}_{2}^{s, t}=\mathrm{E}_{1}^{s+t, s+2 t}=\mathrm{H}^{s+t} \mathrm{gr}^{-t} M \Rightarrow \mathrm{H}^{s+t} M$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{s+n,-s}$ |
| $\mathrm{H}^{*} \mathrm{~F}_{*} M$ | ${ }^{\prime} \mathrm{E}_{2}^{s, t}=\mathrm{E}_{1}^{s+t, s+2 t}=\mathrm{H}^{s+t} \mathrm{gr}_{t} M \Rightarrow \mathrm{H}^{s+t} M$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{-s+n, s}$ |

Figure 6: Reindexing to ${ }^{\prime} \mathrm{E}^{2}$. The differentials have the same bidegree as in the $\mathrm{E}^{1}$-spectral sequences from Figure 1. The filtrations on the abutment are also defined in the same way as in the $\mathrm{E}^{1}$ spectral sequences.

| $\pi_{*} \mathrm{~F}^{*} M$ | $\mathrm{E}_{s, t}^{1}=\pi_{s} \mathrm{gr}^{t} M \Rightarrow \pi_{s} M$ | $(-1, r)$ | $\mathrm{F}^{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}^{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}^{s} \pi_{n} M \cong \mathrm{E}_{n, s}^{\infty}$ |
| :-- | :-- | :-- | :-- | :-- |
| $\pi_{*} \mathrm{~F}_{*} M$ | $\mathrm{E}_{s, t}^{1}=\pi_{s} \mathrm{gr}_{-t} M \Rightarrow \pi_{s} M$ | $(-1, r)$ | $\mathrm{F}_{s} \pi_{n} M=\operatorname{im}\left(\pi_{n} \mathrm{~F}_{s} M \rightarrow \pi_{n} M\right)$ | $\mathrm{gr}_{s} \pi_{n} M \cong \mathrm{E}_{n,-s}^{\infty}$ |
| $\mathrm{H}^{*} \mathrm{~F}^{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s} \mathrm{gr}^{-t} M \Rightarrow \mathrm{H}^{s} M$ | $(1,-r)$ | $\mathrm{F}^{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}^{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}^{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{n,-s}$ |
| $\mathrm{H}^{*} \mathrm{~F}_{*} M$ | $\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s} \mathrm{gr}_{t} M \Rightarrow \mathrm{H}^{s} M$ | $(1,-r)$ | $\mathrm{F}_{s} \mathrm{H}^{n} M=\operatorname{im}\left(\mathrm{H}^{n} \mathrm{~F}_{s} M \rightarrow \mathrm{H}^{n} M\right)$ | $\mathrm{gr}_{s} \mathrm{H}^{n} M \cong \mathrm{E}_{\infty}^{n, s}$ |

Figure 7: Adams indexing spectral sequence conventions.

# 8 Multiplicativity 

Compare the material in this section to related results in Hedenlund's thesis [18].
Definition 8.1. The $\mathrm{E}^{r}$-page construction defines a functor

$$
\mathrm{E}^{r}: \mathrm{F} \mathcal{C} \rightarrow \operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\ominus}\right)\right)
$$

from the $\infty$-category of filtrations in $\mathcal{C}$ to the 1-category of graded objects in cochain complexes in $\mathcal{C}^{\ominus}$. The weight $n$ piece of the $\mathrm{E}^{r}$-page is the cochain complex is the weight $n$ piece of the $\mathrm{E}^{1}$-page of $\operatorname{Dec}^{(r-1)}(\mathrm{F})$, which is

$$
\mathrm{E}_{-\bullet, n}^{1}\left(\operatorname{Dec}^{(r-1)}(\mathrm{F})\right)
$$

Under the regrading, this corresponds to

$$
\mathrm{E}_{(r-1) n-r \bullet,-(r-2) n+(r-1) \bullet}^{r}
$$

which is the line of slope $\frac{1-r}{r}=-1+\frac{1}{r}$ through the point of height $n-\frac{n}{r}$ on the $t$-axis. This cochain complex is indexed so that the cohomological degree 0 term is $\mathrm{E}_{(r-1) n,-(r-2) n}^{r}$ and the cohomological degree 1 term is $\mathrm{E}_{(r-1) n-r,-(r-2) n+(r-1)}^{r}$. Note that the cohomological degree $n$ term in weight $n$ is $\mathrm{E}_{-n, n}^{r}$. See Figure 9 for an illustration of the weight 1 term on the first three pages of a general spectral sequence.

The choice of indexing for the $\mathrm{E}^{r}$-page is not arbitrary but is enforced by the décalage approach to spectral sequences; see Theorem 4.13. We note the following lemma for the readers convenience.

Lemma 8.2. The term $\mathrm{E}_{s, t}^{r}$ is the cohomological degree $(r-2) s+(r-1) t$ term in weight $(r-1) s+r t$.
![img-17.jpeg](img-17.jpeg)

Figure 8: The $\mathrm{E}_{1}, \mathrm{E}_{2}$, and $\mathrm{E}_{3}$-pages of a general spectral sequence.
The reader is referred to [24, Chap. 2] for all conventions about symmetric monoidal structures and the related theory of $\infty$-operads.

For a symmetric monoidal structure $\mathcal{C}^{\otimes}$ on an $\infty$-category $\mathcal{C}$, the tensor product of two objects $X$ and $Y$ is written $X \otimes_{\mathcal{C}} Y$. In the case where $\mathcal{C}=\operatorname{Perf}(k)^{\otimes}$ or $\mathcal{C}=\mathrm{D}(k)^{\otimes}$ for an $\mathbf{E}_{\infty}$-ring $k$, this notation will be simplified to $X \otimes_{k} Y$.

Let $\mathcal{C}$ be a stable $\infty$-category. If $\mathcal{C}$ admits both a symmetric monoidal structure $\mathcal{C}^{\otimes}$ such that the tensor product is exact in each variable and a $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$, the $t$-structure is said to be compatible with the symmetric monoidal structure if $\mathcal{C}_{\geqslant 0}$ contains the unit object $\mathbf{1}_{\mathcal{C}}$ and is closed under tensor products.

![img-18.jpeg](img-18.jpeg)

Figure 9: The weight 1 parts of the $\mathrm{E}_{1}, \mathrm{E}_{2}$, and $\mathrm{E}_{3}$-pages of a general spectral sequence. The o class is degree 0 of the cochain complex.

In this case, the prestable $\infty$-category $\mathcal{C}_{\geqslant 0}$ inherits a symmetric monoidal structure $\mathcal{C}_{\geqslant 0}^{\otimes}$ and the inclusion $\mathcal{C}_{\geqslant 0} \subseteq \mathcal{C}$ is symmetric monoidal.

Suppose that $\mathcal{C}$ is a stable $\infty$-category with a symmetric monoidal structure $\mathcal{C}^{\otimes}$ which is exact in each variable and suppose also that $\mathcal{C}$ admits sequential colimits and that the tensor product preserves sequential colimits in each variable. Using that $\mathbf{Z}^{\text {op }}$ naturally admits a symmetric monoidal structure given by addition of integers, there is an induced Day convolution symmetric monoidal structure $\mathrm{FC}^{\otimes}$ on the $\infty$-category $\operatorname{Fun}\left(\mathbf{Z}^{\text {op }}, \mathcal{C}\right)$ of decreasing filtrations in $\mathcal{C}$. This is constructed in general in the $\infty$-categorical context by Glasman [15]; see also [24, Ex. 2.2.6.17]. To describe the tensor product of any given pair of decreasing filtrations $\mathrm{F}^{*}$ and $\mathrm{G}^{*}$, one considers the left Kan extension
![img-19.jpeg](img-19.jpeg)

The left Kan extension exists by our assumption that $\mathcal{C}$ admits sequential colimits and hence all countable colimits since $\mathcal{C}$ is stable.

The constant filtrations $\mathcal{C} \subseteq \mathrm{F} \mathcal{C}$ form a $\otimes$-ideal in $\mathrm{F} \mathcal{C}$ since if $\mathrm{F}^{\star}$ is the constant filtration on $M$, then $\mathrm{F}^{\star} \otimes_{\mathrm{F} \mathcal{C}} \mathrm{G}^{\star}$ is the constant filtration on $M \otimes_{\mathcal{C}} \mathrm{G}^{-\infty}$, as one sees from the left Kan extension definition above. It follows that if $\mathcal{C}$ admits sequential limits, then $\widetilde{\mathrm{F}} \mathcal{C}$ admits a symmetric monoidal structure $\widetilde{\mathrm{F}} \mathcal{C}^{\otimes}$. The tensor product here is the completed tensor product $\widetilde{\otimes}$ obtained by computing the tensor product in $\mathrm{F} \mathcal{C}$ and then completing.
Warning 8.3. The category $\Xi^{\text {op }}$ which classifies cochain complexes is also symmetric monoidal. However, the induced Day convolution symmetric monoidal structure on $\widetilde{\mathrm{F}} \mathcal{C} \simeq \operatorname{Fun}\left(\Xi^{\mathrm{op}}, \mathcal{C}\right)$ does not agree with the symmetric monoidal structure on $\widetilde{\mathrm{F}} \mathcal{C}$ induced by completing the Day convolution symmetric monoidal structure on $\operatorname{Fun}\left(\mathbf{Z}^{\text {op }}, \mathcal{C}\right)$. Indeed, as pointed out by Thomas Nikolaus, this does not even work in the 1-categorical situation of ordinary cochain complexes of abelian groups. The unit object of $\operatorname{Fun}\left(\Xi^{\mathrm{op}}, \mathcal{A b}\right)$ is the cochain complex $\cdots \rightarrow 0 \rightarrow \mathbf{Z} \xrightarrow{\text { id }} \mathbf{Z} \rightarrow 0 \rightarrow \cdots$, where the non-trivial entries are in cohomological degrees 0 and 1 .

Left Kan extension along $\mathbf{Z}^{\delta} \rightarrow \mathbf{Z}^{\text {op }}$ induces a symmetric monoidal functor ins ${ }^{\star}: \operatorname{GrC}^{\otimes} \rightarrow \mathrm{F} \mathcal{C}^{\otimes}$.
Proposition 8.4. The associated graded functor $\mathrm{F} \mathcal{C} \rightarrow \mathrm{GrC}$ naturally upgrades to a symmetric monoidal functor $\mathrm{F} \mathcal{C}^{\otimes} \rightarrow \mathrm{GrC}^{\otimes}$ and the induced composition $\mathrm{GrC}^{\otimes} \rightarrow \mathrm{F} \mathcal{C}^{\otimes} \rightarrow \mathrm{GrC}^{\otimes}$ is equivalent to the identity as a symmetric monoidal functor.
Proof. This is not a formal result and is proved in [23, Prop. 3.2.1] when $\mathcal{C} \simeq \mathbb{S p}$. That proof works in general.

The proposition gives one of the main ways to understand the tensor product on filtered objects. Indeed, the tensor product on $\mathrm{GrC}^{\otimes}$ is straightforward. If $X(\star)$ and $Y(\star)$ are graded objects in $\mathcal{C}$, then

$$
\left(X \otimes_{\mathrm{GrC}} Y\right)(s) \simeq \bigoplus_{i+j=s} X(i) \otimes_{\mathcal{C}} Y(j)
$$

For example, this is used in the next lemma to understand the compatibility of the Day convolution symmetric monoidal structure on $\mathrm{F} \mathcal{C}$ with Beilinson $t$-structures.
Lemma 8.5. Suppose that $\mathcal{C}$ is a stable $\infty$-category admitting sequential limits and colimits and equipped with a symmetric monoidal structure $\mathcal{C}^{\otimes}$ whose tensor product is exact and preserves sequential colimits in each variable. If $\mathcal{C}$ is additionally equipped with a t-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$ compatible with $\mathcal{C}^{\otimes}$, then the induced Beilinson $t$-structure on $\mathrm{F} \mathcal{C}$ is compatible with the Day convolution symmetric monoidal structure on $\mathrm{F} \mathcal{C}^{\otimes}$.
Proof. The unit object of $\mathrm{F} \mathcal{C}^{\otimes}$ is ins ${ }^{0} \mathbf{1}_{\mathcal{C}}$ which has $\mathrm{gr}^{0}$ ins ${ }^{0} \mathbf{1}_{\mathcal{C}} \simeq \mathbf{1}_{\mathcal{C}}$ and $\mathrm{gr}^{s}$ ins ${ }^{0} \mathbf{1}_{\mathcal{C}} \simeq 0$ for $s \neq 0$. This object is connective in the Beilinson $t$-structure. The tensor product formula $\operatorname{gr}^{s}\left(\mathrm{~F}^{\star} \otimes_{\mathrm{F} \mathcal{C}} \mathrm{G}^{\star}\right) \simeq \oplus_{i+j=s} \operatorname{gr}_{\mathrm{F}}^{i} \otimes_{\mathcal{C}} \operatorname{gr}_{\mathrm{G}}^{j}$ shows that if $\mathrm{F}^{\star}$ and $\mathrm{G}^{\star}$ are connective in the Beilinson $t$-structure, then so is $\mathrm{F}^{\star} \otimes_{\mathrm{F} \mathcal{C}} \mathrm{G}^{\star}$.

If $\mathcal{C}$ is a stable $\infty$-category equipped with a symmetric monoidal structure $\mathcal{C}^{\otimes}$ whose tensor product is exact in each variable and a compatible $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$, then $\mathcal{C}^{\bigcirc}$ inherits a symmetric monoidal structure $\mathcal{C}^{\bigcirc}, \otimes$. Indeed, by definition, the $\infty$-category $\mathcal{C}_{\geqslant 0}$ of connective objects inherits a symmetric monoidal structure $\mathcal{C}_{\geqslant 0}^{\otimes}$ by compatibility. The unit object of $\mathcal{C}^{\bigcirc}, \otimes$ is $\pi_{0} \mathbf{1}_{\mathcal{C}}$ and the tensor product is formed by forming the tensor product in $\mathcal{C}_{\geqslant 0}$ and applying $\pi_{0}$.
Example 8.6 (Koszul symmetric monoidal structure). Let $\mathcal{C}$ be a symmetric monoidal stable $\infty$-category with sequential colimits whose tensor product is exact and preserves sequential colimits in each variable with a compatible $t$-structure. Then, GrC admits a symmetric monoidal structure via Day convolution and a compatible $t$-structure where a graded object $X(\star)$ is connective if $X(i) \in \mathcal{C}_{\geqslant i}$ for all $i \in \mathbf{Z}$. The heart $(\mathrm{GrC})^{\bigcirc}$ is equivalent to the abelian category $\operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right)$ of graded objects in $\mathcal{C}^{\bigcirc}$ and the induced symmetric monoidal structure agrees with the usual monoidal structure on graded objects, with a symmetric braiding given by the Koszul sign rule. We will call this the Koszul symmetric monoidal structure on $\operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right)$.

Lemma 8.7. Suppose that $\mathcal{C}$ is a stable $\infty$-category with sequential colimits equipped with a symmetric monoidal structure $\mathcal{C}^{\otimes}$ whose tensor product is exact and preserves sequential colimits in each variable and a compatible $t$-structure $\left(\mathcal{C}_{\geqslant 0}, \mathcal{C}_{\leqslant 0}\right)$. Then, the functors

$$
\tau_{\geqslant \star}: \mathcal{C} \rightarrow \mathrm{F} \mathcal{C}
$$

and

$$
\pi_{\star}: \mathcal{C} \rightarrow \operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right)
$$

admit lax symmetric monoidal structures, where $\mathrm{F} \mathcal{C}$ is equipped with the Day convolution symmetric monoidal structure and $\operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right)$ is equipped with the Koszul symmetric monoidal structure.

Proof. Consider the $t$-structure on $\mathrm{F} \mathcal{C}$ with connective objects those filtrations $\mathrm{F}^{\star}$ such that $\mathrm{F}^{s}$ is in $\mathcal{C}_{\geqslant s}$ for all $s \in \mathbf{Z}$. This is not a Beilinson $t$-structure, but it is still compatible with the Day convolution symmetric monoidal structure on $\mathcal{C}$. It is called the positive $t$-structure by Raksit in [30]. We will call it the Postnikov $t$-structure and denote its connective objects by $\left(\mathrm{F} \mathcal{C}\right)_{\geqslant 0}^{\mathrm{P}}$. In particular, since the inclusion $\mathrm{F} \mathcal{C}_{\geqslant 0}^{\mathrm{P}} \subseteq \mathrm{F} \mathcal{C}$ is symmetric monoidal, the right adjoint $\tau_{\geqslant 0}^{\mathrm{P}}$ is lax symmetric monoidal. The heart of the positive $t$-structure is $\operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right)$ with the Koszul sign rule. Now, $\tau_{\geqslant \star}$ is the composition of the lax symmetric monoidal functors

$$
\mathcal{C} \xrightarrow{\text { constant }} \mathrm{F} \mathcal{C} \xrightarrow{\tau_{\geqslant 0}^{\mathrm{P}}} \mathrm{~F} \mathcal{C}_{\geqslant 0}^{\mathrm{P}}
$$

and $\pi_{\star}$ is the composition of the lax symmetric monoidal functors

$$
\mathcal{C} \xrightarrow{\text { constant }} \mathrm{F} \mathcal{C} \xrightarrow{\tau_{\geqslant 0}^{\mathrm{P}}} \mathrm{~F} \mathcal{C}_{\geqslant 0}^{\mathrm{P}} \xrightarrow{\pi_{\star}^{\mathrm{P}}} \operatorname{Gr}\left(\mathcal{C}^{\bigcirc}\right) .
$$

This completes the proof.
Construction 8.8 (The $\mathrm{E}^{r}$-monoidal structure). Let $\mathcal{C}^{\otimes}$ be a stable symmetric monoidal $\infty$-category which admits sequential limits and colimits, whose tensor product is exact and preserves sequential colimits in each variable, and which is equipped with a compatible $t$-structure. We view the $\mathrm{E}^{r}$-page functor as a functor from $\mathrm{F} \mathcal{C}$ to $\left.\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)$. We want to view the latter category as being symmetric monoidal. We do this by observing that it is the heart of $\mathrm{F}(\mathrm{F} \mathcal{C})$ with respect to the $t$-structure on bifiltrations $\mathrm{F}^{\star, \star}$ where the connective objects are those where $\mathrm{F}^{i, \star}$ is $i$-connective in the Beilinson $t$-structure. This is $t$-structure is "half-Postnikov, half-Beilinson." Call this the $\mathrm{E}^{1}$-symmetric monoidal structure $\left.\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)^{\otimes_{\mathrm{E}^{1}}}\right.$. The $\mathrm{E}^{r}$-monoidal structure is obtained by transport of structure via the reindexing functor given by

$$
\left(\begin{array}{cc}
0 & -1 \\
1 & 2
\end{array}\right)^{-r+1}
$$

Theorem 8.9. Let $\mathcal{C}^{\otimes}$ be a stable symmetric monoidal $\infty$-category which admits sequential limits and colimits, whose tensor product is exact and preserves sequential colimits in each variable, and which is equipped with a compatible $t$-structure. For each $r \geqslant 1$, the $\mathrm{E}^{r}$-page functor upgrades to a lax symmetric monoidal functor $\mathrm{F} \mathcal{C}^{\otimes} \rightarrow \operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)^{\otimes_{\mathrm{E}^{r}}}$.

Proof. For $r=1$, the result follows by applying Lemma 8.7 with respect to the Beilinson $t$-structure. Now, we claim that the functor $\mathrm{F}^{\star} \mapsto \tau_{\geqslant \star}^{\mathrm{B}}(\mathrm{F})$ from $\mathrm{F} \mathcal{C}$ to $\mathrm{FF} \mathcal{C}$ is lax symmetric monoidal. This is another application of Lemma 8.7. Thus, $\operatorname{Dec}^{(r-1)}$ is lax symmetric monoidal by composition. It follows that $\mathrm{F}^{\star} \mapsto \mathrm{E}^{1}\left(\operatorname{Dec}^{(r-1)}(\mathrm{F})\right)$ is lax symmetric monoidal with target the $\mathrm{E}^{1}$-symmetric monoidal structure on $\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)$. The theorem follows by reindexing.

Corollary 8.10. Let $\mathcal{C}^{\otimes}$ be a stable symmetric monoidal $\infty$-category which admits sequential limits and colimits, whose tensor product is exact and preserves sequential colimits in each variable, and which is equipped with a compatible $t$-structure. Suppose that $\mathcal{O}$ is an $\infty$-operad in $\mathcal{C}_{\geqslant 0}^{\otimes}$. For each $r \geqslant 1$ the $\mathrm{E}^{r}$-page functor upgrades to a functor

$$
\mathrm{E}^{r}: \operatorname{Alg}_{\mathcal{O}}\left(\mathrm{F} \mathcal{C}^{\otimes}\right) \rightarrow \operatorname{Alg}_{\mathcal{O}}\left(\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)^{\otimes_{\mathrm{E}^{r}}}\right)
$$

Example 8.11 (Rings). If $\mathrm{F}^{\star} R$ is a filtered $\mathbf{E}_{1}$-ring spectrum, then each page $\mathrm{E}^{r}$ of the spectral sequence for $\mathrm{F}^{\star} R$ is an associative algebra object in $\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)$. If $\mathrm{F}^{\star} R$ is an $\mathbf{E}_{\infty}$-ring spectrum, then each page $\mathrm{E}^{r}$ of the spectral sequence for $\mathrm{F}^{\star} R$ is a commutative algebra object in $\operatorname{Gr}\left(\mathrm{Ch}^{\bullet}\left(\mathcal{C}^{\bigcirc}\right)\right)$. These cases follow from Theorem 8.9 applied to the $\mathbf{E}_{1}$ and $\mathbf{E}_{\infty}$ operads.

To make this more explicit, if $\mathrm{F}^{\star} R$ is an $\mathbf{E}_{\infty}$-ring, then $\mathrm{E}_{-r \bullet,(r-1) \bullet}^{r}$ is a cdga in $\mathcal{C}^{\bigcirc}$ and the graded collection

$$
\left\{\mathrm{E}_{(r-1) t-r \bullet,-(r-2) t+(r-1) \bullet}^{r}\right\}_{t \in \mathbf{Z}}
$$

forms a graded-commutative ring in graded cochain complexes, meaning that there are morphisms $\mathrm{E}_{s, t}^{r} \otimes$ $\mathrm{E}_{s^{\prime}, t^{\prime}}^{r} \rightarrow \mathrm{E}_{s+s^{\prime}, t+t^{\prime}}^{r}$ satisfying the bigraded Koszul sign rule $x y=(-1)^{(s+t)\left(s^{\prime}+t^{\prime}\right)} y x$ and satisfying the following Leibniz rule for the horizontal differentials: $\mathrm{d}^{1}(x y)=\mathrm{d}^{1}(x) y+(-1)^{s+t} x \mathrm{~d}^{1}(y)$ if $x \in \mathrm{E}_{s, t}^{r}$. These sign rules become the ordinary sign rules on the total complex associated to this graded cochain complex. These are justified by the fact $\mathrm{E}_{s, t}^{r}$ has weight $(n-1) s+n t$ and cohomological degree $(n-2) s+(n-1) t$ by Lemma 8.2, so the total degree $s+t$ has the same parity as $(n-1) s+n t+(n-2) s+(n-1) t=(2 n-3) s+(2 n-1) t$.

# 9 The Atiyah-Hirzebruch spectral sequence 

Let $X$ be a CW complex, which we view as an anima $X$ with an exhaustive increasing filtration $\mathrm{F}_{\star} X$ where $\mathrm{F}_{s} X=\emptyset$ for $s<0$ and each $\mathrm{F}_{s} X / \mathrm{F}_{s-1}$ is equivalent to a bouquet of $s$-spheres, called the $s$-cells of $X$, for $s \geqslant 0$. Taking singular cochains $\mathrm{R} \Gamma(X, \mathbf{Z})$ we obtain an object of $\mathrm{D}(\mathbf{Z})$ which we equip with the decreasing filtration

$$
\mathrm{F}^{s} \mathrm{R} \Gamma(X, \mathbf{Z})=\operatorname{fib}\left(\mathrm{R} \Gamma(X, \mathbf{Z}) \rightarrow \mathrm{R} \Gamma\left(X_{s-1}, \mathbf{Z}\right)\right)
$$

This filtration is complete and exhaustive with graded pieces given by $\operatorname{gr}^{s} \mathrm{R} \Gamma(X, \mathbf{Z}) \simeq \prod_{s \text {-cells }} \mathbf{Z}[-s]$. The associated (cohomological) spectral sequences is

$$
\mathrm{E}_{1}^{s, t}=\mathrm{H}^{s+t} \operatorname{gr}^{s} \mathrm{R} \Gamma(X, \mathbf{Z}) \cong \mathrm{H}^{s+t} \prod_{s \text {-cells }} \mathbf{Z}[-s] \cong \begin{cases}\prod_{s \text {-cells }} \mathbf{Z} & \text { if } t=0 \text { and } \\ 0 & \text { otherwise }\end{cases}
$$

The spectral sequence is thus concentrated on the ray from $(0,0)$ to $(\infty, 0)$, giving a cochain complex

$$
0 \rightarrow \prod_{0 \text {-cells }} \mathbf{Z} \rightarrow \prod_{1 \text {-cells }} \mathbf{Z} \rightarrow \prod_{2 \text {-cells }} \mathbf{Z} \rightarrow \cdots
$$

The differentials in this cochain complex are precisely the differentials in the cochain complex computing the CW cohomology of $X$. In particular, $\pi_{0}^{\mathrm{B}}\left(\mathrm{F}^{\star} \mathrm{R} \Gamma(X, \mathbf{Z})\right)$ is the CW cohomology cochain complex. Thus, $\mathrm{E}_{s, 0}^{2} \cong \mathrm{E}_{s, 0}^{\infty} \cong \mathrm{H}_{\mathrm{CW}}^{s}(X, \mathbf{Z})$ and the spectral sequence collapses at the $\mathrm{E}^{2}$-page. One finds that

$$
\operatorname{Dec}(\mathrm{F})^{s} \mathrm{R} \Gamma(X, \mathbf{Z}) \simeq \begin{cases}0 & \text { if } s>0 \text { and } \\ \mathrm{R} \Gamma(X, \mathbf{Z}) & \text { if } s \leqslant 0\end{cases}
$$

Remark 9.1 (Multiplicative structures and CW cohomology). It is well-known that the $\mathbf{E}_{\infty}$-algebra $\mathrm{R} \Gamma(X, \mathbf{Z})$ cannot generally be computed by a cdga. This implies that for such $X$ no CW filtration $\mathrm{F}^{\star} \mathrm{R} \Gamma(X, \mathbf{Z})$ can be given the structure of an $\mathbf{E}_{\infty}$-algebra object in $\mathrm{FD}(\mathbf{Z})$. If it could be, then $\pi_{0}^{\mathrm{B}}$ would admit the structure of a commutative algebra object by the results of Section 8; this would be a cdga computing $\mathrm{R} \Gamma(X, \mathbf{Z})$.

Suppose that $X$ is a CW complex and fix a spectrum $M$. We will write $\mathrm{H}^{i}(M)=\pi_{-i} M$ below for convenience. There are two classical ways to construct a spectral sequence for computing $\pi_{*} \mathrm{R} \Gamma(X, M)$, either by filtering $M$ or by filtering $X$.

First, consider the cellular filtration given as in the previous section by

$$
\mathrm{F}^{s} \mathrm{R} \Gamma(X, M)=\operatorname{fib}\left(\mathrm{R} \Gamma(X, M) \rightarrow \mathrm{R} \Gamma\left(X_{s-1}, M\right)\right)
$$

The associated graded pieces are

$$
\operatorname{gr}_{\mathrm{F}}^{s} \mathrm{R} \Gamma(X, M) \simeq\left(\mathrm{R} \Gamma\left(X_{s-1}, M\right) / \mathrm{R} \Gamma\left(X_{s}, M\right)\right)[-1] \simeq \prod_{s \text {-cells }} M[-s]
$$

The associated spectral sequence has

$$
\mathrm{E}_{1}^{s, t}(\mathrm{~F})=\mathrm{H}^{s+t}\left(\prod_{s \text {-cells }} M[-s]\right) \cong \prod_{s \text {-cells }} \mathrm{H}^{t}(M) \Rightarrow \mathrm{H}^{s+t}(X, M)
$$

By dévissage one can reduce to the case when $M \simeq \mathbf{Z}$ to compute the differential on the $\mathrm{E}_{1}$-page as the CW cohomology differential. It follows that

$$
\mathrm{E}_{2}^{s, t}(\mathrm{~F})=\mathrm{H}^{s}\left(X, \mathrm{H}^{t}(M)\right)
$$

Second, consider the Whitehead tower

$$
\mathrm{G}^{*} M=\tau_{\geqslant *} M
$$

of $M$ and take cochains to obtain a new filtration $\mathrm{G}^{*} \mathrm{R} \Gamma(X, M)=\mathrm{R} \Gamma\left(X, \tau_{\geqslant *} M\right)$ with graded pieces $\operatorname{gr}_{\mathrm{G}}^{s} \mathrm{R} \Gamma(X, M) \simeq \mathrm{R} \Gamma\left(X, \operatorname{gr}^{s} M\right) \simeq \mathrm{R} \Gamma\left(X,\left(\mathrm{H}^{-s} M\right)[s]\right)$. The $\mathrm{E}_{1}$-page of the associated spectral sequence is

$$
\mathrm{E}_{1}^{s, t}(\mathrm{G})=\mathrm{H}^{s+t}\left(X,\left(\mathrm{H}^{-s} M\right)[s]\right) \cong \mathrm{H}^{2 s+t}\left(X, \mathrm{H}^{-s} M\right) \Rightarrow \mathrm{H}^{s+t} \mathrm{R} \Gamma(X, M)
$$

Via the standard reindexing of an $\mathrm{E}_{1}$-spectral sequence to an ${ }^{\prime} \mathrm{E}_{2}$-spectral sequence discussed in Section 7, one obtains an ${ }^{\prime} \mathrm{E}_{2}$-spectral sequence

$$
{ }^{\prime} \mathrm{E}_{2}^{s, t}(\mathrm{G})=\mathrm{H}^{s}\left(X, \mathrm{H}^{t}(M)\right) \Rightarrow \mathrm{H}^{s+t}(X, M)
$$

It is natural to ask for the relationship between these two spectral sequences.
Proposition 9.2. There is an equivalence $\operatorname{Dec}(\mathrm{F})^{*} \mathrm{R} \Gamma(X, M) \simeq \mathrm{G}^{*} \mathrm{R} \Gamma(X, M)$ of filtered spectra, functorial in $M$ and the $C W$ complex structure on $X$.
Proof. Consider the bifiltration $\mathrm{H}^{a, b}=\operatorname{fib}\left(\mathrm{R} \Gamma\left(X, \tau_{\geqslant a} M\right) \rightarrow \mathrm{R} \Gamma\left(X_{s-1}, \tau_{\geqslant a} M\right)\right)$. If $a$ is fixed, then $\frac{\mathrm{H}^{a, s}}{\mathrm{H}^{a, s+t}} \simeq$ $\prod_{a \text {-cells }}\left(\tau_{\geqslant a} M\right)[-s]$, which is $(a-s)$-connective. In particular, the natural map $\mathrm{H}^{a, *} \rightarrow \mathrm{~F}^{*}$ factors through $\tau_{\geqslant a}^{\mathrm{B}}(\mathrm{F})^{*}$. It is in fact an equivalence. Indeed, both $\mathrm{H}^{a, *}$ and $\tau_{\geqslant a}^{\mathrm{B}}(\mathrm{F})^{*}$ are complete filtrations (the latter because $\mathrm{F}^{*}$ is, see Lemma 4.18), so it suffices to check this on associated graded pieces. However,

$$
\frac{\mathrm{H}^{a, s}}{\mathrm{H}^{a, s+1}} \simeq \prod_{s \text {-cells }}\left(\tau_{\geqslant a} M\right)[-s] \simeq \tau_{\geqslant a-s}\left(\prod_{s \text {-cells }} M[-s]\right) \simeq \tau_{\geqslant a-s} \operatorname{gr}_{\mathrm{F}}^{s} \simeq \operatorname{gr}^{s} \tau_{\geqslant a}^{\mathrm{B}}(\mathrm{~F})
$$

where the second equivalence follows from the compatibility of the $t$-structure on $\delta \mathrm{p}$ with arbitrary products. It follows that $\mathrm{H}^{a, *} \simeq \tau_{\geqslant a}^{\mathrm{B}}(\mathrm{F})$ and hence that $\left|\mathrm{H}^{a, *}\right| \simeq \operatorname{Dec}(\mathrm{F})^{a}$. However, $\left|\mathrm{H}^{a, *}\right| \simeq \mathrm{G}^{a}$. This completes the proof.

The following consequence was proved by Maunder in [26, Thm. 3.3] with different methods.
Corollary 9.3. There is an isomorphism of spectral sequences $\mathrm{E}_{s, t}^{r}(\mathrm{~F}) \cong{ }^{\prime} \mathrm{E}_{s, t}^{r}(\mathrm{G})$ starting at the second page.
One often says that $\mathrm{E}^{r}(\mathrm{~F})$ and ${ }^{\prime} \mathrm{E}^{r}(\mathrm{G})$ agree from the $\mathrm{E}^{2}$-page on.

# References 

[1] Benjamin Antieau, Periodic cyclic homology and derived de Rham cohomology, Ann. K-Theory 4 (2019), no. 3, 505-519. MR 4043467
[2] Benjamin Antieau, David Gepner, and Jeremiah Heller, K-theoretic obstructions to bounded t-structures, Invent. Math. 216 (2019), no. 1, 241-300. MR 3935042
[3] Benjamin Antieau and Thomas Nikolaus, Cartier modules and cyclotomic spectra, J. Amer. Math. Soc. 34 (2021), no. 1, 1-78. MR 4188814
[4] Stefano Ariotta, Coherent cochain complexes and Beilinson t-structures, with an appendix by Achim Krause, arXiv preprint arXiv:2109.01017 (2021).
[5] David Ayala, Aaron Mazel-Gee, and Nick Rozenblyum, Stratified noncommutative geometry, Mem. Amer. Math. Soc. 297 (2024), no. 1485, iii+260. MR 4760797
[6] A. A. Beïlinson, On the derived category of perverse sheaves, $K$-theory, arithmetic and geometry (Moscow, 1984-1986), Lecture Notes in Math., vol. 1289, Springer, Berlin, 1987, pp. 27-41. MR 923133
[7] Bhargav Bhatt, Matthew Morrow, and Peter Scholze, Topological Hochschild homology and integral p-adic Hodge theory, Publ. Math. Inst. Hautes Études Sci. 129 (2019), 199-310. MR 3949030
[8] J. Michael Boardman, Conditionally convergent spectral sequences, Homotopy invariant algebraic structures (Baltimore, MD, 1998), Contemp. Math., vol. 239, Amer. Math. Soc., Providence, RI, 1999, pp. 49-84. MR 1718076
[9] Joana Cirici, Daniela Egas Santander, Muriel Livernet, and Sarah Whitehouse, Model category structures and spectral sequences, Proc. Roy. Soc. Edinburgh Sect. A 150 (2020), no. 6, 2815-2848. MR 4190091
[10] Joana Cirici and Francisco Guillén, Homotopy theory of mixed Hodge complexes, Tohoku Math. J. (2) 68 (2016), no. 3, 349-375. MR 3550924
[11] Dustin Clausen and Akhil Mathew, Hyperdescent and étale K-theory, Invent. Math. 225 (2021), no. 3, 981-1076. MR 4296353
[12] Pierre Deligne, Théorie de Hodge. II, Inst. Hautes Études Sci. Publ. Math. (1971), no. 40, 5-57. MR 498551
[13] , Théorie de Hodge. III, Inst. Hautes Études Sci. Publ. Math. (1974), no. 44, 5-77. MR 498552
[14] Bogdan Gheorghe, Daniel C. Isaksen, Achim Krause, and Nicolas Ricka, $\mathbb{C}$-motivic modular forms, J. Eur. Math. Soc. (JEMS) 24 (2022), no. 10, 3597-3628. MR 4432907
[15] Saul Glasman, Day convolution for $\infty$-categories, Math. Res. Lett. 23 (2016), no. 5, 1369-1385. MR 3601070
[16] Owen Gwilliam and Dmitri Pavlov, Enhancing the filtered derived category, J. Pure Appl. Algebra 222 (2018), no. 11, 3621-3674. MR 3806745
[17] Jeremy Hahn, Arpon Raksit, and Dylan Wilson, A motivic filtration on the topological cyclic homology of commutative ring spectra, arXiv preprint arXiv:2206.11208 (2022).
[18] Alice Hedenlund, Multiplicative Tate spectral sequences, available at https://www.mn.uio.no/math/ personer/vit/rognes/theses/hedenlund-thesis.pdf, 2020, PhD thesis at Oslo.

[19] André Joyal, Notes on quasi-categories, preprint (2008), available at https://www.math.uchicago.edu/ ~may/IMA/Joyal.pdf.
[20] Tyler Lawson, Filtered spaces, filtered objects, arXiv preprint arXiv:2410.08348 (2024).
[21] Marc Levine, The Adams-Novikov spectral sequence and Voevodsky's slice tower, Geom. Topol. 19 (2015), no. 5, 2691-2740. MR 3416112
[22] Muriel Livernet and Sarah Whitehouse, Spectral sequences via linear presheaves, arXiv preprint arXiv:2406.02777 (2024).
[23] Jacob Lurie, Rotation invariance in algebraic K-theory, available at https://www.math.ias.edu/ ~lurie/papers/Waldhaus.pdf.
[24] , Higher algebra, available at https://www.math.ias.edu/ lurie/papers/HA.pdf, version dated 18 September 2017.
[25] , Spectral algebraic geometry, available at https://www.math.ias.edu/ lurie/papers/ SAG-rootfile.pdf, version dated 3 February 2018.
[26] C. R. F. Maunder, The spectral sequence of an extraordinary cohomology theory, Proc. Cambridge Philos. Soc. 59 (1963), 567-574. MR 150765
[27] John McCleary, A user's guide to spectral sequences, second ed., Cambridge Studies in Advanced Mathematics, vol. 58, Cambridge University Press, Cambridge, 2001. MR 1793722
[28] Itamar Mor, Picard and Brauer groups of $K(n)$-local spectra via profinite Galois descent, arXiv preprint arXiv:2306.05393 (2023).
[29] Tasos Moulinos, The geometry of filtrations, Bull. Lond. Math. Soc. 53 (2021), no. 5, 1486-1499. MR 4335221
[30] Arpon Raksit, Hochschild homology and the derived de Rham complex revisited, arXiv preprint arXiv:2007.02576 (2020).
[31] Charles A. Weibel, An introduction to homological algebra, Cambridge Studies in Advanced Mathematics, vol. 38, Cambridge University Press, Cambridge, 1994. MR 1269324

Department of Mathematics, Northwestern University
Max-Planck-Institut für Mathematik Bonn
antieau@northwestern.edu