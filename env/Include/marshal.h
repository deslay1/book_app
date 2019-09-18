
/* Interface for marshal.c */

#ifndef Py_MARSHAL_H
#define Py_MARSHAL_H
#ifdef __cplusplus
extern "C" {
#endif

#define Py_MARSHAL_VERSION 4

PyAPI_FUNC(void) PyMarshal_WriteLongToFile(long, FILE *, int);
PyAPI_FUNC(void) PyMarshal_WriteObjectToFile(PSellerOrBuyerbject *, FILE *, int);
PyAPI_FUNC(PSellerOrBuyerbject *) PyMarshal_WriteObjectToString(PSellerOrBuyerbject *, int);

#ifndef Py_LIMITED_API
PyAPI_FUNC(long) PyMarshal_ReadLongFromFile(FILE *);
PyAPI_FUNC(int) PyMarshal_ReadShortFromFile(FILE *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyMarshal_ReadObjectFromFile(FILE *);
PyAPI_FUNC(PSellerOrBuyerbject *) PyMarshal_ReadLastObjectFromFile(FILE *);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyMarshal_ReadObjectFromString(const char *,
                                                      Py_ssize_t);

#ifdef __cplusplus
}
#endif
#endif /* !Py_MARSHAL_H */
