#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <errno.h>

#include <sys/stat.h>

#define DEBUG_ASSERT 1

#ifndef STDLIB_DIR
#define STDLIB_DIR "~/.kantan/std"
#endif

char const *const get_stdlib_directory() {
    return STDLIB_DIR;
}

// forward decls
ssize_t vformat_str(char **dest, char const *fmt, va_list args);

void assert_fmt(bool condition, char const *fmt, ...) {
#if DEBUG_ASSERT
    if (condition) {
        return;
    }

    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    ssize_t size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return;
    }

    printf("%s\n", s);
    free(s);

    abort();
#endif
}

char const *const l_format_str(size_t *len, char const *fmt, ...) {
    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    ssize_t size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return NULL;
    }

    *len = size;
    return s;
}

char const *const format_str(char const *fmt, ...) {
    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    ssize_t size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return NULL;
    }

    return s;
}

bool is_file(char const *path) {
    struct stat s;
    if (stat(path, &s) == 0) {
        return s.st_mode & S_IFREG;
    }
    return false;
}

// these have to match src/std/files/path.Error
#define ERROR_COULD_NOT_OPEN_FILE       2
#define ERROR_COULD_NOT_ALLOCATE_BUFFER 3
#define ERROR_COULD_NOT_READ_FILE       4

int32_t read_file(char const *path, char const **content, size_t *len) {
    if (!is_file(path)) {
        // TODO: custom error, and check if this works on windows
        return ERROR_COULD_NOT_OPEN_FILE;
    }

    FILE *file = fopen(path, "r");
    if (file == NULL) {
        return ERROR_COULD_NOT_OPEN_FILE;
    }

    fseek(file, 0L, SEEK_END);
    size_t file_size = (size_t) ftell(file);
    rewind(file);

    char *buffer = malloc(file_size + 1);

    if (buffer == NULL) {
        fclose(file);
        return ERROR_COULD_NOT_ALLOCATE_BUFFER;
    }

    size_t bytes_read = fread(buffer, sizeof(char), file_size, file);

    if (bytes_read < file_size) {
        fclose(file);
        free(buffer);
        return ERROR_COULD_NOT_READ_FILE;
    }

    buffer[bytes_read] = '\0';

    fclose(file);
    *content = buffer;
    *len = file_size;

    return 0;
}

ssize_t vformat_str(char **dest, char const *fmt, va_list args){
    int size = 0;
    va_list tmp_args;

    // vsnprintf modifies the arg list, so we have to copy it here
    va_copy(tmp_args, args);

    // pass NULL as str, so that we just get the size
    size = vsnprintf(NULL, 0, fmt, tmp_args);

    va_end(tmp_args);

    if (size < 0) {
        return size;
    }

    char *str = malloc(size + 1);
    if (str == NULL) {
        return -1;
    }
    size = vsprintf(str, fmt, args);
    *dest = str;

    return size;
}

size_t int_num_digits(size_t i) {
    // pass NULL as str, so that we just get the size
    return snprintf(NULL, 0, "%lu", i);
}

size_t ptr_to_int(void* ptr) {
    return (size_t) ptr;
}

void *int_to_ptr(size_t i) {
    size_t s = i;
    return (void *)s;
}

void get_sys(bool *is_linux, bool *is_darwin, bool *is_win32) {
#if defined(linux) || defined(__linux__)
    if (is_linux) *is_linux = true;
#elif defined(darwin) || defined(__APPLE__)
    if (is_darwin) *is_darwin = true;
#elif defined(WIN32) || defined(_WIN32)
    if (is_win32) *is_win32 = true;
#endif
}

int32_t get_errno() {
    return errno;
}
