'''
Created on 10/10/18
@author:   Luke McEvoy
Pledge:    I pledge my honor I have abided by the Stevens Honor System

CS115 - Hw 5
'''
import turtle

def sv_tree(trunk_length, levels):
  #takes a length and level and prints a recursive tree graphic with turtle
  if levels >= 0:
    turtle.forward(trunk_length)
    turtle.left(30)
    #first segment of recursion begins
    sv_tree(trunk_length/2, levels-1)
    turtle.right(60)
    #second part of recursion begins
    sv_tree(trunk_length/2, levels-1)
    turtle.left(30)
    turtle.forward(-trunk_length)
  else:
    #ends recursion once the level reaches 0 or less
    return        
    #function structured in way where a 'Y' is made on 'Y' until level >= 0
def fast_lucas(n):
    #finds a the nth spot of lucas sequence in memo form
    def fast_lucas_helper(n,memo):
      if n in memo:
      #if this has already been computed, return that value
        return memo[n]
      if n <= 0:
      #base case
        answer = 2
      elif n == 1:
      #base case
        answer = 1
      else:
      #operation function with recursion to add up all preexisiting variables
        answer = fast_lucas_helper(n-1,memo) + fast_lucas_helper(n-2,memo)
      #add operation output to memo
      memo[n] = answer
      return answer
    #recursively call helper with the n and the {} so that the dictionary is not restarted
    return fast_lucas_helper(n,{})
    #the {} is built on every time the function is called
  

def fast_change(amount, coins):
    #finds the least quantity of coin needed to give change for a given amount & list of coin values
    def fast_change_helper(amount, coins, memo):
      if (amount, coins) in memo:
        #return if already computed
        return memo[(amount, coins)]
      elif amount == 0:
      #base case
        answer = 0
      elif len(coins) == 0 or amount < 0:
      #base case w/ adjustment for fact no outcomes are possible with input
        answer = float('inf')
      else:
      #operations
        lose = fast_change_helper(amount, coins[1:], memo)
        #scarp the given option, move down coins and recurse
        use = 1 + fast_change_helper(amount - coins[0], coins, memo)
        #use the given option, subtract change and recurse
        answer = min(lose, use)
        #find min of use or lose recurse
      memo[(amount, coins)] = answer
      return answer
    return fast_change_helper(amount, tuple(coins), {})
    #recursively call with {} so memo is not reset every cycle

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)

