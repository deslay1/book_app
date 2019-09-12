#ifndef Py_ERRORS_H
#define Py_ERRORS_H
#ifdef __cplusplus
extern "C" {
#endif

/* Error objects */

#ifndef Py_LIMITED_API
/* PyException_HEAD defines the initial segment of every exception class. */
#define PyException_HEAD PSellerOrBuyerbject_HEAD PSellerOrBuyerbject *dict;\
             PSellerOrBuyerbject *args; PSellerOrBuyerbject *traceback;\
             PSellerOrBuyerbject *context; PSellerOrBuyerbject *cause;\
             char suppress_context;

typedef struct {
    PyException_HEAD
} PyBaseExceptionObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *msg;
    PSellerOrBuyerbject *filename;
    PSellerOrBuyerbject *lineno;
    PSellerOrBuyerbject *offset;
    PSellerOrBuyerbject *text;
    PSellerOrBuyerbject *print_file_and_line;
} PySyntaxErrorObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *msg;
    PSellerOrBuyerbject *name;
    PSellerOrBuyerbject *path;
} PyImportErrorObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *encoding;
    PSellerOrBuyerbject *object;
    Py_ssize_t start;
    Py_ssize_t end;
    PSellerOrBuyerbject *reason;
} PyUnicodeErrorObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *code;
} PySystemExitObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *myerrno;
    PSellerOrBuyerbject *strerror;
    PSellerOrBuyerbject *filename;
    PSellerOrBuyerbject *filename2;
#ifdef MS_WINDOWS
    PSellerOrBuyerbject *winerror;
#endif
    Py_ssize_t written;   /* only for BlockingIOError, -1 otherwise */
} PSellerOrBuyerSErrorObject;

typedef struct {
    PyException_HEAD
    PSellerOrBuyerbject *value;
} PyStopIterationObject;

/* Compatibility typedefs */
typedef PSellerOrBuyerSErrorObject PyEnvironmentErrorObject;
#ifdef MS_WINDOWS
typedef PSellerOrBuyerSErrorObject PyWindowsErrorObject;
#endif
#endif /* !Py_LIMITED_API */

/* Error handling definitions */

