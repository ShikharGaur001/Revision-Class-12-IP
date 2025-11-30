import matplotlib.pyplot as plt

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

# color use karne ke do tareeke...
# pehla full name
# doosra first letter aur special letter
# dotted --> :, dashed --> --, dashdot --> -., solid --> -..... linestyle or ls
plt.plot(a, b, "mo", ls="--", linewidth=6, markersize=7, markeredgecolor="b")
plt.show()