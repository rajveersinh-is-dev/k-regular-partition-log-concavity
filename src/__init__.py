"""k‑regular partition log‑concavity research package.

This package provides a collection of mathematical utilities used in the
analysis of the Heim‑Neuhauser conjecture concerning the log‑concavity
threshold of *k*‑regular partitions.  The public interface re‑exports the most
relevant functions from the sub‑modules so that they can be imported directly
from :pymod:`k_regular_partition_log_concavity`.

The module defines ``__all__`` to make the exported symbols explicit and adds a
``__version__`` attribute that is populated from package metadata when
available.  No runtime side‑effects are introduced – the imports are performed
eagerly because they are lightweight and required for the public API.
"""

from __future__ import annotations

from importlib import metadata
from typing import List

# Re‑export core computational functions from the sub‑modules.
# The imports are kept explicit to aid static analysis tools and to make the
# public API clear.
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

# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------
__all__: List[str] = [
    # partition module
    "compute_partitions_euler",
    "compute_sigma",
    "compute_gk",
    "compute_pk_recurrence",
    "compute_pk_pentagonal_inversion",
    # discriminant module
    "compute_Delta",
    "compute_Dk",
    "boundary_penalty_Theta",
    "cross_coupling_Gamma",
    "verify_transition_decomposition",
    # phase_transition module
    "find_exceptions",
    "compute_threshold_Nk",
    "analyze_boundary_transition",
    "verify_heim_neuhauser_conjecture",
]

# ---------------------------------------------------------------------------
# Version information
# ---------------------------------------------------------------------------
try:
    # ``metadata.version`` raises ``PackageNotFoundError`` when the package is
    # executed from a source checkout without being installed.  In that case we
    # fall back to ``"0.0.0"`` which is sufficient for internal use and testing.
    __version__: str = metadata.version(__name__)  # type: ignore[arg-type]
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
