#include <errno.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if defined(__unix__) || (defined(__APPLE__) && defined(__MACH__))
#define IS_POSIX
#endif

#if defined(IS_POSIX)
#include <sys/stat.h>
#endif

#define DEBUG_ASSERT 1

#ifndef STDLIB_DIR
#define STDLIB_DIR "~/.kantan/std"
#endif

// forward decls
char const *get_stdlib_directory(void);
void assert_fmt(bool condition, char const *fmt, ...);
char const *l_format_str(size_t *len, char const *fmt, ...);
char const *format_str(char const *fmt, ...);
int vformat_str(char **dest, char const *fmt, va_list args);
bool is_file(char const *path);
size_t ptr_to_int(void *ptr);
void *int_to_ptr(size_t i);
void get_sys(bool *is_linux, bool *is_darwin, bool *is_win32);
int32_t get_errno(void);

char const *get_stdlib_directory() {
    return STDLIB_DIR;
}

void assert_fmt(bool condition, char const *fmt, ...) {
#if DEBUG_ASSERT
    if (condition) {
        return;
    }

    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    int size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return;
    }

    printf("%s\n", s);
    free(s);

    abort();
#endif
}

char const *l_format_str(size_t *len, char const *fmt, ...) {
    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    int size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return NULL;
    }

    *len = (size_t)size;
    return s;
}

char const *format_str(char const *fmt, ...) {
    char *s = NULL;
    va_list args;
    va_start(args, fmt);
    int size = vformat_str(&s, fmt, args);
    va_end(args);

    if (size < 0) {
        return NULL;
    }

    return s;
}

int vformat_str(char **dest, char const *fmt, va_list args) {
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

    char *str = malloc((size_t)size + 1);
    if (str == NULL) {
        return 0;
    }
    size = vsprintf(str, fmt, args);
    *dest = str;

    return size;
}

bool is_file(char const *path) {
#if defined(IS_POSIX)
    struct stat s;
    if (stat(path, &s) == 0) {
        return S_ISREG(s.st_mode);
    }
#endif
    return false;
}

size_t ptr_to_int(void *ptr) {
    return (size_t)ptr;
}

void *int_to_ptr(size_t i) {
    size_t s = i;
    return (void *)s;
}

void get_sys(bool *is_linux, bool *is_darwin, bool *is_win32) {
    // don't report unused params for the other platforms
    (void)is_linux;
    (void)is_darwin;
    (void)is_win32;
#if defined(linux) || defined(__linux__)
    if (is_linux)
        *is_linux = true;
#elif defined(darwin) || defined(__APPLE__)
    if (is_darwin)
        *is_darwin = true;
#elif defined(WIN32) || defined(_WIN32)
    if (is_win32)
        *is_win32 = true;
#endif
}

int32_t get_errno() {
    return errno;
}
