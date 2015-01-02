# -------------------------------------------
# Cake eating: constrained optimization
# -------------------------------------------
print("-------------- START ----------------")
rm(list=ls()) # Remove almost everything in the memory


# -----------------------------------------------------------------------------------
# 1. Analytical solution
# -----------------------------------------------------------------------------------
T = 9
beta = 0.9
kv = seq(T+1)
cv = seq(T+1)
uv = seq(T+1)
kv[1] = 100                            # k0
cv[1] = (1-beta)/(1-beta^(T+1))*kv[1]  # c0
uv[1] = log(cv[1])

for (i in 2:(T+1)) {
    cv[i] = beta * cv[i-1]
    kv[i] = kv[i-1] - cv[i-1]
    uv[i] = beta^(i-1)*log(cv[i])  # period utility with discounting
}

log(cv[1])
sum(uv)  # total utility

cv
kv

# par(mfrow = c(2, 1))
# plot(cv)
# title("Consumption")
# 
# plot(kv)
# title("Cake size")

# -----------------------------------------------------------------------------------
# 2. Numerical solution
# -----------------------------------------------------------------------------------
library("Rsolnp")

func1 = function(cv) {
    T = length(cv)
    uv = seq(T)
    for (i in 1:T) {
        beta = 0.9
        uv[i] = beta^(i-1)*log(cv[i])  # period utility with discounting
    }
    return(-sum(uv))
}

# The constraint
eqn1=function(cv){
    k0 = 100
    z1=sum(cv) - k0
    return(c(z1))
}

# Call the optimizer with some starting values for the consumption vector
T = 10
x0 =array(1,c(1,T))*0.1
cake = solnp(x0, fun = func1, eqfun = eqn1, eqB = c(0))


# Plot analytical and numerical solution
par(mfrow = c(1, 1))
plot(cv, type="o", pch=1, lty=2, col="blue")
    # Numerical soln
    lines(cake$pars, type="o", pch=2, lty=2, col="red")
    legend(1,9, c("analytic","numeric"),pch = c(1,2),lty=c(1,2)) 

cat('Analytic solution cv =', cv)
cat('Numeric soluntion cv =', cake$pars)
