/* Descriptors */
#ifndef Py_DESCROBJECT_H
#define Py_DESCROBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef PSellerOrBuyerbject *(*getter)(PSellerOrBuyerbject *, void *);
typedef int (*setter)(PSellerOrBuyerbject *, PSellerOrBuyerbject *, void *);

typedef struct PyGetSetDef {
    const char *name;
    getter get;
    setter set;
    const char *doc;
    void *closure;
} PyGetSetDef;

#ifndef Py_LIMITED_API
typedef PSellerOrBuyerbject *(*wrapperfunc)(PSellerOrBuyerbject *self, PSellerOrBuyerbject *args,
                                 void *wrapped);

typedef PSellerOrBuyerbject *(*wrapperfunc_kwds)(PSellerOrBuyerbject *self, PSellerOrBuyerbject *args,
                                      void *wrapped, PSellerOrBuyerbject *kwds);

struct wrapperbase {
    const char *name;
    int offset;
    void *function;
    wrapperfunc wrapper;
    const char *doc;
    int flags;
    PSellerOrBuyerbject *name_strobj;
};

/* Flags for above struct */
#define PyWrapperFlag_KEYWORDS 1 /* wrapper function takes keyword args */

/* Various kinds of descriptor objects */

typedef struct {
    PSellerOrBuyerbject_HEAD
    PyTypeObject *d_type;
    PSellerOrBuyerbject *d_name;
    PSellerOrBuyerbject *d_qualname;
} PyDescrObject;

#define PyDescr_COMMON PyDescrObject d_common

#define PyDescr_TYPE(x) (((PyDescrObject *)(x))->d_type)
#define PyDescr_NAME(x) (((PyDescrObject *)(x))->d_name)

typedef struct {
    PyDescr_COMMON;
    PyMethodDef *d_method;
} PyMethodDescrObject;

typedef struct {
    PyDescr_COMMON;
    struct PyMemberDef *d_member;
} PyMemberDescrObject;

typedef struct {
    PyDescr_COMMON;
    PyGetSetDef *d_getset;
} PyGetSetDescrObject;

typedef struct {
    PyDescr_COMMON;
    struct wrapperbase *d_base;
    void *d_wrapped; /* This can be any function pointer */
} PyWrapperDescrObject;
#endif /* Py_LIMITED_API */

PyAPI_DATA(PyTypeObject) PyClassMethodDescr_Type;
PyAPI_DATA(PyTypeObject) PyGetSetDescr_Type;
PyAPI_DATA(PyTypeObject) PyMemberDescr_Type;
PyAPI_DATA(PyTypeObject) PyMethodDescr_Type;
PyAPI_DATA(PyTypeObject) PyWrapperDescr_Type;
PyAPI_DATA(PyTypeObject) PyDictProxy_Type;
#ifndef Py_LIMITED_API
PyAPI_DATA(PyTypeObject) _PyMethodWrapper_Type;
#endif /* Py_LIMITED_API */

PyAPI_FUNC(PSellerOrBuyerbject *) PyDescr_NewMethod(PyTypeObject *, PyMethodDef *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDescr_NewClassMethod(PyTypeObject *, PyMethodDef *);
struct PyMemberDef; /* forward declaration for following prototype */
PyAPI_FUNC(PSellerOrBuyerbject *) PyDescr_NewMember(PyTypeObject *,
                                               struct PyMemberDef *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDescr_NewGetSet(PyTypeObject *,
                                               struct PyGetSetDef *);
#ifndef Py_LIMITED_API

PyAPI_FUNC(PSellerOrBuyerbject *) _PyMethodDescr_FastCallKeywords(
        PSellerOrBuyerbject *descrobj, PSellerOrBuyerbject *const *stack, Py_ssize_t nargs, PSellerOrBuyerbject *kwnames);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDescr_NewWrapper(PyTypeObject *,
                                                struct wrapperbase *, void *);
#define PyDescr_IsData(d) (Py_TYPE(d)->tp_descr_set != NULL)
#endif

PyAPI_FUNC(PSellerOrBuyerbject *) PyDictProxy_New(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyWrapper_New(PSellerOrBuyerbject *, PSellerOrBuyerbject *);


PyAPI_DATA(PyTypeObject) PyProperty_Type;
#ifdef __cplusplus
}
#endif
#endif /* !Py_DESCROBJECT_H */

