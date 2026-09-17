"""Generate the header mark: two Lorenz-63 trajectories, one nudged onto the other."""
import numpy as np
from scipy.integrate import solve_ivp

sigma, rho, beta, mu = 10.0, 28.0, 8.0/3.0, 26.0

def rhs(t, s):
    x, y, z, xt, yt, zt = s
    return [
        sigma*(y - x), x*(rho - z) - y, x*y - beta*z,
        sigma*(yt - xt) - mu*(xt - x), xt*(rho - zt) - yt, xt*yt - beta*zt,
    ]

# settle the true trajectory onto the attractor first
warm = solve_ivp(lambda t, s: rhs(t, np.r_[s, s])[:3], [0, 40], [1.0, 1.0, 1.0],
                 rtol=1e-10, atol=1e-12, dense_output=True)
u0 = warm.y[:, -1]

T = 3.4
t = np.linspace(0, T, 420)
sol = solve_ivp(rhs, [0, T], np.r_[u0, [-9.0, 6.0, 30.0]], t_eval=t, rtol=1e-11, atol=1e-13)

y_true, y_nudged = sol.y[1], sol.y[4]

# map to an SVG band
W, H, PAD = 1000.0, 74.0, 7.0
lo = min(y_true.min(), y_nudged.min())
hi = max(y_true.max(), y_nudged.max())
def path(vals):
    xs = W * t / T
    ys = PAD + (H - 2*PAD) * (1 - (vals - lo) / (hi - lo))
    return "M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in zip(xs, ys))

with open("header_trace_paths.txt", "w") as f:
    f.write("TRUE\n" + path(y_true) + "\n\nNUDGED\n" + path(y_nudged) + "\n")

err = np.abs(y_true - y_nudged)
print("initial gap %.2f, final gap %.2e" % (err[0], err[-1]))
print("path chars:", len(path(y_true)))
