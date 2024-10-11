## Thermodynamic Potentials
Up until this point, we have been working a lot with the internal energy if a system, $U$, which is a function of state.

In principle, we can combine $U$ with any other functions of state ($P$, $V$, $S$, $T$) to create new functions of state. This are called **thermodynamic potentials**. Many of these combinations are not particularly useful, but there are 3 that are, and in this next section, we are going to look at these 3.

## Internal Energy
In lecture 6, we used internal energy and the F.T.R. to come up with some useful identities for temperature and pressure. To recap
$$
    {\rm d} U = T{\rm d} S - P {\rm d} V
$$
Now, using one of the tricks we used earlier, given that U is now only a function of S and V, we can write U as
$$
    {\rm d} U = \left( \frac{\partial U}{\partial S}\right)_V {\rm d} S + \left( \frac{\partial U}{\partial V}\right)_S {\rm d} V
$$
let's us identify pressure and temperature as
$$
\begin{align}
    T &= \left( \frac{\partial U}{\partial S}\right)_V\\
    P &= -\left( \frac{\partial U}{\partial V}\right)_S\\
\end{align}
$$
 Now we will define an isochoric process as one during which the volume stays constant (${\rm d} V = 0$). In this case, we have
$$
    {\rm d}U = T{\rm d}S
$$
If we have a reversible isochoric process, then we also have that
$$
    {\rm d}U = {\rm d}Q = C_V {\rm d} T
$$
Thus, the change in internal energy during a reversible, isochoric process is trivial to work out, and is
$$
\Delta U = \int_{T_1}^{T_2} C_{\rm V}\:{\rm d} T
$$
What we want to do now is determine similar useful expressions, but for processes that are not isochoric.

## Enthalpy
Imagine we are studying a small thermodynamic system inside a large room. Keeping track of the total internal energy of the system as it does work (or has work done on it) can be a bit of a pain. Instead, we can always add the work that is needed to make space for the system. This gives us enthalpy:
$$
    H = U+PV.
$$
Thus, an infinitesimal change in $H$ is given by
$$
\begin{align}
    {\rm d} H &= T{\rm d} S - P {\rm d} V + P {\rm d} V + V {\rm d} P\\
    {\rm d} H &= T{\rm d} S + V {\rm d} P
\end{align}
$$
From this, we can say that $H=H(S,P)$. For an isobaric process (${\rm d}P=0$), we then have
$$
    {\rm d} H = T{\rm d} S
$$
and for a reversible, isobaris process we have
$$
    {\rm d}H = {\rm d}Q = C_P {\rm d} T
$$
Thus
$$
    \Delta H = \int_{T_1} ^{T_2} C_P {\rm d} T
$$
Thus, for a process performed at contant pressure, then the enthalpy represents the heat (which is why it's called H) transferred to or from the system.
Our definition of the enthalpy also gives us that
$$
   T = \left(\frac{\partial H}{\partial S}\right)_P ; V = \left(\frac{\partial H}{\partial P}\right)_S
$$
## Helmholtz Free Energy (or Helmholtz Function)
The above potentials are both functions of entropy, $S$, which can difficult to vary experimentally. This next thermodynamic potential does not suffer the same drawback. Let's define the Helmholtz Free Energy as
$$
    F = U - TS.
$$
This gives
$$
\begin{align}
    {\rm d} F &= T {\rm d} S - P {\rm d} V - T {\rm d} S - S {\rm d} T\\
              &= - S {\rm d} T - P {\rm d} V
\end{align}
$$
From this, we can say that $F=F(T,V)$. For an isothermal process, we thus have
$$
    {\rm d} F = - P {\rm d} V
$$
giving
$$
    \Delta F = - \int_{V_1}^{V_2} P {\rm d} V
$$
Our definition of the Helmholtz Free Energy also gives us that
$$
   S = -\left(\frac{\partial F}{\partial T}\right)_V ; P = -\left(\frac{\partial F}{\partial V}\right)_T
$$
## Gibbs Free Energy (or Gibbs Function)
Let
$$
    G = H - TS
$$
This gives
$$
\begin{align}
    {\rm d} G &= T {\rm d} S + V {\rm d} P - T {\rm d} S - S {\rm d} T\\
              &= - S {\rm d} T + V {\rm d} P
\end{align}
$$
Thus $G=G(T,P)$, which is particularly useful as both $T$ and $P$ are easy to control and change in experiments. Thus, if you have an isothermal isobaric process, then ${\rm d} G = 0$. This will be useful when we are studying phase transitions later.
Our definition of the Gibbs Free Energy also gives us that
$$
   S = -\left(\frac{\partial G}{\partial T}\right)_P ; V = \left(\frac{\partial G}{\partial P}\right)_T
$$
## Availability
So what use are these new thermodynamic potentials? As a starting point, consider the setup below where we have a system inside some surroundings. The system will be allowed to exchange heat and to do work on the surroundings.

![Entropy_of_mixing](Figures/Surroundings.svg)

So what happens when energy ${\rm d} U$ and volume ${\rm d} V$ are transferred from the surroundings to the system? First, the internal energy of the surroundings will change according to the 1st law by
$$
    {\rm d} U_0 = - {\rm d} U = T_0 {\rm d} S_0 - P_0 (- {\rm d} V)
$$
The $-$ in ${\rm d} U$ and in ${\rm d} V$ are because these quantites are being transferred **to** the system, and as such are negative for the surroundings. Rearranging we have
$$
    {\rm d} S_0 = - \left(\frac{{\rm d} U + P_0  {\rm d} V}{T_0}\right)
$$
If the entropy of the system changes by ${\rm d} S$ during this process, then the total change in entropy is
$$
    {\rm d} S_{\rm Total} = {\rm d} S_0 + {\rm d} S.
$$
The second law tells us that ${\rm d} S_{\rm Total} \geq 0$. Combining this with the above equation then gives
$$
    T_0 {\rm d} S_{\rm Total} = -({\rm d} U + P_0 {\rm d} V - T_0 {\rm d} S) \geq 0
$$
giving
$$
    {\rm d} U + P_0 {\rm d} V - T_0 {\rm d} S \leq 0.
$$
We will now define a new variable called **availability** and let it be
$$
    A  = U + P_0 V - T_0 S
$$
such that (given that $P_0$ and $T_0$ are constants)
$$
    {\rm d} A  = {\rm d} U + P_0 {\rm d}V - T_0 {\rm d}S.
$$
This means that
$$
    {\rm d} A \leq 0
$$
What does this actually mean? It tells us that any changes in a system as it settles down to equilibrium will decrease $A$. When at equilibrium, $A$ remains constant. As such, in order to figure out what the equilibrium conditions for a system are, all we have to do is minimise $A$. However, the type of equilibrium we are trying to achieve will affect how $A$ is minimised. What exactly does this mean? We'll cover that in our next lecture.