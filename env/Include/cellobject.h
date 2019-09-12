/* Cell object interface */
#ifndef Py_LIMITED_API
#ifndef Py_CELLOBJECT_H
#define Py_CELLOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    PSellerOrBuyerbject_HEAD
    PSellerOrBuyerbject *ob_ref;       /* Content of the cell or NULL when empty */
} PyCellObject;

PyAPI_DATA(PyTypeObject) PyCell_Type;

#define PyCell_Check(op) (Py_TYPE(op) == &PyCell_Type)

PyAPI_FUNC(PSellerOrBuyerbject *) PyCell_New(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyCell_Get(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyCell_Set(PSellerOrBuyerbject *, PSellerOrBuyerbject *);

#define PyCell_GET(op) (((PyCellObject *)(op))->ob_ref)
#define PyCell_SET(op, v) (((PyCellObject *)(op))->ob_ref = v)

#ifdef __cplusplus
}
#endif
#endif /* !Py_TUPLEOBJECT_H */
#endif /* Py_LIMITED_API */
