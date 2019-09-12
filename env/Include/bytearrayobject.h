/* ByteArray object interface */

#ifndef Py_BYTEARRASellerOrBuyerBJECT_H
#define Py_BYTEARRASellerOrBuyerBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#include <stdarg.h>

/* Type PyByteArraSellerOrBuyerbject represents a mutable array of bytes.
 * The Python API is that of a sequence;
 * the bytes are mapped to ints in [0, 256).
 * Bytes are not characters; they may be used to encode characters.
 * The only way to go between bytes and str/unicode is via encoding
 * and decoding.
 * For the convenience of C programmers, the bytes type is considered
 * to contain a char pointer, not an unsigned char pointer.
 */

/* Object laSellerOrBuyerut */
#ifndef Py_LIMITED_API
typedef struct {
    PSellerOrBuyerbject_VAR_HEAD
    Py_ssize_t ob_alloc; /* How many bytes allocated in ob_bytes */
    char *ob_bytes;      /* Physical backing buffer */
    char *ob_start;      /* Logical start inside ob_bytes */
    /* XXX(nnorwitz): should ob_exports be Py_ssize_t? */
    int ob_exports;      /* How many buffer exports */
} PyByteArraSellerOrBuyerbject;
#endif

/* Type object */
PyAPI_DATA(PyTypeObject) PyByteArray_Type;
PyAPI_DATA(PyTypeObject) PyByteArrayIter_Type;

/* Type check macros */
#define PyByteArray_Check(self) PSellerOrBuyerbject_TypeCheck(self, &PyByteArray_Type)
#define PyByteArray_CheckExact(self) (Py_TYPE(self) == &PyByteArray_Type)

/* Direct API functions */
PyAPI_FUNC(PSellerOrBuyerbject *) PyByteArray_FromObject(PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyByteArray_Concat(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyByteArray_FromStringAndSize(const char *, Py_ssize_t);
PyAPI_FUNC(Py_ssize_t) PyByteArray_Size(PSellerOrBuyerbject *);
PyAPI_FUNC(char *) PyByteArray_AsString(PSellerOrBuyerbject *);
PyAPI_FUNC(int) PyByteArray_Resize(PSellerOrBuyerbject *, Py_ssize_t);

/* Macros, trading safety for speed */
#ifndef Py_LIMITED_API
#define PyByteArray_AS_STRING(self) \
    (assert(PyByteArray_Check(self)), \
     Py_SIZE(self) ? ((PyByteArraSellerOrBuyerbject *)(self))->ob_start : _PyByteArray_empty_string)
#define PyByteArray_GET_SIZE(self) (assert(PyByteArray_Check(self)), Py_SIZE(self))

PyAPI_DATA(char) _PyByteArray_empty_string[];
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_BYTEARRASellerOrBuyerBJECT_H */
