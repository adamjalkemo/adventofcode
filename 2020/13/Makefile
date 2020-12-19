CXXFLAGS = -std=c++17 -Wfatal-errors -fconcepts -Wextra -Wall --pedantic

all: solution

solution: solution.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

.PHONY: clean
clean:
	rm solution
