CXX := gcc

NUM_CORES = $(shell nproc)
CXXFLAGS := -Wall -Wextra -Iinclude -J$(NUM_CORES)

SRC = src

SRCS := $(wildcard $(SRC)/*.c)

OUT = build/sysmess

all:
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(OUT)

clean:
	rm -f $(OUT)

run:
	./$(OUT)
