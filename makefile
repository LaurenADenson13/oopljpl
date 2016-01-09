clean:
	cd examples; make clean
	@echo
	cd exercises; make clean

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/oopljpl.git
	git push -u origin master

pull:
	@rsync -r -t -u -v --delete             \
    --include "Hello.py"                    \
    --include "Assertions.py"               \
    --include "UnitTests1.py"               \
    --include "UnitTests2.py"               \
    --include "UnitTests3.py"               \
    --include "Coverage1.py"                \
    --include "Coverage2.py"                \
    --include "Coverage3.py"                \
    --include "Exceptions.py"               \
    --include "Types.py"                    \
    --include "Operators.py"                \
    --include "Variables.py"                \
    --include "Iteration.py"                \
    --exclude "*"                           \
    ../../../examples/python/ examples/
	@rsync -r -t -u -v --delete             \
    --include "IsPrime1.py"                 \
    --include "IsPrime1T.py"                \
    --include "IsPrime2T.py"                \
    --include "FactorialT.py"               \
    --include "ReduceT.py"                  \
    --exclude "*"                           \
    ../../../exercises/python/ exercises/

#   --include "IsPrime2.py"                 \
#   --include "Factorial.py"                \
#   --include "Reduce.py"                   \

#   --include "Cache.py"                    \
#   --include "Arguments.py"                \
#   --include "Iteration.py"                \
#   --include "Iterables.py"                \
#   --include "Assignment.py"               \
#   --include "FunctionParallel.py"         \
#   --include "FunctionKeywords.py"         \
#   --include "FunctionDefaults.py"         \
#   --include "FunctionUnpacking.py"        \
#   --include "FunctionTuple.py"            \
#   --include "FunctionDict.py"             \
#   --include "CommandLine.py"              \
#   --include "FileInputOutput.py"          \
#   --include "Generators.py"               \
#   --include "GlobalVariables.py"          \
#   --include "ClassVariables.py"           \
#   --include "InstanceVariables.py"        \
#   --include "Methods.py"                  \
#   --include "Closures.py"                 \
#   --include "Sequences.py"                \
#   --include "Strings.py"                  \
#   --include "RegExps.py"                  \
#   --include "Lists.py"                    \
#   --include "Sets.py"                     \
#   --include "Dicts.py"                    \
#   --include "FormattedOutput.py"          \
#   --include "Inheritance.py"              \
#   --include "Functions.py"                \
#   --include "Decorators.py"               \
#   --include "Decorators2.py"              \

#   --include "IsSorted.py"                 \
#   --include "IsSorted2.py"                \
#   --include "StDev.py"                    \
#   --include "StDev2.py"                   \
#   --include "Reduce3.py"                  \
#   --include "Reduce4.py"                  \
#   --include "Complex.py"                  \
#   --include "Complex2.py"                 \
#   --include "Count.py"                    \
#   --include "Count2.py"                   \
#   --include "Range.py"                    \
#   --include "Range2.py"                   \
#   --include "Count3.py"                   \
#   --include "Count4.py"                   \
#   --include "Range3.py"                   \
#   --include "Range4.py"                   \
#   --include "Map.py"                      \
#   --include "Map2.py"                     \
#   --include "FortyTwo.py"                 \
#   --include "Map3.py"                     \
#   --include "Map4.py"                     \
#   --include "Collatz.in"                  \
#   --include "TestCollatz.py"              \
#   --include "Collatz.py"                  \
#   --include "Collatz2.py"                 \
#   --include "Collatz3.py"                 \
#   --include "Collatz4.py"                 \

push:
	make clean
	@echo
	git add .travis.yml
	git add examples
	git add exercises
	git add makefile
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

testx:
	cd examples; make testx
	@echo
	cd exercises; make testx

testy:
	cd examples; make testy
	@echo
	cd exercises; make testy
