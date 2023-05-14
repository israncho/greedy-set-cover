# Greedy Set Cover

Implementation of the approximation algorithm for the NP-complete problem SET COVER.

## Set Cover (Optimizacion)

**INSTANCE:** A set $U$, a collection of subsets $C={S_0,S_1,...,S_m}$ such that
$$\bigcup^m_{i = 1} S_i = U$$

**PROBLEM:** Find $C'\subseteq C$ such that each element in $U$ belongs to at least one member of $C'$
and $|C'|$ is minimized. 

## Execution 

The argument for the command is the instance with which the algorithm will be executed.

```bash
python3 src/greedy_set_cover_lists.py 0
```


### Jesus Israel Gutierrez Elizalde