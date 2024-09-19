import sys
print(4, sys.modules.keys(), "\n")
import decorators
models = "models"
print(5, sys.modules.keys(), "\n")
print(decorators.app)
print(6, sys.modules.keys(), "\n")
