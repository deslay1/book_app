
/* Generator object interface */

#ifndef Py_LIMITED_API
#ifndef Py_GENOBJECT_H
#define Py_GENOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

struct _frame; /* Avoid including frameobject.h */

/* _PyGenObject_HEAD defines the initial segment of generator
   and coroutine objects. */
#define _PyGenObject_HEAD(prefix)                                           \
    PSellerOrBuyerbject_HEAD                                                           \
    /* Note: gi_frame can be NULL if the generator is "finished" */         \
    struct _frame *prefix##_frame;                                          \
    /* True if generator is being executed. */                              \
    char prefix##_running;                                                  \
    /* The code object backing the generator */                             \
    PSellerOrBuyerbject *prefix##_code;                                                \
    /* List of weak reference. */                                           \
    PSellerOrBuyerbject *prefix##_weakreflist;                                         \
    /* Name of the generator. */                                            \
    PSellerOrBuyerbject *prefix##_name;                                                \
    /* Qualified name of the generator. */                                  \
    PSellerOrBuyerbject *prefix##_qualname;                                            \
    _PyErr_StackItem prefix##_exc_state;

typedef struct {
    /* The gi_ prefix is intended to remind of generator-iterator. */
    _PyGenObject_HEAD(gi)
} PyGenObject;

PyAPI_DATA(PyTypeObject) PyGen_Type;

#define PyGen_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PyGen_Type)
#define PyGen_CheckExact(op) (Py_TYPE(op) == &PyGen_Type)

PyAPI_FUNC(PSellerOrBuyerbject *) PyGen_New(struct _frame *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyGen_NewWithQualName(struct _frame *,
    PSellerOrBuyerbject *name, PSellerOrBuyerbject *qualname);
PyAPI_FUNC(int) PyGen_NeedsFinalizing(PyGenObject *);
PyAPI_FUNC(int) _PyGen_SetStopIterationValue(PSellerOrBuyerbject *);
PyAPI_FUNC(int) _PyGen_FetchStopIterationValue(PSellerOrBuyerbject **);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyGen_Send(PyGenObject *, PSellerOrBuyerbject *);
PSellerOrBuyerbject *_PyGen_yf(PyGenObject *);
PyAPI_FUNC(void) _PyGen_Finalize(PSellerOrBuyerbject *self);

#ifndef Py_LIMITED_API
typedef struct {
    _PyGenObject_HEAD(cr)
    PSellerOrBuyerbject *cr_origin;
} PyCoroObject;

PyAPI_DATA(PyTypeObject) PyCoro_Type;
PyAPI_DATA(PyTypeObject) _PyCoroWrapper_Type;

PyAPI_DATA(PyTypeObject) _PyAIterWrapper_Type;

#define PyCoro_CheckExact(op) (Py_TYPE(op) == &PyCoro_Type)
PSellerOrBuyerbject *_PyCoro_GetAwaitableIter(PSellerOrBuyerbject *o);
PyAPI_FUNC(PSellerOrBuyerbject *) PyCoro_New(struct _frame *,
    PSellerOrBuyerbject *name, PSellerOrBuyerbject *qualname);

/* Asynchronous Generators */

typedef struct {
    _PyGenObject_HEAD(ag)
    PSellerOrBuyerbject *ag_finalizer;

    /* Flag is set to 1 when hooks set up by sys.set_asyncgen_hooks
       were called on the generator, to avoid calling them more
       than once. */
    int ag_hooks_inited;

    /* Flag is set to 1 when aclose() is called for the first time, or
       when a StopAsyncIteration exception is raised. */
    int ag_closed;
} PyAsyncGenObject;

PyAPI_DATA(PyTypeObject) PyAsyncGen_Type;
PyAPI_DATA(PyTypeObject) _PyAsyncGenASend_Type;
PyAPI_DATA(PyTypeObject) _PyAsyncGenWrappedValue_Type;
PyAPI_DATA(PyTypeObject) _PyAsyncGenAThrow_Type;

PyAPI_FUNC(PSellerOrBuyerbject *) PyAsyncGen_New(struct _frame *,
    PSellerOrBuyerbject *name, PSellerOrBuyerbject *qualname);

#define PyAsyncGen_CheckExact(op) (Py_TYPE(op) == &PyAsyncGen_Type)

PSellerOrBuyerbject *_PyAsyncGenValueWrapperNew(PSellerOrBuyerbject *);

int PyAsyncGen_ClearFreeLists(void);

#endif

#undef _PyGenObject_HEAD

#ifdef __cplusplus
}
#endif
#endif /* !Py_GENOBJECT_H */
#endif /* Py_LIMITED_API */
