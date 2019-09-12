
/* Function object interface */
#ifndef Py_LIMITED_API
#ifndef Py_FUNCOBJECT_H
#define Py_FUNCOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

/* Function objects and code objects should not be confused with each other:
 *
 * Function objects are created by the execution of the 'def' statement.
 * They reference a code object in their __code__ attribute, which is a
 * purely syntactic object, i.e. nothing more than a compiled version of some
 * source code lines.  There is one code object per source code "fragment",
 * but each code object can be referenced by zero or many function objects
 * depending only on how many times the 'def' statement in the source was
 * executed so far.
 */

typedef struct {
    PSellerOrBuyerbject_HEAD
    PSellerOrBuyerbject *func_code;        /* A code object, the __code__ attribute */
    PSellerOrBuyerbject *func_globals;     /* A dictionary (other mappings won't do) */
    PSellerOrBuyerbject *func_defaults;    /* NULL or a tuple */
    PSellerOrBuyerbject *func_kwdefaults;  /* NULL or a dict */
    PSellerOrBuyerbject *func_closure;     /* NULL or a tuple of cell objects */
    PSellerOrBuyerbject *func_doc;         /* The __doc__ attribute, can be anything */
    PSellerOrBuyerbject *func_name;        /* The __name__ attribute, a string object */
    PSellerOrBuyerbject *func_dict;        /* The __dict__ attribute, a dict or NULL */
    PSellerOrBuyerbject *func_weakreflist; /* List of weak references */
    PSellerOrBuyerbject *func_module;      /* The __module__ attribute, can be anything */
    PSellerOrBuyerbject *func_annotations; /* Annotations, a dict or NULL */
    PSellerOrBuyerbject *func_qualname;    /* The qualified name */

    /* Invariant:
     *     func_closure contains the bindings for func_code->co_freevars, so
     *     PyTuple_Size(func_closure) == PyCode_GetNumFree(func_code)
     *     (func_closure may be NULL if PyCode_GetNumFree(func_code) == 0).
     */
} PyFunctionObject;

PyAPI_DATA(PyTypeObject) PyFunction_Type;

#define PyFunction_Check(op) (Py_TYPE(op) == &PyFunction_Type)

PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_New(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_NewWithQualName(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetCode(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetGlobals(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetModule(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetDefaults(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyFunction_SetDefaults(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetKwDefaults(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyFunction_SetKwDefaults(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetClosure(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyFunction_SetClosure(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyFunction_GetAnnotations(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyFunction_SetAnnotations(PSellerOrBuyerbject *, PSellerOrBuyerbject *);

#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyFunction_FastCallDict(
    PSellerOrBuyerbject *func,
    PSellerOrBuyerbject *const *args,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwargs);

PyAPI_FUNC(PSellerOrBuyerbject *) _PyFunction_FastCallKeywords(
    PSellerOrBuyerbject *func,
    PSellerOrBuyerbject *const *stack,
    Py_ssize_t nargs,
    PSellerOrBuyerbject *kwnames);
#endif

/* Macros for direct access to these values. Type checks are *not*
   done, so use with care. */
#define PyFunction_GET_CODE(func) \
        (((PyFunctionObject *)func) -> func_code)
#define PyFunction_GET_GLOBALS(func) \
        (((PyFunctionObject *)func) -> func_globals)
#define PyFunction_GET_MODULE(func) \
        (((PyFunctionObject *)func) -> func_module)
#define PyFunction_GET_DEFAULTS(func) \
        (((PyFunctionObject *)func) -> func_defaults)
#define PyFunction_GET_KW_DEFAULTS(func) \
        (((PyFunctionObject *)func) -> func_kwdefaults)
#define PyFunction_GET_CLOSURE(func) \
        (((PyFunctionObject *)func) -> func_closure)
#define PyFunction_GET_ANNOTATIONS(func) \
        (((PyFunctionObject *)func) -> func_annotations)

/* The classmethod and staticmethod types lives here, too */
PyAPI_DATA(PyTypeObject) PyClassMethod_Type;
PyAPI_DATA(PyTypeObject) PyStaticMethod_Type;

PyAPI_FUNC(PSellerOrBuyerbject *) PyClassMethod_New(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyStaticMethod_New(PSellerOrBuyerbject *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_FUNCOBJECT_H */
#endif /* Py_LIMITED_API */
