FILES :=           \
    IsPrime1T      \
    IsPrime2T      \
    FactorialT     \
    ReduceT        \
    MapT           \
    RMSET          \
    SubtractT      \
    StDevT         \
    RangeIteratorT \
    RangeT

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
