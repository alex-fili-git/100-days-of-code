# scope
global scope is available in the whole document, also for functions
local scope is within functions and is not available outside
if statement indent does not exclude, but a function does. So indents are not leading

## How to modify a global variable:
enemies = "skeleton"
def increase_enemy():
    enemies = "zombie"
    print(enemies) ##prints zombie of local scope

increase_enemy()
print(enemies) ##prints skeleton of global scope

## Now if we insert 'global' we fix it:
enemies = "skeleton"
def increase_enemy():
    global enemies = "zombie"
    print(enemies) ##prints skeleton

increase_enemy()
print(enemies) ##prints skeleton

but don't do it if you want to alter a global value 
## do it outside the function:
enemies = 1
def increase_enemies():
    return enemies + 1
enemies = increase_enemies()

## local only available locally not outside
enemies1 = 1
def increase_enemies():
    enemies2 = 2
print(enemies2) --> gives NameError

# global constants
Use uppercase to remind yourself to not change the variable
PI = 3.14159