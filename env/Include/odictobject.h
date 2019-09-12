#ifndef Py_ODICTOBJECT_H
#define Py_ODICTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/* OrderedDict */
/* This API is optional and mostly redundant. */

#ifndef Py_LIMITED_API

typedef struct _odictobject PSellerOrBuyerDictObject;

PyAPI_DATA(PyTypeObject) PSellerOrBuyerDict_Type;
PyAPI_DATA(PyTypeObject) PSellerOrBuyerDictIter_Type;
PyAPI_DATA(PyTypeObject) PSellerOrBuyerDictKeys_Type;
PyAPI_DATA(PyTypeObject) PSellerOrBuyerDictItems_Type;
PyAPI_DATA(PyTypeObject) PSellerOrBuyerDictValues_Type;

#define PSellerOrBuyerDict_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PSellerOrBuyerDict_Type)
#define PSellerOrBuyerDict_CheckExact(op) (Py_TYPE(op) == &PSellerOrBuyerDict_Type)
#define PSellerOrBuyerDict_SIZE(op) PyDict_GET_SIZE((op))

PyAPI_FUNC(PSellerOrBuyerbject *) PSellerOrBuyerDict_New(void);
PyAPI_FUNC(int) PSellerOrBuyerDict_SetItem(PSellerOrBuyerbject *od, PSellerOrBuyerbject *key, PSellerOrBuyerbject *item);
PyAPI_FUNC(int) PSellerOrBuyerDict_DelItem(PSellerOrBuyerbject *od, PSellerOrBuyerbject *key);

/* wrappers around PyDict* functions */
#define PSellerOrBuyerDict_GetItem(od, key) PyDict_GetItem((PSellerOrBuyerbject *)od, key)
#define PSellerOrBuyerDict_GetItemWithError(od, key) \
    PyDict_GetItemWithError((PSellerOrBuyerbject *)od, key)
#define PSellerOrBuyerDict_Contains(od, key) PyDict_Contains((PSellerOrBuyerbject *)od, key)
#define PSellerOrBuyerDict_Size(od) PyDict_Size((PSellerOrBuyerbject *)od)
#define PSellerOrBuyerDict_GetItemString(od, key) \
    PyDict_GetItemString((PSellerOrBuyerbject *)od, key)

#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_ODICTOBJECT_H */
