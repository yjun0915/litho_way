

"""
Get Information : Map
Set Parameters : N_SA, N_GA, N_FA, N_SGA, N_SFA, N_P, N_R
Set Parameters : α, β, γ, ρ, k_mix, d_0, w_L, w_A, w_P
Initialize : τ, η, I_A, L_R

n_I = 0                                                     > n_I : Iteration Number
while Termination condition dosen`t meet:
    n_I = n_I + 1
    n_R = 0                                                 > n_R : Rank List Number
    for k in range(N_A):                                    > N_A : # of Total Ants
        //Ant k`s travel start.
        j = RouletteSelect((p^k)_j)
        I_(A, K) = j
        PathPurning(j)
        if j == g :                                         > g : Gola Point
            n_R = n_R + 1
            L_R(N_R + n_R) = I_(A, k)
            Initialize(I_(A, k))
    if Arrived ants exist:
        PathCrossover(L_R(1), ..., L_R(N_P), L_R(N_R+1), ..., L_R(N_R+n_R))
        //Sort and Cut L_R by N_R.
        Sort(L_R(1), ..., L_R(N_R+n_R), ..., L_R(N_R+n_R+N_P))
        L_R = Cut(L_R(1), ..., L_R(N_R))
        //Update pheromone.
        UpdatePheromone(τ)
    return L_R(1)
"""
"""
RouletteSelect((p^k)_j) = ┌([τ_j(n_I)]^α)([η_(j, g)]^β)([ξ_j]^γ)/∑(c∈C)(([τ_c(n_I)]^α)([η_(c, g)]^β)([ξ_c]^γ)) if j∈C
                          └0                                                                                   otherwise
C = {c|c=(points in sight - window around point i)}
"""
