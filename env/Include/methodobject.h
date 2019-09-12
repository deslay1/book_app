
/* Method object interface */

#ifndef Py_METHODOBJECT_H
#define Py_METHODOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* This is about the type 'builtin_function_or_method',
   not Python methods in user-defined classes.  See classobject.h
   for the latter. */

PyAPI_DATA(PyTypeObject) PyCFunction_Type;

#define PyCFunction_Check(op) (Py_TYPE(op) == &PyCFunction_Type)

typedef PSellerOrBuyerbject *(*PyCFunction)(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
typedef PSellerOrBuyerbject *(*_PyCFunctionFast) (PSellerOrBuyerbject *, PSellerOrBuyerbject *const *, Py_ssize_t);
typedef PSellerOrBuyerbject *(*PyCFunctionWithKeywords)(PSellerOrBuyerbject *, PSellerOrBuyerbject *,
                                             PSellerOrBuyerbject *);
typedef PSellerOrBuyerbject *(*_PyCFunctionFastWithKeywords) (PSellerOrBuyerbject *,
                                                   PSellerOrBuyerbject *const *, Py_ssize_t,
                                                   PSellerOrBuyerbject *);
typedef PSellerOrBuyerbject *(*PyNoArgsFunction)(PSellerOrBuyerbject *);

PyAPI_FUNC(PyCFunction) PyCFunction_GetFunction(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyCFunction_GetSelf(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyCFunction_GetFlags(PSellerOrBuyerbject *);

/* Macros for direct access to these values. Type checks are *not*
   done, so use with care. */
#ifndef Py_LIMITED_API
#define PyCFunction_GET_FUNCTION(func) \
        (((PyCFunctionObject *)func) -> m_ml -> ml_meth)
#define PyCFunction_GET_SELF(func) \
        (((PyCFunctionObject *)func) -> m_ml -> ml_flags & METH_STATIC ? \
         NULL : ((PyCFunctionObject *)func) -> m_self)
#define PyCFunction_GET_FLAGS(func) \
        (((PyCFunctionObject *)func) -> m_ml -> ml_flags)
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyCFunction_Call(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);

#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyCFunction_FastCallDict(PSellerOrBuyerbject *func,
    PSellerOrBuyerbject *const *args,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwargs);

PyAPI_FUNC(PSellerOrBuyerbject *) _PyCFunction_FastCallKeywords(PSellerOrBuyerbject *func,
    PSellerOrBuyerbject *const *stack,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwnames);
#endif

struct PyMethodDef {
    const char  *ml_name;   /* The name of the built-in function/method */
    PyCFunction ml_meth;    /* The C function that implements it */
    int         ml_flags;   /* Combination of METH_xxx flags, which mostly
                               describe the args expected by the C func */
    const char  *ml_doc;    /* The __doc__ attribute, or NULL */
};
typedef struct PyMethodDef PyMethodDef;

#define PyCFunction_New(ML, SELF) PyCFunction_NewEx((ML), (SELF), NULL)
PyAPI_FUNC(PSellerOrBuyerbject *) PyCFunction_NewEx(PyMethodDef *, PSellerOrBuyerbject *,
                                         PSellerOrBuyerbject *);

/* Flag passed to newmethodobject */
/* #define METH_OLDARGS  0x0000   -- unsupported now */
#define METH_VARARGS  0x0001
#define METH_KEYWORDS 0x0002
/* METH_NOARGS and METH_O must not be combined with the flags above. */
#define METH_NOARGS   0x0004
#define METH_O        0x0008

/* METH_CLASS and METH_STATIC are a little different; these control
   the construction of methods for a class.  These cannot be used for
   functions in modules. */
#define METH_CLASS    0x0010
#define METH_STATIC   0x0020

/* METH_COEXIST allows a method to be entered even though a slot has
   already filled the entry.  When defined, the flag allows a separate
   method, "__contains__" for example, to coexist with a defined
   slot like sq_contains. */

#define METH_COEXIST   0x0040

#ifndef Py_LIMITED_API
#define METH_FASTCALL  0x0080
#endif

/* This bit is preserved for Stackless Python */
#ifdef STACKLESS
#define METH_STACKLESS 0x0100
#else
#define METH_STACKLESS 0x0000
#endif

#ifndef Py_LIMITED_API
typedef struct {
    PSellerOrBuyerbject_HEAD
    PyMethodDef *m_ml; /* Description of the C function to call */
    PSellerOrBuyerbject    *m_self; /* Passed as 'self' arg to the C func, can be NULL */
    PSellerOrBuyerbject    *m_module; /* The __module__ attribute, can be anything */
    PSellerOrBuyerbject    *m_weakreflist; /* List of weak references */
} PyCFunctionObject;

PyAPI_FUNC(PSellerOrBuyerbject *) _PyMethodDef_RawFastCallDict(
    PyMethodDef *method,
    PSellerOrBuyerbject *self,
    PSellerOrBuyerbject *const *args,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwargs);

PyAPI_FUNC(PSellerOrBuyerbject *) _PyMethodDef_RawFastCallKeywords(
    PyMethodDef *method,
    PSellerOrBuyerbject *self,
    PSellerOrBuyerbject *const *args,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwnames);
#endif

PyAPI_FUNC(int) PyCFunction_ClearFreeList(void);

#ifndef Py_LIMITED_API
PyAPI_FUNC(void) _PyCFunction_DebugMallocStats(FILE *out);
PyAPI_FUNC(void) _PyMethod_DebugMallocStats(FILE *out);
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_METHODOBJECT_H */
