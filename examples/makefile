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
    CommandLine       \
    FileInputOutput   \
    FormattedOutput

%.pyx: %.py
	./$<

%.pyy: %.py
	coverage run --branch ./$<
	coverage report -m

CommandLine.pyx: CommandLine.py
	CommandLine.py Nothing to be done.

CommandLine.pyy: CommandLine.py
	coverage run --branch CommandLine.py Nothing to be done.
	coverage report -m

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

testx: $(FILES:=.pyx)

testy: $(FILES:=.pyy)
