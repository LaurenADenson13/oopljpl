FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3         \
    Exceptions        \
    Operators         \
    Iteration         \
    Yield             \
    Lambda            \
    Comprehensions    \
    Iterables         \
    FileInputOutput   \
    FormattedOutput   \
    GlobalVariables   \
    ClassVariables    \
    InstanceVariables \
    Closures          \
    Methods

%.pyx: %.py
	./$<

%.pyy: %.py
	coverage run --branch ./$<
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

testx: $(FILES:=.pyx)

testy: $(FILES:=.pyy)
