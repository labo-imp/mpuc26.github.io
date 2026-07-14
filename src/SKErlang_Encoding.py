import sys
import random

# Single Key Erlang Encoding
SKEE_rng = random.Random()   # local random numbers
SKEE_rng.seed(732378426541)  # magic sauce

# This function calculates the Single Key Erlang Encoding
#  given the same input, each call gives a different output
#  x nominal primal dimension must be under 13
def SKErlangEncoding(x):

  SKE = SKEE_rng.randint(0, sys.maxsize )

  # ejecucion
  return  (( x + (x%13)) ^ SKE)

