K_FILES = src/ast/generics.kan \
		  src/ast/expr.kan \
		  src/ast/item.kan \
		  src/ast/lexer.kan \
		  src/ast/mod.kan \
		  src/ast/parser.kan \
		  src/ast/signature.kan \
		  src/ast/stmt.kan \
		  src/ast/token.kan \
		  src/ast/tyid.kan \
		  src/cdeps.kan \
		  src/cli/config.kan \
		  src/cli/opt.kan \
		  src/cli/report.kan \
		  src/codegen/target.kan \
		  src/compiler.kan \
		  src/error.kan \
		  src/main.kan \
		  src/memory/arena.kan \
		  src/source/file.kan \
		  src/source/ident.kan \
		  src/source/modmap.kan \
		  src/source/position.kan \
		  src/source/span.kan \
		  src/std/alloc.kan \
		  src/std/dbg.kan \
		  src/std/files/path.kan \
		  src/std/files/unix.kan \
		  src/std/io.kan \
		  src/std/libc.kan \
		  src/std/map.kan \
		  src/std/num.kan \
		  src/std/ptrvec.kan \
		  src/std/str.kan \
		  src/std/vec.kan \
		  src/std/vmap.kan \
		  src/types/check/binary.kan \
		  src/types/check/call.kan \
		  src/types/check/expr.kan \
		  src/types/check/item.kan \
		  src/types/check/literal.kan \
		  src/types/check/stmt.kan \
		  src/types/check/unary.kan \
		  src/types/ctx.kan \
		  src/types/data.kan \
		  src/types/function.kan \
		  src/types/graph.kan \
		  src/types/info.kan \
		  src/types/instances.kan \
		  src/types/primitive.kan \
		  src/types/resolve/functions.kan \
		  src/types/scope.kan \
		  src/types/template.kan \
		  src/types/types.kan \
		  src/types/util.kan \
		  src/util.kan

START_FOLDER := $(shell pwd)

BIN_NAME ?= kantan

STDLIB_DIR ?= $(START_FOLDER)/src/std
KANTAN_STABLE ?= $(START_FOLDER)/../kantan -g
CC ?= gcc

C_DEFINES := -DSTDLIB_DIR=\"$(STDLIB_DIR)\"
C_FILES := lib.c
C_FLAGS := -O3 -Wall -Wextra -pedantic -std=c99 -Werror

$(BIN_NAME) : Makefile $(K_FILES) $(C_FILES)
	$(KANTAN_STABLE) $(K_FILES) -o $(BIN_NAME).o
	$(CC) $(C_FLAGS) $(C_FILES) $(BIN_NAME).o -o $(BIN_NAME)
	rm $(BIN_NAME).o

# This makes it possible to do stuff like `make test -- --show-skipped`
# see https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
# If the first argument is "test"...
ifeq (test,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "test"
  TEST_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TEST_ARGS):;@:)
endif

type-graph.png : $(BIN_NAME) test.kan
	( \
		. tools/venv/bin/activate ;\
		./$(BIN_NAME) test.kan --mi --dump-type-graph | tools/graphformat.py | dot -Tpng > type-graph.png \
	)

.PHONY: test
test : $(BIN_NAME)
	cd test && \
	python3 -m runner.main ../$(BIN_NAME) runner/cases $(TEST_ARGS)

.PHONY: clean
clean :
	rm $(BIN_NAME)