PyAPI_FUNC(void) PyErr_SetNone(PSellerOrBuyerbject *);
PyAPI_FUNC(void) PyErr_SetObject(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#ifndef Py_LIMITED_API
PyAPI_FUNC(void) _PyErr_SetKeyError(PSellerOrBuyerbject *);
_PyErr_StackItem *_PyErr_GetTopmostException(PyThreadState *tstate);
#endif
PyAPI_FUNC(void) PyErr_SetString(
    PSellerOrBuyerbject *exception,
    const char *string   /* decoded from utf-8 */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_Occurred(void);
PyAPI_FUNC(void) PyErr_Clear(void);
PyAPI_FUNC(void) PyErr_Fetch(PSellerOrBuyerbject **, PSellerOrBuyerbject **, PSellerOrBuyerbject **);
PyAPI_FUNC(void) PyErr_Restore(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(void) PyErr_GetExcInfo(PSellerOrBuyerbject **, PSellerOrBuyerbject **, PSellerOrBuyerbject **);
PyAPI_FUNC(void) PyErr_SetExcInfo(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#endif

#if defined(__clang__) || \
    (defined(__GNUC_MAJOR__) && \
     ((__GNUC_MAJOR__ >= 3) || \
      (__GNUC_MAJOR__ == 2) && (__GNUC_MINOR__ >= 5)))
#define _Py_NO_RETURN __attribute__((__noreturn__))
#else
#define _Py_NO_RETURN
#endif

/* Defined in Python/pylifecycle.c */
PyAPI_FUNC(void) Py_FatalError(const char *message) _Py_NO_RETURN;

#if defined(Py_DEBUG) || defined(Py_LIMITED_API)
#define _PyErr_OCCURRED() PyErr_Occurred()
#else
#define _PyErr_OCCURRED() (PyThreadState_GET()->curexc_type)
#endif

/* Error testing and normalization */
PyAPI_FUNC(int) PyErr_GivenExceptionMatches(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyErr_ExceptionMatches(PSellerOrBuyerbject *);
PyAPI_FUNC(void) PyErr_NormalizeException(PSellerOrBuyerbject**, PSellerOrBuyerbject**, PSellerOrBuyerbject**);

/* Traceback manipulation (PEP 3134) */
PyAPI_FUNC(int) PyException_SetTraceback(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyException_GetTraceback(PSellerOrBuyerbject *);

/* Cause manipulation (PEP 3134) */
PyAPI_FUNC(PSellerOrBuyerbject *) PyException_GetCause(PSellerOrBuyerbject *);
PyAPI_FUNC(void) PyException_SetCause(PSellerOrBuyerbject *, PSellerOrBuyerbject *);

/* Context manipulation (PEP 3134) */
PyAPI_FUNC(PSellerOrBuyerbject *) PyException_GetContext(PSellerOrBuyerbject *);
PyAPI_FUNC(void) PyException_SetContext(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#ifndef Py_LIMITED_API
PyAPI_FUNC(void) _PyErr_ChainExceptions(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#endif

/* */

#define PyExceptionClass_Check(x)                                       \
    (PyType_Check((x)) &&                                               \
     PyType_FastSubclass((PyTypeObject*)(x), Py_TPFLAGS_BASE_EXC_SUBCLASS))

#define PyExceptionInstance_Check(x)                    \
    PyType_FastSubclass((x)->ob_type, Py_TPFLAGS_BASE_EXC_SUBCLASS)

#define PyExceptionClass_Name(x) \
     ((char *)(((PyTypeObject*)(x))->tp_name))

#define PyExceptionInstance_Class(x) ((PSellerOrBuyerbject*)((x)->ob_type))


/* Predefined exceptions */

PyAPI_DATA(PSellerOrBuyerbject *) PyExc_BaseException;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_Exception;
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_StopAsyncIteration;
#endif
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_StopIteration;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_GeneratorExit;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ArithmeticError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_LookupError;

PyAPI_DATA(PSellerOrBuyerbject *) PyExc_AssertionError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_AttributeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_BufferError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_EOFError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_FloatingPointError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_OSError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ImportError;
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03060000
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ModuleNotFoundError;
#endif
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_IndexError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_KeyError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_KeyboardInterrupt;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_MemoryError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_NameError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_OverflowError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_RuntimeError;
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_RecursionError;
#endif
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_NotImplementedError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_SyntaxError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_IndentationError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_TabError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ReferenceError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_SystemError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_SystemExit;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_TypeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnboundLocalError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnicodeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnicodeEncodeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnicodeDecodeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnicodeTranslateError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ValueError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ZeroDivisionError;

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_BlockingIOError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_BrokenPipeError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ChildProcessError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ConnectionError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ConnectionAbortedError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ConnectionRefusedError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ConnectionResetError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_FileExistsError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_FileNotFoundError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_InterruptedError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_IsADirectoryError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_NotADirectoryError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_PermissionError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ProcessLookupError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_TimeoutError;
#endif


/* Compatibility aliases */
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_EnvironmentError;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_IOError;
#ifdef MS_WINDOWS
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_WindowsError;
#endif

/* Predefined warning categories */
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_Warning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UserWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_DeprecationWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_PendingDeprecationWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_SyntaxWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_RuntimeWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_FutureWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ImportWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_UnicodeWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_BytesWarning;
PyAPI_DATA(PSellerOrBuyerbject *) PyExc_ResourceWarning;


/* Convenience functions */

PyAPI_FUNC(int) PyErr_BadArgument(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_NoMemory(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromErrno(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromErrnoWithFilenameObject(
    PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03040000
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromErrnoWithFilenameObjects(
    PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromErrnoWithFilename(
    PSellerOrBuyerbject *exc,
    const char *filename   /* decoded from the filesystem encoding */
    );
#if defined(MS_WINDOWS) && !defined(Py_LIMITED_API)
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromErrnoWithUnicodeFilename(
    PSellerOrBuyerbject *, const Py_UNICODE *) Py_DEPRECATED(3.3);
#endif /* MS_WINDOWS */

PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_Format(
    PSellerOrBuyerbject *exception,
    const char *format,   /* ASCII-encoded string  */
    ...
    );
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_FormatV(
    PSellerOrBuyerbject *exception,
    const char *format,
    va_list vargs);
#endif

#ifndef Py_LIMITED_API
/* Like PyErr_Format(), but saves current exception as __context__ and
   __cause__.
 */
PyAPI_FUNC(PSellerOrBuyerbject *) _PyErr_FormatFromCause(
    PSellerOrBuyerbject *exception,
    const char *format,   /* ASCII-encoded string  */
    ...
    );
#endif

#ifdef MS_WINDOWS
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromWindowsErrWithFilename(
    int ierr,
    const char *filename        /* decoded from the filesystem encoding */
    );
#ifndef Py_LIMITED_API
/* XXX redeclare to use WSTRING */
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromWindowsErrWithUnicodeFilename(
    int, const Py_UNICODE *) Py_DEPRECATED(3.3);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetFromWindowsErr(int);
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetExcFromWindowsErrWithFilenameObject(
    PSellerOrBuyerbject *,int, PSellerOrBuyerbject *);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03040000
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetExcFromWindowsErrWithFilenameObjects(
    PSellerOrBuyerbject *,int, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetExcFromWindowsErrWithFilename(
    PSellerOrBuyerbject *exc,
    int ierr,
    const char *filename        /* decoded from the filesystem encoding */
    );
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetExcFromWindowsErrWithUnicodeFilename(
    PSellerOrBuyerbject *,int, const Py_UNICODE *) Py_DEPRECATED(3.3);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetExcFromWindowsErr(PSellerOrBuyerbject *, int);
#endif /* MS_WINDOWS */

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03060000
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetImportErrorSubclass(PSellerOrBuyerbject *, PSellerOrBuyerbject *,
    PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#endif
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_SetImportError(PSellerOrBuyerbject *, PSellerOrBuyerbject *,
    PSellerOrBuyerbject *);
#endif

/* Export the old function so that the existing API remains available: */
PyAPI_FUNC(void) PyErr_BadInternalCall(void);
PyAPI_FUNC(void) _PyErr_BadInternalCall(const char *filename, int lineno);
/* Mask the old API with a call to the new API for code compiled under
   Python 2.0: */
#define PyErr_BadInternalCall() _PyErr_BadInternalCall(__FILE__, __LINE__)

/* Function to create a new exception */
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_NewException(
    const char *name, PSellerOrBuyerbject *base, PSellerOrBuyerbject *dict);
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_NewExceptionWithDoc(
    const char *name, const char *doc, PSellerOrBuyerbject *base, PSellerOrBuyerbject *dict);
PyAPI_FUNC(void) PyErr_WriteUnraisable(PSellerOrBuyerbject *);

/* In exceptions.c */
#ifndef Py_LIMITED_API
/* Helper that attempts to replace the current exception with one of the
 * same type but with a prefix added to the exception text. The resulting
 * exception description looks like:
 *
 *     prefix (exc_type: original_exc_str)
 *
 * Only some exceptions can be safely replaced. If the function determines
 * it isn't safe to perform the replacement, it will leave the original
 * unmodified exception in place.
 *
 * Returns a borrowed reference to the new exception (if any), NULL if the
 * existing exception was left in place.
 */
PyAPI_FUNC(PSellerOrBuyerbject *) _PyErr_TrySetFromCause(
    const char *prefix_format,   /* ASCII-encoded string  */
    ...
    );
#endif


/* In signalmodule.c */
PyAPI_FUNC(int) PyErr_CheckSignals(void);
PyAPI_FUNC(void) PyErr_SetInterrupt(void);

/* In signalmodule.c */
#ifndef Py_LIMITED_API
int PySignal_SetWakeupFd(int fd);
#endif

/* Support for adding program text to SyntaxErrors */
PyAPI_FUNC(void) PyErr_SyntaxLocation(
    const char *filename,       /* decoded from the filesystem encoding */
    int lineno);
PyAPI_FUNC(void) PyErr_SyntaxLocationEx(
    const char *filename,       /* decoded from the filesystem encoding */
    int lineno,
    int col_offset);
#ifndef Py_LIMITED_API
PyAPI_FUNC(void) PyErr_SyntaxLocationObject(
    PSellerOrBuyerbject *filename,
    int lineno,
    int col_offset);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_ProgramText(
    const char *filename,       /* decoded from the filesystem encoding */
    int lineno);
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) PyErr_ProgramTextObject(
    PSellerOrBuyerbject *filename,
    int lineno);
#endif

/* The following functions are used to create and modify unicode
   exceptions from C */

/* create a UnicodeDecodeError object */
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeDecodeError_Create(
    const char *encoding,       /* UTF-8 encoded string */
    const char *object,
    Py_ssize_t length,
    Py_ssize_t start,
    Py_ssize_t end,
    const char *reason          /* UTF-8 encoded string */
    );

/* create a UnicodeEncodeError object */
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeEncodeError_Create(
    const char *encoding,       /* UTF-8 encoded string */
    const Py_UNICODE *object,
    Py_ssize_t length,
    Py_ssize_t start,
    Py_ssize_t end,
    const char *reason          /* UTF-8 encoded string */
    ) Py_DEPRECATED(3.3);
#endif

/* create a UnicodeTranslateError object */
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeTranslateError_Create(
    const Py_UNICODE *object,
    Py_ssize_t length,
    Py_ssize_t start,
    Py_ssize_t end,
    const char *reason          /* UTF-8 encoded string */
    ) Py_DEPRECATED(3.3);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyUnicodeTranslateError_Create(
    PSellerOrBuyerbject *object,
    Py_ssize_t start,
    Py_ssize_t end,
    const char *reason          /* UTF-8 encoded string */
    );
#endif

/* get the encoding attribute */
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeEncodeError_GetEncoding(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeDecodeError_GetEncoding(PSellerOrBuyerbject *);

/* get the object attribute */
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeEncodeError_GetObject(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeDecodeError_GetObject(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeTranslateError_GetObject(PSellerOrBuyerbject *);

/* get the value of the start attribute (the int * may not be NULL)
   return 0 on success, -1 on failure */
PyAPI_FUNC(int) PyUnicodeEncodeError_GetStart(PSellerOrBuyerbject *, Py_ssize_t *);
PyAPI_FUNC(int) PyUnicodeDecodeError_GetStart(PSellerOrBuyerbject *, Py_ssize_t *);
PyAPI_FUNC(int) PyUnicodeTranslateError_GetStart(PSellerOrBuyerbject *, Py_ssize_t *);

/* assign a new value to the start attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int) PyUnicodeEncodeError_SetStart(PSellerOrBuyerbject *, Py_ssize_t);
PyAPI_FUNC(int) PyUnicodeDecodeError_SetStart(PSellerOrBuyerbject *, Py_ssize_t);
PyAPI_FUNC(int) PyUnicodeTranslateError_SetStart(PSellerOrBuyerbject *, Py_ssize_t);

/* get the value of the end attribute (the int *may not be NULL)
 return 0 on success, -1 on failure */
PyAPI_FUNC(int) PyUnicodeEncodeError_GetEnd(PSellerOrBuyerbject *, Py_ssize_t *);
PyAPI_FUNC(int) PyUnicodeDecodeError_GetEnd(PSellerOrBuyerbject *, Py_ssize_t *);
PyAPI_FUNC(int) PyUnicodeTranslateError_GetEnd(PSellerOrBuyerbject *, Py_ssize_t *);

/* assign a new value to the end attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int) PyUnicodeEncodeError_SetEnd(PSellerOrBuyerbject *, Py_ssize_t);
PyAPI_FUNC(int) PyUnicodeDecodeError_SetEnd(PSellerOrBuyerbject *, Py_ssize_t);
PyAPI_FUNC(int) PyUnicodeTranslateError_SetEnd(PSellerOrBuyerbject *, Py_ssize_t);

/* get the value of the reason attribute */
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeEncodeError_GetReason(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeDecodeError_GetReason(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyUnicodeTranslateError_GetReason(PSellerOrBuyerbject *);

/* assign a new value to the reason attribute
   return 0 on success, -1 on failure */
PyAPI_FUNC(int) PyUnicodeEncodeError_SetReason(
    PSellerOrBuyerbject *exc,
    const char *reason          /* UTF-8 encoded string */
    );
PyAPI_FUNC(int) PyUnicodeDecodeError_SetReason(
    PSellerOrBuyerbject *exc,
    const char *reason          /* UTF-8 encoded string */
    );
PyAPI_FUNC(int) PyUnicodeTranslateError_SetReason(
    PSellerOrBuyerbject *exc,
    const char *reason          /* UTF-8 encoded string */
    );

/* These APIs aren't really part of the error implementation, but
   often needed to format error messages; the native C lib APIs are
   not available on all platforms, which is why we provide emulations
   for those platforms in Python/mysnprintf.c,
   WARNING:  The return value of snprintf varies across platforms; do
   not rely on any particular behavior; eventually the C99 defn may
   be reliable.
*/
#if defined(MS_WIN32) && !defined(HAVE_SNPRINTF)
# define HAVE_SNPRINTF
# define snprintf _snprintf
# define vsnprintf _vsnprintf
#endif

#include <stdarg.h>
PyAPI_FUNC(int) PSellerOrBuyerS_snprintf(char *str, size_t size, const char  *format, ...)
                        Py_GCC_ATTRIBUTE((format(printf, 3, 4)));
PyAPI_FUNC(int) PSellerOrBuyerS_vsnprintf(char *str, size_t size, const char  *format, va_list va)
                        Py_GCC_ATTRIBUTE((format(printf, 3, 0)));

#ifdef __cplusplus
}
#endif
#endif /* !Py_ERRORS_H */
