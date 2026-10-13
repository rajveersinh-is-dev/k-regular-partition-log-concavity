"""
k-regular partition log-concavity research package.
"""

from .partition import (
    compute_partitions_euler,
    compute_sigma,
    compute_gk,
    compute_pk_recurrence,
    compute_pk_pentagonal_inversion,
)
from .discriminant import (
    compute_Delta,
    compute_Dk,
    boundary_penalty_Theta,
    cross_coupling_Gamma,
    verify_transition_decomposition,
)
from .phase_transition import (
    find_exceptions,
    compute_threshold_Nk,
    analyze_boundary_transition,
    verify_heim_neuhauser_conjecture,
)
