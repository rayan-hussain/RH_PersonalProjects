# Author - Rayan Hussain

import numpy as np
from scipy.stats import norm

# Assign values to necessary variables
r = eval(input("Enter the risk-free interest rate (r): "))
S = eval(input("Enter the current stock price (S): "))
K = eval(input("Enter the strike price of the option (K): "))
t = eval(input("Enter the time to expiration in years (t): "))
sigma = eval(input("Enter the volatility of the stock (sigma): "))
# Allow for evalution for call or put options
option_type = input("Enter the option type ('Call' or 'Put'): ")

# Implement Black Scholes formula as a function
def blackScholes(r, S, K, t, sigma, option_type):
    d1 = (np.log(S/K) + (r + sigma**2/2)*t)/(sigma*np.sqrt(t))
    d2 = d1 - (sigma*np.sqrt(t))

    try:
        if option_type == "Call":
            price = (norm.cdf(d1, 0, 1)*S) - (norm.cdf(d2, 0, 1)*K*np.exp(-r*t))
        elif option_type == "Put":
            price = (norm.cdf(-d2, 0 ,1)*K*np.exp(-r*t)) - (norm.cdf(-d1, 0, 1)*S)
        return price
    except:
        print("Please check all option parameters above...")


# Implement Delta Option Greek formula as a function
def delta(r, S, K, T, sigma, option_type):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    try:
        if option_type == "Call":
            delta = norm.cdf(d1, 0, 1)
        elif option_type == "Put":
            delta = -norm.cdf(-d1, 0, 1)
        return delta
    except:
        print("Please check all option parameters above...")

# Implement Gamma Option Greek formula as a function
def gamma(r, S, K, T, sigma):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        gamma = norm.pdf(d1, 0, 1)/(S*sigma*np.sqrt(T))
        return gamma
    except:
        print("Please check all option parameters above...")

# Implement Vega Option Greek formula as a function
def vega(r, S, K, T, sigma):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        vega = S*norm.pdf(d1, 0, 1)*np.sqrt(T)
        return vega*0.01
    except:
        print("Please check all option parameters above...")

# Implement Theta Option Greek formula as a function
def theta(r, S, K, T, sigma, option_type):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if option_type == "Call":
            theta = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif option_type == "Put":
            theta = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return theta/365
    except:
        print("Please check all option parameters above...")

# Implement Rho Option Greek formula as a function
def rho(r, S, K, T, sigma, option_type):

    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if option_type == "Call":
            rho = K*T*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif option_type == "Put":
            rho = -K*T*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return rho*0.01
    except:
        print("Please check all option parameters above...")

# Printing results
print("Option Price is:", round(blackScholes(r, S, K, t, sigma, option_type), 4))
print("Delta:", round(delta(r, S, K, t, sigma, option_type), 4))
print("Gamma", round(gamma(r, S, K, t, sigma), 4))
print("Vega", round(vega(r, S, K, t, sigma), 4))
print("Theta", round(theta(r, S, K, t, sigma, option_type), 4))
print("Rho", round(rho(r, S, K, t, sigma, option_type), 4))